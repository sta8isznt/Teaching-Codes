import pygame as pg
import sys # Για να μπορούμε να κλείσουμε το παράθυρο

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((1200, 650))
        self.screen_rect = self.screen.get_rect()
        self.image = pg.image.load("super_mario.bmp")
        self.image_rect = self.image.get_rect() # Function for getting the rect of an image
        #Placing the image in the center of the screen
        self.image_rect.centerx = self.screen_rect.centerx

    def run(self):
        while True:
            self.update_screen()
            self.check_events()

    def check_events(self):
        """A function to check the events in the game"""
        # Docstring
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def update_screen(self):
        self.screen.fill("blue") # fills the screen with blue color

        # Puts the image in the screen
        self.screen.blit(self.image, self.image_rect)
        
        pg.display.update() # updates the screen

game = Game() # making an object of the class Game
game.run() # Καλούμε τις συναρτήσεις της κλάσεις μόνο μέσα από αντικείμενα

