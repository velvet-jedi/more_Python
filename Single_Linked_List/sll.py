#!/usr/bin/env python

# define a class that inherits from builtin object class
class SingleLinkedListNode(object):

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
    

# controller class
class SingleLinkedList(object):
    def __init__(self):
        # initialise first and last nodes of the linked list
        self.begin = None
        self.end = None

    def push(self, obj):
        """Appends a new value on the end of the list."""
    
    def pop(self):
        """Removes the last item and returns it."""

    def shift(self, obj):
        """Another name for push."""

    def unshift(self):
        """Removes the first item and returns it."""
    
    def remove(self, obj):
        """Finds a matching item and removes it from the list."""

    def first(self):
        """Returns a *reference* to the first item, does not remove."""

    def last(self):
        """Returns a reference to the last item, does not remove."""

    def count(self):
        """Counts the number of elements in the list."""

    def get(self, index):
        """Get the value at index."""

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""


    # Creating nodes
node3 = SingleLinkedListNode(3, None)
node2 = SingleLinkedListNode(2, node3)
node1 = SingleLinkedListNode(1, node2)

    # Printing nodes
print(node1)  # Output: [1:2]
print(node2)  # Output: [2:3]
print(node3)  # Output: [3:None]