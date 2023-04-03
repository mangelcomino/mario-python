import pygame,sys
from settings import *
from tile import Tile
from level import Level

#pygame setup
pygame.init()

screen = pygame.display.set_mode((screen_with,screen_height))
clock = pygame.time.Clock()
fps = 60
level=Level(level_map,screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('black')
    level.run()
    
    pygame.display.update()
    clock.tick(fps)