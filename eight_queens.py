"""
backtracking algorithm to solve eight queens problem
"""

from typing import List


def print_board(board: List[List[int]]):
    """
    prints out board
    """
    for i in range(len(board)):
        print(*board[i], sep=" ")


def solve_nq_til(board: List[List[int]], col: int, n: int) -> bool:
    """
    recursively places queens until all are placed
    """
    if col >= n:
        return True
    for i in range(N):
        if is_valid(board, i, col):
            board[i][col] = 1
            if solve_nq_til(board, col + 1, n):
                return True
            board[i][col] = 0

    return False

def is_valid(board: List[List[int]], row: int, col: int) -> bool:
    """
    checks to see placing the queen at row, col will make a valid board
    """
    n = len(board)
    # checks all the tiles in the column
    for i in range(n):
        if board[i][col]:
            return False
        if board[row][i]:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True

def solve_nq(board: List[List[int]], n: int) -> bool:
    """
    solves
    """
    if solve_nq_til(board, 0, n):
        print_board(board)
        return True

    print("No solution!")
    return False

if __name__ == "__main__":
    N = 5

    BOARD = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]

    solve_nq(BOARD, N)
