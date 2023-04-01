import pygame,sys

#pygame setup
pygame.init()
screen_with = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_with,screen_height))
clock = pygame.time.Clock()
fps = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('black')

    pygame.display.update()
    clock.tick(fps)