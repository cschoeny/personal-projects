# Read in input
input = '59718730609456731351293131043954182702121108074562978243742884161871544398977055503320958653307507508966449714414337735187580549358362555889812919496045724040642138706110661041990885362374435198119936583163910712480088609327792784217885605021161016819501165393890652993818130542242768441596060007838133531024988331598293657823801146846652173678159937295632636340994166521987674402071483406418370292035144241585262551324299766286455164775266890428904814988362921594953203336562273760946178800473700853809323954113201123479775212494228741821718730597221148998454224256326346654873824296052279974200167736410629219931381311353792034748731880630444730593'
input_list = [int(char) for char in input]
input_list = input_list * 10000
# where to start
start_idx = len(input_list) - 5971873
# start_idx

# part 2
# input_list = input_list * 10000
# len(input_list)

# Create dot product function


def dot(list1, list2):
    return sum(x * y for (x, y) in zip(list1, list2))


# Create function to produce pattern
base_pattern = [0, 1, 0, -1]
input_length = len(input_list)


def fft_pattern(row):
    new_base = [x for x in base_pattern for _ in range(row + 1)]
    while len(new_base) <= input_length:
        new_base = new_base * 10
    return new_base[start_idx + 1:input_length + 1]


NUM_PHASES = 1
cur_output = input_list[start_idx:]
for _ in range(NUM_PHASES):
    prev_output = cur_output[:]
    cur_output = []
    for row in range(start_idx, input_length):
        # import pdb; pdb.set_trace()
        val = dot(prev_output, fft_pattern(row))
        cur_output.append(int(str(val)[-1]))

final_output_list = cur_output

print(final_output_list[:8])
