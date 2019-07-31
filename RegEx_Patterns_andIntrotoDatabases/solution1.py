# Consider a database table, Emails, which has the attributes First Name and Email ID. 
# Given N rows of data simulating the Emails table, print an alphabetically-ordered list of people
# whose email address ends in @gmail.com .
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    name_list =[]
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]
        
        emailID = firstNameEmailID[1]
        # using regular find the @gmail.com and alphabatic order
        if re.findall(".?[a-z]+@gmail.com$",emailID): 
            name_list.append(firstName)
    name_list.sort()
    for i in(name_list):
        print(i)
