import pygame as pg

# Цвета
# 1. RGB (red, green, blue) от 0 до 255
# 2. HSL/HSV (hue, saturation, lightness/value) (0-360, 0-100, 0-100)
# 3. CMYK (cyan, magenta, yellow, key(black))
# 4. HEX (#rrggbb)

colors = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'magenta': (255, 0, 255),
    'cyan': (0, 255, 255),
    'gray': (128, 128, 128)
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

    screen.fill(colors['black'])

    # --- Прямоугольник ---
    # цельный - .rect(surface, color, (start_x, start_y, width, height))
    pg.draw.rect(screen, colors['red'], (50, 50, 100, 40))

    # контур - .rect(surface, color, (start_x, start_y, width, height), line_width)
    pg.draw.rect(screen, colors['blue'], (50, 50, 100, 40), 5)

    # --- Круг ---
    # цельный - .circle(surface, color, (center_x, center_y), radius)
    pg.draw.circle(screen, colors['yellow'], (250, 100), 50)

    # контур - .circle(surface, color, (center_x, center_y), radius, line_width)
    pg.draw.circle(screen, colors['blue'], (250, 100), 50, 5)

    # --- Эллипс ---
    # цельный - .ellipse(surface, color, (start_x, start_y, width, height))
    pg.draw.ellipse(screen, colors['magenta'], (250, 100, 500, 200))

    # контур - .ellipse(surface, color, (start_x, start_y, width, height), line_width)
    pg.draw.ellipse(screen, colors['magenta'], (250, 100, 500, 200), 3)

    # Линия
    # прямая - .line(surface, color, (start_x, start_y), (end_x, end_y), line_width)
    pg.draw.line(screen, colors['yellow'], (20, 500), (500, 650), 3)

    # ломаная - .lines(surface, color, closed, point_list, line_width)
    points = [
        (365, 331),
        (182, 587),
        (484, 507),
        (245, 214),
        (700, 568)
    ]
    pg.draw.lines(screen, colors['cyan'], False, points, 3)

    # Полигон (произвольный многоугольник)
    # .polygon(surface, color, point_list, line_width)
    # треугольник
    triangle = [(150, 200), (250, 350), (50, 350)]
    pg.draw.polygon(screen, colors['green'], triangle) # цельный
    pg.draw.polygon(screen, colors['green'], triangle, 4) # контур

    # многоугольник
    polygon = [
        (100, 400), (250, 350), (400, 450),
        (300, 550), (100, 500)
    ]
    pg.draw.polygon(screen, colors['gray'], polygon)


    # Пример, отрисовка радуги
    rainbow = {
        'red': (250, 0, 0),
        'orange': (255, 123, 0),
        'yellow': (255, 255, 0),
        'green': (0, 255, 0),
        'light_blue': (46, 199, 255),
        'blue': (0, 0, 255),
        'purple': (170, 0, 222),
    }

    end_radius = 400
    line_width = 40

    for i, color in enumerate(rainbow.values()):
        raduis = end_radius - (i * line_width)
        pg.draw.circle(screen, color, (400, 600), raduis, line_width)

    pg.display.flip()
    clock.tick(60)

pg.quit()