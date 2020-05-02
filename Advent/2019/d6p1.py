import csv
from collections import defaultdict

# Read in the list or orbits
orbits_list = []
with open('d6p1.txt', 'r') as f:
    csv = csv.reader(f, delimiter=')')
    for row in csv:
        orbits_list.append(row)

orbits_dict = defaultdict(list)
for orbit in orbits_list:
    orbits_dict[orbit[0]].append(orbit[1])

current_planets = ['COM']
orbit_dist = {'COM': 0}
for planet in current_planets:
    current_orbits_list = orbits_dict[planet]
    for current_orbit in current_orbits_list:
        orbit_dist[current_orbit] = orbit_dist[planet]+1
        current_planets.append(current_orbit)

sum(val for _, val in orbit_dist.items())
