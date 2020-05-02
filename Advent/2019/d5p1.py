import csv

# Read in the intcode
with open('d5p1.txt', 'r') as f:
    csv = csv.reader(f, delimiter=',')
    for row in csv:
        intcode = row


# Convert to ints
intcode = [int(num) for num in intcode]

# OPCODES:
# 1: addition (3 more parameter)
# 2: multiplication (3 more parameters)
# 3: input (1 parameter)
# 4: output (1 parameter)
# PARAMETER MODES
# 0: position mode
# 1: immediate mode
# Loop until we break or terminate


def p5():
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
            v1 = int(input("Please enter an input: "))
            location = idx + 1
            if opcode[2] == '0':
                location = intcode[location]
            intcode[location] = v1
            idx += 2
        elif opcode_val == 4:
            if opcode[2] == '0':
                print(f'{intcode[intcode[idx+1]]}')
            else:
                print(f'{intcode[idx+1]}')
            idx += 2
        else:
            print(opcode)
            print(opcode_val)
            raise ValueError('Bad OPCODE')


p5()
