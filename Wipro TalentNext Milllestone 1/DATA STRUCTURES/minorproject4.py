                      #Project: 4

# Given a string of n words, help Alex to find out how many times his name appears in the string.
# Constraint: 1 <= n <= 200

# Sample input: Hi Alex WelcomeAlex Bye Alex.
# Sample output: 3

# Explanation:
# Alex name appears 3 times in the string. Hi Alex WelcomeAlex Bye Alex.


# ----------------------- Code -----------------------

def count_alex(input_string):
    count = input_string.count("Alex")
    return count

sample_input = "Hi Alex WelcomeAlex Bye Alex."
sample_output = count_alex(sample_input)

print(f"Sample output: {sample_output}") 
