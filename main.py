import read_matrix
import __maze
import A_star

file_path = "data_maze/maze1.txt"
# Đọc ma trận từ file_path trên
maze1 = read_matrix.read(file_path)
# Lời giải của mê cung
ans = A_star.sol_maze(maze1, (19, 19), (39, 38))
# Vẽ mê cung
if ans:
    __maze.draw_maze(maze1, ans)
else:
    __maze.draw_maze(maze1, ans)
    print("Không có đường đi thoát khỏi mê cung")
