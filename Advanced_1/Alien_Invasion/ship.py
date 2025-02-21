import pygame as pg
from settings import Settings

class Ship:
    """A class to manage our ship"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pg.image.load("images/ship.bmp")
        self.image.set_colorkey((230, 230, 230))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        # Moving Flag
        self.moving_right = False
        self.moving_left = False

        # Settings
        self.settings = Settings()

    def update(self):
        """Update the ship's position base on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)