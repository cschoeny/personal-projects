import csv
from collections import defaultdict
from math import gcd

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


def get_quad(x_del, y_del):
    if x_del == 0 and y_del > 0:
        quad = 0.5
    elif x_del < 0 and y_del >= 0:
        quad = 1
    elif x_del < 0 and y_del < 0:
        quad = 2
    elif x_del == 0 and y_del < 0:
        quad = 2.5
    elif x_del > 0 and y_del < 0:
        quad = 3
    else:
        quad = 4
    return quad


def get_gcd_tuple(x_del, y_del):
    x, y = x_del / gcd(abs(x_del), abs(y_del)), y_del / gcd(abs(x_del), abs(y_del))
    return (x, y)


def quad_frac_man(base, asteroid):
    if base == asteroid:
        assert ValueError("shouldn't pass in the base itself as the asteroid")
    base_x, base_y = base
    ast_x, ast_y = asteroid
    x_del = base_x - ast_x
    y_del = base_y - ast_y

    # Calculate Quadrant
    quad = get_quad(x_del, y_del)

    # Calculate gcd tuple
    angle_tuple = get_gcd_tuple(x_del, y_del)

    # Calculate the manhattan distance
    man_dist = abs(x_del) + abs(y_del)

    return (quad, angle_tuple, man_dist)


# Answer from part 1
base = (29, 26)
# Remove the base from the list of asteroids
asteroids.remove(base)

# Create the asteroids_dict with all data
# Create the diff_count defaultdict
asteroids_dict = defaultdict(list)
diff_count = defaultdict(int)
for asteroid in asteroids:
    cur_quad, cur_angle, _ = quad_frac_man(base, asteroid)
    asteroids_dict[cur_quad].append(quad_frac_man(base, asteroid))
    diff_count[cur_angle] += 1


# Now need to arrange all the angles in order.
def sort_angles_in_quad(quad):
    angles = set()
    for tup in quad:
        cur_angle = tup[1]
        angles.add(cur_angle)
    cur_angles = list(angles)
    return sorted(cur_angles, key=lambda x: (x[1] / x[0]))

ordered_angles = []
ordered_angles.append(asteroids_dict[0.5][0][1])
ordered_angles.extend(sort_angles_in_quad(asteroids_dict[1]))
ordered_angles.extend(sort_angles_in_quad(asteroids_dict[2]))
ordered_angles.append(asteroids_dict[2.5][0][1])
ordered_angles.extend(sort_angles_in_quad(asteroids_dict[3]))
ordered_angles.extend(sort_angles_in_quad(asteroids_dict[4]))

ordered_angles

# Now we need to repeatedly through the ordered angles and decrement from the counter until 200.
destroyed = 0
for cur_angle in ordered_angles:
    if diff_count[cur_angle] != 0:
        diff_count[cur_angle] -= 1
        destroyed += 1

ordered_angles[199]

# The diff is (22, 21) so I need to add base to it
ordered_angles[199]
base
