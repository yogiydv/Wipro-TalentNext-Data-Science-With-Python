# Q1) Write a program to accept the numbers from the user and perform division.
# If any exception occurs, print an error message or else print the result.

try:
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))
    result = num1 / num2
    print("Result of division:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")
except Exception as e:
    print("Unexpected error:", e)

print("\n" + "-"*50 + "\n")

# Q2) Write a program to accept a number from the user and check whether it's prime or not.
# If user enters anything other than number, handle the exception and print an error message.

try:
    num = int(input("Enter a number to check for prime: "))
    if num < 2:
        print("Not a prime number.")
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print("Not a prime number.")
                break
        else:
            print("It is a prime number.")
except ValueError:
    print("Error: Please enter a valid integer.")

print("\n" + "-"*50 + "\n")

# Q3) Write a program to accept the file name to be opened from the user.
# If file exists print the contents of the file in title case or else handle the exception and print an error message.

try:
    file_name = input("Enter the file name to open: ")
    with open(file_name, 'r') as file:
        content = file.read()
        print("\nFile content in title case:\n")
        print(content.title())
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("Unexpected error:", e)

print("\n" + "-"*50 + "\n")

# Q4) Declare a list with 10 integers and ask the user to enter an Index.
# Check whether the number in that index is positive or negative number.
# If any invalid index is entered, handle the exception and print error message.

numbers = [5, -3, 8, -1, 0, 7, -9, 4, -2, 6]

try:
    index = int(input("Enter an index (0 to 9): "))
    value = numbers[index]
    if value > 0:
        print("The number at index", index, "is Positive.")
    elif value < 0:
        print("The number at index", index, "is Negative.")
    else:
        print("The number at index", index, "is Zero.")
except IndexError:
    print("Error: Invalid index. Please enter an index between 0 and 9.")
except ValueError:
    print("Error: Please enter a valid integer.")
except Exception as e:
    print("Unexpected error:", e)
