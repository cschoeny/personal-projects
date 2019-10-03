import requests
from bs4 import BeautifulSoup


def full_names_that_need_cleaning(names, event_table):
    # names, _ = pu.parse_dk(date_of_event)
    names_dict = {name: False for name in names}
    for row in event_table.find_all('tr'):
        if row.find('th').text in names_dict:
            names_dict[row.find('th').text] = True
    bad_names = []
    for name, val in names_dict.items():
        if val is False:
            bad_names.append(name)
    return bad_names


def short_names_that_need_cleaning(short_names, event_table):
    names_dict = {f'{name} wins by decision': False for name in short_names}
    for row in event_table.find_all('tr'):
        if row.find('th').text in names_dict:
            names_dict[row.find('th').text] = True
    bad_names = []
    for name, val in names_dict.items():
        if val is False:
            bad_names.append(name)
    return bad_names


def get_odds_table(table_num):
    url = 'https://www.bestfightodds.com/'
    headers = {'User-Agent': 'Mozilla/5.0'}
    f = requests.get(url, headers=headers).text
    html = BeautifulSoup(f.replace('\n', ''), 'html.parser')
    tables = html.find_all('table')
    return tables[table_num * 2 - 1]


def get_odds_for_fighter(full_name, name, table, five_rounds):
    odds = {'name': full_name}
    if five_rounds:
        current_dict_fields = {f'{full_name}': 'win', f'{name} wins by decision': 'DEC', f'{name} wins by TKO/KO': 'KO/TKO', f'{name} wins by submission': 'SUB', f'{name} wins in round 1': '1', f'{name} wins in round 2': '2', f'{name} wins in round 3': '3', f'{name} wins in round 4': '4', f'{name} wins in round 5': '5'}
    else:
        current_dict_fields = {f'{full_name}': 'win', f'{name} wins by decision': 'DEC', f'{name} wins by TKO/KO': 'KO/TKO', f'{name} wins by submission': 'SUB', f'{name} wins in round 1': '1', f'{name} wins in round 2': '2', f'{name} wins in round 3': '3'}
    for row in table.find_all('tr'):
        if row.find('th').text in current_dict_fields:
            odds[current_dict_fields[row.find('th').text]] = ''.join(filter(lambda x: ord(x) < 128, row.find('td').text))
    return odds
