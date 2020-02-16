def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # Compare the first and the last elements. If the last is larger than the 
    # first, the array is not rotated

    low  =  0
    high = len(input_list)-1

    while (low <= high):

        mid = (low + high)//2

        if number==input_list[mid]: # Case 1: number found
            return mid

        if input_list[mid] <= input_list[high]:# Case 2: Right half is sorted
            if number > input_list[mid] and number <= input_list[high]:
                low =  mid + 1 ## go searching in the right sorted half
            else:
                high = mid-1
        else:
            if input_list[low] <= number and number < input_list[mid]:
                high = mid-1
            else:
                low = mid + 1
    return -1

    # https://www.youtube.com/watch?v=6pSzsJH56BA

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 16])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[4,5,6,7,0,1,2],2])
