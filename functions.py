import sys
import pygame


def check_keydown_events(event, ship):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        ship.rect.centerx += 1

    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT:
        ship.moving_right = True 

def check_keyup_events(event, ship):
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT:
        ship.moving_right = False

def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()

def check_events(ship):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == pygame.KEYDOWN:
        check_keydown_events(event, ship) 
    elif event.type == pygame.KEYUP:
        check_keyup_events(event, ship)






