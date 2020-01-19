"""
Traverse a tree (depth first search)
Traversing a tree means "visiting" all the nodes in the tree once. Unlike an array or linked list, there's more than one way to walk through a tree, starting from the root node.

Traversing a tree is helpful for printing out all the values stored in the tree, as well as searching for a value in a tree, inserting into or deleting values from the tree. There's depth first search and breadth first search.

Depth first search has 3 types: pre-order, in-order, and post-order.

Let's walk through pre-order traversal by hand first, and then try it out in code.
"""

# Crate a tree

class Node(object):

    def __init__(self, value=None):
        self.value = value 
        self.left = None
        self.right = None
    

    def set_value(self,value):
        self.value = value

    
    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    
    def get_right_child(self):
        return self.right

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"


    def __str__(self):
        return f"Node({self.get_value()})"


class Tree():

    def __init__(self,value = None):
        self.root = Node(value)

    def get_root(self):
        return self.root


#Depth first, pre-order traversal with a stack
# Let's define a stack to help keep track of the tree nodes
class Stack():
    def __init__(self):
        self.list = list()
        
    def push(self,value):
        self.list.append(value)
        
    def pop(self):
        return self.list.pop()
        
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.list) == 0
    
    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s
        
        else:
            return "<stack is empty>"

            

# create a tree and add some nodes
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))


# check Stack
stack = Stack()
stack.push("apple")
stack.push("banana")
stack.push("cherry")
stack.push("dates")
print(stack.pop())
print("\n")
print(stack)