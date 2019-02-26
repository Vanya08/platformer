import pygame
from constants import *
from player import Player
from enemy import Enemy

pygame.init()
pygame.font.init() # Инициализация pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Создаем окно для отрисовки
pygame.display.set_caption(TITLE) # Устанавливает заголовок окна
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
enemy = Enemy()
all_sprites.add(player)
all_sprites.add(enemy)

myfont = pygame.font.SysFont('Arial', 30)

running = True
# Игровой цикл
while running:
    clock.tick(FPS)
    # events()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: 
            ''' 
                Если (if) тип(type) события (event)
                равен (==)
                нажатию клавиши на клавиатуре (pygame.KEYDOWN)
            '''
            if event.key == pygame.K_ESCAPE:
                running = False


    # update()
    all_sprites.update()

    # draw()
    screen.fill(BACKGROUND_COLOR) # Заполняем экран цветом
    all_sprites.draw(screen)
    coord = "({0}, {1})".format(player.rect.midtop[0], player.rect.midtop[1])
    textsurface = myfont.render(coord, False, (224, 24, 24))
    screen.blit(textsurface, (0,0))
    print(coord)

    pygame.display.flip() # Отображаем нарисованое в Double buffer

pygame.quit()