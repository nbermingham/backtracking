import pygame
import random
import sys

from pygame import rect

class snake(object):
    
    def __init__(self):
        pass

    def get_head_position(self):
        pass
    
    def turn(self):
        pass

    def draw(self):
        pass

    def reset(self):
        pass

    def handle_keys(self):
        pass


class food(object):
    
    def __init__(self):
        pass

    def randomize_position(self):
        pass

    def draw(self, surface):
        pass


def draw_grid(surface):
    for x in range(GRID_HEIGHT):
        for y in range(GRID_WIDTH):
            r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
            c = (93, 216, 228) if (x+y)%2 == 0 else (84, 194, 205)
            pygame.draw.rect(surface, c, r)


SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

GRIDSIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRIDSIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRIDSIZE

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)

    snake = snake()

main()

