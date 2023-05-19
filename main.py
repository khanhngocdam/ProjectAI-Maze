import read_matrix
import maze
import A_star

file_path = "data_maze/maze1.txt"
# Đọc ma trận từ file_path trên
maze1 = read_matrix.read(file_path)
# Lời giải của mê cung
ans = A_star.sol_maze(maze1, (1, 0), (19, 18))
# Vẽ mê cung
maze.draw_maze(maze1, ans)
