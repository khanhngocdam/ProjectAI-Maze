def read(file_path):
    with open(file_path, "r") as file:
        # Đọc dòng đầu tiên và lấy kích thước ma trận
        size = int(file.readline())
        # Khởi tạo ma trận rỗng
        matrix = []
        # Đọc các dòng và thêm vào ma trận
        for i in range(size):
            values = file.readline().split()
            row = [int(value) for value in values]
            matrix.append(row)
    return matrix
