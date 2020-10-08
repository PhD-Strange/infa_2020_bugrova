import pygame
from pygame.draw import *

FPS = 30
screen = pygame.display.set_mode((400, 500))


def Cat(n, x, y, eye_color, color, flipbool):
    kitty = pygame.Surface((500, 600), pygame.SRCALPHA)
 #tail
    chvost = pygame.Surface((600, 600), pygame.SRCALPHA)
    ellipse(chvost, color, (100, 100, 100, 30))
    ellipse(chvost, (0, 0, 0), (100, 100, 100, 30), 1)
    chvost = pygame.transform.rotate(chvost, 330)
    kitty.blit(chvost, (-10, 125))
 #body
    ellipse(kitty, color, (100, 225, 250, 125))
    ellipse(kitty, (0, 0, 0), (100, 225, 250, 125), 1)
 #back leg
    circle(kitty, color, (300, 325), 40)
    circle(kitty, (0, 0, 0),  (300, 325), 40, 1)
    ellipse(kitty, color, (300, 325, 35, 70))
    ellipse(kitty, (0, 0, 0), (300, 325, 35, 70), 1)
 #front legs
    ellipse(kitty, color, (100, 325, 80, 40))
    ellipse(kitty, (0, 0, 0), (100, 325, 80, 40), 1)
    ellipse(kitty, color, (70, 255, 40, 80))
    ellipse(kitty, (0, 0, 0), (70, 255, 40, 80), 1)
 #head
    circle(kitty, color, (100, 275), 50)
    circle(kitty, (0, 0, 0), (100, 275), 50, 1)
 #eyes
    circle(kitty, eye_color, (120, 275), 16)
    circle(kitty, (0, 0, 0), (120, 275), 16, 1)
    circle(kitty, eye_color, (80, 275), 16)
    circle(kitty, (0, 0, 0), (80, 275), 16, 1)
    ellipse(kitty, (0, 0, 0), (123, 263, 4, 26))
    ellipse(kitty, (0, 0, 0), (83, 263, 4, 26))
    shine1 = pygame.Surface((600, 600), pygame.SRCALPHA)
    ellipse(shine1, (255, 255, 255), (100, 100, 12, 5))
    shine1 = pygame.transform.rotate(shine1, 330)
    kitty.blit(shine1, (-265, 130))
    shine2 = pygame.Surface((600, 600), pygame.SRCALPHA)
    ellipse(shine2, (255, 255, 255), (100, 100, 12, 5))
    shine2= pygame.transform.rotate(shine2, 330)
    kitty.blit(shine2, (-225, 130))
 #mouth
    polygon(kitty, (255, 100, 100), [(95, 287), (105, 287), (100, 292)])
    polygon(kitty, (0, 0, 0), [(95, 287), (105, 287), (100, 292)], 1)
    line(kitty, (0, 0, 0), [100, 292], [100, 302], 1)
    arc(kitty, (0, 0, 0), (100, 297, 15, 10), 3.14, 6.28, 1)
    arc(kitty, (0, 0, 0), (86, 297, 15, 10), 3.14, 6.28, 1)
 #ears
    polygon(kitty, color, [(65, 245), (90, 230), (72, 215)])
    polygon(kitty, (0, 0, 0), [(65, 245), (90, 230), (72, 215)], 1)
    polygon(kitty, (255, 100, 100), [(70, 237), (83, 228), (74, 225)])
    polygon(kitty, (0, 0, 0), [(70, 237), (83, 228), (74, 225)], 1)                               
    polygon(kitty, color, [(135, 245), (110, 230), (128, 215)])
    polygon(kitty, (0, 0, 0), [(135, 245), (110, 230), (128, 215)], 1)
    polygon(kitty, (255, 100, 100), [(130,237), (117,228), (126,225)])
    polygon(kitty, (0, 0, 0), [(130,237), (117,228), (126,225)],1)                              
 #whiskeys
    w1 = pygame.Surface((600, 600), pygame.SRCALPHA)
    arc(w1, (0, 0, 0), (100, 100, 200, 50), 0, 1)
    w1= pygame.transform.rotate(w1, 20)
    kitty.blit(w1, (-245, 80))
    w1= pygame.transform.flip(w1, True, False)
    kitty.blit(w1, (-322, 80))
    w2 = pygame.Surface((600, 600), pygame.SRCALPHA)
    arc(w2, (0, 0, 0), (100, 100, 200, 50), 0, 1)
    w2= pygame.transform.rotate(w2, 30)
    kitty.blit(w2, (-243, 43))
    w2= pygame.transform.flip(w2, True, False)
    kitty.blit(w2, (-375, 45))
    w3 = pygame.Surface((600, 600), pygame.SRCALPHA)
    arc(w3, (0, 0, 0), (100, 100, 200, 50), 0, 1)
    w3= pygame.transform.rotate(w3, 40)
    kitty.blit(w3, (-230, 15))
    w3= pygame.transform.flip(w3, True, False)
    kitty.blit(w3, (-415, 15))
 #blit
    if flipbool:
        kitty= pygame.transform.flip(kitty, True, False)
    kitty= pygame.transform.scale(kitty, (int(500*n), int(600*n)))
    screen.blit(kitty, (x, y))
    
    
