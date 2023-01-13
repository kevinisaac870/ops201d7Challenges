#!/usr/bin/python3

# Script:                       Ops Challenge 10
# Author:                       Kevin Isaac
# Date of latest revision:      20221222
# Purpose:     Using Pyhton to amend a *.txt file


# Importing Python OS
import os

#Using file handling commands, create a Python script that creates a new .txt file

f = open("kevintest.txt", "w")

# Appends three lines

line1 = "Merry\n"
line2 = "Christmas\n"
line3 = "To You all"

f.write(line1)
f.write(line2)
f.write(line3)

# Prints to the screen the first time

f = open("kevintest.txt", "r")

print(f.read())

# Then delete the *.txt file

os.remove("kevintest.txt")

# End
# Attribution: Class Zoom videos and class peers
