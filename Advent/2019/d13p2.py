import csv
from collections import defaultdict


class Intcode:

    def __init__(self, filename):
        self.intcode = self.read_intcode(filename)
        self.idx = 0
        self.relative_base = 0

        self.display = []
        self.paddle_x = None
        self.ball_x = None
        self.num_blocks = 0
        self.current_score = 0

    def read_intcode(self, filename):
        with open(filename, 'r') as f:
            csv_file = csv.reader(f, delimiter=',')
            for row in csv_file:
                intcode = row
        # Convert to ints
        intcode = [int(num) for num in intcode]
        intcode_dict = defaultdict(int, zip(range(len(intcode)), intcode))
        return intcode_dict

    @property
    def value1(self):
        return self.get_value(self.mode1, 1)

    @property
    def value2(self):
        return self.get_value(self.mode2, 2)

    def literal_location(self, mode, diff):
        loc = self.intcode[self.idx + diff]
        if mode == '2':
            loc += self.relative_base
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

    @property
    def move_direction(self):
        if self.paddle_x == self.ball_x:
            return 0
        elif self.paddle_x < self.ball_x:
            return 1
        else:
            return -1

    def get_value(self, mode, position):
        value = self.intcode[self.idx + position]
        if mode == '0':
            value = self.intcode[value]
        elif mode == '2':
            value = self.intcode[value + self.relative_base]
        return value

    def addition_1(self):
        self.intcode[self.literal_location(self.mode3, 3)] = self.value1 + self.value2
        self.idx += 4

    def multiplication_2(self):
        self.intcode[self.literal_location(self.mode3, 3)] = self.value1 * self.value2
        self.idx += 4

    def input_3(self):
        # When we get here we should have a whole display scren
        # input_value = int(input("Please enter an input: "))
        input_value = self.move_direction
        # import pdb; pdb.set_trace()
        # print(f'Paddle loc: {self.paddle_x}')
        # print(f'Ball loc: {self.ball_x}\n')

        self.intcode[self.literal_location(self.mode1, 1)] = input_value
        # Need to reset stuff
        if self.num_blocks == 0:
            pass
            # print(self.current_score)
        else:
            self.num_blocks = 0
        self.idx += 2

    def output_4(self):
        self.display.append(self.value1)
        if len(self.display) == 3:
            # Check if paddle
            if self.display[-1] == 3:
                self.paddle_x = self.display[0]
            # Check if ball
            elif self.display[-1] == 4:
                self.ball_x = self.display[0]
            # Check if block
            elif self.display[-1] == 2:
                self.num_blocks += 1
            elif self.display[0] == -1 and self.display[1] == 0:
                self.current_score = self.display[-1]
            # Reset display to empty
            self.display = []
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
            self.intcode[self.literal_location(self.mode3, 3)] = 1
        else:
            self.intcode[self.literal_location(self.mode3, 3)] = 0
        self.idx += 4

    def equal_8(self):
        if self.value1 == self.value2:
            self.intcode[self.literal_location(self.mode3, 3)] = 1
        else:
            self.intcode[self.literal_location(self.mode3, 3)] = 0
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
            if self.opcode_val == '99':
                break
            else:
                self.perform_action()


a = Intcode('d13.txt')
a.parse()
a.current_score
