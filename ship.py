import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_r = False
        self.moving_l = False

    def update(self):
        if self.moving_r and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_f
        if self.moving_l and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_f

        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image,self.rect)