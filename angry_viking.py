import sys
import pygame
from settings import Settings
from board import Board
from king import King
from defender import Defender
from attacker import Attacker
from selector import Selector
from movehandler import Player
from movehandler import Movehandler

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
        self.active_piece = pygame.sprite.Group()
        self.selectors_position = []
        self.defenders_position = []
        self.attackers_position = []
        self.Player = Player()
        self.movehandler = Movehandler()
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
        if event.key == pygame.K_t:
            pass
        if event.key == pygame.K_DOWN:
            if self.selector.rect.bottom != 720:
                self.selector.rect.centery += 60
                self._update_selector_coordinates()
        if event.key == pygame.K_UP:
            if self.selector.rect.top != 60:
                self.selector.rect.centery -= 60
                self._update_selector_coordinates()
        if event.key == pygame.K_LEFT:
            if self.selector.rect.left != 60:
                self.selector.rect.centerx -= 60
                self._update_selector_coordinates()
        if event.key == pygame.K_RIGHT:
            if self.selector.rect.right != 720:
                self.selector.rect.centerx += 60
                self._update_selector_coordinates()
        if event.key == pygame.K_SPACE:
            if self.movehandler.is_active == False:
                self._select_piece()
            elif self.movehandler.is_active == True:
                self._move_piece()

    def _update_display(self):
        """helpfunction for updating the screen"""

        self.screen.fill(self.settings.bg_color)
        self.board.draw_board()
        self.defenders.draw(self.screen)
        self.attackers.draw(self.screen)
        self.selectors.draw(self.screen)
        if self.movehandler.is_active == True:
            for square in self.movehandler.legal_squares:
                pygame.draw.circle(self.screen, (255, 0, 0), (square[0], square[1]), 10.0)
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
        self._get_start_coordinates()

    def _get_start_coordinates(self):
        
        for defender in self.defenders:
            self.defenders_position.append(defender.rect.center)
            self.movehandler.defender_coords.append(defender.rect.center)
        for attacker in self.attackers:
            self.attackers_position.append(attacker.rect.center)
            self.movehandler.attacker_coords.append(attacker.rect.center)

    def _update_selector_coordinates(self):

        for selector in self.selectors:
            self.selectors_position = selector.rect.center

    def _select_piece(self):

        if self.selectors_position in self.defenders_position:
            for defender in self.defenders.sprites():
                if self.selectors_position == defender.rect.center:
                    defender.add(self.active_piece)
                    current_sqr = self.board.get_square_num(self.selectors_position)
                    self.movehandler.get_legal_moves(current_sqr)
        elif self.selectors_position in self.attackers_position:
            print("Attacker Selected!")
        else:
            print("No piece here!")
    
    
    def _move_piece(self):
        
        if self.selectors_position not in self.defenders_position:
            if self.selectors_position not in self.attackers_position:
                if self.selectors_position in self.movehandler.legal_squares:
                    for defender in self.defenders.sprites():
                        if defender in self.active_piece.sprites():
                            defender.rect.center = self.selectors_position
                            defender.remove(self.active_piece)       
        self.movehandler.legal_squares = []
        self.movehandler.is_active = False
        self.defenders_position = []
        self.movehandler.defender_coords = []
        self.movehandler.defender_sqrs = []
        self.attackers_position = []
        self.movehandler.attacker_coords = []
        self.movehandler.attacker_sqrs = []
        self._get_start_coordinates()
        
if __name__ == ("__main__"):

    av = AngryViking()
    av.run_game()