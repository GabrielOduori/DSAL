
import heapq

# Create an empty list

heap = list()


# insert 5 into the heap

heapq.heappush(heap, 5)


# Insert 6 into the heap

heapq.heappush(heap, 6)



# insert 2 into heap
heapq.heappush(heap, 2)

# insert 1 into heap
heapq.heappush(heap, 1)

# insert 9 into heap
heapq.heappush(heap, 9)



print("After pushing, heal looks like :{}".format(heap))


# pop and return smallest element from the heap
smallest = heapq.heappop(heap)   


print("Smallest element in the original list was: {}".format(smallest))

print("After popping, heap looks like: {}".format(heap))



print("New Heap")
new_heap = list()

heapq.heappush(new_heap, (0, 1))

heapq.heappush(new_heap, (-1, 5))

heapq.heappush(new_heap, (2, 0))

heapq.heappush(new_heap, (5, -1))

print("After pushing, now heap looks like: {}".format(new_heap))


# pop the smallest item from the heap

smallest = heapq.heappop(new_heap)

print("Smallest element in the oroginal list was :{}".format(smallest))
print("After popping,heap looks like:{}".format(new_heap))
