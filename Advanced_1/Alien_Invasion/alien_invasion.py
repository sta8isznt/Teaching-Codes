import pygame as pg
import sys
import time
import random

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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

        # Aliens
        self.aliens = pg.sprite.Group()

        self._create_fleet()

    def run(self):
        """Runs the Game"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self.update_fleet()
            self._update_screen()
            self.clock.tick(60)

    def update_fleet(self):
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions
        if pg.sprite.spritecollideany(self.ship, self.aliens):
            print("Ship hit!")

    def _check_fleet_edges(self):
        """Respond appropriately if any alien have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change its moving direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_bullets(self):
        # Get rid of bullets that are out of the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= self.screen_rect.top:
                self.bullets.remove(bullet)
        # Code for checking
        #print(len(self.bullets))

        # Check for any bullets that have hit aliens
        # If so get rid of the bullet and the aline
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions = pg.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destroy any existing bullets and create a new fleet
            self.bullets.empty()
            self._create_fleet()
            

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
        self.aliens.draw(self.screen)
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

    def _create_fleet(self):
        """Create the fleet of aliens"""
        # Create an alien and keep adding aliens until there is no space left
        # Spacing between aliens is one alien width and one alien height

        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        current_x = alien_width
        current_y = alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                new_alien = Alien(self)
                new_alien.x = current_x
                new_alien.rect.x = current_x
                new_alien.rect.y = current_y
                self.aliens.add(new_alien)
                current_x += 2 * alien_width
            # If a row is finished reset x value and increment y value
            current_x = alien_width
            current_y += 2 * alien_height


my_game = Alien_Invasion()
my_game.run()
