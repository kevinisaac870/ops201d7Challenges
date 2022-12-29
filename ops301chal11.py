#!/usr/bin/env python3

# Script:                       Ops Challenge 11
# Author:                       Kevin Isaac
# Date of latest revision:      20221221
# Purpose:      Using Psutil and Libraries to gather system info

#Main

import psutil
print("\n")

print("Time spent by normal processes executing in user mode:")
output = psutil.cpu_times()
print(output)

print("\nTime spent by processes executing in kernel mode:")
print(output.system)
print("\nTime when system was idle:")
print(output.idle)
print("\nTime spent by priority processes executing in user mode:")
print(output.nice)
print("\nTime spent waiting for I/O to complete:")
print(output.iowait)
print("\nTime spent for servicing hardware interrupts:")
print(output.irq)
print("\nTime spent for servicing software interrupts:")
print(output.softirq)
print("\nTime spent by other operating systems running in a virtualized environment:")
print(output.steal)
print("\nTime spent running a virtual CPU for guest operating systems under the control of the Linux kernel:")
print(output.guest)

print("\n")

#End
