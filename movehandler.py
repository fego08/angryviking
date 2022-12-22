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
        self.legal_moves = []
        self.edgesquares = [
            1,2,3,4,5,6,7,8,9,10,11,22,33,44,55,66,77,88,99,110,121,12,23,34,45,56,67,78,89,100,111,112,113,114,115,116,117,118,119,120
        ]
    def get_legal_moves(self, square):

        # right
        for i in range(12):
            x = square + i
            self.legal_moves.append(x)
            if x in self.edgesquares:
                break
            y = square - i
            if y != square:
                self.legal_moves.append(y)
            if y in self.edgesquares:
                break
            z = square + i*11
            if z != square:
                self.legal_moves.append(z)
            if z in self.edgesquares:
                break
            p = square - i*11
            if p != square:
                self.legal_moves.append(p)
            if p in self.edgesquares:
                break
        print(sorted(self.legal_moves))
        self.legal_moves = []
        
    def show_legal_moves(self, setsqr):
        
        pass