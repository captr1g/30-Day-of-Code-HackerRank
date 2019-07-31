import math
# find the prime number first take input and start loop for how many times check the number is prime or not.  
a = int(input())
for i in range(a):
    n = int(input())
    # if number is 1 them print "Not prime" this is condition.
    if n == 1:
        print("Not prime")
        continue
    # find the square root of number then round off the number with floor.
    divisor = math.floor(math.sqrt(n))
    for d in range(2,divisor + 1):
        if n % d == 0:
            print("Not prime")
            break
    else:
        print("Prime")
# For-Else 
# Condition One, If for dosen't break else will run.