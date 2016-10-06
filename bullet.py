import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0,0,ai_settings.bullet_w,ai_settings.bullet_h)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_f = ai_settings.bullet_speed_f

    def update(self):
    	self.y -= self.speed_f
    	self.rect.y = self.y

    def draw_bullet(self):
    	pygame.draw.rect(self.screen,self.color,self.rect)

