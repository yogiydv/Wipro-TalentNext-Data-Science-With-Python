"""
Q1) Write a program to read the entire content from a txt file and display it to the user.
"""

def read_entire_file(filename):
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found.")

"""
Q2) Write a program to read first n lines from a txt file. Get n as user input.
"""

def read_n_lines(filename, n):
    try:
        with open(filename, 'r') as file:
            for i in range(n):
                print(file.readline(), end='')
    except FileNotFoundError:
        print("File not found.")

"""
Q3) Write a program to accept input from user and append it to a txt file.
"""

def append_input_to_file(filename):
    try:
        user_input = input("Enter the text to append: ")
        with open(filename, 'a') as file:
            file.write(user_input + '\n')
    except Exception as e:
        print(f"An error occurred: {e}")

"""
Q4) Write a program to read contents from a txt file line by line and store each line into a list.
"""

def file_lines_to_list(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        return [line.strip() for line in lines]
    except FileNotFoundError:
        print("File not found.")
        return []

"""
Q5) Write a program to find the longest word from the txt file contents, assuring that the file will have only one longest word in it.
"""

def find_longest_word(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().split()
        longest = max(words, key=len)
        print("Longest word:", longest)
    except FileNotFoundError:
        print("File not found.")

"""
Q6) Write a program to count the frequency of a user entered word in a txt file.
"""

def count_word_frequency(filename, word):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(f"Frequency of '{word}':", content.split().count(word))
    except FileNotFoundError:
        print("File not found.")
