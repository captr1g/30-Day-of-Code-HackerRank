#!/bin/python3

import math
import os
import random
import re
import sys

# using recursion find the factorial of the number 
def factorial(n):
    # if number is 0 then print 1 otherwise use the recursion
    if n==0:
        return 1
    return n*factorial(n-1)
    
if __name__ == '__main__':
     
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)
    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
