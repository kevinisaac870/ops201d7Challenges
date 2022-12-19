# Script:                       Ops Challenge 6
# Author:                       Kevin Isaac
# Date of latest revision:      20221219
# Purpose:      Create a Python script that executes a few bash commands successfully.

import os

whoami_output = os.system("whoami")
ip_a_output = os.system("ip a")
lshw_ouput = os.system("lshw -short")

print(whoami_output)
print(ip_a_output)
print(lshw_ouput)

