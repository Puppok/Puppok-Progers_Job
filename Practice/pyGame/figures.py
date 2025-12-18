import pygame as pg

def draw_traffic_light(surface):
    colors = {
        'red': (255, 0, 0),
        'yellow': (255, 255, 0),
        'green': (0, 255, 0),
        'grey': (128, 128, 128),
        'black': (0, 0, 0),
    }

    # box
    pg.draw.rect(surface, colors['grey'], (100, 60, 200, 450))
    pg.draw.rect(surface, colors['black'], (100, 60, 200, 450), 5)

    # lights
    pg.draw.circle(surface, colors['red'], (200, 150), 60)
    pg.draw.circle(surface, colors['black'], (200, 150), 60, 5)

    pg.draw.circle(surface, colors['yellow'], (200, 290), 60)
    pg.draw.circle(surface, colors['black'], (200, 290), 60, 5)

    pg.draw.circle(surface, colors['green'], (200, 430), 60)
    pg.draw.circle(surface, colors['black'], (200, 430), 60, 5)

    # leg
    pg.draw.rect(surface, colors['grey'], (150, 505, 100, 250))
    pg.draw.rect(surface, colors['black'], (150, 505, 100, 250), 5)

def draw_home(surface):
    colors = {
        'black': (0, 0, 0),
        'bisque': (240, 230, 175),
        'brown': (120, 85, 50),
        'light_blue': (70, 200, 240)
    }

    # box
    pg.draw.rect(surface, colors['bisque'], (400, 400, 400, 355))
    pg.draw.rect(surface, colors['black'], (400, 400, 400, 355), 4)

    # roof
    pg.draw.polygon(surface, colors['bisque'], [(600, 200), (400, 400), (800, 400)])
    pg.draw.polygon(surface, colors['black'], [(600, 200), (400, 400), (800, 400)], 4)

    # door
    pg.draw.rect(surface, colors['brown'], (500, 600, 100, 155))
    pg.draw.rect(surface, colors['black'], (500, 600, 100, 155), 4)

    # window_1
    pg.draw.rect(surface, colors['light_blue'], (650, 550, 110, 110))
    pg.draw.rect(surface, colors['black'], (650, 550, 110, 110), 4)
    pg.draw.line(surface, colors['black'], (705, 550), (705, 659), 4)
    pg.draw.line(surface, colors['black'], (650, 605), (759, 605), 4)

    # window_2
    pg.draw.rect(surface, colors['light_blue'], (450, 450, 110, 110))
    pg.draw.rect(surface, colors['black'], (450, 450, 110, 110), 4)
    pg.draw.line(surface, colors['black'], (505, 450), (505, 559), 4)
    pg.draw.line(surface, colors['black'], (450, 505), (559, 505), 4)

def draw_chessboard(surface):
    colors = {
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        'grey': (128, 128, 128)
    }
    face_size = 68.75

    pg.draw.rect(surface, colors['grey'], (890, 190, 570, 570), 10)

    for y in range(8):
        for x in range(8):
            if (x + y) % 2 == 0:
                pg.draw.rect(surface, colors['white'], (900 + (x * face_size), 200 + (y * face_size), face_size, face_size))
            else:
                pg.draw.rect(surface, colors['black'], (900 + (x * face_size), 200 + (y * face_size), face_size, face_size))

pg.init()
screen = pg.display.set_mode((1500, 800))
clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((65, 178, 209))

    draw_traffic_light(screen)
    draw_home(screen)
    draw_chessboard(screen)

    pg.display.flip()
    clock.tick(60)

pg.quit()

# Задача 1: Нарисуй светофор (три круга: красный, жёлтый, зелёный, черная обводка и серый корпус)
# Задача 2: Нарисуй домик (квадрат + треугольник крыша + прямоугольник дверь + квадраты окна)
# Задача 3: Создай шахматную доску 8x8 (чередование чёрных и белых квадратов)
# Задача 4: Нарисуй смайлик (жёлтый круг, два глаза, улыбка)
# Задача 5: Создай функцию draw_star(x, y, size, color), которая рисует звезду
# Бонус задача: Нарисуй автомобиль, используя только примитивы