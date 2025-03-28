import pygame as pg
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute
        self.image = pg.image.load("Images/alien.bmp")
        self.rect = self.image.get_rect()

        # Start each alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the aliens x position as float to get the exact value
        self.x = float(self.rect.x)