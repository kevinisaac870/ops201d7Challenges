#!/bin/bash

# Script:                       Ops Challenge 5
# Author:                       Kevin Isaac
# Date of latest revision:      20221217
# Purpose:      Write a log clearing bash script.


# Print to the screen the file size of the log files before compression
# Compress the contents of the log files listed below to a backup directory
# /var/log/syslog
# /var/log/wtmp
# The file name should contain a time stamp with the following format -YYYYMMDDHHMMSS
# Example: /var/log/backups/syslog-20220928081457.zip

target1=syslog
target2=wtmp

clear_log () {
  target_size=$(stat -c%s /var/log

