import pygame
from constants import *
from settings import player_image

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        surface = pygame.image.load(player_image).convert()
        self.image = pygame.transform.scale(surface, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
 #x1=240 y1=294 x2=659 y2=462 

    def update(self):
        pass


    def draw(self):
        self.image.draw()
        pass
        
