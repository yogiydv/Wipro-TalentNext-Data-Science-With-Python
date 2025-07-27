# Assignment 1: Write a program to remove a given item from the set

sample_set = {1, 2, 3, 4, 5}
item_to_remove = 3
sample_set.discard(item_to_remove)
print("Set after removing item:", sample_set)


# Assignment 2: Write a program to create an intersection of sets

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
intersection = set_a & set_b
print("Intersection of sets:", intersection)


# Assignment 3: Write a program to create a union of sets

set_x = {7, 8, 9}
set_y = {9, 10, 11}
union = set_x | set_y
print("Union of sets:", union)


# Assignment 4: Write a program to find the maximum and minimum value in a set

numeric_set = {15, 3, 9, 27, 6}
max_value = max(numeric_set)
min_value = min(numeric_set)
print("Maximum value:", max_value)
print("Minimum value:", min_value)