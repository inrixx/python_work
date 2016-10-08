class Settings():
    def __init__(self):
        self.screen_w = 800
        self.screen_h = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_f = 1.5

        self.bullet_speed_f = 3
        self.bullet_w = 3
        self.bullet_h = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 4

        self.alien_speed_f = 1

        self.fleet_drop_speed = 10
        self.fleet_direction = 1
