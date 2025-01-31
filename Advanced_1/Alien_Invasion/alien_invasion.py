import pygame as pg
import sys
import time
import random


class Alien_Invasion:
    def __init__(self):
        pg.init()
        self.backround_image = pg.image.load("images/space_image.jpg")
        self.spaceship_window = pg.image.load("images/mamalakis.jpg")

        # screen settings
        self.screen = pg.display.set_mode((1200, 800)) 
        self.screen_rect = self.screen.get_rect()
        pg.display.set_caption("speis inveiderz")
        pg.display.set_icon(self.spaceship_window)

        #Clock Settings
        self.clock = pg.time.Clock()

        #player settings



    def run(self):
        """Runs the Game"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
            

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

        
        pg.display.update()










my_game = Alien_Invasion()
my_game.run()
