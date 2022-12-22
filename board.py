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
        self.sqr_num = 0
        self.ranks = {}
        self.files = {}

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
        """gets key from coords value"""

        for k, v in self.coordinates.items():
            if coords == v:
                return k
                

    def define_ranks_files(self):

        rank1 = [i for i in range(1, 12)]
        rank2 = [i for i in range(12, 23)]
        rank3 = [i for i in range(23, 34)]
        rank4 = [i for i in range(34, 45)]
        rank5 = [i for i in range(45, 56)]
        rank6 = [i for i in range(56, 67)]
        rank7 = [i for i in range(67, 78)]
        rank8 = [i for i in range(78, 89)]
        rank9 = [i for i in range(89, 100)]
        rank10 = [i for i in range(100, 111)]
        rank11 = [i for i in range(111, 122)]

        for k, v in self.coordinates.items():
            if k in rank1:
                sqrs = [].append(v)
            else: 
                self.ranks[1] = sqrs

        print(self.ranks)