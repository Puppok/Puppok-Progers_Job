import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
frame = 0

RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

colors = [
    (255, 0, 0),      # Красный
    (255, 127, 0),    # Оранжевый
    (255, 255, 0),    # Жёлтый
    (0, 255, 0),      # Зелёный
    (3, 194, 252),      # Синий
    (0, 0, 255),     # Индиго
    (148, 0, 211)     # Фиолетовый
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((135, 206, 235))

    if frame < 10:
        # === Отрисовка прямоугольника ===
        # Заполненный прямоугольник
        # pygame.draw.rect(surface, color, (x, y, width, height))
        pygame.draw.rect(screen, RED, (10, 10, 50, 80))
        # Контур прямоугольника (последний параметр - толщина линии)
        pygame.draw.rect(screen, BLUE, (70, 10, 50, 80), 5)

        # === Отрисовка круга ===
        # pygame.draw.circle(surface, color, (center_x, center_y), radius)
        # Заполненный круг
        pygame.draw.circle(screen, RED, (170, 50), 40)
        # Контур круга
        pygame.draw.circle(screen, BLUE, (260, 50), 40, 3)

        # === Отрисовка линий ===
        # pygame.draw.line(surface, color, (start_x, start_y), (end_x, end_y), width)
        # Линия толщиной 1 пиксель
        pygame.draw.line(screen, RED, (0, 0), (800, 600), 1)
        # Толстая линия
        pygame.draw.line(screen, BLUE, (100, 300), (700, 300), 10)
        # Несколько соединённых линий
        points = [(100, 100), (200, 50), (300, 100), (400, 50)]
        pygame.draw.lines(screen, GREEN, False, points, 5)  # False = не замыкать

        # === Многоугольники ===
        # pygame.draw.polygon(surface, color, points_list)
        # Треугольник
        triangle = [(400, 100), (300, 300), (500, 300)]
        pygame.draw.polygon(screen, RED, triangle)
        # Пятиугольник
        pentagon = [(400, 200), (450, 250), (425, 325), (375, 325), (350, 250)]
        pygame.draw.polygon(screen, BLUE, pentagon, 3)  # 3 = толщина контура

        frame += 1

    center_x, center_t = 400, 600
    start_radius = 400
    line_width = 40

    for i, color in enumerate(colors):
        radius = start_radius - (i * line_width)
        pygame.draw.circle(screen, color, (center_x, center_t), radius, line_width)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


# 📝 Задачи для практики
# Задача 1: Нарисуй светофор (три круга: красный, жёлтый, зелёный)
# Задача 2: Нарисуй домик (квадрат + треугольник крыша + прямоугольник дверь + квадраты окна)
# Задача 3: Создай шахматную доску 8x8 (чередование чёрных и белых квадратов)
# Задача 4: Нарисуй смайлик (жёлтый круг, два глаза, улыбка)
# Задача 5: Создай функцию draw_star(x, y, size, color), которая рисует звезду
# Бонус задача: Нарисуй автомобиль, используя только примитивы