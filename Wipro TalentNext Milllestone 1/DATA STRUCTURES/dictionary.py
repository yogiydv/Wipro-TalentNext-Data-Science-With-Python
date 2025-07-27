# 1. Write a program to add a key and value to a dictionary.
# Sample Dictionary: {0: 10, 1: 20}
# Expected Result: {0: 10, 1: 20, 2: 30}

d = {0: 10, 1: 20}
d[2] = 30
print("Updated Dictionary:", d)


# 2. Write a program to concatenate the following dictionaries to create a new one.
# Sample Dictionary: dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50, 6:60}
# Expected Result: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
merged_dict = {**dic1, **dic2, **dic3}
print("Concatenated Dictionary:", merged_dict)


# 3. Write a program to check if a given key already exists in a dictionary.

key_to_check = 3
if key_to_check in merged_dict:
    print(f"Key {key_to_check} exists in the dictionary.")
else:
    print(f"Key {key_to_check} does not exist in the dictionary.")


# 4. Write a program to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values.

print("Keys:")
for key in merged_dict.keys():
    print(key)

print("Values:")
for value in merged_dict.values():
    print(value)

print("Keys and Values:")
for key, value in merged_dict.items():
    print(f"{key}: {value}")


# 5. Write a program to prepare a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of the keys.

squares = {x: x**2 for x in range(1, 16)}
print("Dictionary of Squares:", squares)


# 6. Write a program to sum all the values in a dictionary, considering the values will be of int type.

total = sum(squares.values())
print("Sum of all values:", total)
