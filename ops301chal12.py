#!/usr/bin/env python3

# Script:                       Ops Challenge 12
# Author:                       Kevin Isaac
# Date of latest revision:      20221228
# Purpose:      Python Requests Library

# Attribution: Class Zoom video and collaboration with classmates.  I had assistance on this from classmates.

# First step is to install the requests library
import requests

# Assign a requests.get function to a variable. Pass a parameter (the URL) into the function for it to work.
# response = requests.get('https://api.github.com')

aim = 'https://api.github.com'

# [404] = 'Site not found'
# HTTP Method Options:

print("Choose between options:")
print("1. GET\n2. POST\n3. PUT\n4. DELETE\n5. HEAD\n6. PATCH\n7. OPTIONS")

method_choice = input()
method_choice = int(method_choice)
print(type(method_choice))

if method_choice == 1:
    print(requests.get(aim))

if method_choice == 2:
    print(requests.post(aim))

if method_choice == 3:
    print(requests.put(aim))

if method_choice == 4:
    print(requests.delete(aim))

if method_choice == 5:
    print(requests.head(aim))

if method_choice == 6:
    print("Site not found")

elif method_choice == 7:
    print(requests.options(aim))  


else:
    print("Sorry, try agsin!")
