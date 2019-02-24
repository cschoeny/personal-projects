import requests
from bs4 import BeautifulSoup
import csv

# A list of url's with the relevant 2019 statistics
url_list = ['https://www.pgatour.com/stats/stat.112.html',  # par 3 birdie or better
            'https://www.pgatour.com/stats/stat.447.html',  # par 4 eagles
            'https://www.pgatour.com/stats/stat.113.html',  # par 4 birdies or better
            'https://www.pgatour.com/stats/stat.448.html',  # par 5 eagles
            'https://www.pgatour.com/stats/stat.114.html',  # par 5 birdies or better
            'https://www.pgatour.com/stats/stat.02419.html',  # bogey average
            'https://www.pgatour.com/stats/stat.02415.html']  # birdie to bogey ratio (to get DB)

filenames = ['raw_2019/par3_bird_2019.csv', 'raw_2019/par4_eag_2019.csv', 'raw_2019/par4_bird_2019.csv',
             'raw_2019/par5_eag_2019.csv', 'raw_2019/par5_bird_2019.csv', 'raw_2019/bogey_2019.csv',
             'raw_2019/doublebogey_2019.csv']

for idx, url in enumerate(url_list):
    f = requests.get(url).text  # gets the html text
    html = BeautifulSoup(f.replace('\n', ''), 'html.parser')  # parses the html
    csv_lines = []  # ininiate empty csv list
    table = html.find('table', class_='table-styled')  # get the headers
    headings = [t.text for t in table.find('thead').find_all('th')]
    csv_lines.append(headings)
    for tr in table.find('tbody').find_all('tr'):  # get all the data
        info = [td.text.replace(u'\xa0', u' ').strip()
                for td in tr.find_all('td')]
        csv_lines.append(info)
    cur_filename = filenames[idx]
    with open(cur_filename, "w") as output:  # save the data to file
        writer = csv.writer(output, delimiter=',', lineterminator='\n')
        writer.writerows(csv_lines)
