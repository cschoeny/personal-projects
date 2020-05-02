nums = []

with open('d1p1.txt', 'r') as f:
    line = f.readline()
    while line:
        nums.append(int(line))
        line = f.readline()


# Going to use recursion to calculate total fuel
def calc_total_fuel(mass):
    if mass < 9:
        return 0
    else:
        return mass//3-2 + calc_total_fuel(mass//3-2)


ans = sum([calc_total_fuel(cur) for cur in nums])

ans
