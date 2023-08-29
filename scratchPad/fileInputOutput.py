#!/usr/bin/env python

import sys

"""
##############################################
Opening files and doing operations examples
##############################################
"""

f = open("testfile1.txt" , "r")
print(f.read())

f = open("testfile1.txt" , "w")
f.write("HelloWorld")

f = open("testfile1.txt" , "a")
f.write("Appending hello world to existing file")

def Cat(filename):
  f = open(filename, "r")
  for line in f:
    print(line,)

'''
##############################################
Network IP Addressing related code examples
##############################################
'''

ip_addr = '10.1.1.1'
if '10.1' in ip_addr:
    print(f"IP Address found {ip_addr}")
'''
##############################################
Conditional examples
##############################################
'''

##############################################################

ssh_timeout = 20
if ssh_timeout == 10:
    print('SSH timeout is 10 seconds')
elif ssh_timeout > 30:
    print('SSH timeout is greather than 30 seconds')
else:
    print('Unexpected SSH timeout')

##############################################################

ssh_timeout = 20
host_reachable = True
ip_addr = '10.1.1.1'

# First conditional IF either are NOT TRUE it will go to ELIF
# In this example both variables evaluate to true so block of if executes
if host_reachable and ssh_timeout >= 10:
    print('Try to connect')
elif not host_reachable or ip_addr == '10.1.1.1':
    print('Invalid host, do not try connection')
else:
    print('Unexpected error , go home')

##############################################################

'''
##############################################
Looping and repetition examples
##############################################
'''

##############################################################

ip_list = [
    '10.1.1.1',
    '10.1.1.2',
    '10.1.1.3',
    '10.1.1.4',
]

for ip in ip_list:
    print(ip)

##############################################################


if __name__ == "__main__":
  Cat("testfile1.txt") 
  #Cat(sys.argv[1])
