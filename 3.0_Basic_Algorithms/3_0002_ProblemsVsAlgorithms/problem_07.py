"""
HTTPRouter using a Trie
For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using
the Trie data structure we learned previously.

There are many different implementations of HTTP Routers such as regular expressions or simple string matching
, but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post"
and figure out what content to return. In a dynamic web server, the content will often come from a block of code
called a handler.
"""

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        # self.is_path  = False
        self.children = {}
        self.handler = None

    def insert(self, p):
        # Insert the node as before
        if p not in self.children:
            self.children[p] =  RouteTrieNode()
        else:
            pass


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, 
        # this is the root path or home page node
        self.root= RouteTrieNode()
        self.handler = root_handler

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root

        for p in path:
            node.insert(p)
            node = node.children[p]
        # node.is_path = True
        node.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        node = self.root

        for p in path:
            if p not in node.children:
                return False
            node = node.children[p]

        return node.handler




# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie(root_handler=root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, input_path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path = self.split_path(input_path)

        self.router.insert(path=path, handler=handler)

    def lookup(self, input_path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path = self.split_path(input_path)

        if len(path)==0:
            return self.router.handler
        
        found = self.router.find(path=path)

        if found is None:
            return self.not_found_handler
        else:
            return found


    def split_path(self, input_path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        # path_paths = input_path.split('/')
        # for item in path_paths:
        #     if item != '':
        #         return item

        # path_split = [item for item in input_path.split('/') if item != '']
        return [item for item in input_path.split('/') if item != '']
        # path_split = [item for item in path_paths if item != '']
        # return path_split


# TEST CASES

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home", "home handler")  # add a route
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
# Prints root handler

print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
# Prints home handler

print(router.lookup("/home/about")) # should print 'about handler'
# Prints about handler

print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
# Prints about handler

print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
# Prints False as not implemented