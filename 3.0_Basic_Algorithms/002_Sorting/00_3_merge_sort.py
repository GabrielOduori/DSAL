def mergesort(items):
    # Base case, a list of 0 or 1 items is already sorted
    if len(items) <= 1:
        return items

    # Otherwise, find the midpoint and split the list
    mid = len(items)//2
    right = items[:mid]
    left = items[mid:]

    # Call mergesort recursively with the left and right half
    left = mergesort(left)
    right = mergesort(right)

    # Merge our two halves and return
    return merge(left, right)

def merge(left, right):
    # Given two ordered lists, merge them together in order,
    # returning the merged list.
    merged = []

    left_index= 0
    right_index = 0

    while left_index < len(left) and right_index < len(right_index):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index +=1
        else:
            merged.append(left[left_index])
            left_index += 1
    merged += left[left_index]
    merged += right[right_index]

    return merged
