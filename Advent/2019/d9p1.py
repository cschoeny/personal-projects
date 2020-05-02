import csv


class Intcode:
    NUM_ZEROS = 100000

    def __init__(self, filename):
        self.intcode = self.read_intcode(filename)
        self.idx = 0
        self.relative_base = 0

    def read_intcode(self, filename):
        with open(filename, 'r') as f:
            csv_file = csv.reader(f, delimiter=',')
            for row in csv_file:
                intcode = row
        # Convert to ints
        intcode = [int(num) for num in intcode]
        # Append zeros buffer
        zeros = [0] * self.NUM_ZEROS
        intcode.extend(zeros)
        return intcode

    @property
    def value1(self):
        return self.get_value(self.mode1, 1)

    @property
    def value2(self):
        return self.get_value(self.mode2, 2)

    def location(self, mode, diff):
        loc = self.idx + diff
        if mode == '0':
            loc = self.intcode[loc]
        elif mode == '2':
            loc = self.intcode[loc + self.relative_base]
        return loc

    @property
    def mode1(self):
        return self.opcode[2]

    @property
    def mode2(self):
        return self.opcode[1]

    @property
    def mode3(self):
        return self.opcode[0]

    @property
    def opcode(self):
        return str(self.intcode[self.idx]).zfill(5)

    @property
    def opcode_val(self):
        return self.opcode[-2:]

    def get_value(self, mode, position):
        value = self.intcode[self.idx + position]
        if mode == '0':
            value = self.intcode[value]
        elif mode == '2':
            value = self.intcode[value + self.relative_base]
        return value

    def addition_1(self):
        self.intcode[self.location(self.mode3, 3)] = self.value1 + self.value2
        self.idx += 4

    def multiplication_2(self):
        self.intcode[self.location(self.mode3, 3)] = self.value1 * self.value2
        self.idx += 4

    def input_3(self):
        input_value = int(input("Please enter an input: "))
        self.intcode[self.location(self.mode1, 1)] = input_value
        self.idx += 2

    def output_4(self):
        print(self.value1)
        self.idx += 2

    def jump_true_5(self):
        if self.value1 != 0:
            self.idx = self.value2
        else:
            self.idx += 3

    def jump_false_6(self):
        if self.value1 == 0:
            self.idx = self.value2
        else:
            self.idx += 3

    def less_than_7(self):
        if self.value1 < self.value2:
            self.intcode[self.location(self.mode3, 3)] = 1
        else:
            self.intcode[self.location(self.mode3, 3)] = 0
        self.idx += 4

    def equal_8(self):
        if self.value1 == self.value2:
            self.intcode[self.location(self.mode3, 3)] = 1
        else:
            self.intcode[self.location(self.mode3, 3)] = 0
        self.idx += 4

    def base_change_9(self):
        self.relative_base += self.value1
        self.idx += 2

    def perform_action(self):
        if self.opcode_val == '01':
            self.addition_1()
        elif self.opcode_val == '02':
            self.multiplication_2()
        elif self.opcode_val == '03':
            self.input_3()
        elif self.opcode_val == '04':
            self.output_4()
        elif self.opcode_val == '05':
            self.jump_true_5()
        elif self.opcode_val == '06':
            self.jump_false_6()
        elif self.opcode_val == '07':
            self.less_than_7()
        elif self.opcode_val == '08':
            self.equal_8()
        elif self.opcode_val == '09':
            self.base_change_9()
        else:
            raise ValueError('Bad OPCODE')

    def parse(self):
        while True:
            # import pdb; pdb.set_trace()
            if self.opcode_val == '99':
                break
            else:
                self.perform_action()


a = Intcode('d9p1.txt')

# Passes this test
# a.intcode = [1102,34915192,34915192,7,4,7,99,0]
# a.parse()

# Passes this test
# a.intcode = [104,1125899906842624,99]
# a.parse()

# Fails this, out of range
a.intcode = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
a.parse()
