# New file containing 8 queens backtracking problem
from typing import List

def print_board(board: List[List[int]]):
    """
    prints out the entire board
    """
    for i in range(len(board)):
        print(board[i])

def is_safe(board: List[List[int]], row: int, col: int) -> bool:
    """
    check the row, column and diagonals to see if another queen is there
    """

    n = len(board)

    #checks the row
    for i in range(col):
        if board[row][i]:
            return False

    #checks upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    #checks lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, n, 1)):
        if board[i][j]:
            return False

    return True

def solve_nq_til(board, col) -> bool:
    """
    solves
    """

    #base case: we've already placed all the queens 
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_nq_til(board, col + 1):
                return True

            board[i][col] = 0

    return False


def solve_nq(board: List[List[int]], int) -> bool:
    """
    solves
    """
    if not solve_nq_til(board, 0):
        print("Solution does not exist")
        return False

    print_board(board)
    return True


N = 8

board_two = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]


# print(board_two)

solve_nq(board_two, N)
