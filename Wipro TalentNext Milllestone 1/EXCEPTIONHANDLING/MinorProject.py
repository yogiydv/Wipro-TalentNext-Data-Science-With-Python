'''PROJECT1:- You had saved the items and their price details in a text file, which you
purchased yesterday from a nearby super market.

You need to know:
1. How many items did you purchase?
2. How many items are free?
3. What is the total amount you had to pay?
4. What is the discount amount?
5. What is the final amount did you pay after the discount?

Help yourself by writing a python code to do this. Include necessary code to handle the possible exceptions.

Note:
     #Data is stored in a text file Purchase-1.txt.
     # Each line contains one item's details.
     # Item name and price is separated by a space.
     # You have to enter the file name during run time.

Sample input 1:  Purchase-1.txt
Chocolate 50
Biscuit 35
Icecream 50
(blank line)
Discount 5

Sample output 1:
Enter the file name: Purchase-1
No of items purchased: 3
No of free items: 0
Amount to pay: 135
Discount given: 5
Final amount paid: 130

Sample input 2:  Purchase-2.txt
Chocolate 50
Biscuit 35
Icecream 50
Rice 100
Chicken 250
(blank line)
Perfume Free
Soup Free
(blank line)
Discount 80

Sample output 2:
Enter the file name: Purchase-2
No of items purchased: 5
No of free items: 2
Amount to pay: 485
Discount given: 80
Final amount paid: 405
'''
def process_purchase_file():
    try:
        file_name = input("Enter the file name: ").strip()
        if not file_name.endswith(".txt"):
            file_name += ".txt"

        with open(file_name, 'r') as file:
            lines = file.readlines()

        total_amount = 0
        discount = 0
        item_count = 0
        free_items = 0

        for line in lines:
            line = line.strip()
            if not line:
                continue  # skip blank lines

            parts = line.split()

            if len(parts) == 2:
                item, price = parts
                if price.lower() == "free":
                    free_items += 1
                elif item.lower() == "discount":
                    try:
                        discount = int(price)
                    except ValueError:
                        print("Invalid discount value, assuming 0.")
                        discount = 0
                else:
                    try:
                        total_amount += int(price)
                        item_count += 1
                    except ValueError:
                        print(f"Invalid price for item '{item}', skipping it.")
            else:
                print(f"Invalid line format: {line}, skipping it.")

        final_amount = total_amount - discount

        print(f"No of items purchased: {item_count}")
        print(f"No of free items: {free_items}")
        print(f"Amount to pay: {total_amount}")
        print(f"Discount given: {discount}")
        print(f"Final amount paid: {final_amount}")

    except FileNotFoundError:
        print("Error: File not found. Please check the file name and try again.")
    except Exception as e:
        print("An unexpected error occurred:", e)


if __name__ == "__main__":
    process_purchase_file()
