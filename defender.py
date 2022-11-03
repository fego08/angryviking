import pygame
from settings import Settings
from board import Board
from pygame.sprite import Sprite

class Defender(Sprite):

    def __init__(self):
        super().__init__()
        
        self.settings = Settings()
        self.board = Board()

        self.screen = self.screen = pygame.display.set_mode((
            self.settings.screen_width, 
            self.settings.screen_height
        ))
        self.screen_rect = self.screen.get_rect()
        
        self.image = pygame.transform.scale(
            pygame.image.load("images/defender.gif"), (
                self.board.cell_size, self.board.cell_size
            )
        )
        self.rect = self.image.get_rect()