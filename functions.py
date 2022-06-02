import sys
import pygame
def check_events():
 """Respond to keypresses and mouse events."""
def check_events(ship):
      for event in pygame.event.get():
       if event.type == pygame.QUIT:
        sys.exit()
       elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
 # Move the ship to the right.
         ship.rect.centerx += 1
      ship.blitme()


def check_events():
  def update_screen(ai_settings, screen, ship):
   """Update images on the screen and flip to the new screen."""
 """Respond to keypresses and mouse events."""