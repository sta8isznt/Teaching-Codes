import pygame

class Ship:
    def __init__(self, game):
        # Screen Settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Ship image
        self.image = pygame.image.load("Images/ship.bmp")
        self.rect = self.image.get_rect()
        self.image.set_colorkey((230, 230, 230))

        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """Draw the ship in the screen"""
        self.screen.blit(self.image, self.rect)

