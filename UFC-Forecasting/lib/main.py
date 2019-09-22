from collections import Counter
import time

import lib.pandas_utils as pu
import lib.LP_solver as lps
import lib.scrape_ufc_stats as sus

from lib.Fighter_Class import Fighter
from lib.Fight_Class import Fight
from lib.Event_Class import Event

start = time.time()

# Update UFC stats (only need to run once)
sus.add_new_event('http://ufcstats.com/event-details/4834ff149dc9542a')
pu.read_clean_save_event_stats()
pu.read_clean_save_fight_stats()
pu.merge_two_stat_sources_and_score()

##########
# Create the Fighters
date_of_event = '2019-09-21'
names, salaries = pu.parse_dk(date_of_event)
names
# For now need to manually do the weightclasses
weightclasses = [
    "Women's Bantamweight",
    "Women's Bantamweight",
    "Flyweight",
    "Flyweight",
    "Featherweight",
    "Featherweight",
    "Women's Strawweight",
    "Women's Strawweight",
    "Women's Bantamweight",
    "Women's Bantamweight",
    "Light Heavyweight",
    "Light Heavyweight",
    "Women's Strawweight",
    "Women's Strawweight",
    "Bantamweight",
    "Bantamweight",
    "Lightweight",
    "Lightweight",
    "Flyweight",
    "Flyweight",
    "Featherweight",
    "Featherweight",
    "Featherweight",
    "Featherweight"
]
championship = [False] * len(names)
championship[-1], championship[-2] = (True, True)
championship

# Manually set the main event / championship fights to 5 rounds.

fighter_attributes = list(zip(names, salaries, weightclasses, championship))
fighter_list = [Fighter(*fighter_attribute) for fighter_attribute in fighter_attributes]

##########
# Create the odds (for now do it manually, really need to figure this out though)
odds = [
    {'win': '-615', 'DEC': '-125', 'KO/TKO': '+330', 'SUB': '+495', '1': '+400', '2': '+600', '3': '+1100'},
    {'win': '+510', 'DEC': '+720', 'KO/TKO': '+1500', 'SUB': '+1715', '1': '+1950', '2': '+2250', '3': '+3050'},
    {'win': '+140', 'DEC': '+400', 'KO/TKO': '+590', 'SUB': '+485', '1': '+550', '2': '+750', '3': '+1350'},
    {'win': '-150', 'DEC': '+220', 'KO/TKO': '+684', 'SUB': '+225', '1': '+425', '2': '+600', '3': '+1200'},
    {'win': '+100', 'DEC': '+175', 'KO/TKO': '+665', 'SUB': '+800', '1': '+800', '2': '+1000', '3': '+1900'},
    {'win': '-110', 'DEC': '+195', 'KO/TKO': '+590', 'SUB': '+685', '1': '+675', '2': '+900', '3': '+1475'},
    {'win': '-140', 'DEC': '+110', 'KO/TKO': '+775', 'SUB': '+1340', '1': '+1100', '2': '+1375', '3': '+2050'},
    {'win': '+130', 'DEC': '+190', 'KO/TKO': '+925', 'SUB': '+1360', '1': '+1250', '2': '+1425', '3': '+2075'},
    {'win': '-110', 'DEC': '+120', 'KO/TKO': '+375', 'SUB': '+525', '1': '+425', '2': '+650', '3': '+1225'},
    {'win': '+100', 'DEC': '+325', 'KO/TKO': '+1315', 'SUB': '+2000', '1': '+1725', '2': '+2025', '3': '+2825'},
    {'win': '+100', 'DEC': '+445', 'KO/TKO': '+715', 'SUB': '+250', '1': '+375', '2': '+575', '3': '+1175'},
    {'win': '-110', 'DEC': '+400', 'KO/TKO': '+690', 'SUB': '+250', '1': '+375', '2': '+575', '3': '+1125'},
    {'win': '+105', 'DEC': '+165', 'KO/TKO': '+1180', 'SUB': '+1000', '1': '+1125', '2': '+1450', '3': '+2000'},
    {'win': '-125', 'DEC': '+135', 'KO/TKO': '+885', 'SUB': '+995', '1': '+975', '2': '+1275', '3': '+2050'},
    {'win': '-140', 'DEC': '+155', 'KO/TKO': '+550', 'SUB': '+680', '1': '+625', '2': '+875', '3': '+1550'},
    {'win': '+130', 'DEC': '+335', 'KO/TKO': '+423', 'SUB': '+950', '1': '+575', '2': '+750', '3': '+1450'},
    {'win': '-300', 'DEC': '+530', 'KO/TKO': '+465', 'SUB': '-110', '1': '+150', '2': '+375', '3': '+875'},
    {'win': '+270', 'DEC': '+530', 'KO/TKO': '+750', 'SUB': '+1970', '1': '+1225', '2': '+1525', '3': '+2100'},
    {'win': '+305', 'DEC': '+1016', 'KO/TKO': '+500', 'SUB': '+1300', '1': '+775', '2': '+1000', '3': '+1600'},
    {'win': '-335', 'DEC': '-240', 'KO/TKO': '+1150', 'SUB': '+1440', '1': '+1425', '2': '+1650', '3': '+2225'},
    {'win': '+105', 'DEC': '+425', 'KO/TKO': '+250', 'SUB': '+1045', '1': '+400', '2': '+650', '3': '+1150'},
    {'win': '-115', 'DEC': '+500', 'KO/TKO': '+205', 'SUB': '+525', '1': '+325', '2': '+500', '3': '+950'},
    {'win': '-115', 'DEC': '+475', 'KO/TKO': '+150', 'SUB': '+1400', '1': '+475', '2': '+650', '3': '+850', '4': '+1250', '5': '+2000'},
    {'win': '-105', 'DEC': '+300', 'KO/TKO': '+270', 'SUB': '+1385', '1': '+650', '2': '+850', '3': '+1200', '4': '+1450', '5': '+2000'}
]

##########
# Create the fights
num_fights_sim = 50000
fight_list = []
for idx in range(0, len(fighter_list), 2):
    fight_list.append(Fight(fighter_list[idx], odds[idx], fighter_list[idx + 1], odds[idx + 1], num_fights_sim))

##########
# Create the event
cur_event = Event(*fight_list)
a = cur_event.get_event_outcomes()
# Need to also include salary in the outcome for the LP solver.
# First let's get the names, salaries and points of the first fight
num_fights_per_event = len(names) // 2
nuts_list = []
for universe_idx in range(num_fights_sim):
    names = []
    salaries = []
    points = []
    for fight_idx in range(num_fights_per_event):
        names.append(a[fight_idx][universe_idx][0])
        salaries.append(a[fight_idx][universe_idx][4])
        points.append(a[fight_idx][universe_idx][3])
    nuts_list.append(lps.event_nuts(names, salaries, points))


# Now need to count on nuts_list.
new_nuts = map(tuple, nuts_list)
final_count = Counter(new_nuts)

final_count.most_common(10)
# once in a while a weird bug where only 4 fighters are on the winning card.... not sure where bug lives.

end = time.time()
total_time = end - start
total_time
