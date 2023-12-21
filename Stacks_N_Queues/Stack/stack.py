class StackNode(object):

    def __init__(self, value, nxt):
        self.value = value      # current node's value
        self.next = nxt    # Pointer to the under (next) node

    def __repr__(self):
    # create a string representation of a node in the form of [value:next_value]
        nval = self.next and self.next.value or None # Get the value of the next node
        return f"[{self.value}:{repr(nval)}]"
        
class Stack(object):
    def __init__(self):
        # Initialize top to None
        # the stack is initially empty
        self.top_node = None

    """Pushes a new value to the top of the stack."""
    def push(self, obj):
        # make a new node and make its next point to the top
        new = StackNode(obj, self.top_node)  
        # change the top to the new node
        self.top_node = new
    
    """Pops the value that is currently on the top of the stack."""
    def pop(self):
        if self.top_node:    # if top exists
            popped = self.top_node.value     # remove the top node
            self.top_node = self.top_node.next  # next node to top
            return popped
        else:
            return None

    """Returns a *reference* to the first item, does not remove."""
    def get_top(self):
        return self.top_node.value if self.top_node else None

    """Counts the number of elements in the stack."""
    def count(self):
        count = 0
        # traverse and count
        current_node = self.top_node
        while current_node:
            count += 1 
            current_node = current_node.next
        return count

    """Prints the contents of the stack."""
    def dump(self, mark="----"):
        cur_node = self.top_node
        print(mark)
        while cur_node:
            print(cur_node.value)
            cur_node = cur_node.next
        print(mark)