#!/usr/bin/env python

# define a class that inherits from builtin object class
class SingleLinkedList(object):

    #  Initialize a SingleLinkedListNode node with a given value
    # and reference to the next node (nxt) which is also an object of the same class.
    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    # __repr__ is a special method to represent the objects in a class as a string
    def __repr__(self):

        # store the info of next node. This is the edge
        nval = self.next and self.next.value or None

        # Return information of the current node's value and the value of
        # the next node in the linked list
        return f"[{self.value}:{repr(nval)}]"
    
    # Creating nodes
node3 = SingleLinkedList(3, None)
node2 = SingleLinkedList(2, node3)
node1 = SingleLinkedList(1, node2)

    # Printing nodes
print(node1)  # Output: [1:2]
print(node2)  # Output: [2:3]
print(node3)  # Output: [3:None]