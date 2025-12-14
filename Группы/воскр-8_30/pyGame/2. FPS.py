import pygame as pg

# FPS - frames per second (частота обновления экрана)

# переменная для хранения цветов
colors = {
    'white': (255, 255, 255),
    'black': (0, 0, 0)
}

pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Писька бобра')
clock = pg.time.Clock() # создание часов для доступа к кадрам, времени и тд
font = pg.font.Font(None, 60) # шрифт для текста (название, размер)

isActive = True
while isActive:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isActive = False

    screen.fill(colors['black']) # закрашиваем экран черным

    fps = int(clock.get_fps()) # полчение кол-ва fps в приложении

    # заготовка текста для отрисовки (текст, сглаживание, цвет)
    fps_text = font.render(f'FPS: {fps}', True, colors['white'])

    # отрисовка текста на экране (текст, позиция [x, y])
    screen.blit(fps_text, [10, 10])

    pg.display.flip()
    clock.tick(60) # создание ограничения частоты кадров

pg.quit()

# Задачи
# 1. посчитать и вывести, сколько всего кадров было за время работы игры
# 2. каждые 60 кадров менять цвет заднего фона на случайный
    # import random
    # random.choice(массив)
    # list(colors.values())
# 3. посчитать, сколько времени прошло с начала игры
    # import time
    # точка старта = time.time()
    # текущее время в игре = time.time() - точка старта

