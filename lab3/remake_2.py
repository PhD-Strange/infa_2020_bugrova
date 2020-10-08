import pygame
from pygame.draw import *

# Surfaces that were used
FPS = 30
screen = pygame.display.set_mode((400, 500))
chvost = pygame.Surface((600, 600), pygame.SRCALPHA)
shine1 = pygame.Surface((600, 600), pygame.SRCALPHA)
shine2 = pygame.Surface((600, 600), pygame.SRCALPHA)
w1 = pygame.Surface((600, 600), pygame.SRCALPHA)
w2 = pygame.Surface((600, 600), pygame.SRCALPHA)
w3 = pygame.Surface((600, 600), pygame.SRCALPHA)
windows = pygame.Surface((500, 600), pygame.SRCALPHA)
balls = pygame.Surface((500, 600), pygame.SRCALPHA)


def Cat(n, x, y, eye_color0, color0, flipbool):
    """
    Функция возвращает кота с координатами (x, y), используя вспомогательные
    функции, которые описаны ниже.
    Цвет глаз кота задается памаметром eye_color0.
    Цвет самого кота определяется параметром color0.
    Функция позволяет повернуть кота на 180 градусов вокруг своей оси,
    если задать значение True для переменной flipbool. Параметр n задает
    размер относительно исходного размера на исходной картинке.

    """
    kitty = pygame.Surface((500, 600), pygame.SRCALPHA)
    tail(chvost, kitty, color0)
    body(kitty, color0)
    back_leg(kitty, color0)
    front_legs(kitty, color0)
    head(kitty, color0)
    eyes(kitty, shine1, shine2, eye_color0)
    mouth(kitty)
    ears(kitty, color0)
    whiskeys(w1, w2, w3, kitty)
    # Blit:
    if flipbool:
        kitty = pygame.transform.flip(kitty, True, False)
    kitty = pygame.transform.scale(kitty, (int(500*n), int(600*n)))
    screen.blit(kitty, (x, y))


def tail(surface1, surface2, color):
    """
    Рисует хвост кота на surface1.
    Цвет хвоста определяется параметром color.
    Потом функция переносит хвост с surface1 на surface2.

    """
    ellipse(surface1, color, (100, 100, 100, 30))
    ellipse(surface1, (0, 0, 0), (100, 100, 100, 30), 1)
    surface1 = pygame.transform.rotate(surface1, 330)
    surface2.blit(surface1, (-10, 125))


def body(surface, color):
    """
    Функция рисует тело кота на surface.
    Цвет тела задается параметром color.

    """
    ellipse(surface, color, (100, 225, 250, 125))
    ellipse(surface, (0, 0, 0), (100, 225, 250, 125), 1)


def back_leg(surface, color):
    """
    Функция рисует заднюю ногу кота на surface.
    Цвет ноги определяется параметром color.

    """
    circle(surface, color, (300, 325), 40)
    circle(surface, (0, 0, 0),  (300, 325), 40, 1)
    ellipse(surface, color, (300, 325, 35, 70))
    ellipse(surface, (0, 0, 0), (300, 325, 35, 70), 1)


def front_legs(surface, color):
    """
    Функция рисует передние ноги кота на surface.
    Цвет ног задается параметром color.

    """
    ellipse(surface, color, (100, 325, 80, 40))
    ellipse(surface, (0, 0, 0), (100, 325, 80, 40), 1)
    ellipse(surface, color, (70, 255, 40, 80))
    ellipse(surface, (0, 0, 0), (70, 255, 40, 80), 1)


def head(surface, color):
    """
    Функция рисует голову кота на surface.
    Цвет задается памаретром color.

    """
    circle(surface, color, (100, 275), 50)
    circle(surface, (0, 0, 0), (100, 275), 50, 1)


