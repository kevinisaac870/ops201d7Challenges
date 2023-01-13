#!/usr/bin/env python3

# Script:                       Ops Challenge 9
# Author:                       Kevin Isaac
# Date of latest revision:      20221222
# Purpose:      Create a Python script to use lists & sets.

# Attribution: Class Zoom video and fellow classmates

import os

# Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met.
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b


# Equals: a == b
a = 5
b = 5

if a == b:
    print("A is equal to B")

# Not Equals: a != b

a = 5
b = 10

if a != b:
    print("A is not equal B")

# Less than: a < b

a = 5
b = 10

if a < b:
    print("A is less than B")

# Less than or equal to: a <= b

a = 5
b = 10

if a <= b:
    print("A is less or equal to B")

# Greater than: a > b

a = 10
b = 5

if a > b:
    print("A is greater than B")

# Greater than or equal to: a >= b

a = 10
b = 5

if a >= b:
    print("A is greater than or equal to B")

# Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions are not met.

a = 5
b = 10

if a == b:
    print("All Things Being Equal...")
elif a < b:
        print("Not this time...")

# Create an if statement that includes both elif and else to execute when both if and elif are not met.

a = 5
b = 10

if a == b:
    print("I raelly hope my code works")
elif a > b:
    print("You sure?")
else: a <= b
print("Bingo Bango!")

# End
