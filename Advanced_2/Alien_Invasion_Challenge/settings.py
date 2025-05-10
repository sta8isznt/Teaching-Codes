class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 650

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 4

        # Alien Settings
        self.fleet_drop_speed = 10

        # Statistics
        self.ship_limit = 3

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 4
        self.bullet_speed = 6.5
        self.alien_speed = 1.0
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale