#!/bin/python3

import math
import os
import random
import re
import sys
# Given an integer,n, perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5 , print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20, print Not Weird
if __name__ == '__main__':
    n = int(input())
    if  n%2==1 :
        print('Weird')
    a=range(2,6)
    for i in a:
        if n==i and n%2==0:
            print('Not Weird')
    e=range(6,21)
    for j in e:
        if n==j and n%2==0:
            print('Weird')
    if n>20 and n%2==0:
        print('Not Weird') 
