nums = []

with open('d1p1.txt', 'r') as f:
    line = f.readline()
    while line:
        nums.append(int(line))
        line = f.readline()


def calc_fuel(mass_list):
    return sum([val//3-2 for val in mass_list])


ans = calc_fuel(nums)
ans
