import sys
import pygame
from settings import Settings
from board import Board
from gamepieces import Gamepieces

class AngryViking:
    """main game class"""

    def __init__(self):
        """initializes game assets and functions"""
        # initialize pygame and assets
        pygame.init()
        self.settings = Settings()
        self.board = Board()
        self.gamepieces = Gamepieces()

        # display stuff (keep display.flip() at the end of this block)
        self.screen = pygame.display.set_mode((self.settings.screen_width, 
        self.settings.screen_height))
        self.bg_color = self.settings.bg_color
        self.rect = self.screen.get_rect()
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("AngryViking")
        

    def run_game(self):
        """main game loop"""

        while True:
            self.check_events()
            self._update_display()
    
    def check_events(self):
        """checks for keypresses etc"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys(exit)
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
   
    def draw_board(self):
        """draws the gameboard"""

        for i in range(1,12):
            for j in range(1,12):
                    pygame.draw.rect(self.screen, self.board.cell_color, 
                    (self.board.cell_size * i ,self.board.cell_size * j,
                    self.board.cell_size, self.board.cell_size), 
                    1)

    def draw_pieces(self):
        """draws the gamepieces"""

        self.attacker = pygame.draw.circle(self.screen, 
        self.gamepieces.att_color, (40, 40), 20.0)

        
    def _check_keydown_events(self, event):
        """helpfunction for keydown events"""

        if event.key == pygame.K_q:
            sys.exit()

    def _update_display(self):
        """helpfunction for updating the screen"""

        self.screen.fill(self.settings.bg_color)
        self.draw_board()
        self.draw_pieces()
        pygame.display.flip()


if __name__ == ("__main__"):

    av = AngryViking()
    av.run_game()