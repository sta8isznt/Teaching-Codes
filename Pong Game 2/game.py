import pygame as pg
import sys

class Game:
    def __init__(self):
        pg.init()

        #Screen Settings
        self.screen = pg.display.set_mode((1280, 700))
        self.screen_rect = self.screen.get_rect()
        pg.display.set_caption("Pong Game")

        #Clock Settings
        self.clock = pg.time.Clock()

        #Ball Settings
        self.ball = pg.Rect(0,0,30,30)
        self.ball.center = self.screen_rect.center
        self.ball_speed_x = 6
        self.ball_speed_y = 6
        self.ball_x_direction = 1
        self.ball_y_direction = 1

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
        self.screen.fill('black')
        pg.draw.line(self.screen, 'white', self.screen_rect.midtop, self.screen_rect.midbottom)
        pg.draw.ellipse(self.screen, (255,255,255), self.ball)
        self._update_ball_position()
        pg.display.update()

    def _update_ball_position(self):
        self.ball.x = self.ball.x + (self.ball_speed_x * self.ball_x_direction)
        self.ball.y = self.ball.y + (self.ball_speed_y * self.ball_y_direction)

pong_game = Game()
pong_game.run()