from collections import Counter
import time

import lib.pandas_utils as pu
import lib.LP_solver as lps
import lib.scrape_ufc_stats as sus
import lib.scrape_odds as so

from lib.Fighter_Class import Fighter
from lib.Fight_Class import Fight
from lib.Event_Class import Event

##################################################
# # Update UFC stats (only need to run once anytime in the week to add the latest event)
# # LAST RUN: 10/2/19
# sus.add_new_event('http://ufcstats.com/event-details/1bf49bf829964144')
# pu.read_clean_save_event_stats()
# pu.read_clean_save_fight_stats()
# pu.merge_two_stat_sources_and_score()

##################################################
# Create the Fighters
date_of_event = '2019-10-05'
names, salaries = pu.parse_dk(date_of_event)

# Get the full odds table
table = so.get_odds_table(2)

# Properly format the names in accordance with the odds table
# Keep editing these until the function prints an empty list
names
names[5] = 'Zarah Fairn Dos Santos'
names[-1] = 'Sergey Spivak'
print(so.full_names_that_need_cleaning(names, table))

# Properly format the short names in accordance with the odds table
# Keep editing these until the function prints an empty list
short_names = ['Whittaker',
               'Adesanya',
               'Akman',
               'Matthews',
               'Anderson',
               'Santos',
               'Castro',
               'Tafa',
               'Iaquinta',
               'Hooker',
               'Jumeau',
               'Lima',
               'Kassem',
               'Kim',
               'Riddell',
               'Mullarkey',
               'Pitolo',
               'Potter',
               'Taha',
               'Silva',
               'Tuivasa',
               'Spivak']

print(so.short_names_that_need_cleaning(short_names, table))

# Assign which fights are 5 round fights
championship = [False] * len(names)
championship[0], championship[1] = (True, True)

# Create the odds list of dictionaries
odds = []
for full_name, short_name, five_round in zip(names, short_names, championship):
    odds.append(so.get_odds_for_fighter(full_name, short_name, table, five_round))


# Manually create the weightclasses
weightclasses = [
    "Middleweight",
    "Middleweight",
    "Welterweight",
    "Welterweight",
    "Women's Featherweight",
    "Women's Featherweight",
    "Heavyweight",
    "Heavyweight",
    "Lightweight",
    "Lightweight",
    "Welterweight",
    "Welterweight",
    "Women's Flyweight",
    "Women's Flyweight",
    "Lightweight",
    "Lightweight",
    "Welterweight",
    "Welterweight",
    "Bantamweight",
    "Bantamweight",
    "Heavyweight",
    "Heavyweight"
]

# Create the list of Fighters
fighter_attributes = list(zip(names, salaries, weightclasses, championship))
fighter_list = [Fighter(*fighter_attribute) for fighter_attribute in fighter_attributes]

##################################################
# Create the fights
start = time.time()

num_fights_sim = 100000
fight_list = []
for idx in range(0, len(fighter_list), 2):
    fight_list.append(Fight(fighter_list[idx], odds[idx], fighter_list[idx + 1], odds[idx + 1], num_fights_sim))

# Create the event
cur_event = Event(*fight_list)
a = cur_event.get_event_outcomes()
num_fights_per_event = len(weightclasses) // 2
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


end = time.time()
total_time = end - start
total_time

final_count.most_common(100)

#how many couldn't choose 6 winners
bad=0
for entry in nuts_list:
    if len(entry)!=6:
        bad+=1

bad/num_fights_sim


### TODO:
# Build a simple LP to calculate the LU with highest odds of having 6/6. (non-stacked might make it a big difficult though)
    # the reason to do this is to make sure that the DK points and methods system is actually having some affect and not just calculating the highest prob one
# Build a way to manually select a fighter (do this before my girl Joanna fights).
