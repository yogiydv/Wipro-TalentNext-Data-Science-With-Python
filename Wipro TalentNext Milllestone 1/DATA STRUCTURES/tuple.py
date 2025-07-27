# 1. Write a program to print the 4th element from first and 4th element from last in a tuple.

t = (10, 20, 30, 40, 50, 60, 70)
print("4th element from start:", t[3])
print("4th element from end:", t[-4])


# 2. Write a program to check whether an element exists in a tuple or not.

element = 50
if element in t:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")


# 3. Write a program to convert a list into a tuple.

list1 = [1, 2, 3, 4, 5]
tuple1 = tuple(list1)
print("Converted tuple:", tuple1)


# 4. Write a program to find the index of an item in a tuple.

index_item = 40
index = t.index(index_item)
print(f"Index of {index_item} in tuple:", index)


# 5. Write a program to replace last value of tuples in a list to 100.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

list_of_tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
updated_list = [t[:-1] + (100,) for t in list_of_tuples]
print("Updated list of tuples:", updated_list)
