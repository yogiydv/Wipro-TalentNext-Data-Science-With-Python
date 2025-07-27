import sys
import os

# Q1) Write a program to accept two numbers as command line arguments and display their sum.
if len(sys.argv) == 3:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print("Sum:", num1 + num2)

# Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.
elif len(sys.argv) == 2:
    print("File Name:", sys.argv[0])
    print("Welcome Message:", sys.argv[1])

# Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.

elif len(sys.argv) == 11:
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    nums = [int(x) for x in sys.argv[1:]]
    prime_sum = sum(n for n in nums if is_prime(n))
    print("Sum of prime numbers:", prime_sum)

else:
    print("Invalid arguments. Please check the question and provide the correct number of arguments.")