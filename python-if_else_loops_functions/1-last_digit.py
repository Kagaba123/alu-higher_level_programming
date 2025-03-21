#!/usr/bin/python3
import random

# Generate a random number
number = random.randint(-10000, 10000)

# Get the last digit
last_digit = abs(number) % 10

# If number is negative, make last_digit negative
if number < 0:
    last_digit = -last_digit

# Print output based on conditions
print(f"Last digit of {number} is {last_digit}", end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
