import pygame

WIDTH = 640
HEIGHT = 480
FPS = 60
TITLE = "Platformer"
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BACKGROUND_COLOR = (239, 188, 33)



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

running = True
while running:
    #events()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE
            running = False    

    #update()
    pass
    #draw()
    screen.fill(BACKGROUND_COLOR)

    pygame.display.flip()

pygame.quit()


