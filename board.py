import pygame
from settings import Settings

class Board:
        
    def __init__(self):

        self.settings = Settings()
        self.surface = pygame.display.get_surface()
        self.cell_color = ((255, 255, 255))
        self.cell_size = 60
