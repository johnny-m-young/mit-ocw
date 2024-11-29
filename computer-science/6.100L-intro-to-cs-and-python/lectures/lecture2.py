#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 08:46:20 2024
"""

# Newton-Raphson guess-and-check method for finding the cube root of a number
# x = float(input("Find the cube root of: "))
# g = float(input("Initial guess: "))
# next_g = g-((g**3-x)/(3*g**2))

# print(f'Current guess cubed: {g**3}')
# print(f'Next guess to try: {next_g}')



# Secret number game
# secret_number = 6
# guess = int(input("Guess a number between 1 and 10: "))

# print(guess == secret_number)


# Debugging problem
# x = int(input("Enter a number for x: "))
# y = int(input("Enter a different number for y: "))

# if x == y:
#     print(f'{x} is the same as {y}')
#     print("These are equal!")



# Secret number game v2
secret_number = 6
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print(f'You got it! The secret number was {secret_number}')
elif guess > secret_number:
    print(f'The secret number is less than {guess}')
elif guess < secret_number:
    print(f'The secret number is more than {guess}')