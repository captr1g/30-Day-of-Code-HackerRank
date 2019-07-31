#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    if __name__ == '__main__':
        meal_cost = float(input())
        tip_percent = int(input())
        tax_percent = int(input())
        # Find the tip percent
        a=meal_cost*tip_percent/100
        # Find the tax percent
        b=meal_cost*tax_percent/100
        # Find the total percent
        total=meal_cost+a+b
        # Round off the percent
        tax=round(total)
        print(tax)

solve(12.00,20,8)
