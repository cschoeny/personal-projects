import csv
from fractions import Fraction
from collections import defaultdict


# Read in asteroid locations to tuple list
asteroids = []
row_num = 0
with open('d10p1.txt', 'r') as f:
    csv_file = csv.reader(f, delimiter=',')
    for row_string in csv_file:
        row = [item for item in row_string[0]]
        for col_num in range(len(row)):
            if row[col_num] == '#':
                asteroids.append((col_num, row_num))
        row_num += 1

# Create angle calculator (from point to other point)
def angle(base, asteroid):
    base_x, base_y = base
    ast_x, ast_y = asteroid
    x_del = base_x - ast_x
    y_del = base_y - ast_y

    if x_del == 0:
        if y_del == 0:
            return None
        elif y_del > 0:
            return "inf"
        else:
            return "-inf"
    else:
        return (Fraction(y_del, x_del), x_del>0)

max = 0
asteroid_dict = defaultdict(set)
for cur_asteroid in asteroids:
    # import pdb; pdb.set_trace()
    for all_asteroids in asteroids:
        asteroid_dict[cur_asteroid].add(angle(cur_asteroid, all_asteroids))
    if len(asteroid_dict[cur_asteroid])-1 > max:
        max = len(asteroid_dict[cur_asteroid])-1
        # print(cur_asteroid)

# max
# len(asteroid_dict[(26,29)])

# Asteroid location is (26, 29)
# max value is 304
