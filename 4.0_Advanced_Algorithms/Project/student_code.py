"""
start - The "start" node for the search algorithm.
goal - The "goal" node.
path - An array of integers which corresponds to a valid sequence of intersection visits on the map.
"""
from collections import heapq

class Graph:
  def __init__(self):
    self.edges  = {}
    self.road = {}
    self.


  def neigbours(self, id):
    return self.edges[id]


class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]




def heuristic(a,b):
  (x1,y1)  = a
  (x2,y2)  = b

  return abs(x1-x2) + abs(y1-y2)



def shortest_path(M,start,goal):

  """
  Implementng A* Search
  """
  frontier  = PriorityQueue()
  frontier.put(start,0)

  come_from = {}
  cost_so_far  = {}

  came_from[start] = None
  cost_so_far[start] = 0

  while not frontie.empty():
    current = frontier.get()
    





  print("shortest path called")
  return



path = shortest_path(map_40, 5, 34)
if path == [5, 16, 37, 12, 34]:
    print("great! Your code works for these inputs!")
else:
    print("something is off, your code produced the following:")
    print(path)