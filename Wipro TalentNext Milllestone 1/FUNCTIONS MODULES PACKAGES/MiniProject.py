"""
Project: 1

Write a Python function that accepts a hyphen-separated sequence of colors as input 
and returns the colors in a hyphen-separated sequence after sorting them alphabetically.

Constraint: All the colors will be completely in either lower case or upper case.

Sample input1: green-red-yellow-black-white  
Sample output1: black-green-red-white-yellow

Sample input2: PINK-BLUE-TAN-PURPLE  
Sample output2: BLUE-PINK-PURPLE-TAN
"""

def sort_colors(color_sequence): 
    color_list = color_sequence.split('-')
    sorted_list = sorted(color_list)
    return '-'.join(sorted_list)

print("=== Project 1 ===")
input1 = "green-red-yellow-black-white"
print("Sample output1:", sort_colors(input1))

input2 = "PINK-BLUE-TAN-PURPLE"
print("Sample output2:", sort_colors(input2))

print("\n=== Project 2 ===")
"""
Project: 2

Create a Python module with the following functions:
Function Name Task ispalindrome(name)
Given the user name as input, this function should tell us whether the name is a palindrome or not.
count_the_vowels(name) Given the user name as input, this function should tell us how many vowels are present in it.
frequency_of_letters(name) Given the user name as input, this function should tell us 
how many times each letter appears in the name.

Note: name will be completely in either lower case or upper case.
Import the module in another python script and test the functions by passing appropriate inputs.

Sample input1: bob
Sample output 1: Yes it is a palindrome.
No of vowels: 1
Frequency of letters: b-2, o-1

Sample input2: marcelbentok tanaka
Sample output 2: No it is not a palindrome.
No of vowels: 7
Frequency of letters: m-1, a-4, r-1, c-1, e-2, l-1, b-1, n-2, t-2, o-1, k-2
"""

def ispalindrome(name):
    name = name.replace(" ", "")
    if name == name[::-1]:
        return "Yes it is a palindrome."
    else:
        return "No it is not a palindrome."

def count_the_vowels(name):
    vowels = "aeiouAEIOU"
    return sum(1 for char in name if char in vowels)

def frequency_of_letters(name):
    freq = {}
    for char in name.replace(" ", ""):
        freq[char] = freq.get(char, 0) + 1
    return ', '.join(f"{k}-{v}" for k, v in sorted(freq.items()))

name1 = "bob"
print("Input:", name1)
print(ispalindrome(name1))
print("No of vowels:", count_the_vowels(name1))
print("Frequency of letters:", frequency_of_letters(name1))

print()

name2 = "marcelbentok tanaka"
print("Input:", name2)
print(ispalindrome(name2))
print("No of vowels:", count_the_vowels(name2))
print("Frequency of letters:", frequency_of_letters(name2))