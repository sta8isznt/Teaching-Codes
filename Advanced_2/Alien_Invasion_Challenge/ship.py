import pygame
from settings import Settings

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

        # Ship Movement
        self.moving_right = False
        self.moving_left = False

        # Settings
        self.settings = Settings()

        self.x = float(self.rect.x)
    
    def blitme(self):
        """Draw the ship in the screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ships position"""
        # Flag -> A bool variable
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = self.rect.x
