# Code using ideas from https://www.redblobgames.com/pathfinding/a-star/implementation.html


import math
# from queue import PriorityQueue
import heapq

"""
Using the function-based interface provided by queue instead of building a class-based interface.
"""

def shortest_path(M,start,goal):
    frontier = []
    
    # frontier = PriorityQueue()
    heapq.heappush(frontier,(start, 0))

    # frontier.put(start, 0)
    
    came_from = {start: None}
    cost_so_far = {start: 0}
    # while not frontier.empty():
    while frontier:
        current = heapq.heappop(frontier)
        # current = frontier.get()

        if current == goal:
            generate_path(came_from, start, goal)

        for node in M.roads[current]:
            updated_cost = cost_so_far[current] + heuristic(M.intersections[current], M.intersections[node]) + heuristic(M.intersections[node], M.intersections[goal])
     
            if node not in cost_so_far or updated_cost < cost_so_far[node]:
                cost_so_far[node] = updated_cost
#                 print(f' {node}: {updated_cost}')
                heapq.heappush(frontier, node, updated_cost)
                # frontier.put(node, updated_cost)
#                 print(f' {node}: {updated_cost}')
                came_from[node] = current
                print(current)
        
    return generate_path(came_from, start, goal)


#Calculate heuristic
def heuristic(start, goal):
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))


# Drawing the path from start to goal
def generate_path(came_from,start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path