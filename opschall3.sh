#!/bin/bash

# Script:                       Ops Challenge 3
# Author:                       Kevin Isaac
# Date of latest revision:      20221214
# Purpose:      Change file/user permissions with a shell script

# https://www.linuxtrainingacademy.com/linux-commands-cheat-sheet/
# https://stevenbarrett1984.wordpress.com/2014/02/08/linux-mac-and-unix-file-permissions-and-the-chmod-command-part-1/

echo "Please enter a directory path for permission change:"
read dirpath
# mkdir $dirpath
cd $dirpath

touch testfile.txt
echo Please enter desired permissions for file e.g. 777, 775, 755, 664, 644:
read permnumber
chmod -R $permnumber
ls -al ./

#end
