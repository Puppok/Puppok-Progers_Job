import pygame as pg

# FPS - frames per second (кадры в секунду)

total_frames = 0

# переменная для хранения цветов
color = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
}

pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption("FPS Control")
clock = pg.time.Clock() # взаимодействие с кадрами, временем
font = pg.font.Font(None, 60) # создание шрифта для текста (название шрифта, размер)

isActive = True
while isActive:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isActive = False

    total_frames += 1

    screen.fill(color['black']) # заливка экрана черным цветом

    fps = int(clock.get_fps()) # получаем текущее кол-во FPS

    # шаблон текста для отрисовки fps
    fps_text = font.render(f'FPS: {fps}', True, color['white'])
    total_frames_text = font.render(f'Total Frames: {total_frames}', True, color['white'])

    # отрисовка текста на экране
    screen.blit(fps_text, [10, 10])
    screen.blit(total_frames_text, [10, 50])

    pg.display.flip()
    clock.tick(60) # ограничение частоты FPS

pg.quit()

# Задачи
# 1. посчитать и вывести, сколько всего кадров было за время работы игры
# 2. каждые 60 кадров менять цвет заднего фона на случайный
    # import random
    # random.choice(массив)
    # list(colors.values())