import pygame
from settings import Settings
from board import Board

class Gamepieces:

    def __init__(self):
        
        self.settings = Settings()
        self.board = Board()

        self.screen = self.screen = pygame.display.set_mode((
            self.settings.screen_width, 
            self.settings.screen_height
        ))
        self.screen_rect = self.screen.get_rect()
        
        self.king = pygame.transform.scale(
            pygame.image.load("images/king.gif"), (
                self.board.cell_size, self.board.cell_size
            )
        )
        self.attacker = pygame.transform.scale(
            pygame.image.load("images/attacker.gif"), (
                self.board.cell_size, self.board.cell_size
            )
        )
        self.defender = pygame.transform.scale(
            pygame.image.load("images/defender.gif"), (
                self.board.cell_size, self.board.cell_size
            )
        )

        self.king_rect = self.king.get_rect()
        self.attacker_rect = self.attacker.get_rect()
        self.defender_rect = self.defender.get_rect()

        self.king_rect.center = self.screen_rect.center
        self.attacker_rect.top = self.screen_rect.top
        self.defender_rect.centerx = self.screen_rect.centerx

    def blitme(self):

        self.screen.blit(self.king, self.king_rect)
        self.screen.blit(self.attacker, self.attacker_rect)
        self.screen.blit(self.defender, self.defender_rect)

    