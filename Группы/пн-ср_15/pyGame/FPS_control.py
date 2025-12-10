from subprocess import check_output

import pygame as pg
import random
import time

# переменная для хранения цветов
colors = {
    'white': (255, 255, 255), # для текста
    'black': (0, 0, 0) # для заливки экрана
}
countFrames = 0
bg_change_counter = 0
current_bg = colors['black']
time_start = time.time()

bg_colors = {
    'green': (0, 255, 0),
    'red': (255, 0, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'pink': (255, 0, 255),
}

pg.init()

# FPS - frames per second (кадры в секунду)
screen = pg.display.set_mode((800, 600))
screen.fill(current_bg)
pg.display.set_caption("FPS control")
clock = pg.time.Clock() # создаем часы для отсчета времени работы игры
font = pg.font.Font(None, 36) # создание шрифта (название шрифта, размер)

isStarted = True
while isStarted:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isStarted = False

    current_time = time.time() - time_start
    countFrames += 1
    bg_change_counter += 1

    if countFrames == 60 or bg_change_counter == 60:
        current_bg = random.choice(list(bg_colors.values()))
        bg_change_counter = 0
    screen.fill(current_bg)
    # screen.fill(colors['black'])  # красим экран в черный цвет

    # отображение fps
    fps = int(clock.get_fps()) # получаем текущий fps игры

    fps_text = font.render(f'FPS: {fps}', True, colors['white']) # шаблон текста для экрана игры
    frames_text = font.render(f'Total frames: {countFrames}', True, colors['white'])
    bg_text = font.render(f'Current bg: {current_bg}', True, colors['white'])
    time_text = font.render(f'Ingame time: {current_time:.0f} sec', True, colors['white'])

    screen.blit(fps_text, [10, 10]) # отрисовка шаблона на экране игры
    screen.blit(frames_text, [10, 40])
    screen.blit(bg_text, [10, 70])
    screen.blit(time_text, [10, 90])

    pg.display.flip()
    clock.tick(60)  # установка раскадровку игры (60 FPS)
    # dt = clock.tick(60) / 1000.0 # delta time - привязка ко времени (позже)

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






