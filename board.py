import pygame

class Board:

    def __init__(self, av_game):

        self.screen = av_game.screen
        self.screen_rect = av_game.screen.get_rect()
        
        # draw board
        cellSize = 20
        self.singleCell = (cellSize, cellSize, cellSize, cellSize)
        self.board = pygame.Surface((cellSize * 11, cellSize * 11))
        self.rect = self.board.get_rect()
        cell = pygame.draw.rect(self.board, (255, 255, 255), (self.singleCell), width=1)


    def blitme(self):

        self.screen.blit(self.board, self.rect)