#!/bin/python3
# we are sorting the array using bubble sort algorithem. 
import sys
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
swap = 0
for i in range (len(a)-1,0,-1):
    for j in range (i):
        if a[j] > a[j+1]:
            b = a[j] 
            a[j] = a[j+1]
            a[j+1] = b
            swap += 1 
print("Array is sorted in", swap ,'swaps.')
print("First Element:",a[0])
print("Last Element:",a[-1])
