#!/bin/python3

import math
import os
import random
import re
import sys

# take input amd converted into binary form .take counter which initiate with 0.
# take  variable name maximum which is use for store the vale of maximum number chain of 1 init.    
# range start to 2 to end of the number because first 2 number is "0b".
if __name__ == '__main__':
    n = int(input())
    x=bin(n)
    count = 0
    maximum=0
    # loop start in the range of binary number lengthcd 
    for i in x[2:]:
        if int(i)==0:
            count=0
        else:
            #increase counter
            count += 1
            if count>maximum:
                # print('entered magic condition')
                maximum += 1
    print(maximum)
    

