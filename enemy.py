import pygame
from constants import *
from settings import enemy_image

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        surface = pygame.image.load(enemy_image).convert_alpha()
        scale_coefficient = ENEMY_SHIP_WIDTH / surface.get_rect().width
        self.image = pygame.transform.rotozoom(surface, 0, scale_coefficient)
        self.rect = self.image.get_rect()
        self.rect.midtop = (WIDTH / 2, 20)