import pygame
pygame.init()
pygame.font.init()

WHITE = (255, 255,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
GREEN = (0, 255, 0)

FPS = 60

WIDTH, HEIGHT = 600, 700

TOOLBAR_HEIGHT = HEIGHT - WIDTH

ROWS = COLS = 50

PIXEL_SIZE = WIDTH // ROWS

BG_COLOR = WHITE

DRAW_GRID_LINES = False

def get_font(size):
   return pygame.font.SysFont('comicsans', size)