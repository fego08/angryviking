import pygame
from settings import Settings
from board import Board
from pygame.sprite import Sprite

class Defender(Sprite):

    def __init__(self):
        super().__init__()
        
        self.settings = Settings()
        self.board = Board()
        self.startsqrs = [
            49, 50, 51, 60, 62, 71, 72, 73, 59, 39, 63, 83
        ]

        self.screen = self.screen = pygame.display.set_mode((
            self.settings.screen_width, 
            self.settings.screen_height
        ))
        self.screen_rect = self.screen.get_rect()
        
        self.image = pygame.transform.scale(
            pygame.image.load("images/defenderthicc.gif"), (
                self.board.cell_size, self.board.cell_size
            )
        )
        self.rect = self.image.get_rect()
        self.active = False
        self.position = ()
