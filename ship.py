import pygame



#Initialize the ship and set its starting position.
class Ship():
  def __init__(self, screen):
    self.screen = screen
    self.image = pygame.image.load('images/ship.bmp')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()

#start each new ship at the bottom center of the screen
    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom

#Draw the ship at its current location.
  
  def blitme(self):
    self.screen.blit(self.image, self.rect)