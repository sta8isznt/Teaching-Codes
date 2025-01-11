import pygame as pg
import sys

class Game:
    """The Game Class"""
    def __init__(self):
        """Initialize the basic game attributes"""
        pg.init()

        #Screen Settings
        self.screen = pg.display.set_mode((1280, 700)) #pygame Surface
        self.screen_rect = self.screen.get_rect()
        pg.display.set_caption("Pong Game")

        #Clock Settings
        self.clock = pg.time.Clock()

        #Ball Settings
        self.ball = pg.Rect(0,0, 30, 30) #Coordinates, Shape
        self.ball.center = self.screen_rect.center
        self.ball_speed_x = 6
        self.ball_speed_y = 6
        self.ball_x_direction = 1
        self.ball_y_direction = 1

        #Paddles
        self.player_1 = pg.Rect(0,0,20,100)
        self.player_1.midright = self.screen_rect.midright
        self.player_2 = pg.Rect(0,0,20,100)
        self.player_2.midleft = self.screen_rect.midleft
        self.player_1_speed = 0
        self.player_2_speed = 0


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
        self.screen.fill('black')
        pg.draw.line(self.screen, 'white', self.screen_rect.midtop, self.screen_rect.midbottom)
        pg.draw.ellipse(self.screen, 'white', self.ball)
        self._update_ball_position()
        pg.display.update() #pg.display.flip()

    def _check_keydown_events(self, event):
        pass

    def _check_keyup_events(self, event):
        pass

    def _update_ball_position(self):
        self.ball.x += (self.ball_speed_x * self.ball_x_direction)
        self.ball.y += (self.ball_speed_y * self.ball_y_direction)

        if self.ball.bottom >= self.screen_rect.bottom or self.ball.top <= 0:
            self.ball_y_direction *= -1
        if self.ball.left <= self.screen_rect.left or self.ball.right >= self.screen_rect.right:
            self.ball_x_direction *= -1


my_game = Game()
my_game.run()
