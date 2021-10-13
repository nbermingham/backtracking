"""
solves a given sudoku solver given a 9 by 9 board
"""
from eight_queens import print_board
from typing import List

def find_next_tile(board: List[List[int]]) -> tuple(int, int):
    """
    finds the next tile with no number in it
    """
    for i in range(N):
        for j in range(N):
            if not board[i][j]:
                return (i, j)
    
    return None


def solve_board_til(board: List[List[int]], curr: int, val: int) -> bool:
    """
    recursively solves board
    """
    next_tile = find_next_tile(board)
    if not next_tile:
        return True
    else:
        row, col = next_tile

    
    row, col = divmod(curr, N)
    if is_valid(board, tuple(row, col), val):
        board[row][col] = val
        if solve_board_til(board, curr+1, 1):
            return True
        
        solve_board_til(board, curr, val+1)

    

    
#    for i in range(N**2):
#        val = 1
#        row, col = divmod(i, N)
#        if is_valid(board, row, col, val):
#            board[row][col] = val
#            if solve_board_til(board, presets, curr+1, val):
#                return True
#            if val == 8:
#                return False
#            else:
#                return solve_board_til(board, presets, curr, val + 1)
        
    
    return False

def solve_board(board: List[List[int]]) -> bool:
    """
    solves the board
    """
    if solve_board_til(board, 0, 1):
        print_board(board)
        return True
    print("no solution") 
    return False

def is_valid(board: List[List[int]], coords: tuple(int, int), num: int) -> bool:
    """
    checks to see if placing a number num at position (row, col) is valid, by
    checking if the row, column, and 3x3 tile does not already contain num
    """
    (row, col) = coords
    # checks the row to see if num already exists
    for i in range(N):
        if board[row][i] == num and (row, i) != coords:
            return False

    # checks the column to see if num already exists
    for i in range(N):
        if board[i][col] == num and (i, col) != coords:
            return False


    row_box = row // 3
    col_box = col // 3

    for i in range(row_box*3, row_box*3 + 3):
        for j in range(col_box*3, col_box*3 + 3):
            if board[i][j] == num and (i, j) != coords:
                return False

    return True

if __name__ == "__main__":
    N = 9
    board = [[9, 0, 0, 0, 0, 0, 0, 3, 8],
             [0, 5, 0, 2, 4, 6, 7, 9, 1],
             [0, 0, 0, 3, 0, 0, 4, 0, 0],
             [7, 0, 3, 0, 5, 8, 1, 0, 2],
             [0, 0, 0, 0, 0, 0, 0, 6, 7],
             [0, 0, 0, 0, 9, 0, 3, 8, 0],
             [0, 3, 0, 0, 0, 5, 8, 2, 4],
             [5, 8, 2, 4, 0, 3, 6, 1, 9],
             [0, 6, 9, 0, 2, 1, 5, 0, 0]]

    solve_board(board)