# Implementing stack using linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None # No items in the stack, so head should be None
        self.num_elements = 0 # No items in the stack, so num_elements should be 0


    # Add a push method

    def push(self,value):
        new_node = Node(value)
        # if stack is empty
        if self.head is None:
            self.head = new_node
        # Or should we add him to the head?
        else:
            new_node = self.head
            self.head   = new_node

        self.num_elements += 1
        
   # Add a pop method
    def pop(self, value):
        # check if the stack is empty
        if self.is_empty():
            value = self.head.value # Copy data to a local variable
            self.head = self.head.next # move head pointer to the next node
            self.num_elements -= 1
            return value

    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0


