from threads import NetThread
import pygame
import sys

pygame.init()

class GameInfo:

    def __init__(self):
        self.COLS = 7
        self.ROWS = 6
        self.SQUARE_SIZE = 90
        self.CHIP_SIZE = int(self.SQUARE_SIZE/2 - 6)
        self.FRAMERATE = 60
        self.BLACK = (5, 5, 5)
        self.BLUE = (10, 10, 220)
        self.RED = (220, 10, 10)
        self.YELLOW = (250, 250, 5)
        self.width = self.COLS * self.SQUARE_SIZE
        self.height = (self.ROWS + 1) * self.SQUARE_SIZE
        self.size = (self.width, self.height)
        self.netThread = NetThread()
        self.mousex = 0
        self.no_winner = True
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.win_msg = pygame.font.SysFont("Comic Sans MS", 75)
