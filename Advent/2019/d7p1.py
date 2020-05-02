import csv
from itertools import permutations

# Read in the intcode
with open('d7p1.txt', 'r') as f:
    csv = csv.reader(f, delimiter=',')
    for row in csv:
        intcode = row


# Convert to ints
intcode = [int(num) for num in intcode]


def p5(setting, prev_output):
    inputs = 0
    # import pdb; pdb.set_trace()
    idx = 0
    while True:
        # import pdb; pdb.set_trace()
        opcode = str(intcode[idx]).zfill(5)
        # Break if opcode is 99
        opcode_val = int(opcode[-1])
        if opcode_val == 9:
            return
        elif opcode_val == 1 or opcode_val == 2:
            mode3, mode2, mode1 = opcode[:3]
            value1 = intcode[idx + 1]
            if mode1 == '0':
                value1 = intcode[value1]
            value2 = intcode[idx + 2]
            if mode2 == '0':
                value2 = intcode[value2]
            location = idx + 3
            if mode3 == '0':
                location = intcode[location]
            if opcode_val == 1:
                intcode[location] = value1 + value2
            else:
                intcode[location] = value1 * value2
            idx += 4
        elif opcode_val == 3:
            # v1 = int(input("Please enter an input: "))
            if inputs == 0:
                v1 = setting
                inputs += 1
            else:
                v1 = prev_output
            location = idx + 1
            if opcode[2] == '0':
                location = intcode[location]
            intcode[location] = v1
            idx += 2
        elif opcode_val == 4:
            if opcode[2] == '0':
                # print(f'{intcode[intcode[idx+1]]}')
                return intcode[intcode[idx+1]]
            else:
                # print(f'{intcode[idx+1]}')
                return intcode[idx+1]
            idx += 2
        elif opcode_val == 5 or opcode_val == 6:
            _, mode2, mode1 = opcode[:3]
            value1 = intcode[idx + 1]
            if mode1 == '0':
                value1 = intcode[value1]
            value2 = intcode[idx + 2]
            if mode2 == '0':
                value2 = intcode[value2]
            if opcode_val == 5:
                if value1 != 0:
                    idx = value2
                else:
                    idx += 3
            else:
                if value1 == 0:
                    idx = value2
                else:
                    idx += 3
        elif opcode_val == 7 or opcode_val == 8:
            mode3, mode2, mode1 = opcode[:3]
            value1 = intcode[idx + 1]
            if mode1 == '0':
                value1 = intcode[value1]
            value2 = intcode[idx + 2]
            if mode2 == '0':
                value2 = intcode[value2]
            location = idx + 3
            if mode3 == '0':
                location = intcode[location]
            if opcode_val == 7:
                if value1 < value2:
                    intcode[location] = 1
                else:
                    intcode[location] = 0
            else:
                if value1 == value2:
                    intcode[location] = 1
                else:
                    intcode[location] = 0
            idx += 4
        else:
            print(opcode)
            print(opcode_val)
            raise ValueError('Bad OPCODE')


# Enumerate all the combos (5! of them) call it combos
combos = list(permutations([0, 1, 2, 3, 4]))


max = 0
for combo in combos:
    # import pdb; pdb.set_trace()
    amp_a = p5(combo[0], 0)
    amp_b = p5(combo[1], amp_a)
    amp_c = p5(combo[2], amp_b)
    amp_d = p5(combo[3], amp_c)
    amp_e = p5(combo[4], amp_d)
    if amp_e > max:
        max = amp_e

max
