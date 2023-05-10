#!/usr/bin/env python3

import sys

def print_board(board):
    for row in board:
        print(" ".join(row))

def is_safe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == "Q":
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    # The position is safe
    return True

def solve_n_queens(board, col, n):
    if col == n:
        print_board(board)
        return True

    # Consider this column and try placing a queen in all rows one by one
    solved = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = "Q"
            solved = solve_n_queens(board, col + 1, n) or solved
            board[i][col] = "."

    return solved

def n_queens(n):
    # Check input arguments
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize board
    board = [["." for _ in range(n)] for _ in range(n)]

    # Solve N-Queens problem
    if not solve_n_queens(board, 0, n):
        print("No solution exists for N={}".format(n))
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    n_queens(n)
