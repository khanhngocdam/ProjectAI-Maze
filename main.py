import read_matrix
import maze
import A_star

file_path = "data_maze/maze2.txt"
# Đọc ma trận từ file_path trên
maze1 = read_matrix.read(file_path)
# Lời giải của mê cung
ans = A_star.sol_maze(maze1, (1, 0), (19, 18))
# Vẽ mê cung
if ans:
    maze.draw_maze(maze1, ans)
else:
    maze.draw_maze(maze1, ans)
    print("Không có đường đi thoát khỏi mê cung")
