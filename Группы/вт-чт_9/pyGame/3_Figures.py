import pygame as pg
# === Отрисовка фигур ===
# Цвета
# 1. RGB (red, green, blue) - от 0 до 255
# 2. HSL / HSV (hue, saturation, lightness/value)
# 3. CMYK (cyan, magenta, yellow, key)
# 4. HEX (#f3c95b)

colors = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'yellow': (255, 255, 0),
    'blue': (0, 0, 255),
    'magenta': (255, 0, 255),
    'cyan': (33, 217, 255)
}

pg.init()
screen = pg.display.set_mode((600, 400))
pg.display.set_caption('Писька бабуина')
clock = pg.time.Clock()

isGameStarted = True
while isGameStarted:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isGameStarted = False

    screen.fill(colors['black'])

    # --- Прямоугольник ---
    # цельный прямоугольник - .rect(surface, color, (start_x, start_y, width, height))
    pg.draw.rect(screen, colors['magenta'], (20, 20, 100, 200))

    # контур - .rect(surface, color, (start_x, start_y, width, height), line_width)
    pg.draw.rect(screen, colors['red'], (20, 20, 100, 200), 6)

    # --- Круг ---
    # цельный - .circle(surface, color, (center_x, center_y), radius)
    pg.draw.circle(screen, colors['cyan'], (250, 100), 50)

    # контур - .circle(surface, color, (center_x, center_y), radius, line_width)
    pg.draw.circle(screen, colors['blue'], (250, 100), 50, 4)

    # --- Линии ---
    # прямая - .line(surface, color, (start_x, start_y), (end_x, end_y), line_width)
    pg.draw.line(screen, colors['green'], (20, 400), (500, 20), 10)

    # контур из линий - .lines(surface, color, closed, point_list, line_width)
    points = [ # массив точек линии
        (10, 10),
        (50, 150),
        (280, 400),
        (450, 120)
    ]
    pg.draw.lines(screen, colors['white'], True, points, 3)

    # --- Многоугольник ---


    pg.display.flip()
    clock.tick(60)

pg.quit()