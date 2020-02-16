"""
Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. 
You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, 
that would still be an O(n) solution but it will not count as single traversal.
"""

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # initialize the variables 

    i = 0 # low
    j = 0 # medium
    k = len(input_list)-1 # length of the array

    while j <= k:
        if input_list[j] ==0:
            input_list[i],input_list[j] = input_list[j],input_list[i]
            i += 1
            j += 1

        elif input_list[j]==2:
            input_list[j],input_list[k] = input_list[k],input_list[j]
            k -= 1
        else:
            j += 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# TEST CASE
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
# Pass

test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
# Pass

test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# Pass

# EDGE CASES
test_function([2, 2, 2, 1, 1, 1, 2, 2])
# Pass

test_function([2, 2, 2,2, 2])
# Pass

test_function([])
# Pass