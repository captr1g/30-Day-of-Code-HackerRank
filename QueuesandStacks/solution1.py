import sys
import queue
# create a class and make methods of Queue and Stacks. In methods first we create Queue and stacks and  
# then add the value in both Queue and stacks.now we take(get,pop) the value one by one both Queue and stack. 
class Solution:

    def __init__(self):
        self.st= []
        self.q=queue.Queue()

    def pushCharacter(self,c):
        self.st.append(c)  
        
    def enqueueCharacter(self,s):
        self.q.put(s)
    
    def popCharacter(self):
        return self.st.pop()

    def dequeueCharacter(self):
        return self.q.get()     

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    