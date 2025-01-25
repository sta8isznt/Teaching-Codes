import pygame as pg
import sys

class Game:
    def __init__(self):
        pg.init()

        #Screen Settings
        self.screen = pg.display.set_mode((1280, 700))
        self.screen_rect = self.screen.get_rect()
        pg.display.set_caption("Pong Game")

        #Ball Settings
        self.ball = pg.Rect(0, 0, 30, 30)
        self.ball.center = self.screen_rect.center
        self.ball_speed_x = 6
        self.ball_speed_y = 6
        self.ball_x_direction = 1
        self.ball_y_direction = 1

        #Paddles Settings
        self.player_1 = pg.Rect(0,0, 20, 100)
        self.player_1.midleft = self.screen_rect.midleft
        self.player_1.x += 20
        self.player_2 = pg.Rect(0,0, 20, 100)
        self.player_2.midright = self.screen_rect.midright
        self.player_2.x -= 20
        self.player_1_speed = 0
        self.player_2_speed = 0

        #Clock Settings
        self.clock = pg.time.Clock()

        #Scoring
        self.player_1_score, self.player_2_score = 0, 0
        self.score_font = pg.font.Font(None, 80)
    
    def run(self):
        while True:
            self._update_screen()
            self._check_events()
            self.clock.tick(60)

    def _update_screen(self):
        self.screen.fill('black')
        pg.draw.aaline(self.screen, 'white', self.screen_rect.midtop, self.screen_rect.midbottom)
        pg.draw.ellipse(self.screen, 'red', self.ball)
        pg.draw.rect(self.screen, 'white', self.player_1)
        pg.draw.rect(self.screen, 'white', self.player_2)
        self._update_ball_position()
        self._update_player_1_pos()
        self._update_player_2_pos()
        self._update_score()
        pg.display.update()

    def _update_score(self):
        player_1_score_image = self.score_font.render(str(self.player_1_score), True, 'white', 'black')
        player_2_score_image = self.score_font.render(str(self.player_2_score), True, 'white', 'black')

        self.screen.blit(player_1_score_image, (self.screen_rect.width /4, 20))
        self.screen.blit(player_2_score_image, (self.screen_rect.width /4 *3, 20))

    def _update_player_1_pos(self):
        self.player_1.y += self.player_1_speed

        if self.player_1.top < 0:
            self.player_1.top = 0
        elif self.player_1.y > self.screen_rect.bottom - 100:
            self.player_1.y = self.screen_rect.bottom - 100

    def _update_player_2_pos(self):
        self.player_2.y += self.player_2_speed

        if self.player_2.top < 0:
            self.player_2.top = 0
        elif self.player_2.y > self.screen_rect.bottom - 100:
            self.player_2.y = self.screen_rect.bottom - 100     


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
        if event.key == pg.K_UP:
            self.player_2_speed = 0
        if event.key == pg.K_DOWN:
            self.player_2_speed = 0
        if event.key == pg.K_w:
            self.player_1_speed = 0
        if event.key == pg.K_s:
            self.player_1_speed = 0

    def _update_ball_position(self):
        self.ball.x += (self.ball_speed_x * self.ball_x_direction)
        self.ball.y += (self.ball_speed_y * self.ball_y_direction)

        if self.ball.bottom >= self.screen_rect.bottom or self.ball.top <= 0:
            self.ball_y_direction *= -1
        if self.ball.colliderect(self.player_2) or self.ball.colliderect(self.player_1):
            self.ball_x_direction *= -1

        if self.ball.right >= self.screen_rect.right - 20:
            self.point_won("player_1")
        if self.ball.x <= 20:
            self.point_won("player_2")

    def point_won(self, winner):
        if winner == "player_1":
            self.player_1_score += 1
        elif winner == "player_2":
            self.player_2_score += 1

        self.reset_ball()

    def reset_ball(self):
        self.ball.x = self.screen_rect.centerx
        

if __name__ == "__main__":     
    my_game = Game()
    my_game.run()