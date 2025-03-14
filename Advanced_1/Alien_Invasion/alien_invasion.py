import pygame as pg
import sys
import time
import random

from settings import Settings
from ship import Ship
from bullet import Bullet

class Alien_Invasion:
    def __init__(self):
        self.screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
        # settings
        self.settings = Settings()

        pg.init()
        self.backround_image = pg.image.load("images/space_image.jpg")
        self.backround_image = pg.transform.scale(self.backround_image, (self.screen.get_width(),self.screen.get_height()))

        # screen settings
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.screen_rect = self.screen.get_rect()
        pg.display.set_caption("speis inveiderz")

        #Clock Settings
        self.clock = pg.time.Clock()

        # Ship
        self.ship = Ship(self)

        # Bullets
        self.bullets = pg.sprite.Group()

    def run(self):
        """Runs the Game"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _update_bullets(self):
        # Get rid of bullets that are out of the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= self.screen_rect.top:
                self.bullets.remove(bullet)
        # Code for checking
        #print(len(self.bullets))
            

    def _check_events(self):
        """Chech for new events"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        """Updates the screen"""
        self.screen.blit(self.backround_image, (0, 0))
        for bullet in self.bullets.sprites():
            bullet.draw()
        self.ship.blitme()
        pg.display.update()

    def _check_keydown_events(self, event):
        if event.key == pg.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pg.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pg.K_ESCAPE:
            pg.quit()
            sys.exit()
        elif event.key == pg.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        """Create a new bullet and add it to the Group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            bullet = Bullet(self)
            self.bullets.add(bullet)

    def _check_keyup_events(self, event):
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = False










my_game = Alien_Invasion()
my_game.run()
