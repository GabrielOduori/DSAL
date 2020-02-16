"""
Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of
unsorted integers. The code should run in O(n) time. 
Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?
"""

import math
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None

    min_ = math.inf
    max_ =  - math.inf

    for number in ints:
        if number > max_:
            max_ = number
        if number < min_:
            min_ = number
            
    return(min_,max_)

## Example Test Case of Ten Integers
import random

# Test 1
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
# Pass

# Test 2
l = [i for i in range(9, 19)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((9, 18) == get_min_max(l)) else "Fail")
# Pass

# Test 3
l = [i for i in range(-9, 10)]  # a list containing -9  to 10
random.shuffle(l)
print ("Pass" if ((-9, 9) == get_min_max(l)) else "Fail")
# Pass

# EDGE CASES
l = [i for i in range(101, 1500)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((101, 1499) == get_min_max(l)) else "Fail")
# Pass

l = []  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if (0== get_min_max(l)) else "Fail")
# Fail
