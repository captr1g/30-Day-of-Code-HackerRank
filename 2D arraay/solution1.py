#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    # make a empty array and take a counter with initial value 0. take a variable for inserting 
    # the valuse in array using while loop. 
    arr =[]
    count=0
    lc=True
    while lc:
        try:
            inp = input()
            arr.append(list(map(int, inp.rstrip().split())))
        except Exception:
            lc=False
    # start  using loop in range with the length of array and make a 6*6 2D array. 
    for i in range(len(arr)):
        for j in range(len(arr)):
            # using index number in the form of "I" and add all the index number value 
            if i<=3 and j<=3:
                count= arr[0+i][0+j]+arr[0+i][1+j]+arr[0+i][2+j]+arr[1+i][1+j]+arr[2+i][0+j]+arr[2+i][1+j]+arr[2+i][2+j]
                # if total value is bigger than the previous value then replaced the vale and finally print the biggest 
                # value of 2D array
                if i==0 and j==0:
                    maxar=count
                if count>maxar:
                    maxar=count
                    
    print(maxar)