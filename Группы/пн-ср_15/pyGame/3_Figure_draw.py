import pygame as pg

# Цвета
# RGB (red, green, blue) - от 0 до 255
# HSL (hue, saturation, lightness) (0-360, 0-100, 0-100)
# HEX (#00ff00) #3e0cab

colors = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'purple': (255, 0, 255),
    'grey': (128, 128, 128),
    'pink': (245, 140, 236),
}

pg.init()

screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()

gameStarted = True
while gameStarted:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameStarted = False

    screen.fill(colors['black'])

    # === Отрисовка геометрии ===

    # --- Прямоугольник ---
    # цельная фигура - .rect(surface, color, (x, y, with, height))
    pg.draw.rect(screen, colors['pink'], (50, 50, 100, 150))

    # контур фигуры - .rect(surface, color, (x, y, with, height), line_width)
    pg.draw.rect(screen, colors['red'], (50, 50, 100, 150), 5)

    # --- Круг ---
    # цельный круг - .circle(surface, color, (center_x, center_y), radius)
    pg.draw.circle(screen, colors['green'], (500, 150), 50)

    # контур круга - .circle(surface, color, (center_x, center_y), radius, line_width)
    pg.draw.circle(screen, colors['green'], (500, 300), 50, 4)

    # --- Линии ---
    # одиночная линия - .line(surface, color, (start_x, start_y), (end_x, end_y), width)
    pg.draw.line(screen, colors['yellow'], (30, 100), (500, 550), 2)

    # набор линий
    points = [
        (100, 100),
        (150, 120),
        (200, 60),
        (500, 10),
        (300, 300),
        (60, 250)
    ]
    # контур из линий - .lines(surface, color, closed, point_list, width)
    pg.draw.lines(screen, colors['blue'], False, points, 8)


    # Многоугольники

    # Пример: Радуга

    pg.display.flip()
    clock.tick(60)

pg.quit()