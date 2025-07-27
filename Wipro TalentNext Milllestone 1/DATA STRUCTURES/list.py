# 1. Write a program to create a list of 5 integers and display the list items. Access individual elements through index.

int_list = [10, 20, 30, 40, 50]
print("List:", int_list)
print("Accessing elements by index:")
for i in range(len(int_list)):
    print(f"Element at index {i}: {int_list[i]}")

# 2. Write a program to append a new item to the end of the list.

int_list.append(60)
print("\nAfter appending 60:", int_list)

# 3. Write a program to reverse the order of the items in the list.

int_list.reverse()
print("\nReversed list:", int_list)

# 4. Write a program to print the number of occurrences of a specified element in a list.

element = 30
count = int_list.count(element)
print(f"\nNumber of occurrences of {element}: {count}")

# 5. Write a program to append the items of list1 to list2 in the front.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list2 = list1 + list2
print("\nAfter appending list1 to front of list2:", list2)

# 6. Write a program to insert a new item before the second element in an existing list.

list2.insert(1, 99)
print("\nAfter inserting 99 before second element:", list2)

# 7. Write a program to remove the item from a specified index in a list.

del list2[3]
print("\nAfter removing item at index 3:", list2)

# 8. Write a program to remove the first occurrence of a specified element from a list.

list2.remove(99)
print("\nAfter removing first occurrence of 99:", list2)
