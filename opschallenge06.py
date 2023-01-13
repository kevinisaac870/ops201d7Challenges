# Script:                       Ops Challenge 6
# Author:                       Kevin Isaac
# Date of latest revision:      20221219
# Purpose:      Create a Python script that executes a few bash commands successfully.


# The Python module "os" must be utilized
# At least three variables must be declared in Python that contain results of bash operations
# The Python function print() must be used at least three times
# Include execution of the following bash commands inside your Python script:

# This command calls on the Python OS to be utilized
import os

# This command will display my username
whoami_output = os.system("whoami")

# This command will display system IP information/address
ip_a_output = os.system("ip a")

# This command will display hardware configuration information
lshw_ouput = os.system("lshw -short")

# The following commands call in the above variables to execute
print(whoami_output)
print(ip_a_output)
print(lshw_ouput)

# End
