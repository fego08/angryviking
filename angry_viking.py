import sys
import pygame
from settings import Settings


class AngryViking:
    """main game class"""

    def __init__(self):
        """initializes game assets and functions"""
        # initialize pygame and settings
        pygame.init()
        self.settings = Settings()
        # display stuff (keep display.flip() at the end of this block)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.bg_color = self.settings.bg_color
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("AngryViking")
        

    def run_game(self):
        """main game loop"""

        while True:
            self.check_events()
            self._update_display()
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys(exit)

    def _update_display(self):
        """helpfunction for updating the screen"""

        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()

    
if __name__ == ("__main__"):

    av = AngryViking()
    av.run_game()