import pygame
from settings import Settings
from board import Board
from selector import Selector
from king import King
from attacker import Attacker
from defender import Defender

class Player:
    """determines player def or att"""
    def __init__(self):
        self.switch_player = True

class Movehandler:
    """adds piece functionality"""

    def __init__(self):
        self.settings = Settings()
        self.board = Board()
        self.selector = Selector()
        self.king = King()
        self.attacker = Attacker()
        self.Defender = Defender()
        self.screen = pygame.display.set_mode((
            self.settings.screen_width, 
            self.settings.screen_height
        ))
        self.screen_rect = self.screen.get_rect()
        self.is_attacker = False
        self.is_defender = False
        self.is_active = False
        self.legal_moves = {}
    
    def select_piece(self):
        pass

    def determine_legal_moves(self):
        
        pass


    def show_legal_moves(self):
        if self.is_active == True:
            pass
            # highlight legal squares
            # pygame.draw.rect(self.screen_rect, (255, 0, 0), asdf)