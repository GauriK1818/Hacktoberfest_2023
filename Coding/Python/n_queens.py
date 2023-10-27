def is_safe(board, row, col, n):
    # Check if a queen can be placed at board[row][col] without conflicts

    # Check the left side of the column
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower left diagonal
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    
    def solve(col):
        if col == n:
            return True
        
        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                if solve(col + 1):
                    return True
                board[i][col] = 0

        return False
    
    if not solve(1):
        return None  # No solution
    
    return board

def print_board(board):
    if board is None:
        print("No solution exists.")
    else:
        for row in board:
            print(" ".join("Q" if cell == 1 else "." for cell in row))

if __name__ == "__main__":
    n = 8  # Change this to the desired board size
    first_queen_row = 0  # Change this to the desired row for the first queen
    board = solve_n_queens(n)
    if board is not None:
        board[first_queen_row][0] = 1  # Place the first queen
    print_board(board)
