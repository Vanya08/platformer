import pygame
from constants import *
from settings import player_image

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        surface = pygame.image.load(player_image).convert_alpha()
        scale_coefficient = PLAYER_SHIP_WIDTH / surface.get_rect().width
        self.image = pygame.transform.rotozoom(surface, 0, scale_coefficient)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (WIDTH / 2, HEIGHT - 20)
        self.speedx = 0
        self.accx = 5 
        self.speedy = 0
        self.accy = 5
        self.myfont = pygame.font.SysFont('Arial', 30)

    def update(self):
        self.speedx = 0
        self.speedy = 0
        key_state = pygame.key.get_pressed()
        if (key_state[pygame.K_LEFT]):
            self.speedx -= self.accx
        if (key_state[pygame.K_RIGHT]):
            self.speedx += self.accx
        if (key_state[pygame.K_UP]):
            self.speedy -= self.accy
        if(key_state[pygame.K_DOWN]):
            self.speedy += self.accy

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if  (self.rect.x < 0):
            self.rect.x = 0
        if (self.rect.right > WIDTH):
            self.rect.right = WIDTH

        if (self.rect.y < 0):
            self.rect.y = 0
        if (self.rect.bottom > HEIGHT):
            self.rect.bottom = HEIGHT    
    
    # def draw(self, screen):
        # coord = "({0}, {1})".format(self.rect.x, self.rect.y)
        # textsurface = self.myfont.render(coord, False, (224, 24, 24))
        # screen.blit(textsurface, (0,0))
