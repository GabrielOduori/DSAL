class Stack:
    def __init__(self):
        # initialize the stack
        self.items = []


    def size(self):
        # check the size of the stack
        return len(self.items)

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

def equation_checker(quation):
    """
    Check equation for balanced parentheses

    Args:
    equation(string): String form of equation
    Returns:
    bool: Return if parentheses are balanced or not
    """
    stack = Stack()


    for char in quation:
        if char=="(":
            stack.push(char)
        elif char ==")":
            if stack.pop()==None:
                return False
    if stack.size()==0:
        return True
    else:
        return False



print ("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")

# MyStack = Stack()

# MyStack.push("Web Page 1")
# MyStack.push("Web Page 2")
# MyStack.push("Web Page 3")

# print (MyStack.items)

# MyStack.pop()
# MyStack.pop()

# print ("Pass" if (MyStack.items[0] == 'Web Page 1') else "Fail")

# MyStack.pop()

# print ("Pass" if (MyStack.pop() == None) else "Fail")