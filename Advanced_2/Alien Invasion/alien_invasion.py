import pygame as pg
import sys

from settings import Settings
from ship import Ship
from bullet import Bullet

class Alien_Invasion:
    def __init__(self):
        pg.init()

        # General Settings
        self.settings = Settings()

        #screen settings
        self.screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.screen_rect = self.screen.get_rect()
        pg.display.set_caption("Alien Invasion")

        #Background Image
        self.bg_image = pg.image.load("Images/space_image.jpg")
        self.bg_image = pg.transform.scale(self.bg_image, (self.settings.screen_width, self.settings.screen_height))

        # Window Image
        self.window_image = pg.image.load("Images/spaceship_window.png")
        pg.display.set_icon(self.window_image)

        #clock settings
        self.clock = pg.time.Clock()

        # Ship settings
        self.ship = Ship(self)

        # Bullets
        self.bullets = pg.sprite.Group()

    def run(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _update_bullets(self):
        #  Get rid of the bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= self.screen_rect.top:
                self.bullets.remove(bullet)

    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pg.K_ESCAPE:
            pg.quit()
            sys.exit()
        elif event.key == pg.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) <= self.settings.bullets_allowed:
            bullet = Bullet(self)
            self.bullets.add(bullet)

    def _check_keyup_events(self, event):
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        self.screen.blit(self.bg_image, (0,0))
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        pg.display.update()

game = Alien_Invasion()
game.run()