'''Create a function max_of_three that takes three numbers as arguments and returns the largest of them and 
also create a parameter function that checks whether a given number is Armstrong or not.
'''

# Function to find the largest of three numbers
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# Function to check Armstrong number
def armstrong(num):
    temp = num
    power = len(str(num))
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** power
        temp = temp // 10

    if sum == num:
        return True
    else:
        return False


# Taking input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Largest number is:", max_of_three(a, b, c))

num = int(input("\nEnter a number to check Armstrong: "))

if armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")