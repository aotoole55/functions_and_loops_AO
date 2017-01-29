#SECTION 2 - FUNCTIONS (20PTS TOTAL)

#PROBLEM 1 (Length of String - 3pts)
# Make a function which asks the user to enter a string, then prints the length of that string.
# You will need to use the input() function.
# Make a call to that function
def length():
    string = input("Enter a string: ")
    print(len(string))

length()
# PROBLEM 2 (Pythagorean theorem - 4pts)
# The Pythagorean theorem states that of a right triangle, the square of the
# length of the diagonal side is equal to the sum of the squares of the lengths
# of the other two sides (or a^2 + b^2 = c^2).
# Write a program that asks the user for the lengths of the two sides that meet at a right angle.
# Then calculate the length of the third side, and display it in a nicely formatted way.
# You may ignore the fact that the user can enter negative or zero lengths for the sides.
def pythag():
    length_a = int(input("Enter the length of triangle side a: "))
    length_b = int(input("Enter the length of triangle side b: "))
    print("The third side of the triangle is equal to: ", (length_a**2 + length_b**2)**0.5)

pythag()

# PROBLEM 3 (Biggest, smallest, average - 4pts)
# Make a function to ask the user to enter three numbers.
# Then print the largest, the smallest, and their average, rounded to 2 decimals.
# Display the answers in a "nicely" formatted way.
# Make a call to your function.

def compare():
    number1 = int(input("Enter your first number: "))
    number2 = int(input("Enter your second number: "))
    number3 = int(input("Enter your third number: "))

    if number1 >= number2 and number1 >= number3:
        print(number1, "is the largest.")
    elif number2 >= number1 and number2 >= number3:
        print(number2, "is the largest.")
    elif number3 >= number1 and number3 >= number2:
        print(number3, "is the largest.")

    if number1 <= number2 and number1 <= number3:
        print(number1, "is the smallest.")
    elif number2 <= number1 and number2 <= number3:
        print(number2, "is the smallest.")
    elif number3 <= number2 and number3 <= number1:
        print(number3, "is the smallest.")

    print(round((number1+number2+number3)/3,2))

compare()

# PROBLEM 4 (e to the... - 3pts)
# Calculate the value of e (from the math library) to the power of -1, 0, 1, 2, and 3.
# display the results, with 5 decimals, in a nicely formatted manner.
import math


print(round(math.e**(-1),5))
print(round(math.e**(0),5))
print(round(math.e**(1),5))
print(round(math.e**(2),5))
print(round(math.e**(3),5))

# PROBLEM 5 (Random int - 3pts)
# Generate a random integer between 1 and 10 (1 and 10 both included),
# but only use the random() function (randrange is not allowed here)

import random

i = random.random()*9+1

print(i)


# PROBLEM 6 (add me, multiply me - 3pts)
# Make a function which takes in two integers and RETURNS their sum AND their product.

def sum_product(x, y):
    add = x + y
    product = x * y
    return add, product

print(sum_product(int(input("Enter your first number: ")), int(input("Enter your second number: "))))


