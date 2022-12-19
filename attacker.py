import pygame
from settings import Settings
from board import Board
from pygame.sprite import Sprite

class Attacker(Sprite):

    def __init__(self):
        super().__init__()
        
        self.settings = Settings()
        self.board = Board()
        self.startsqrs = [
            4, 5, 6, 7, 8, 17, 34, 45, 56, 67, 78, 57, 114, 115, 116, 117, 118, 105, 44, 55, 66, 77, 88, 65
        ]
    
        self.screen = pygame.display.set_mode((
            self.settings.screen_width, 
            self.settings.screen_height
        ))
        self.screen_rect = self.screen.get_rect()
        
        self.image = pygame.transform.scale(
            pygame.image.load("images/attackerthicc.gif"), (
                self.board.cell_size, self.board.cell_size
            )
        )
        self.rect = self.image.get_rect()
        self.active = False
        self.position = ()