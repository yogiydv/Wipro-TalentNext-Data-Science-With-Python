# 1. Write a LC program to create an output dictionary 
# which contains only the odd numbers
# that are present in the input list = [1,2,3,4,5,6,7] as keys and their cubes as values

input_list = [1,2,3,4,5,6,7]
output_dict = {x: x**3 for x in input_list if x % 2 != 0}
print(output_dict)

# 2. Make a dictionary of the 26 English alphabets 
# mapping each with the corresponding integer.

import string
alphabet_dict = {ch: idx for idx, ch in enumerate(string.ascii_lowercase, 1)}
print(alphabet_dict)