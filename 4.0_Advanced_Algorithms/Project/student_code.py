"""
start - The "start" node for the search algorithm.
goal - The "goal" node.
path - An array of integers which corresponds to a valid sequence of intersection visits on the map.
"""
import heapq

# Import graph/map from helper file
# from helpers import *

class PriorityQueue:
    def __init__(self):
        self.elements = []

    @property
    def empty(self):
        # return len(self.elements) == 0
        return not self.elements # This will not be true for an empty elements
    
    def push(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def pop(self):
        return heapq.heappop(self.elements)

    def __repr__(self):
      return repr(self.elements)





def heuristic(a,b):
  (x1,y1)  = a
  (x2,y2)  = b

  return abs(x1-x2) + abs(y1-y2)

M = Map()

def shortest_path(M,start,goal):


  """
  OPEN = priority queue containing START
  CLOSED = empty set
  while lowest rank in OPEN is not the GOAL:
    current = remove lowest rank item from OPEN
    add current to CLOSED
    for neighbors of current:
      cost = g(current) + movementcost(current, neighbor)
      if neighbor in OPEN and cost less than g(neighbor):
        remove neighbor from OPEN, because new path is better
      if neighbor in CLOSED and cost less than g(neighbor): ⁽²⁾
        remove neighbor from CLOSED
      if neighbor not in OPEN and neighbor not in CLOSED:
        set g(neighbor) to cost
        add neighbor to OPEN
        set priority queue rank to g(neighbor) + h(neighbor)
        set neighbor's parent to current

  reconstruct reverse path from goal to start
  by following parent pointers
  """
  frontier = PriorityQueue()
  frontier.put(start, 0)

  came_from = {}
  cost_so_far = {}

  came_from[start] = None
  cost_so_far[start] = 0

  while not frontier.empty():
    current= frontier.get()

    # Testing for early exit
    if current == goal:
      break

    for next in M.intersection(current):
      new_cost = cost_so_far[current]+M.cost(current. next)
      if next not in cost_so_far or new_cost < cost_so_far[next]:
        cost_so_far[next] = new_cost
        priority = new_cost + heuristic(goal, next)
        frontier.put(next, priority)
        came_from[next] = current


  



  # Check if the start is the same as the goal
  if start== goal:
    return [start]

  M.intersection
  M.roads

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