"""
Designing a Linked List DataStructure.

A Linked List has a value and the next value it is pointing to.
Eg: 1 -> 2 -> 3
Head -> Next
1 -> 2
2 -> 3
"""
class Node:
    """The class defined for each Node."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """The main Linked List head."""
    def __init__(self):
        self.head = None

    def pushLeft(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pushAt(self, pos, data):
        new_node = Node(data)
        cur_node = self.head
        for i in range(pos):
            cur_node = cur_node.next
        cur_node.next, new_node.next = new_node, cur_node.next

    def append(self, data):
        new_node = Node(data)
        cur_node = self.head
        while(cur_node.next):
            cur_node = cur_node.next
        cur_node.next = new_node

    def printNodes(self):
        cur_node = self.head
        while(cur_node):
            print(f"{cur_node.data} -> {cur_node.next}")
            cur_node = cur_node.next

# Initialise the LinkedList
new_list = LinkedList()

# Add values to the linkedlist.
new_list.head = Node(5)
second = Node(8)
third = Node(9)

# Create pointers.
new_list.head.next = second
second.next = third


