# LOOPS (22pts TOTAL)

# PROBLEM 1 (Fibonacci - 4pts)
## The Fibonacci sequence is a sequence of numbers that starts with 1, followed by 1 again.
# Every next number is the sum of the two previous numbers.
# I.e., the sequence starts with 1, 1, 2, 3, 5, 8, 13, 21,...
# Write a program that calculates and prints the Fibonacci sequence
# until the numbers get higher than 1000.

a = 1
b = 0
old_a = a
while (old_a + b) < 1000:
    old_a = a
    a = b
    b = old_a + b
    print(b)


# PROBLEM 2 (Number Guessing Game - 6pts)
# Write a program that takes a random integer between 1 and 1000
# The program then asks the user to guess the number.
# After every guess, the program will say either “Lower”
# if the number it took is lower, “Higher” if the number it took is higher,
# and “You guessed it!” if the number it took is equal to the number
# It might be wise, for testing purposes, to also display the number that the
# program randomly picks, until you are sure that the program works correctly

import random

done = False

number = random.randrange(1, 101)

while done == False:
    user_input = int(input("Enter a number between 1-100: "))
    if user_input <= 0 or user_input >= 101:
        print("Number entered not between interval.")
    elif user_input > number:
        print("Higher.")
    elif user_input < number:
        print("Lower.")
    elif user_input == number:
        print("You guessed it!")
        done = True



# PROBLEM 3 (Dice Hi-Low - 6pts)
# You roll five six-sided dice, one by one.
# How big is the probability that the value of each die
# is greater than or equal to the value of the previous die that you rolled?
# For example, the sequence “1, 1, 4, 4, 6” is a success,
# but “1, 1, 4, 3, 6” is not. Determine the
# probability of success using a simulation of a large number of trials.

import random

success = 0
trials = 0

for i in range(5000):
    roll1 = random.randrange(1,7)
    roll2 = random.randrange(1, 7)
    roll3 = random.randrange(1, 7)
    roll4 = random.randrange(1, 7)
    roll5 = random.randrange(1, 7)
    if roll1 <= roll2 and roll2 <= roll3 and roll3 <= roll4 and roll4 <= roll5:
        success += 1
    trials += 1

print("Probability =", str((success/trials)*100)+"%")

# PROBLEM 4 (Number Puzzler - 6pts)
# A, B, C, and D are all different digits.
# The number DCBA is equal to 4 times the number ABCD.
# What are the digits?
# Note: to make ABCD and DCBA conventional numbers, neither A nor D can be zero.
# Use a quadruple-nested loop to solve.

for a in range(1,10):
    for b in range(10):
        for c in range(10):
            for d in range(1, 10):
                number = 4 * (int(a)*1000 + int(b)*100 + int(c)*10 + int(d))
                number2 = int(d)*1000 + int(c)*100 + int(b)*10 + int(a)
                if number2 == number and a != b and a != c and a != d and b != c and b!= d and c!= d:
                    print("A =", a, "B =", b,"C =", c,"D =", d)
