class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700

        # Ship Settings
        self.ship_speed = 7

        # Bullet Settings
        self.bullet_speed = 10.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 5

        # Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1