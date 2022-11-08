import pygame
from settings import Settings
from board import Board
from pygame.sprite import Sprite

class Selector(Sprite):

    def __init__(self):
        super().__init__()

        self.settings = Settings()
        self.board = Board()
        self.startsqrs = [61]

        self.screen = self.screen = pygame.display.set_mode((
            self.settings.screen_width, 
            self.settings.screen_height
        ))
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("images/selector.gif")
        self.rect = self.image.get_rect()

        self.y_move = 0
        self.x_move = 0