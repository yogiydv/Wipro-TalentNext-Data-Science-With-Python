
# Q1) Write a function to return the sum of all numbers in a list.
# Sample List: (8, 2, 3, 0, 7)
# Expected Output: 20

def sum_of_list(numbers):
    return sum(numbers)

print("Q1 Output:", sum_of_list([8, 2, 3, 0, 7]))

print("\n" + "-"*50 + "\n")

# Q2) Write a function to return the reverse of a string.
# Sample String: "1234abcd"
# Expected Output: "dcba4321"

def reverse_string(s):
    return s[::-1]

print("Q2 Output:", reverse_string("1234abcd"))

print("\n" + "-"*50 + "\n")

# Q3) Write a function to calculate and return the factorial of a number (a non-negative integer).

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

print("Q3 Output:", factorial(5))

print("\n" + "-"*50 + "\n")

# Q4) Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.

def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    print("No. of Upper case characters:", upper)
    print("No. of Lower case characters:", lower)

print("Q4 Output:")
count_case("Hello World")

print("\n" + "-"*50 + "\n")

# Q5) Write a function to print the even numbers from a given list.
# List is passed to the function as an argument.
# Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result: [2, 4, 6, 8]

def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

print("Q5 Output:", even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))

print("\n" + "-"*50 + "\n")

# Q6) Write a function that takes a number as a parameter and checks whether the number is prime or not.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Q6 Output: Is 7 prime?", is_prime(7))
