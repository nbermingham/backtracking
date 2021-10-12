"""
solves a given sudoku solver given a 9 by 9 board
"""
from eight_queens import print_board
from typing import List

def solve_board_til(board: List[List[int]], presets: set(int), curr: int, val: int) -> bool:
    """
    recursively solves board
    """

    if val > 8:
        return False
    
    if curr >= N**2:
        return True

    # if current coordinates is in presets, go to next coordinate
    if curr in presets:
        return solve_board_til(board, presets, curr + 1, 1)
    
    row, col = divmod(curr, N)
    if is_valid(board, (row, col), val):
        board[row][col] = val
        if solve_board_til(board, presets, curr+1, 1):
            return True
        
        solve_board_til(board, presets, curr, val+1)

    

    
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
    presets = ()
    for i in range(N):
        for j in range(N):
            presets.add(9*i+j)
    if solve_board_til(board, presets, 0, 1):
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
    # checks the row and the column to see if num already exists
    for i in range(N):
        if board[row][i] == num or board[i][col] == num:
            return False

    if 0 <= row <= 2 and 0 <= col <= 2:
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == num:
                    return False
        
    if 0 <= row <= 2 and 3 <= col <= 5:
        for i in range(0, 3):
            for j in range(2, 5):
                if board[i][j] == num:
                    return False
    
    if 0 <= row <= 2 and 6 <= col <= 8:
        for i in range(0, 3):
            for j in range(6, 8):
                if board[i][j] == num:
                    return False

    if 3 <= row <= 5 and 0 <= col <= 2:
        for i in range(3, 5):
            for j in range(0, 3):
                if board[i][j] == num:
                    return False

    if 3 <= row <= 5 and 3 <= col <= 5:
        for i in range(3, 5):
            for j in range(3, 5):
                if board[i][j] == num:
                    return False

    if 3 <= row <= 5 and 6 <= col <= 8:
        for i in range(3, 5):
            for j in range(6, 8):
                if board[i][j] == num:
                    return False

    if 6 <= row <= 8 and 0 <= col <= 2:
        for i in range(6, 8):
            for j in range(0, 3):
                if board[i][j] == num:
                    return False

    if 6 <= row <= 8 and 3 <= col <= 5:
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == num:
                    return False

    if 6 <= row <= 8 and 6 <= col <= 8:
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == num:
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