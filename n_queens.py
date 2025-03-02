def n_queens(n):
    board = [[0]*n for _ in range(n)]
    fill_board(board, 0)
    for row in board:
        updated_row = ["♛" if _ == 1 else "_" for _ in row ]
        print(updated_row)

def is_valid(board, i, j):
    for index in range(j):
        if board[i][index] == 1:
            return False
    for index in range(i):
        if board[index][j] == 1:
            return False
    row_index = i-1
    col_index = j-1
    while row_index>=0 and col_index>=0:
        if board[row_index][col_index] == 1:
            return False
        row_index-=1
        col_index-=1
    row_index = i - 1
    col_index = j + 1
    while row_index >= 0 and col_index < len(board[0]):
        if board[row_index][col_index] == 1:
            return False
        row_index -= 1
        col_index += 1
    return True


def fill_board(board, row):
    if row >= len(board):
        return True
    for col in range(len(board[0])):
        board[row][col]=1
        if is_valid(board, row, col):
            if fill_board(board, row+1):
                return True
        board[row][col]=0
    return False

def main():
    n = input("Enter the number of queens: ")
    n_queens(int(n))

main()