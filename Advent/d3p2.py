def get_new_path(cur, command):
    """
    cur: tuple of ints. ex: (2, 14)
    command: str: ex: 'R12'
    """
    new_path = [cur]
    direction = command[0]
    cur_x = cur[0]
    cur_y = cur[1]
    if direction == 'R':
        for step in range(1, int(command[1:]) + 1):
            new_path.append((cur_x + step, cur_y))
    elif direction == 'L':
        for step in range(1, int(command[1:]) + 1):
            new_path.append((cur_x - step, cur_y))
    elif direction == 'U':
        for step in range(1, int(command[1:]) + 1):
            new_path.append((cur_x, cur_y + step))
    elif direction == 'D':
        for step in range(1, int(command[1:]) + 1):
            new_path.append((cur_x, cur_y - step))
    else:
        raise ValueError('Bad direction input')
    return new_path[1:]

# First go get list for first one.


# Get the lists of commands
with open('d3p1.txt', 'r') as f:
    line = f.readline()
    line = line.split(",")
    commands_1 = line
    line = f.readline()
    line = line.split(",")
    commands_2 = line

# Get the paths both traverse
path_1 = [(0, 0)]
for command in commands_1:
    cur = path_1[-1]
    path_1.extend(get_new_path(cur, command))

path_2 = [(0, 0)]
for command in commands_2:
    cur = path_2[-1]
    path_2.extend(get_new_path(cur, command))

# Drop the initial point cause it doesn't count
path_1 = path_1[1:]
path_2 = path_2[1:]

# Need to get them in sets and then see the intersection of the sets
path_1_set = set(path_1)
path_2_set = set(path_2)

intersection = path_1_set & path_2_set

path_1.index((1, 0))

# This should be very similar, instead of manhattan distance need to add first location in each path
min = 1000000
for location in intersection:
    min_traverse = path_1.index(location) + path_2.index(location) + 2  # Need to add 2 because of indexing at 0
    if min_traverse < min:
        min = min_traverse

min
