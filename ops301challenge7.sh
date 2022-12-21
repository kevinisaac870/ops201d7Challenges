#!/usr/bin/env python3

# Script:                       Ops Challenge 7
# Author:                       Kevin Isaac
# Date of latest revision:      20221220
# Purpose:      Create a Python script that generates all directories, sub-directories and files for a user-provided directory path.




# Script must use the os.walk() function from the os library.
import os


## Script must ask the user for a file path and read a user input string into a variable.
dir = input("Enter a directory name:")

# Script must enclose the os.walk() function within a python function that hands it the user input file path.
def os_walk_target(target_arg):
    for (root, dirs, files) in os.walk(target_arg):
        ## Add a print command here to print ==root==
        print(root)
        ## Add a print command here to print ==dirs==
        print(dirs)
        ## Add a print command here to print ==files==
        print(files)

os_walk_target(dir)





