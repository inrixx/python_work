import sys
import pygame
from bullet import Bullet
from alien import Alien
from ship import Ship

def check_keydown_events(event,ship,ai_settings,screen,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_r = True
    elif event.key == pygame.K_LEFT:
        ship.moving_l = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_r = False
    elif event.key == pygame.K_LEFT:
        ship.moving_l = False

def check_events(ai_settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship,ai_settings,screen,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def update_screen(ai_settings,screen,ship,bullets,aliens):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    pygame.display.flip()


def update_bullets(bullets,aliens,ai_settings,screen,ship):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(bullets,aliens,ai_settings,screen,ship)

def check_bullet_alien_collisions(bullets,aliens,ai_settings,screen,ship):
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if len(aliens) == 0:
        bullets.empty()
        creat_fleet(ai_settings,screen,aliens,ship)

def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_buttle = Bullet(ai_settings,screen,ship)
        bullets.add(new_buttle)


def creat_fleet(ai_settings,screen,aliens,ship):
    alien = Alien(ai_settings,screen)
    alien_w = alien.rect.width
    number_aliens_x = get_number_aliens_x(ai_settings,alien_w)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            creat_alien(ai_settings,screen,aliens,alien_number,alien_w,row_number)

def get_number_aliens_x(ai_settings,alien_w):
    available_space_x = ai_settings.screen_w - 2 * alien_w
    number_alien_x = int(available_space_x / (2 * alien_w))
    return number_alien_x

def creat_alien(ai_settings,screen,aliens,alien_number,alien_w,row_number):
    alien = Alien(ai_settings,screen)
    alien.x = alien_w + 2 * alien_w * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(ai_settings,ship_h,alien_h):
    available_space_y = (ai_settings.screen_h - (3 * alien_h) - ship_h)
    number_rows = int(available_space_y / (2 * alien_h))
    return number_rows

def update_aliens(ai_settings,aliens):
    check_fleet_edges(ai_settings,aliens)
    aliens.update()



def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
        ai_settings.fleet_direction *= -1










