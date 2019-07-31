#!/bin/python3

import math
import os
import random
import re
import sys

#  table making using loop 

if __name__ == '__main__':
    n = int(input())
    for i in range(1,11):
        print(n +'x'+ i +"="+ n*i)
        i=i+1
