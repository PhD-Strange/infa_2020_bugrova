import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 194, 73), (200, 200), 150)
circle(screen, (0, 0, 0), (200, 200), 250, 2)
circle(screen, (186, 62, 52), (150, 170), 30)
circle(screen, (0, 0, 0), (150, 170), 30, 1)
circle(screen, (0, 0, 0), (150, 170), 20)
circle(screen, (186, 62, 52), (250, 170), 40)
circle(screen, (0, 0, 0), (250, 170), 40, 1)
circle(screen, (0, 0, 0), (250, 170), 20)
polygon(screen, (0, 0, 0), [(300,250), (100,250),
                               (100,240), (300,240)])
polygon(screen, (0, 0, 0), [(300,100), (310,110),
                               (210,160), (205,155)])
polygon(screen, (0, 0, 0), [(100,100), (90,110),
                               (190,160), (195,155)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()