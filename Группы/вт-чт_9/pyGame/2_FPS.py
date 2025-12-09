import pygame as pg

pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Отображение кадров (FPS)')
clock = pg.time.Clock() # создание часов, для отслеживания кадров и времени

isGameStarted = True
while isGameStarted:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isGameStarted = False

    pg.display.flip()

pg.quit()
