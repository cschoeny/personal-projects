# Read in input
input = '80871224585914546619083218645595'
input_list = [int(char) for char in input]


# Create dot product function
def dot(list1, list2):
    return sum(x * y for (x, y) in zip(list1, list2))


# Create function to produce pattern
base_pattern = [0, 1, 0, -1]
input_length = len(input_list)


def fft_pattern(row):
    new_base = [x for x in base_pattern for _ in range(row + 1)]
    while len(new_base) <= input_length:
        new_base = new_base * 2
    return new_base[1:input_length + 2]


NUM_PHASES = 100
cur_output = input_list
for _ in range(NUM_PHASES):
    prev_output = cur_output[:]
    cur_output = []
    for row in range(input_length):
        val = dot(prev_output, fft_pattern(row))
        cur_output.append(int(str(val)[-1]))

print(cur_output)
# dot(prev_output, fft_pattern(0))
# 1894
