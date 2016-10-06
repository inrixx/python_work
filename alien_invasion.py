import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship

import game_functions as gf

def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_w,ai_settings.screen_h))
	pygame.display.set_caption("alien invasion")
	ship = Ship(ai_settings,screen)
	bullets = Group()
	aliens = Group()
	gf.creat_fleet(ai_settings,screen,aliens,ship)

	while True:
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings,screen,ship,bullets,aliens)


run_game()


