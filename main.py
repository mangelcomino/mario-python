import pygame,sys
from settings import *
from tile import Tile

#pygame setup
pygame.init()

screen = pygame.display.set_mode((screen_with,screen_height))
clock = pygame.time.Clock()
fps = 60
test_tile = pygame.sprite.Group(Tile((100,100),200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('black')

    test_tile.draw(screen)
    
    pygame.display.update()
    clock.tick(fps)