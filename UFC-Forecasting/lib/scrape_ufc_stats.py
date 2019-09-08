import requests
from bs4 import BeautifulSoup
import csv
import os


def create_csv(filename):
    """
    Creats a new csv with only the UFC stats headers.
    """
    url = 'http://ufcstats.com/event-details/a79bfbc01b2264d6'
    f = requests.get(url).text
    html = BeautifulSoup(f.replace('\n', ''), 'html.parser')
    table = html.find('table', class_='b-fight-details__table b-fight-details__table_style_margin-top b-fight-details__table_type_event-details js-fight-table')  # get the headers
    headings = [t.text.strip() for t in table.find('thead').find_all('th')]
    csv_lines = []
    csv_lines.append(headings)

    with open(filename, "w") as output:  # save the data to file
        writer = csv.writer(output, delimiter=',', lineterminator='\n')
        writer.writerows(csv_lines)


def get_event_urls(page_url):
    """
    Returns the individual UFC event URLs from the overall page
    """
    f = requests.get(page_url).text
    html = BeautifulSoup(f.replace('\n', ''), 'html.parser')
    table = html.find('table', class_='b-statistics__table-events')  # get the headers
    return [a['href'] for a in table.find_all('a', href=True)]


def get_fight_data(event_url):
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
    # First let's create the file with the headers.
    dirname = os.path.abspath('')
    filename = dirname + "/data/UFC_stats.csv"
    create_csv(filename)

    # Data goes back to the beginning of 2016
    page_urls = ['http://ufcstats.com/statistics/events/completed?page=1',
                 'http://ufcstats.com/statistics/events/completed?page=2',
                 'http://ufcstats.com/statistics/events/completed?page=3',
                 'http://ufcstats.com/statistics/events/completed?page=4',
                 'http://ufcstats.com/statistics/events/completed?page=5',
                 'http://ufcstats.com/statistics/events/completed?page=6']

    # For each page, get the event urls and add the data
    for page_url in page_urls:
        event_urls = get_event_urls(page_url)
        for event_url in event_urls:
            append_to_csv(filename, get_fight_data(event_url))
