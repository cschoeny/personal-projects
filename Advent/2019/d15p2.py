# OKAY, so what I need to do is to keep a collection of already visited good points in a set. then, I need to only add to good if not in the set.

import csv
from collections import defaultdict
import copy


class Intcode:

    def __init__(self, filename):
        self.filename = filename
        self.intcode = self.read_intcode(filename)
        self.vanilla_intcode = copy.deepcopy(self.intcode)
        self.idx = 0
        self.relative_base = 0
        self.good_paths = ['EENNEESSSSEEEENNWWNNEENNEEEENNNNNNNNWWSSWWSSEESSWWWWWWWWWWWWSSEESSWWSSWWSSWWNNNNEENNWWNNEENNWWNNEEEESSEENNNNNNEENNEEEEEENNEEEENNWWWWWWWWWWSSWWNNWWSSWWSSSSSSWWWWSSSSSSWWSSSSEESSWWWWWWWWWWWWNNEEEENNNNWWSSWWNNNNNNEESSEEEESSEENNEENNWWNNEENNNNNNNNWWSSWWNNWWSSWWSSWWSSSSEEEENNNNEESSEENN']
        self.test_paths = []
        self.directions = ['N', 'S', 'W', 'E']
        self.dir_int = {'N': 1,
                        'S': 2,
                        'W': 3,
                        'E': 4}
        self.move = {'N': (0, 1),
                     'S': (0, -1),
                     'E': (1, 0),
                     'W': (-1, 0)}
        self.cur_len = len(self.good_paths[0])
        self.word_idx = 0
        self.char_idx = 0
        self.already_visited = []

    def read_intcode(self, filename):
        with open(filename, 'r') as f:
            csv_file = csv.reader(f, delimiter=',')
            for row in csv_file:
                intcode = row
        # Convert to ints
        intcode = [int(num) for num in intcode]
        intcode_dict = defaultdict(int, zip(range(len(intcode)), intcode))
        return intcode_dict

    def reset_intcode(self):
        # self.intcode = self.read_intcode(self.filename)
        self.intcode = copy.deepcopy(self.vanilla_intcode)
        self.idx = 0
        self.relative_base = 0

    def create_test_paths(self):
        # if len(self.test_paths) == 0:
            # self.test_paths = self.directions

        # else:
        if len(self.good_paths) == 0:
            print(f'FINISHED total search with length {self.cur_len}!')
            raise ValueError('Finished')
        self.test_paths = []  # Reset test_paths
        for good_path in self.good_paths:
            for direction in self.directions:
                self.test_paths.append(good_path + direction)
        # import pdb; pdb.set_trace()
        self.good_paths = []  # Also resets the good paths

    def get_current_input_direction(self):
        if len(self.test_paths) == 0:  # only initial creation
            self.create_test_paths()
            self.cur_len += 1
        if self.char_idx == self.cur_len:  # End of current word
            self.word_idx += 1
            self.char_idx = 0
            self.reset_intcode()
            if self.word_idx == len(self.test_paths):  # end of all test paths for current length
                self.create_test_paths()
                self.cur_len += 1
                self.char_idx = 0
                self.word_idx = 0
        # print(f'current length: {self.cur_len}')
        # print(f'current word: {self.word_idx}')
        # print(f'current character: {self.char_idx}')
        cur_input_direction = self.test_paths[self.word_idx][self.char_idx]
        self.char_idx += 1
        return cur_input_direction

    def update_with_output(self, value1):
        if self.char_idx == self.cur_len:  # Final character in word
            if value1 == 1:
                # import pdb; pdb.set_trace()
                # Go through and find final place
                x = 0
                y = 0
                for char in self.test_paths[self.word_idx]:
                    x += self.move[char][0]
                    y += self.move[char][1]
                if (x, y) not in self.already_visited:
                    self.already_visited.append((x, y))
                    self.good_paths.append(self.test_paths[self.word_idx])
            # elif value1 == 2:
            #     print(f'Found the oxygen {self.cur_len} away')
            #     print(f'Final successful path: \n {self.test_paths[self.word_idx]}')
            #     raise ValueError('Finished')

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
        # input_value = int(input("Please enter an input: "))
        input_value = self.dir_int[self.get_current_input_direction()]
        self.intcode[self.literal_location(self.mode1, 1)] = input_value
        self.idx += 2

    def output_4(self):
        # print(self.value1)
        self.update_with_output(self.value1)
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

# from datetime import datetime
# start=datetime.now()
a = Intcode('d15.txt')
a.parse()
# total_time = datetime.now()-start
# total_time
# a.parse()
# a.good_paths
# len(a.test_paths[0])
# a.cur_len
681-280
