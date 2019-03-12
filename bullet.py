import pygame
from constants import *
from settings import bullet_image
from spritesheet import Spritesheet

class Bullet(pygame.sprite.Sprite):     
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ss = Spritesheet(bullet_image)
        self.bullets = ss.images_at([\
            (275, 69, 20, 10)\
        ], -1)
        self.idx = 0
        self.image = self.bullets[self.idx]
        self.last_idx = len(self.bullets) - 1
        self.rect = self.image.get_rect()
        self.rect.midbottom = (WIDTH / 2, HEIGHT)
        self.speed = 4
        self.frames_count = 0
        self.animate_each_frame = 10


    def update(self):

        self.frames_count += 1
        if (self.frames_count == self.animate_each_frame):
            self.frames_count = 0
            self.idx = 0 if self.idx == self.last_idx else (self.idx + 1)
            self.image = self.bullets[self.idx]
            (x,y) = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = (x,y)

        self.rect.centery -= self.speed
        print(self.rect.midbottom)
        if (self.rect.midbottom[1] <= 0):
            self.kill()


