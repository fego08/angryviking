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
    
        # self.sidesqrl = self.coordinates.keys[1, 12, 23, 34, 45, 56, 67, 78, 89, 100, 111]
        # self.sidesqrr = self.coordinates.keys[11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121]
        # self.topsqr = self.coordinates.keys[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        # self.bottomsqr = self.coordinates.keys[111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121]