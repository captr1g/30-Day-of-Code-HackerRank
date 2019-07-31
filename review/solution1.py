# program to calcuate index vale is even or odd and print the output
S=int(input())
for i in range(S):
    string=input()
    even=''
    odd=''
    for j in range(len(string)):
        if j%2==0:
            even += string[j]
        else :
            odd += string[j]
    print(even  , odd)
