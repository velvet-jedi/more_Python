class QueueNode:
    # self is the first parameter of a method within a class, refers to the instance of the class itself.
    def __init__(self, value, nxt, prv):
        # Initialize a new node with the given data
        self.value = value
        # Pointers to the previous and next nodes in the queue
        self.prev = nxt
        self.next = prv
    
    def __repr__(self):
        nval = self.next and self.next.value or None 
        pval = self.prev and self.prev.value or None
        return f"[{self.value}:next={repr(nval)}:prev={repr(pval)}]"

class Queue:
    def __init__(self):
        # Initialize an empty queue with head and tail set to None
        self.head = None
        self.tail = None


    """Shifts a new element onto the back of the queue."""
    def enqueue(self, obj): 
        assert obj != None, "Cannot add None to queue."  # if empty node supplied to add

        if self.head: # if there is/are elements in the queue
            new_node = QueueNode(obj, None, self.tail)  # make a new node with prev pointing to tail and next to None
            self.tail.next = new_node   # the new node is next in line now
            self.tail = new_node    # the new node is the new tail now

        else:
            self.head = QueueNode(obj, None, None) # the queue has only one element no next no previous
            self.tail = self.head   #both tail and head are the same node

    """Removes the element that is first in the queue."""
    def dequeue(self): # unshift
        if self.head:
            node = self.head
            if self.head == self.tail: # if both head and tail are one node 
                self.head = self.tail = None # set both to none
            else:
                self.head = node.next
                self.head.prev = None
            return node.value
        else:
            return None

    def first(self):
        return self.head.value if self.head else None
    
    def empty(self):
        """Indicates if the Queue is empty."""
        return self.head == None
    
    def count(self):
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def printQueue(self, mark="----"):
        cur_node = self.head
        # print(mark)
        result = [mark]
        while cur_node:
            result.append(str(cur_node.value))
            cur_node = cur_node.next
        result.append(mark)
        return '\n'.join(result)
