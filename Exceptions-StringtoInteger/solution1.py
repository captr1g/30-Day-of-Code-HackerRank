#!/bin/python3
#Read a string,S, and print its integer value; if S cannot be converted to an integer, print Bad String.
S = input().strip()
try :
    x= int(S)
    print(x)
except Exception :
    print("Bad String")
