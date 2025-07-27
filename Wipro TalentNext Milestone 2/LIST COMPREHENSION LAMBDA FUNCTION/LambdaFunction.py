# 1. Cube every number in the given list using a lambda function.

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cubed_list = list(map(lambda x: x ** 3, list_1))
print(cubed_list)