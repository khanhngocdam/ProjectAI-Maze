import pygame

# Khởi tạo màn hình pygame
width, height = 640, 640
screen = pygame.display.set_mode((width, height))
# Đặt tên cho cửa sổ
pygame.display.set_caption("Maze")
# Định nghĩa màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
# Kích thước 1 ô
cell_size = 20


def create_maze(matrix):
    size_maze = len(matrix)
    for i in range(size_maze):
        for j in range(size_maze):
            if matrix[i][j] == 1:
                pygame.draw.rect(screen, BLACK, (j * cell_size, i * cell_size, cell_size, cell_size))
            elif matrix[i][j] == 0:
                pygame.draw.rect(screen, WHITE, (j * cell_size, i * cell_size, cell_size, cell_size))
            else:
                pygame.draw.rect(screen, RED, (j * cell_size, i * cell_size, cell_size, cell_size))


# Hàm chính
def draw_maze(matrix, ans):
    running = True
    draw_path = False
    clock = pygame.time.Clock()
    while running:
        # Xử lý sự kiện
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    draw_path = True

        # Xóa màn hình
        screen.fill(BLACK)

        # Vẽ mê cung
        create_maze(matrix)
        clock.tick(3)  # Giới hạn tốc độ 1 khung hình mỗi giây
        # Vẽ đường
        if draw_path:
            if len(ans) > 0:
                x, y = ans.pop(0)
                matrix[x][y] = 2
        # Cập nhật màn hình
        pygame.display.flip()

    # Kết thúc Pygame
    pygame.quit()
