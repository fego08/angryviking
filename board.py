import pygame
from settings import Settings

class Board:
        
    def __init__(self):
        
        self.settings = Settings()
        self.screen = self.screen = pygame.display.set_mode((
            self.settings.screen_width, 
            self.settings.screen_height
        ))
        self.screen_rect = self.screen.get_rect()        
        self.cells = []
        self.ROWS, self.COLUMNS = 12, 12
        self.border_color = ((84, 84, 84))
        self.cell_color = ((239, 245, 203))
        self.cell_size = 60
        self.castle_color = ((53, 115, 109))
        self.coordinates = {}

    def draw_board(self):
        """draws the gameboard"""
        
        # draws base board
        for i in range(1, self.COLUMNS):
            for j in range(1, self.ROWS):
                pygame.draw.rect(
                    self.screen, self.cell_color, (
                        self.cell_size * i, self.cell_size * j, 
                        self.cell_size, self.cell_size
                    )
                )
                cell = pygame.draw.rect(
                    self.screen, self.border_color, (
                        self.cell_size * i, self.cell_size * j, 
                        self.cell_size, self.cell_size
                    ), 1
                )
                if len(self.cells) <= 120:
                    self.cells.append(cell.center)
                if (
                    i == 1 and j == 1
                ) or (
                    i == 11 and j == 1
                ) or (
                    i == 1 and j == 11
                ) or (
                    i == 11 and j == 11
                ) or  (
                    i == 6 and j == 6
                ):
                    pygame.draw.rect(
                        self.screen, self.castle_color, (
                            self.cell_size * i, self.cell_size * j, 
                            self.cell_size, self.cell_size
                        )
                    )
                    pygame.draw.rect(
                        self.screen, self.border_color, (
                            self.cell_size * i, self.cell_size * j, 
                            self.cell_size, self.cell_size
                    ), 1
                )
        
    def get_coords(self):
        """takes coords from cells[] and puts into dict for future use"""

        self.coordinates = {}
        for i, x in enumerate(self.cells[:], start=1):
            self.coordinates[i] = x
        self.coordinates = self.coordinates

    def get_square_num(self, coords):

        sqr_num = [k for k, v in self.coordinates.items() if v == coords][0]
        return sqr_num

        
