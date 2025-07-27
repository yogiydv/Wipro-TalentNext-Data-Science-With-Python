# Question 1: Write a program to count the number of upper and lower case letters in a String.

def count_upper_lower(input_string):
    upper_count = 0
    lower_count = 0
    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

# Question 2: Write a program that will check whether a given String is Palindrome or not.

def is_palindrome(input_string):
    cleaned_string = "".join(filter(str.isalnum, input_string)).lower()
    return cleaned_string == cleaned_string[::-1]

# Question 3: Given a string, return a new string made of n copies of the first 2 chars of the
# original string where n is the length of the string. The string length will be >=2.
# If input is "Wipro" then output should be "WiWiWiWiWi".

def repeat_first_two_chars(input_string):
    if len(input_string) < 2:
        return input_string * len(input_string)
    first_two = input_string[:2]
    n = len(input_string)
    return first_two * n

# Question 4: Given a string, if the first or last character is 'x', return the string without
# those 'x' character, else return the string unchanged. If the input is "xHix", then output is "Hi".

def remove_x_ends(input_string):
    result = input_string
    if len(result) > 0 and result[0] == 'x':
        result = result[1:]
    if len(result) > 0 and result[-1] == 'x':
        result = result[:-1]
    return result

# Question 5: Given a string and an integer n, return a string made of n repetitions of the last n
# characters of the string. You may assume that n is between 0 and the length of the string inclusive.
# For example if the inputs are "Wipro" and 3, then the output should be "propropro".

def repeat_last_n_chars(input_string, n):
    if not (0 <= n <= len(input_string)):
        return ""
    if n == 0:
        return ""
    last_n_chars = input_string[-n:]
    return last_n_chars * n
