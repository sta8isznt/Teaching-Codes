class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 650

        # Ship settings
        self.ship_speed = 4

        # Bullet settings
        self.bullet_speed = 6.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 4

        # Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet direction represents right; -1 represents left
        self.fleet_direction = 1

        # Statistics
        self.ship_limit = 3