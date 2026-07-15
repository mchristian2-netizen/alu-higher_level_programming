#!/usr/bin/python3
"""N-Queens puzzle solver using backtracking."""

import sys


def print_solution(board):
    """Print the board configuration as a list of [row, col] pairs."""
    solution = []
    for row in range(len(board)):
        solution.append([row, board[row]])
    print(solution)


def is_safe(board, row, col):
    """Check if a queen can be placed at board[row][col]."""
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(board, row, n):
    """Recursively place queens using backtracking."""
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n)
            board[row] = -1  # backtrack


def main():
    """Main entry point for the N-Queens program."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    main()
