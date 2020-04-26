import csv

# Read in the list or orbits
orbits_list = []
with open('d6p1.txt', 'r') as f:
    csv = csv.reader(f, delimiter=')')
    for row in csv:
        orbits_list.append(row)

orbits_dict = {}
for orbit in orbits_list:
    orbits_dict[orbit[1]] = orbit[0]


YOU_list = ['YOU']

for planet in YOU_list:
    cur = orbits_dict[planet]
    YOU_list.append(cur)
    if cur == 'COM':
        break

SAN_list = ['SAN']

for planet in SAN_list:
    cur = orbits_dict[planet]
    SAN_list.append(cur)
    if cur == 'COM':
        break

common = [i for i in YOU_list if i in SAN_list]

YOU_list.index(common[0]) + SAN_list.index(common[0]) - 2
