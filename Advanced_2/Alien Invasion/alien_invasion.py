import pygame as pg
import sys

class Alien_Invasion:
    def __init__(self):
        pg.init()

        #screen settings
        self.screen = pg.display.set_mode((1200, 800))
        self.screen_rect = self.screen.get_rect()
        pg.display.set_caption("Alien Invasion")

        #Background Image
        self.bg_image = pg.image.load("Images/space_image.jpg")

        # Window Image
        self.window_image = pg.image.load("Images/spaceship_window.png")
        pg.display.set_icon(self.window_image)

        #clock settings
        self.clock = pg.time.Clock()

    def run(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def _update_screen(self):
        self.screen.blit(self.bg_image, (0,0))
        pg.display.update()

game = Alien_Invasion()
game.run()