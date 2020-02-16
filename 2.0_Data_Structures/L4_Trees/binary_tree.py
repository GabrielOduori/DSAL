
class Node:
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value

    def set_left_child(self, node):
        self.left = node
    
    def set_right_child(self, node):
        self.right = node

    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_right_child(self):
        return self.left != None 


    def has_left_child(self):
         return self.right != None





node0 = Node()

node0 = Node("apple")
node1 = Node("banana")
node2 = Node("orange")


node0.set_left_child(node1)
node0.set_right_child(node2)

print(f"""
node0:{node0.value}
node0 left child:{node0.left.value}
node0 right child:{node0.right.value}
""")

print(f"has left child? {node0.has_left_child()}")
print(f"has right child? {node0.has_right_child()}")