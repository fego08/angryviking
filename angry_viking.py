import sys
import pygame
from settings import Settings
from board import Board
from king import King
from defender import Defender
from attacker import Attacker
from selector import Selector

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
        self.selector = Selector()
        self.selectors = pygame.sprite.Group()
        self.defenders = pygame.sprite.Group()
        self.attackers = pygame.sprite.Group()
        self.board.draw_board()
        self.board.get_coords()
        self._set_start()

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
        if event.key == pygame.K_DOWN:
            if self.selector.rect.center != self.board.coordinates.items[111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121]:
                self.selector.rect.centery += 60
        if event.key == pygame.K_UP:
            self.selector.rect.centery -= 60
        if event.key == pygame.K_LEFT:
            self.selector.rect.centerx -= 60
        if event.key == pygame.K_RIGHT:
            self.selector.rect.centerx += 60

    def _update_display(self):
        """helpfunction for updating the screen"""

        self.screen.fill(self.settings.bg_color)
        self.board.draw_board()
        self.defenders.draw(self.screen)
        self.attackers.draw(self.screen)
        self.selectors.draw(self.screen)
        pygame.display.flip()

    def _set_start(self):
        """sets up the pieces"""

        self.selector.rect.center = self.board.coordinates[61]
        self.selector.add(self.selectors)
        
        self.king.rect.center = self.board.coordinates[61]
        self.defenders.add(self.king)
        
        for sqr in self.defender.startsqrs:
            self.defender_new = Defender()
            self.defender_new.rect.center = self.board.coordinates[sqr]
            self.defender_new.add(self.defenders)

        for sqr in self.attacker.startsqrs:
            self.attacker_new = Attacker()
            self.attacker_new.rect.center = self.board.coordinates[sqr]
            self.attacker_new.add(self.attackers)
    
if __name__ == ("__main__"):

    av = AngryViking()
    av.run_game()