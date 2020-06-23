# We Create linked list 

#Create class node 
class Node:
    
    # Initiallize method
    def __init__(self, data=None, next= None):
        self.data = data
        self.next = next

    # basic mechanism for displaying the string type
    def __str__(self):
        return str(self.data)
    
#--- Assigning Nodes here ---# 
NodeA = Node(2)
NodeB = Node(3)
NodeC = Node(4)
NodeD = Node(5)

#--- Linking Nodes ---#

# First node refer to second node
NodeA.next = NodeB
# Seond node refer to third node
NodeB.next = NodeC
# Third node refer to fourth node
NodeC.next = NodeD




# Print Nodes
# print(NodeA)

# Traverse linked list
def PrintLinkedList(head):
    if head is not None:
        current = head
        ListSize = 1
        while current is not None:
            print(current.data)
            current = current.next
            ListSize += 1
        return print("List Size is : ", ListSize , end=" ")
    else:
        return print("Head has no value")

PrintLinkedList(NodeA)

# Insert element in linked list
# Remove element in linked list