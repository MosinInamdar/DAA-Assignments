# Utility function to check if it's safe to place a queen at board[row][col]
def is_safe(board, row, col, n):
    # Check the column on the left side
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

# Utility function to solve n-Queens problem using backtracking
def solve_n_queens(board, row, n):
    # Base case: If all queens are placed, return True
    if row >= n:
        return True

    # Try placing the queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            # Place the queen
            board[row][col] = 1

            # Recursively place the rest of the queens
            if solve_n_queens(board, row + 1, n):
                return True

            # If placing queen at board[row][col] doesn't lead to a solution, backtrack
            board[row][col] = 0

    # If the queen cannot be placed in any column in this row, return False
    return False

# Function to initialize the board and place the first queen
def n_queens_with_first_queen_placed(n, first_queen_row, first_queen_col):
    # Initialize the board with all 0s
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Place the first queen at the given position
    board[first_queen_row][first_queen_col] = 1

    # Solve the rest of the n-Queens problem starting from the next row
    if solve_n_queens(board, first_queen_row + 1, n):
        return board
    else:
        return None  # No solution found

# Function to print the board
def print_board(board):
    if board is None:
        print("No solution exists!")
    else:
        for row in board:
            print(" ".join(str(cell) for cell in row))

# Example usage
n = 8  # Size of the chessboard (n x n)
first_queen_row = 0  # Row index of the first queen
first_queen_col = 0  # Column index of the first queen

# Solve the n-Queens problem with the first queen placed
solution = n_queens_with_first_queen_placed(n, first_queen_row, first_queen_col)

# Print the solution
print_board(solution)

'''
Time complexity : O(n!)
Space complexity : O(n^2)
'''
