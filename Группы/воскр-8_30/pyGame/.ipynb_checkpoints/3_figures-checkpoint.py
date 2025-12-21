import pygame as pg

# Цвета
# 1. RGB (red, green, blue), от 0 до 255
# 2. HSL/HSV (hue, saturation, lightness/value), (0-360, 0-100, 0-100)
# 3. CMYK (cyan, magenta, yellow, key), процентное соотношение от 0 до 100
# 4. HEX (#rrggbb) от 0 до F (0-9 - A-F)

colors = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'purple': (255, 0, 255),
    'cyan': (0, 255, 255)
}

pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Писька бобра')
clock = pg.time.Clock()

isActive = True
while isActive:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isActive = False

    # === Отрисовка фигур ===
    # --- Прямоугольник ---
    # цельный - .rect(surface, color, (start_x, start_y, width, height))
    pg.draw.rect(screen, colors['cyan'], (50, 50, 150, 100))

    # контур - .rect(surface, color, (start_x, start_y, width, height), line_width)
    pg.draw.rect(screen, colors['red'], (50, 50, 150, 100), 4)

    # --- Круг ---
    # цельный - .circle(surface, color, (center_x, center_y), radius)
    pg.draw.circle(screen, colors['yellow'], (300, 100), 50)

    # контур - .circle(surface, color, (center_x, center_y), radius, line_width)
    pg.draw.circle(screen, colors['red'], (300, 100), 50, 5)

    # --- Линии ---
    # прямая - .line(surface, color, (start_x, start_y), (end_x, end_y), line_width)
    pg.draw.line(screen, colors['yellow'], (400, 150), (550, 50), 10)

    # ломаная - .lines(surface, color, closed, pont_list, line_width)
    points = [
        (600, 100), (650, 50), (650, 150), (750, 150),
        (700, 100), (750, 50), (800, 100)
    ]
    pg.draw.lines(screen, colors['cyan'], False, points, 4)

    # --- Полигон (произвольный многоугольник) ---
    # цельный - .polygon(surface, color, point_list)
    # контур - .polygon(surface, color, point_list, line_width)

    triangle = [(200, 200), (350, 350), (50, 350)]
    pg.draw.polygon(screen, colors['green'], triangle)
    pg.draw.polygon(screen, colors['green'], triangle, 4)

    polygon = [
        (450, 300), (450, 200), (550, 250), (700, 200),
        (750, 250), (750, 350), (650, 300), (600, 350)
    ]
    pg.draw.polygon(screen, colors['purple'], polygon)

    # Пример: радуга
    rainbow_colors = {
        'red': (250, 0, 0),
        'orange': (255, 123, 0),
        'yellow': (255, 255, 0),
        'green': (0, 255, 0),
        'light_blue': (46, 199, 255),
        'blue': (0, 0, 255),
        'purple': (170, 0, 222),
    }

    end_raduis = 200
    line_width = 20

    for i, color in enumerate(rainbow_colors.values()):
        radius = end_raduis - (i * line_width)
        pg.draw.circle(screen, color, (400, 600), radius, line_width)


    pg.display.flip()
    clock.tick(60)

pg.quit()