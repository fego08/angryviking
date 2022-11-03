import sys
import pygame
from settings import Settings
from board import Board
from king import King
from defender import Defender
from attacker import Attacker

class AngryViking:
    """main game class"""

    def __init__(self):
        """initializes game assets and functions"""
        # initialize pygame and assets
        pygame.init()
        self.settings = Settings()
        self.board = Board()
        self.king = King()
        self.defender = Defender()
        self.attacker = Attacker()
        self.defenders = pygame.sprite.Group()
        self.attackers = pygame.sprite.Group()
        self.board.draw_board()
        self.board.get_coords()

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
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
        
    def _check_keydown_events(self, event):
        """helpfunction for keydown events"""

        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_u:
            self._set_start()
        
    def _update_display(self):
        """helpfunction for updating the screen"""

        self.screen.fill(self.settings.bg_color)
        self.board.draw_board()
        self.defenders.draw(self.screen)
        self.attackers.draw(self.screen)
        pygame.display.flip()

    def _set_start(self):
        """sets up the pieces"""

        self.king.rect.center = self.board.coordinates[60]
        self.defenders.add(self.king)
        self.defender.rect.center= self.board.coordinates[1]
        self.defenders.add(self.defender)
        self.attacker.rect.center = self.board.coordinates[120]
        self.attackers.add(self.attacker)

    
if __name__ == ("__main__"):

    av = AngryViking()
    av.run_game()