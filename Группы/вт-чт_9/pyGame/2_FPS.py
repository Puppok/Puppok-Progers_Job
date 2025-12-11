import pygame as pg

# FPS - кол-во кадров в секунду (frames per second)

# цвета для заливки экрана и текста
colors = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
}

pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Отображение кадров (FPS)')
clock = pg.time.Clock() # создание часов, для отслеживания кадров и времени
font = pg.font.Font(None, 100) # создание шрифта для текста (название, размер)
# формат шрифтов .ttf

isGameStarted = True
while isGameStarted:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isGameStarted = False

    # заполняем экран черным цветом
    screen.fill(colors['black'])

    # получаем текущий FPS
    fps = int(clock.get_fps())

    # создаем шаблон текста для отрисовки на экране
    fps_text = font.render(f'FPS: {fps}', True, colors['white'])

    # отрисовка текста на экране игры
    screen.blit(fps_text, (10, 10))

    pg.display.flip()
    clock.tick(60) # ограничение работы игры (60 FPS)

pg.quit()
