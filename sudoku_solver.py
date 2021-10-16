"""
solves a given sudoku solver given a 9 by 9 board
"""
from eight_queens import print_board
from typing import List

def print_board(board: List[List[int]]):
    for i in range(N):
        if i%(N//3) == 0 and i != 0:
            print("- - - - - - - - - - -")
        
        for j in range(N):
            if j%(N//3) == 0 and j != 0:
                print("| ", end="")
            print(f"{str(board[i][j])} ", end="")
            if j == N-1:
                print()
    
    


def find_next_tile(board: List[List[int]]) -> tuple[int, int]:
    """
    finds the next tile with no number in it
    """
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                return (i, j)
    
    return None


def solve_board_til(board: List[List[int]]) -> bool:
    """
    recursively solves board
    """
    
    next_tile = find_next_tile(board)
    if not next_tile:
        return True
    else:
        row, col = next_tile
    
    for i in range(1, 10):
        if is_valid(board, row, col, i):
            board[row][col] = i 

            if solve_board_til(board):
                return True
            
            board[row][col] = 0
    
    return False

def solve_board(board: List[List[int]]) -> bool:
    """
    solves the board
    """
    if solve_board_til(board):
        print_board(board)
        return True
    print("no solution") 
    return False

def is_valid(board: List[List[int]], row: int, col: int, num: int) -> bool:
    """
    checks to see if placing a number num at position (row, col) is valid, by
    checking if the row, column, and 3x3 tile does not already contain num
    """

    # checks the row to see if num already exists
    for i in range(N):
        if board[row][i] == num and i != col:
            return False

    # checks the column to see if num already exists
    for i in range(N):
        if board[i][col] == num and i != row:
            return False


    row_box = row // 3
    col_box = col // 3

    for i in range(row_box*3, row_box*3 + 3):
        for j in range(col_box*3, col_box*3 + 3):
            if board[i][j] == num and (i, j) != (row, col):
                return False

    return True

if __name__ == "__main__":
    N = 9
    # board = [[9, 0, 0, 0, 0, 0, 0, 3, 8],
    #          [0, 5, 0, 2, 4, 6, 7, 9, 1],
    #          [0, 0, 0, 3, 0, 0, 4, 0, 0],
    #          [7, 0, 3, 0, 5, 8, 1, 0, 2],
    #          [0, 0, 0, 0, 0, 0, 0, 6, 7],
    #          [0, 0, 0, 0, 9, 0, 3, 8, 0],
    #          [0, 3, 0, 0, 0, 5, 8, 2, 4],
    #          [5, 8, 2, 4, 0, 3, 6, 1, 9],
    #          [0, 6, 9, 0, 2, 1, 5, 0, 0]]
    
    # board = [[5, 0, 4, 0, 7, 8, 9, 1, 0],
    #          [6, 7, 2, 1, 9, 5, 3, 4, 8],
    #          [1, 9, 8, 3, 4, 2, 5, 6, 7],
    #          [8, 5, 9, 0, 6, 1, 4, 2, 0],
    #          [4, 2, 6, 8, 5, 3, 7, 9, 1],
    #          [0, 0, 0, 9, 0, 4, 8, 5, 0],
    #          [9, 6, 1, 5, 0, 0, 2, 8, 4],
    #          [2, 8, 7, 4, 1, 9, 6, 0, 5],
    #          [3, 0, 5, 2, 8, 0, 1, 7, 0]]

    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    solve_board(board)