import A_star
import __maze
import read_matrix
import time
from collections import deque

def sol_maze(maze, start, end):
    fringe = deque()
    fringe.appendleft(start)
    closed = deque()
    came_from = {}
    while (len(fringe) > 0):
        current = fringe.pop()
        __maze.draw_path(maze, A_star.reconstruct_path(maze, current))
        # time.sleep(0.3)
        closed.append(current)
        if current == end:
            return A_star.reconstruct_path(came_from, current)
        
        neighbors = A_star.get_neighbors(maze, current)
        for neighbor in neighbors:
            if neighbor in closed:
                neighbors.remove(neighbor)
            else:
                came_from[neighbor] = current
        
        fringe.extendleft(neighbors)