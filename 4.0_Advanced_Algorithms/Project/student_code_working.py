
# https://www.youtube.com/watch?v=EQ_1i8nWnDs
https://www.youtube.com/watch?v=-L-WgKMFuhE
http://www.policyalmanac.org/games/aStarTutorial.htm
https://brilliant.org/wiki/a-star-search/?quiz=a-star-search#the-a-algorithm
https://en.wikipedia.org/wiki/A*_search_algorithm#Pseudocode



http://www.policyalmanac.org/games/aStarTutorial.htm
https://www.redblobgames.com/pathfinding/a-star/implementation.html


https://stackoverflow.com/questions/9511118/is-a-the-best-pathfinding-algorithm


import heapq
import math

class Graph:
  def __init__(self):
    self.edges ={}

  def neighbors(self, id):
    return self.edges.id  

  
class PriorityQueus:
  def __init__(self):
    self.elements = []

  def empty(self):
    return len(self.elements) == 0

  def put(self, item, priority):
    heapq.heappush(self.elements, (priority, item))

  def get(self):
    return heapq.heappop(self.elements)[1]
    


def euclidean_distance():
  """
  Eucleadian Distance from the starts
  """
  pass



def esimated_distance():
  """
  Estimated distance from the start.
  """
  pass



def shortest_path(M,start,goal):
  """
  Return shortests path based on A* Algoriths using a given start and end points
  """
  print("shortest path called")
  return
