import heapq


def sol_maze(maze, start, end):
    open_list = []
    g_score = {start: 0}
    heapq.heappush(open_list, (heuristic(start, end), g_score[start], start))
    came_from = {}
    while open_list:
        current = heapq.heappop(open_list)[2]

        if current == end:
            return reconstruct_path(came_from, end)

        neighbors = get_neighbors(maze, current)
        for neighbor in neighbors:
            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, end)
                heapq.heappush(open_list, (f_score, g_score[neighbor], neighbor))
                came_from[neighbor] = current

    return None


# Hàm tính khoảng cách heuristic
def heuristic(cell, goal):
    x1, y1 = cell
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)


def get_neighbors(maze, cell):
    x, y = cell
    neighbors = []

    # Kiểm tra ô hàng xóm bên trên
    if x > 0 and maze[x - 1][y] == 1:
        neighbors.append((x - 1, y))

    # Kiểm tra ô hàng xóm bên dưới
    if x < len(maze) - 1 and maze[x + 1][y] == 1:
        neighbors.append((x + 1, y))

    # Kiểm tra ô hàng xóm bên trái
    if y > 0 and maze[x][y - 1] == 1:
        neighbors.append((x, y - 1))

    # Kiểm tra ô hàng xóm bên phải
    if y < len(maze[0]) - 1 and maze[x][y + 1] == 1:
        neighbors.append((x, y + 1))

    return neighbors


# Hàm truy vết đường đi từ điểm đích đến điểm xuất phát
def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path
