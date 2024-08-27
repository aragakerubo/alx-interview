#!/usr/bin/python3
"""N queens puzzle"""
import sys


def isSafe(board, row, col):
    """Check if a queen can be placed on board[row][col]"""
    for q in range(col):
        if board[q] is row or abs(board[q] - row) is abs(q - col):
            return False
    return True


def solveNQ(board, col):
    """Solve N queens problem"""
    n = len(board)
    if col is n:
        print(str([[c, board[c]] for c in range(n)]))
        return
    for i in range(n):
        if isSafe(board, i, col):
            board[col] = i
            solveNQ(board, col + 1)


if __name__ == "__main__":
    if len(sys.argv) is not 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [0 for i in range(N)]
    solveNQ(board, 0)
