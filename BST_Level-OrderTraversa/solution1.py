# A level-order traversal, also known as a breadth-first search, visits each level of a tree's nodes from 
# left to right, top to bottom. You are given a pointer,root, pointing to the root of a binary search tree.
import sys

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
    
    def levelOrder(self,root):
        node_search = list()
        node_traversal = ''
        node_search.append(root)
        while len(node_search)>0:
            node = node_search.pop(0)
            if node.left:
                node_search.append(node.left)
            if node.right:
                node_search.append(node.right)
            node_traversal += str(node.data)+ ' '
        print (node_traversal)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
