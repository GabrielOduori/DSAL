def min_max(merged_list):
    x = 0
    y = 0
    for i in range(0,len(merged_list)):
        if i%2 == 0: 
            # fill x with digits at the even indices of sorted array
            x = x * 10 + merged_list[i]
            i += 2
        else:
            # for i in range(1,len(merged_list)):
            # fill y with digits at the odd indices of sorted array
            y = y * 10 + merged_list[i]
            i += 2
    return x,y

def merge_sort(unsorted_list):
    """
    Takes in an unsorted list and sorts the list recursively descending
    """
    if len(unsorted_list)==1:
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

unsorted_list = [9,2,5,6,0,10]

print(min_max(merge_sort(unsorted_list)))