import requests
from bs4 import BeautifulSoup
import csv
import os


def create_csv_fight(filename):
    """
    Creats a new csv with only the UFC stats headers. Fight based page.
    """
    url = 'http://ufcstats.com/fight-details/01a4827b3596d111'
    f = requests.get(url).text
    html = BeautifulSoup(f.replace('\n', ''), 'html.parser')
    table = html.find(class_='b-fight-details__table-head')
    headings = [t.text.strip() for t in table.find_all('th')]

    with open(filename, "w") as output:  # save the data to file
        writer = csv.writer(output, delimiter=',', lineterminator='\n')
        writer.writerows([headings])


def create_csv_event(filename):
    """
    Creats a new csv with only the UFC stats headers. Event based page.
    """
    url = 'http://ufcstats.com/event-details/a79bfbc01b2264d6'
    f = requests.get(url).text
    html = BeautifulSoup(f.replace('\n', ''), 'html.parser')
    table = html.find('table', class_='b-fight-details__table b-fight-details__table_style_margin-top b-fight-details__table_type_event-details js-fight-table')  # get the headers
    headings = [t.text.strip() for t in table.find('thead').find_all('th')]

    with open(filename, "w") as output:  # save the data to file
        writer = csv.writer(output, delimiter=',', lineterminator='\n')
        writer.writerows([headings])


def get_event_urls(page_url):
    """
    Returns the individual UFC event URLs from the overall page
    """
    f = requests.get(page_url).text
    html = BeautifulSoup(f.replace('\n', ''), 'html.parser')
    table = html.find('table', class_='b-statistics__table-events')  # get the headers
    return [a['href'] for a in table.find_all('a', href=True)]


def get_fight_urls(event_url):
    """
    Returns the individual UFC fight URLs from the event page
    """
    f = requests.get(event_url).text
    html = BeautifulSoup(f.replace('\n', ''), 'html.parser')
    table = html.find(class_='b-fight-details__table-body')
    urls = [a['href'] for a in table.find_all('a', href=True)]
    return [url for url in urls if 'fight-details' in url]


def get_fight_data_fight(fight_url):
    """
    Returns a list with the relevant fight details for the winner of a specific fight
    """
    f = requests.get(fight_url).text
    html = BeautifulSoup(f.replace('\n', ''), 'html.parser')
    WL = html.find_all(class_='b-fight-details__person')
    if WL[0].text.strip()[0] == 'W':
        winner = 0
    elif WL[1].text.strip()[0] == 'W':
        winner = 1
    else:  # Weird situation like a draw or no contest
        return None  # Need to test to see what happens if None is appended to csv list
    table = html.find(class_='b-fight-details__table-body')
    info_list = []
    for tr in table.find_all('tr'):  # get all the data
        info = [td.text.strip()
                for td in tr.find_all('td')]
        info_list.append(info)

    if winner == 0:
        return [info_0.partition('  ')[0] for info_0 in info_list[0]]
    elif winner == 1:
        return [info_1.partition('  ')[2].strip() for info_1 in info_list[0]]


def get_fight_data_event(event_url):
    """
    Returns a list with the relevant fight details for the winners of a specific event
    """
    f = requests.get(event_url).text
    html = BeautifulSoup(f.replace('\n', ''), 'html.parser')
    table = html.find('table', class_='b-fight-details__table b-fight-details__table_style_margin-top b-fight-details__table_type_event-details js-fight-table')  # get the headers
    info_list = []
    for tr in table.find('tbody').find_all('tr'):  # get all the data
        info = [td.text.strip().split('  ')[0]
                for td in tr.find_all('td')]
        info_list.append(info)
    return info_list


def append_to_csv(filename, event_stats):
    """
    Appends the results of an event to the overall stats csv
    """
    with open(filename, "a") as output:
        writer = csv.writer(output, delimiter=',', lineterminator='\n')
        writer.writerows(event_stats)


def initial_setup():
    """
    This should only be run once. After this should only be appending.
    """
    # Data goes back to the beginning of 2016
    page_urls = ['http://ufcstats.com/statistics/events/completed?page=1',
                 'http://ufcstats.com/statistics/events/completed?page=2',
                 'http://ufcstats.com/statistics/events/completed?page=3',
                 'http://ufcstats.com/statistics/events/completed?page=4',
                 'http://ufcstats.com/statistics/events/completed?page=5',
                 'http://ufcstats.com/statistics/events/completed?page=6']

    # First, let's create the event specific stats csv.
    dirname = os.path.abspath('')
    filename = dirname + "/data/UFC_statistics.csv"
    create_csv_fight(filename)

    for page_url in page_urls:
        event_urls = get_event_urls(page_url)
        for event_url in event_urls:
            fight_data = get_fight_data_event(event_url)
            append_to_csv(filename, fight_data)

    # Second, let's create the fight specific stats csv.
    filename = dirname + "/data/UFC_statistics.csv"
    create_csv_fight(filename)

    # For each page, get the event urls and add the data
    for page_url in page_urls:
        event_urls = get_event_urls(page_url)
        for event_url in event_urls:
            fight_urls = get_fight_urls(event_url)
            for fight_url in fight_urls:
                try:
                    fight_data = get_fight_data_fight(fight_url)
                except IndexError as error:  # In case of weird parsing issues
                    print(error)
                else:
                    if fight_data is None:
                        continue
                    else:
                        append_to_csv(filename, [fight_data])
