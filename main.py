import pygame


SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')

# BG_COLOR = pygame.Color('grey12')
BG_COLOR = (50, 50, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    clock.tick(60)
    pygame.display.flip()

