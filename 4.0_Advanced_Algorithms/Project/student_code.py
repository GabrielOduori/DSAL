"""
start - The "start" node for the search algorithm.
goal - The "goal" node.
path - An array of integers which corresponds to a valid sequence of intersection visits on the map.
"""



def heuristic(a,b):
  (x1,y1)  = a
  (x2,y2)  = b

  return abs(x1-x2) + abs(y1-y2)



def shortest_path(M,start,goal):

    print("shortest path called")
    return



path = shortest_path(map_40, 5, 34)
if path == [5, 16, 37, 12, 34]:
    print("great! Your code works for these inputs!")
else:
    print("something is off, your code produced the following:")
    print(path)