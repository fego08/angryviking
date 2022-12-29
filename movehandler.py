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
        self.leftsquares = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.topsquares = [12, 23, 34, 45, 56, 67, 78, 89, 100, 111]
        self.bottomsquares = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121]
        self.rightsquares = [111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121]
        self.attacker_coords = []
        self.attacker_sqrs = []
        self.defender_coords = []
        self.defender_sqrs = []
        self.legal_squares = []
    
    def get_legal_moves(self, square):
        """gets squarenumbers of legal squares"""
        
        self.is_active = True

        for coord in self.attacker_coords:
            for k, v in self.settings.coordinates.items():
                if coord == v:
                    self.attacker_sqrs.append(k)
        
        for coord in self.defender_coords:
            for k, v in self.settings.coordinates.items():
                if coord == v:
                    self.defender_sqrs.append(k)

        for i in range(12):
            x = square + i
            self.legal_moves.append(x)
            if x in self.bottomsquares:
                break
        for i in range(12):
            y = square - i
            if y != square:
                self.legal_moves.append(y)
            if y in self.topsquares:
                break
        for i in range(12):
            z = square + i*11
            if z != square:
                self.legal_moves.append(z)
            if z in self.rightsquares:
                break
        for i in range(12):
            p = square - i*11
            if p != square:
                self.legal_moves.append(p)
            if p in self.leftsquares:
                break
        for move in self.legal_moves:
            if move in self.attacker_sqrs:
                self.legal_moves.remove(move)
        
        self.legal_moves = [x for x in self.legal_moves if x not in self.attacker_sqrs]
        self.legal_moves = [x for x in self.legal_moves if x not in self.defender_sqrs]
        self.write_legal_moves(self.legal_moves)
        self.legal_moves = []
        
    def write_legal_moves(self, squares):
        
        for square in squares:
            
            coord = self.settings.coordinates[square]
            self.legal_squares.append(coord)