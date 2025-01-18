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

        # Paddles
        self.player_1 = pg.Rect(0,0,20,100)
        self.player_2 = pg.Rect(0, 0, 20, 100)
        self.player_1.midleft = self.screen_rect.midleft
        self.player_2.midright = self.screen_rect.midright
        self.player_1_speed = 0
        self.player_2_speed = 0

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
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        if event.key == pg.K_UP:
            self.player_2_speed = -6
        if event.key == pg.K_DOWN:
            self.player_2_speed = 6
        if event.key == pg.K_w:
           self.player_1_speed = -6
        if event.key == pg.K_s:
            self.player_1_speed = 6

    def _check_keyup_events(self, event):
        if event.key == pg.K_UP or event.key == pg.K_DOWN:
            self.player_2_speed = 0
        if event.key == pg.K_w or event.key == pg.K_s:
            self.player_1_speed = 0

    def _update_screen(self):
        self.screen.fill('black')
        pg.draw.line(self.screen, 'white', self.screen_rect.midtop, self.screen_rect.midbottom)
        pg.draw.ellipse(self.screen, (255,255,255), self.ball)
        self._update_ball_position()
        pg.draw.rect(self.screen, 'white', self.player_1)
        pg.draw.rect(self.screen, 'white', self.player_2)
        self._update_player_1_position()
        self._update_player_2_position()
        pg.display.update()

    def _update_ball_position(self):
        self.ball.x = self.ball.x + (self.ball_speed_x * self.ball_x_direction)
        self.ball.y = self.ball.y + (self.ball_speed_y * self.ball_y_direction)

        if self.ball.bottom >= self.screen_rect.bottom or self.ball.top <= self.screen_rect.top:
            self.ball_y_direction *= -1
        if self.ball.right >= self.screen_rect.right or self.ball.left <= 0:
            self.ball_x_direction *= -1

    def _update_player_1_position(self):
        self.player_1.y = self.player_1.y + self.player_1_speed
        if self.player_1.top < 0:
            self.player_1.top = 0
        elif self.player_1.bottom > self.screen_rect.bottom:
            self.player_1.bottom = self.screen_rect.bottom

    def _update_player_2_position(self):
        self.player_2.y = self.player_2.y + self.player_2_speed
        if self.player_2.top < 0:
            self.player_2.top = 0
        elif self.player_2.bottom > self.screen_rect.bottom:
            self.player_2.bottom = self.screen_rect.bottom





pong_game = Game()
pong_game.run()