import pygame as pg
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        # Create a bullet rect at (0,0) and then set its proper position
        self.rect = pg.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the position of the bullet as a float
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        # Update the exact position of the bullet
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.y

    def draw(self):
        """Draw the bullet to the screen"""
        pg.draw.rect(self.screen, self.color, self.rect)
