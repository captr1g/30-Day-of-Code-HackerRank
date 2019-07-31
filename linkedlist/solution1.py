# creates a new Node (pass data as the Node constructor argument) and inserts it at the tail of the linked 
# list referenced by the head parameter.
#  Once the new node is added, return the reference to the head node.
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    # now we make the method to insert the data.
    def insert(self,head,data): 
        new_node = Node(data)
        if not head:
            return new_node
        else:
            current_node = head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node 
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head) 	  