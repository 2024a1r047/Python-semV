"""
3. Write a program to take an amount in rupees and calculate how many
500 and 100 notes are needed"""

amount = int(input("Enter amount in rupees:"))
notes500 = amount // 500
rem = amount % 500
notes100 = rem // 100
print(f"Number of 500 rupee notes required:", notes500, "and number of 100 notes required:", notes100)