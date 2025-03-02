import tkinter as tk
import time


def n_queens(n, canvas, cell_size, delay=0.5):
    board = [[0] * n for _ in range(n)]
    draw_empty_board(canvas, n, cell_size)
    fill_board(board, 0, canvas, cell_size, delay)
    return board


def is_valid(board, i, j):
    for index in range(j):
        if board[i][index] == 1:
            return False
    for index in range(i):
        if board[index][j] == 1:
            return False
    row_index, col_index = i - 1, j - 1
    while row_index >= 0 and col_index >= 0:
        if board[row_index][col_index] == 1:
            return False
        row_index -= 1
        col_index -= 1
    row_index, col_index = i - 1, j + 1
    while row_index >= 0 and col_index < len(board[0]):
        if board[row_index][col_index] == 1:
            return False
        row_index -= 1
        col_index += 1
    return True


def draw_empty_board(canvas, n, cell_size):
    for i in range(n):
        for j in range(n):
            x1, y1 = j * cell_size, i * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            color = "white" if (i + j) % 2 == 0 else "gray"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, tags="board")


def update_board(canvas, board, cell_size):
    canvas.delete("queen")
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                x1, y1 = j * cell_size, i * cell_size
                x2, y2 = x1 + cell_size, y1 + cell_size
                canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill="black", tags="queen")
    canvas.update()


def fill_board(board, row, canvas, cell_size, delay):
    if row >= len(board):
        return True

    for col in range(len(board[0])):
        board[row][col] = 1
        update_board(canvas, board, cell_size)
        time.sleep(delay)

        if is_valid(board, row, col):
            if fill_board(board, row + 1, canvas, cell_size, delay):
                return True

        board[row][col] = 0
        update_board(canvas, board, cell_size)
        time.sleep(delay / 2)  # Shorter delay for backtracking

    return False


def visualize_n_queens():
    n = 4  # Change this value for different board sizes
    cell_size = 50
    canvas_width = canvas_height = n * cell_size
    delay = 0.1  # Delay between steps (seconds)

    root = tk.Tk()
    root.title("N-Queens Visualization")

    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    board = n_queens(n, canvas, cell_size, delay)

    # Add a label to indicate completion
    tk.Label(root, text="Solution found!", font=("Arial", 14)).pack()

    root.mainloop()


visualize_n_queens()