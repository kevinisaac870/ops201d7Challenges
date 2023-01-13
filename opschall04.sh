#!/bin/bash

# Script:                       Ops Challenge 4
# Author:                       Kevin Isaac
# Date of latest revision:      20221215
# Purpose:      Change file/user permissions with a shell script

# Attribution: Class Zoom video, classmates and https://www.thegeekstuff.com/2008/09/bash-shell-take-control-of-ps1-ps2-ps3-ps4-and-prompt_command/

# Create a bash script that launches a menu system with the following options:
# Hello world (prints “Hello world!” to the screen)
# Ping self (pings this computer’s loopback address)
# IP info (print the network adapter information for this computer)
# Exit
# Next, the user input should be requested.
# The program should next use a conditional statement to evaluate the user’s input, then act according to what the user selected.
# Use a loop to bring up the menu again after the request has been executed.

PS3='Please enter your choice: '
options=("Choice 1" "Choice 2" "Choice 3" "Exit")
select opt in "${options[@]}"
do
    case $opt in
        "Choice 1")
            echo "Hello World!"
            ;;
        "Choice 2")
            echo "Ping 127.0.0.1"
            ping '127.0.0.1'
            ;;
        "Choice 3")
            echo "IP info"
            ip a
            ;;
        "Exit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done

# End
