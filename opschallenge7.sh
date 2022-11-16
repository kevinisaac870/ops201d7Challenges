#!/bin/bash

# Script:                       Ops Challenge 07
# Author:                       Kevin Isaac
# Date of latest revision:      20221116
# Purpose:                      Info on Your Computer

# Declaration of variables

# Main
# Search the output of lshw command and returns every line with the word bridge in it
# lshw | grep “bridge” 
    echo "CPU"
    lshw | grep "cpu" -A 6 | head -6
    echo "MEMORY"
    lshw | grep "memeory" -A 4 | head -4
    echo | "DISPLAY ADAPTER"
    lshw | grep "diplay" -A 12 | head -12
    echo "NETWORK ADAPTER"
    lshw | grep "network" -A 9 | head -9
    