def eyes(surface1, surface2, surface3, eye_color):
    """
    Функция рисует глаза кота на surface1.
    Цвет глаз задается параметром eye_color.

    """
    circle(surface1, eye_color, (120, 275), 16)
    circle(surface1, (0, 0, 0), (120, 275), 16, 1)
    circle(surface1, eye_color, (80, 275), 16)
    circle(surface1, (0, 0, 0), (80, 275), 16, 1)
    ellipse(surface1, (0, 0, 0), (123, 263, 4, 26))
    ellipse(surface1, (0, 0, 0), (83, 263, 4, 26))
    ellipse(surface2, (255, 255, 255), (100, 100, 12, 5))
    surface2 = pygame.transform.rotate(surface2, 330)
    surface1.blit(surface2, (-265, 130))
    ellipse(surface3, (255, 255, 255), (100, 100, 12, 5))
    surface3 = pygame.transform.rotate(surface3, 330)
    surface1.blit(surface3, (-225, 130))


def mouth(surface):
    """Функция рисует рот кота на surface."""
    polygon(surface, (255, 100, 100), [(95, 287), (105, 287), (100, 292)])
    polygon(surface, (0, 0, 0), [(95, 287), (105, 287), (100, 292)], 1)
    line(surface, (0, 0, 0), [100, 292], [100, 302], 1)
    arc(surface, (0, 0, 0), (100, 297, 15, 10), 3.14, 6.28, 1)
    arc(surface, (0, 0, 0), (86, 297, 15, 10), 3.14, 6.28, 1)


def ears(surface, color):
    """
    Функция рисует уши на surface.
    Цвет ушей задается параметром color.

    """
    polygon(surface, color, [(65, 245), (90, 230), (72, 215)])
    polygon(surface, (0, 0, 0), [(65, 245), (90, 230), (72, 215)], 1)
    polygon(surface, (255, 100, 100), [(70, 237), (83, 228), (74, 225)])
    polygon(surface, (0, 0, 0), [(70, 237), (83, 228), (74, 225)], 1)
    polygon(surface, color, [(135, 245), (110, 230), (128, 215)])
    polygon(surface, (0, 0, 0), [(135, 245), (110, 230), (128, 215)], 1)
    polygon(surface, (255, 100, 100), [(130, 237), (117, 228), (126, 225)])
    polygon(surface, (0, 0, 0), [(130, 237), (117, 228), (126, 225)], 1)


def whiskeys(surface1, surface2, surface3, surface4):
    """
    Функция рисует усы кота. Каждый из 3 усов рисуется на своей поверхности,
    потом сжимается и переносится на surface4.

    """
    arc(surface1, (0, 0, 0), (100, 100, 200, 50), 0, 1)
    surface1 = pygame.transform.rotate(surface1, 20)
    surface4.blit(surface1, (-245, 80))
    surface1 = pygame.transform.flip(surface1, True, False)
    surface4.blit(surface1, (-322, 80))
    arc(surface2, (0, 0, 0), (100, 100, 200, 50), 0, 1)
    surface2 = pygame.transform.rotate(surface2, 30)
    surface4.blit(surface2, (-243, 43))
    surface2 = pygame.transform.flip(surface2, True, False)
    surface4.blit(surface2, (-375, 45))
    arc(surface3, (0, 0, 0), (100, 100, 200, 50), 0, 1)
    surface3 = pygame.transform.rotate(surface3, 40)
    surface4.blit(surface3, (-230, 15))
    surface3 = pygame.transform.flip(surface3, True, False)
    surface4.blit(surface3, (-415, 15))


