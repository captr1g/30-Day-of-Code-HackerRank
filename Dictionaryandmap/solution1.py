# we're learning about Key-Value pair mappings using a Map or Dictionary data structure
import sys
# take input and make a empty dictionary
s=int(input())
custom_dict={} 
# from input start a loop to take key and value and insert them into dictionary 
for _ in range(s):
    name,number = input().split(" ")
    custom_dict[name] = number
# search the key in dictionary
for iput in sys.stdin:
    iput=iput.strip('\n')
    # key in the dictionary then print key and value otherwise print not found
    if iput in custom_dict:
        print(iput+'='+custom_dict.get(iput))
    else:
        print('Not found')