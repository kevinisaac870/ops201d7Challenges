#!/bin/bash

# Script:                       Ops Challenge 4
# Author:                       Kevin Isaac
# Date of latest revision:      20221215
# Purpose:      Change file/user permissions with a shell script

# Create a bash script that launches a menu system with the following options:
# Hello world (prints “Hello world!” to the screen)
# Ping self (pings this computer’s loopback address)
# IP info (print the network adapter information for this computer)
# Exit
# Next, the user input should be requested.
# The program should next use a conditional statement to evaluate the user’s input, then act according to what the user selected.
# Use a loop to bring up the menu again after the request has been executed.

msg="Please select from below menu"

echo $message
    select $opt in "Print 'Hello World'" "Ping Self" "IP Info" "Exit" ; do
            case $opt in
                "Print 'Hello World'" ) echo "Hello World" && echo -e "/n$again" ;;
                "Ping Self" ) ping 127.0.0.1 -c 3 && echo -e "/n$again" ;;
                "IP Info" ) ls -a   ;;
                "Exit" ) echo "Good Bye"; break;
            esac
            REPLY=
        done

# end
