import pygame as pg
import sys
import random

class Game:
    def __init__(self):
        pg.init()

        #Screen Settings
        self.screen = pg.display.set_mode((1280, 700))
        self.screen_rect = self.screen.get_rect()
        pg.display.set_caption("Pong Game")
        self.bg_image = pg.image.load("bg_image1.bmp")
        self.bg_image = pg.transform.scale(self.bg_image, (self.screen_rect.width, self.screen_rect.height))

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

        #Colors
        self.colors = ["white", "red", "blue", "green", "pink", "purple"]
        self.ball_color = self.colors[0]

        # Scores
        self.player_1_score = 0
        self.player_2_score = 0
        self.score_font = pg.font.Font(None, 80)

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
        self.screen.blit(self.bg_image, (0, 0))
        # pg.draw.line(self.screen, 'white', self.screen_rect.midtop, self.screen_rect.midbottom)
        pg.draw.ellipse(self.screen, self.ball_color, self.ball)
        self._update_ball_position()
        pg.draw.rect(self.screen, 'black', self.player_1)
        pg.draw.rect(self.screen, 'black', self.player_2)
        self._update_player_1_position()
        self._update_player_2_position()
        self.update_score()
        pg.display.update()

    def update_score(self):
        player_1_bg_color = self.bg_image.get_at((int(self.screen_rect.width / 4), 20))
        player_2_bg_color = self.bg_image.get_at((int(3 * self.screen_rect.width / 4), 20))

        player_1_image = self.score_font.render(str(self.player_1_score), True, 'black', player_1_bg_color)
        player_2_image = self.score_font.render(str(self.player_2_score), True, 'black', player_2_bg_color)

        self.screen.blit(player_1_image, (self.screen_rect.width /4, 20))
        self.screen.blit(player_2_image, (self.screen_rect.width /4 * 3, 20))

    def _update_ball_position(self):
        self.ball.x = self.ball.x + (self.ball_speed_x * self.ball_x_direction)
        self.ball.y = self.ball.y + (self.ball_speed_y * self.ball_y_direction)

        if self.ball.bottom >= self.screen_rect.bottom or self.ball.top <= self.screen_rect.top:
            self.ball_y_direction *= -1
        if self.ball.colliderect(self.player_2) or self.ball.colliderect(self.player_1):
            self.ball_x_direction *= -1
            self.ball_color = random.choice(self.colors)
            self.ball_speed_x += 0.5
            self.ball_speed_y += 0.5

        if self.ball.right >= self.screen_rect.width - 10:
            self.point_won("player_1")
        elif self.ball.left <= 10:
            self.point_won("player_2")

    def point_won(self, winner):
        if winner == "player_1":
            self.player_1_score += 1
        elif winner == "player_2":
            self.player_2_score += 1

        self.reset_ball()

    def reset_ball(self):
        self.ball.x = self.screen_rect.centerx
        self.ball_speed_x = self.ball_speed_y = 6
        self.ball.y = random.randint(10, 100)
        self.ball_x_direction = random.choice([-1, 1])
        self.ball_y_direction = random.choice([-1, 1])


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