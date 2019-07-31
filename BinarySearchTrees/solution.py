# The height of a binary search tree is the number of edges between the tree's root and its furthest leaf. 
# We are taking  a pointer,root, pointing to the root of a binary search tree.
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
    # Now we make the mathod of name getHight to find the hight of the tree.
    # if root not present print -1  
    def getHeight(self,root):
        if not root:
            return -1
        if not root.left and not root.right:
            return 0
        left= self.getHeight(root.left)
        right= self.getHeight(root.right)
        return max(left,right) + 1
        
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       