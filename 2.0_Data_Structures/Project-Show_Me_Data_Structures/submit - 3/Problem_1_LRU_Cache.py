
from collections import OrderedDict

class LRU_Cache(object):
    def __init__(self, capacity):
        # cache variables
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.

        try:  # If value in the cache

            # Update priority due to access
            value = self.cache.pop(key)
            self.cache[key] = value
            return value

        except KeyError:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        if self.capacity == 0:
            print("Cache has a zero capacity!")
            return

        if key in self.cache:  # Update priority due to access
            self.cache.pop(key)
            self.cache[key] = value

        else: 
            if len(self.cache) < self.capacity:
                self.cache[key] = value

            else: 
                self.cache.popitem(last=False)
                self.cache[key] = value


# TEST CASES
our_cache = LRU_Cache(5)
our_cache.set(1, 2)
our_cache.set(2, 3)
our_cache.set(3, 4)
our_cache.set(4, 5)
our_cache.set(5, 6)

print(our_cache.get(1))# Prints 2
print(our_cache.get(2))# Prints 3
print(our_cache.get(5))# Prints 6
print(our_cache.get(10))# Prints -1 because 10 is not present in the cache

# Edge Case:
our_cache = LRU_Cache(2)
our_cache.set(1, 4)
our_cache.set(2, 6)
our_cache.set(1, 23)
print(our_cache.get(1)) # Prints 23
print(our_cache.get(2)) # Prints 6

our_cache = LRU_Cache(0)
our_cache.set(1, 1)
# Prints Cache has a zero capacity!
print(our_cache.get(1))# Prints -1