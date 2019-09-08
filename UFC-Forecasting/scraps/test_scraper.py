import requests
from bs4 import BeautifulSoup
import csv


# Get URL's for the individual events:
overall_url = 'http://ufcstats.com/statistics/events/completed?page=2'
f = requests.get(overall_url).text
html = BeautifulSoup(f.replace('\n', ''), 'html.parser')
table = html.find('table', class_='b-statistics__table-events')
urls = []
urls = [a['href'] for a in table.find_all('a', href=True)]


# For a specific event
def get_fight_data(url):
    f = requests.get(url).text
    html = BeautifulSoup(f.replace('\n', ''), 'html.parser')
    table = html.find('table', class_='b-fight-details__table b-fight-details__table_style_margin-top b-fight-details__table_type_event-details js-fight-table')  # get the headers
    info_list = []
    for tr in table.find('tbody').find_all('tr'):  # get all the data
        info = [td.text.strip().split('  ')[0]
                for td in tr.find_all('td')]
        info_list.append(info)
    return info_list


# Get headers
url = 'http://ufcstats.com/event-details/a79bfbc01b2264d6'
f = requests.get(url).text
html = BeautifulSoup(f.replace('\n', ''), 'html.parser')
table = html.find('table', class_='b-fight-details__table b-fight-details__table_style_margin-top b-fight-details__table_type_event-details js-fight-table')  # get the headers
headings = [t.text.strip() for t in table.find('thead').find_all('th')]

# Make csv
csv_lines = []
csv_lines.append(headings)

for url in urls:
    cur_data = get_fight_data(url)
    print(cur_data)
    csv_lines.extend(cur_data)

# Write to file
cur_filename = 'page2.csv'
with open(cur_filename, "w") as output:  # save the data to file
    writer = csv.writer(output, delimiter=',', lineterminator='\n')
    writer.writerows(csv_lines)

# Now just need to have enfunction such that I can append to already existing one.
# Testing append
to_add = get_fight_data('http://ufcstats.com/event-details/2d5fbe2103f97053')
with open(cur_filename, "a") as output:
    writer = csv.writer(output, delimiter=',', lineterminator='\n')
    writer.writerows(to_add)

###########
# Need to be able to pul stats from the actual fight page itself to get all of the stats.
# FIRST: need to be able to get individual fight urls from event url.
    # Okay, bad news, the fighters there are listed alphabetically, not necessarily by winner.
fight_url = 'http://ufcstats.com/fight-details/8e1ae2ae6694b131'
f = requests.get(fight_url).text
html = BeautifulSoup(f.replace('\n', ''), 'html.parser')
WL = html.find_all(class_='b-fight-details__person')
WL[1].text.strip()[0]
# Okay, so we can strip and see if it's index 0 or 1 that won.

# Let's now see how the table works.
table = html.find(class_='b-fight-details__table-body')
info_list = []
for tr in table.find_all('tr'):  # get all the data
    info = [td.text.strip()
            for td in tr.find_all('td')]
    info_list.append(info)

tt = info_list[0][2]

tt
fighter_0, _, fighter_1 = tt.partition('  ')
print(fighter_1.strip())
