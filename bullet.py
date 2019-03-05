import pygame
from constants import *
from settings import bullet_image
from spritesheet import Spritesheet

class Bullet(pygame.sprite.Sprite):     
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ss = Spritesheet(bullet_image)
        surface = ss.image_at((275, 69, 20, 10), -1)
        self.image = pygame.transform.rotozoom(surface, 90, 1)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (WIDTH / 2, HEIGHT / 2)


