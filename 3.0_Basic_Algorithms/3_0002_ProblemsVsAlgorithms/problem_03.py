"""
Rearrange Array Elements
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. 
You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot
differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected 
time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. 
In scenarios such as these when there are more than one possible answers, return any one.

Here is some boilerplate code and test cases to start with:
"""

def rearrange_digits(merged_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    x = 0
    y = 0
    for i in range(0,len(merged_list)):
    # for i in merged_list[i]:
        if i % 2 == 0: 
            # fill x with digits at the even indices of sorted array
            x = x * 10 + merged_list[i]
            i += 2
        else:
            # for i in range(1,len(merged_list)):
            # fill y with digits at the odd indices of sorted array
            y = y * 10 + merged_list[i]
            i += 2
    return x,y


# print(rearrange_digits([4,6,2,7,9,8]))

def merge_sort(unsorted_list):
    """
    Takes in an unsorted list and sorts the list recursively descending
    """
    if len(unsorted_list)<=1:
        return unsorted_list

    mid_point = int(len(unsorted_list))//2

    first_half = unsorted_list[:mid_point]
    second_half = unsorted_list[mid_point:]

    half_a = merge_sort(first_half)
    half_b = merge_sort(second_half)
    return merge(half_a, half_b)

def merge(first_sublist, second_sublist):
    i=j=0

    merged_list = []


    while i < len(first_sublist) and j < len(second_sublist):
        if first_sublist[i] > second_sublist[j]:
            merged_list.append(first_sublist[i])
            i += 1
        else:
            merged_list.append(second_sublist[j])
            j += 1
        
    while i < len(first_sublist):
        merged_list.append(first_sublist[i])
        i += 1
        
    while j < len(second_sublist):
        merged_list.append(second_sublist[j])
        j += 1
    return merged_list

# Testing

def test_function(test_case):
    output = rearrange_digits(merge_sort(test_case[0]))
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")
print('TEST 0')
test_function([[1, 2, 3, 4, 5], [542, 31]])
# Prints Pass
print('TEST 1')
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
# Prints Pass

print('TEST 2')
test_function([[4, 6, 2, 5, 9, 8], [964, 85]])
# Prints Fail

# EDGE CASE 

test_function([[], [964, 85]])
# Prints Fail

test_function([[1], []])
# Prints Fail

test_function([[0,0,0], [00,0]])
# Prints Pass

