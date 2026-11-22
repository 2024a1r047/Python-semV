'''
Write a python program that accepts the length of three sides of a triangle as inputs. The program should 
indicate whether or not the triangle is a right-angled triangle. (Use Pythagorean theorem) Also find out its 
area using Heron’s formula.
'''

import math
# Taking input from user
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Checking whether the sides form a valid triangle
if a + b > c and a + c > b and b + c > a:

    # Checking right-angled triangle
    sides = sorted([a, b, c])

    if math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2):
        print("It is a Right-Angled Triangle")
    else:
        print("It is not a Right-Angled Triangle")

    # Heron's Formula
    s = (a + b + c) / 2

    area = math.sqrt(s * (s-a) * (s-b) * (s-c))

    print("Area of Triangle:", area)

else:
    print("The given sides do not form a valid triangle.")