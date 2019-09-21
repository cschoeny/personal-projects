import requests
from bs4 import BeautifulSoup
import csv
import os


def get_odds_for_fighter(name):
    return


# Need to add headers, was getting error before
url = 'https://www.bestfightodds.com/'
headers = {'User-Agent': 'Mozilla/5.0'}
f = requests.get(url, headers=headers).text
# f.status_code
html = BeautifulSoup(f.replace('\n', ''), 'html.parser')
html
a = html.find_all(class_='odds-table')
b = a[2]
b
c = b.find_all(class_="bestbet")
html.find(class_="bestbet")




### tutorial 1
url = 'https://www.bestfightodds.com/'
headers = {'User-Agent': 'Mozilla/5.0'}
f = requests.get(url, headers=headers).text
# f.status_code
soup = BeautifulSoup(f.replace('\n', ''), 'html.parser')
