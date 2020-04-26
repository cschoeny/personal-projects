from math import ceil
import csv
import re
from collections import defaultdict

lines = []
with open('d14.txt', 'r') as f:
    csv_file = csv.reader(f, delimiter='=')
    for row in csv_file:
        line = row
        lines.append(line)

# Read in the data in dict to list tuple form
nums = '[0-9]'
letters = '[a-zA-Z]+'
mat_dict = defaultdict(list)
for line in lines:
    key = line[-1]
    clean = re.sub('\W', '', key)
    cur_material = re.sub(nums, '', clean)
    mat_dict[cur_material].append(int(re.sub(letters, '', clean)))
    materials = line[0].split(',')
    for material in materials:
        clean_material = re.sub('\W', '', material)
        mat_dict[cur_material].append((int(re.sub(letters, '', clean_material)), re.sub(nums, '', clean_material)))


# def get_num_material(num, element):
#     """
#     num is the number of element needed.
#     first thing to be passed in should be (1 Fuel) final answer should be in terms of ore.
#     """
#     materials = mat_dict[element]
#     # Calculate number of reactions needed
#     reactions = ceil(num / materials[0])
#     # Base case of recursion
#     if materials[1][1] == 'ORE':
#         # print(materials[1][0] * reactions)
#         return materials[1][0] * reactions
#
#     for idx in range(1, len(materials)):
#         # print((materials[idx][0] * reactions, materials[idx][1]))
#         get_num_material(materials[idx][0] * reactions, materials[idx][1])


# core_element = defaultdict(int)
#
#
# def get_num_material2(num, element):
#     """
#     num is the number of element needed.
#     first thing to be passed in should be (1 Fuel) final answer should be in terms of ore.
#     """
#     materials = mat_dict[element]
#     # Base case of recursion
#     if materials[1][1] == 'ORE':
#         # print(materials[1][0] * reactions)
#         core_element[element] += num
#         return
#     # Calculate number of reactions needed
#     reactions = ceil(num / materials[0])
#     for idx in range(1, len(materials)):
#         # print((materials[idx][0] * reactions, materials[idx][1]))
#         get_num_material2(materials[idx][0] * reactions, materials[idx][1])
#
#
#
# get_num_material2(1, 'FUEL')
# # core_element
#
# # mat_dict
# ore = 0
# for element in core_element:
#     # import pdb; pdb.set_trace()
#     ore += ceil(core_element[element] / mat_dict[element][0]) * mat_dict[element][1][0]
# ore
# core_element


core_element = defaultdict(int)
garbage = defaultdict(int)

def get_num_material3(num, element):
    """
    num is the number of element needed.
    first thing to be passed in should be (1 Fuel) final answer should be in terms of ore.
    doing some extra garbage collection for non core materials
    """
    materials = mat_dict[element]
    # Base case of recursion
    if materials[1][1] == 'ORE':
        # print(materials[1][0] * reactions)
        core_element[element] += num
        return
    # Calculate number of reactions needed
    extra = garbage[element]
    new_needed = num - extra
    reactions = ceil(new_needed / materials[0])
    garbage[element] = (reactions * materials[0]) - new_needed
    for idx in range(1, len(materials)):
        # print((materials[idx][0] * reactions, materials[idx][1]))
        get_num_material3(materials[idx][0] * reactions, materials[idx][1])


get_num_material3(1893569, 'FUEL')
# core_element

# mat_dict
ore = 0
for element in core_element:
    # import pdb; pdb.set_trace()
    ore += ceil(core_element[element] / mat_dict[element][0]) * mat_dict[element][1][0]


print(ore)
