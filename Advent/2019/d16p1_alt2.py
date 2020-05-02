# this is to check that all ones keeps the singles digit
import numpy as np
from numpy.linalg import matrix_power

input = '12345678'
input_array = np.fromiter((x for x in input), dtype=int)


base_pattern = [0, 1, 0, -1]
input_length = len(input_array)


def fft_pattern(row):
    new_base = [x for x in base_pattern for _ in range(row + 1)]
    while len(new_base) <= input_length:
        new_base = new_base * 2
    new_base = new_base[1:input_length + 1]
    return np.fromiter((x for x in new_base), dtype=int)


def create_matrix():
    array_list = []
    for row in range(input_length):
        array_list.append(fft_pattern(row))
    return np.array(array_list)

A = create_matrix()
NUM_PHASES = 100
for _ in range(NUM_PHASES):
    # input_array = output_array(np.matmul(A, input_array))
    input_array = np.matmul(A, input_array)

input_array[:8]
