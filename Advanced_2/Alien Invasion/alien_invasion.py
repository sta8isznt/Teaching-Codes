import pygame as pg
import sys
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button

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

        # Aliens
        self.aliens = pg.sprite.Group()

        # Create an instance to store game statistics
        self.stats = GameStats(self)

        # Start Alien Invasion in an inactive state
        self.game_active = False

        # Make the Play button
        self.play_button = Button(self, "Play")

        self._create_fleet()

    def run(self):
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self.bullets.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(60)

    def _update_aliens(self):
        """Update the positions of all the aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()
        
        # Look for alien-ship collisions
        if pg.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

    def _update_bullets(self):
        #  Get rid of the bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= self.screen_rect.top:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien
        collisions = pg.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destroy the existings bullets and create a new fleet
            self.bullets.empty()
            self._create_fleet()



    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos() # Takes the position of the mouse
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player hits the Play button"""
        if self.play_button.rect.collidepoint(mouse_pos):
            # Reset the game stats
            self.stats.reset_stats()
            self.game_active = True

        # Get rid of any remaining bullets and aliens
        self.bullets.empty()
        self.aliens.empty()

        # Create a new fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()

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
        self.aliens.draw(self.screen)

        # Draw the play button if the game is inactive
        if not self.game_active:
            self.play_button.draw_button()
        pg.display.update()

    def _create_fleet(self):
        """Create the fleet of aliens"""
        # Make an Alien
        # Create an alien and keep adding aliens until there is no room left
        # Spacing between aliens is one alien width and one alien height

        new_alien = Alien(self)
        alien_width = new_alien.rect.width
        alien_height = new_alien.rect.height

        current_x = alien_width
        current_y = alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2*alien_width
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Respond appropriatly if any alien has reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
                
    def _change_fleet_direction(self):
        """Drop the entire fleet and change its moving direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Respond to ship being hit by an alien"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(2)
        else:
            self.game_active = False

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.screen_rect.bottom:
                self._ship_hit()
                break


game = Alien_Invasion()
game.run()