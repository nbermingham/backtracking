import pygame
import importlib.util
import sys

from pygame import color

class Board:

    def __init__(self, rows: int, cols: int, width: int, height: int, done: bool) -> None:
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.done = done
    
    def draw(self):
        gap = self.width // 9
        for i in range(self.rows+1):
            if i % 3 == 0:
                thickness = 4
            else: 
                thickness = 1
            pygame.draw.line(self.win, (0, 0, 0), (0, i*gap), (self.width, i*gap), thickness)
            pygame.draw.line(self.win, (0, 0, 0), (i*gap, 0), (i*gap, self.height), thickness)

class Tile:
    rows = 9
    cols = 9

    def __init__(self, val: int, row: int, col: int, width: int, height: int) -> None:
        self.val = val
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height

    def draw(self, win):
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width // 9
        x = self.col * gap
        y = self.row * gap

def redraw_window(win, board):
    win.fill((255, 255, 255))
    board.draw()

def main():
    run = True
    win = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku")

    board = [[9, 0, 0, 0, 0, 0, 0, 3, 8],
             [0, 5, 0, 2, 4, 6, 7, 9, 1],
             [0, 0, 0, 3, 0, 0, 4, 0, 0],
             [7, 0, 3, 0, 5, 8, 1, 0, 2],
             [0, 0, 0, 0, 0, 0, 0, 6, 7],
             [0, 0, 0, 0, 9, 0, 3, 8, 0],
             [0, 3, 0, 0, 0, 5, 8, 2, 4],
             [5, 8, 2, 4, 0, 3, 6, 1, 9],
             [0, 6, 9, 0, 2, 1, 5, 0, 0]]
    
    board = Board(9, 9, 540, 540, win)


    while run:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # redraw_window(win, board)



main()
pygame.quit()