def Ball(surface, n, x, y, color, flipbool):
    """
    Функция возвращает клубок с координатами (x, y), который отрисовывается
    на surface. Цвет клубка задается параметром color. Направление нити
    можно изменить, присваивая параметру flipbool значения True или False.
    Параметр n задает размер относительно исходного размера на исходной
    картинке.

    """
    circle(surface, color, (300, 425), 40)
    circle(surface, (0, 0, 0), (300, 425), 40, 1)
    arc(surface, (0, 0, 0), (283, 422, 20, 60), 1.6, 3.2, 1)
    arc(surface, (0, 0, 0), (273, 414, 35, 65), 1.6, 3.2, 1)
    arc(surface, (0, 0, 0), (293, 430, 15, 55), 1.6, 3.2, 1)
    arc(surface, (0, 0, 0), (270, 410, 40, 60), 0, 1.5, 1)
    arc(surface, (0, 0, 0), (280, 400, 50, 60), 0, 1.5, 1)
    arc(surface, (0, 0, 0), (280, 400, 30, 20), 0.3, 1.57, 1)
    arc(surface, (0, 0, 0), (310, 378, 50, 60), 3.2, 3.9, 1)
    arc(surface, (0, 0, 0), (310, 428, 10, 30), 0.3, 1.57, 1)
    arc(surface, color, (260, 445, 40, 20), 3.14, 6.29, 1)
    arc(surface, color, (230, 450, 30, 10), 0, 3.15, 1)
    arc(surface, color, (210, 449, 20, 10), 3.14, 6.29, 1)
    arc(surface, color, (190, 449, 20, 10), 0, 3.15, 1)
    # Blit0
    if flipbool:
        surface = pygame.transform.flip(surface, True, False)
    surface = pygame.transform.scale(surface, (int(500*n), int(600*n)))
    screen.blit(surface, (x, y))


def Window(surface, n, x, y, color1, color2):
    """
    Функция рисует окно с координатами (x, y). Цвет рамки определяется
    параметром color1. Цвет стекол определяется параметром color2. Параметр
    n задает размер относительно исходного размера на исходной картинке.

    """
    rect(surface, color1, (200, 50, 100, 160))
    rect(surface, color2, (205, 55, 40, 30))
    rect(surface, color2, (255, 55, 40, 30))
    rect(surface, color2, (205, 95, 40, 110))
    rect(surface, color2, (255, 95, 40, 110))
    surface = pygame.transform.scale(surface, (int(500*n), int(600*n)))
    screen.blit(surface, (x, y))


rect(screen, (210, 179, 130), (0, 0, 400, 500))  # Background
rect(screen, (150, 130, 100), (0, 250, 400, 300))  # Background
Window(1, 0, 0, (255, 255, 255), (100, 170, 200))  # Windows
Window(1, -150, 0, (255, 255, 255), (100, 170, 200))
Window(1, -300, 0, (255, 255, 255), (100, 170, 200))
Window(1, 150, 0, (255, 255, 255), (100, 170, 200))
Ball(1, -130, 0, (190, 190, 220), False)  # Balls
Ball(0.4, 0, 100, (190, 190, 220), False)
Ball(0.3, 0, 270, (190, 190, 220), False)
Ball(0.6, 120, 120, (190, 190, 220), True)
Ball(0.4, 230, 190, (190, 190, 220), True)
Ball(0.6, 210, 185, (190, 190, 220), True)
Ball(0.3, 180, 350, (190, 190, 220), False)
Cat(0.2, 300, 320, (0, 120, 0), (220, 130, 30), True)  # Cats
Cat(0.2, 0, 210, (0, 120, 0), (220, 130, 30), True)
Cat(0.2, 220, 380, (0, 120, 0), (220, 130, 30), False)
Cat(0.5, 200, 150, (0, 120, 0), (220, 130, 30), False)
Cat(0.5, -40, 190, (0, 100, 190), (100, 100, 100), True)
Cat(0.2, 0, 390, (0, 100, 190), (100, 100, 100), True)
Cat(0.2, 300, 420, (0, 100, 190), (100, 100, 100), False)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()


"""
Что было изменено в исходном коде?
Функция cat была разбита на несколько подфункций. Были написаны документации
к функциям. Немного теретасовал строчки, но это не очень существенно.
Все используемые поверхности задаются в начале, до объявления функций.
Немного допилил PEP8 в коде.

"""
