#!/bin/python3
# Given an array,A, of N integers,A print 's elements in reverse order as a single line of space-separated numbers
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    # split the vale and make them into list
    arr = list(map(int, input().rstrip().split()))
    # reverse the array
    arr.reverse()
    # print them using loop in reverse order 
    for i in range (len(arr)):
        print(arr[i],'',end="" )
