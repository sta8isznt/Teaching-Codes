import pygame as pg

class Ship:
    """A class to manage our ship"""

    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pg.image.load("images/ship.bmp")
        self.image.set_colorkey((230, 230, 230))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)