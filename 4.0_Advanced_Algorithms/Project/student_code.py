# Code inspitaion borroweed from https://www.redblobgames.com/pathfinding/a-star/implementation.html




import math
#  Using the function-based interface provided by heapq instead of building a class-based interface.
from queue import PriorityQueue


def shortest_path(M,start,goal):
    
    frontier= PriorityQueue()
    frontier.put(start, 0)
    
    prev = {start: None}
    score = {start: 0}

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            generate_path(prev, start, goal)

        for node in M.roads[current]:
            updateScore = score[current] + heuristic(M.intersections[current], M.intersections[node])
            
            if node not in score or updateScore < score[node]:
                score[node] = updateScore
                totalScore = updateScore + heuristic(M.intersections[current], M.intersections[node])
                frontier.put(node, totalScore)
                prev[node] = current

    return generate_path(prev, start, goal)


#Calculate heuristic
def heuristic(start, goal):
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))


#returning distance from start to goal
def generate_path(prev, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = prev[current]
        path.append(current)
    path.reverse()
    return path