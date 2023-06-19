import A_star
import __maze
import time
import read_matrix
from collections import deque

def sol_maze(maze, start, end):
    fringe = deque()
    fringe.append(start)
    closed = deque()
    came_from = {}
    while (len(fringe) > 0):
        current = fringe.pop()
        __maze.draw_path(maze, A_star.reconstruct_path(maze, current))
        # time.sleep(0.1)
        closed.append(current)
        if current == end:
            return A_star.reconstruct_path(came_from, current)
        
        neighbors = A_star.get_neighbors(maze, current)
        for neighbor in neighbors:
            if neighbor in closed:
                neighbors.remove(neighbor)
            else:
                came_from[neighbor] = current
        
        fringe.extend(neighbors)


# file_path = "data_maze/maze1.txt"
# Đọc ma trận từ file_path trên
# maze1 = read_matrix.read(file_path)
# print(sol_maze(maze1, (19, 19), (39, 38)))