def Ball(n, x, y, color, flipbool):
 #draw
    balls = pygame.Surface((500, 600), pygame.SRCALPHA)
    circle(balls, color, (300, 425), 40)
    circle(balls, (0, 0, 0), (300, 425), 40, 1)
    arc(balls, (0, 0, 0), (283, 422, 20, 60), 1.6, 3.2, 1)
    arc(balls, (0, 0, 0), (273, 414, 35, 65), 1.6, 3.2, 1)
    arc(balls, (0, 0, 0), (293, 430, 15, 55), 1.6, 3.2, 1)
    arc(balls, (0, 0, 0), (270, 410, 40, 60), 0, 1.5, 1)
    arc(balls, (0, 0, 0), (280, 400, 50, 60), 0, 1.5, 1)
    arc(balls, (0, 0, 0), (280, 400, 30, 20), 0.3, 1.57, 1)
    arc(balls, (0, 0, 0), (310, 378, 50, 60), 3.2, 3.9, 1)
    arc(balls, (0, 0, 0), (310, 428, 10, 30), 0.3, 1.57, 1)
    arc(balls, color, (260, 445, 40, 20), 3.14, 6.29, 1)
    arc(balls, color, (230, 450, 30, 10), 0, 3.15, 1)
    arc(balls, color, (210, 449, 20, 10), 3.14, 6.29, 1)
    arc(balls, color, (190, 449, 20, 10), 0, 3.15, 1)
 #blit
    if flipbool:
        balls= pygame.transform.flip(balls, True, False)
    balls= pygame.transform.scale(balls, (int(500*n), int(600*n)))
    screen.blit(balls, (x, y))

def Window(n, x, y, color1, color2):
    windows = pygame.Surface((500, 600), pygame.SRCALPHA)
    rect(windows, color1, (200, 50, 100, 160))
    rect(windows, color2, (205, 55, 40, 30))
    rect(windows, color2, (255, 55, 40, 30))
    rect(windows, color2, (205, 95, 40, 110))
    rect(windows, color2, (255, 95, 40, 110))
    windows= pygame.transform.scale(windows, (int(500*n), int(600*n)))
    screen.blit(windows, (x, y))



#background
rect(screen, (210,179,130), (0, 0, 400, 500))
rect(screen, (150, 130, 100), (0, 250, 400, 300))
#windows
Window (1, 0, 0, (255, 255, 255), (100, 170, 200))
#cats
Cat(1,0 ,0 , (0, 120, 0), (220, 130, 30), False)
#balls
Ball(1, -100, 0, (130, 130, 220), False)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()