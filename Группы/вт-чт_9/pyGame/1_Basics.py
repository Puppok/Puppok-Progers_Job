import pygame as pg

icon = pg.image.load('assets/icon.png') # загрузка картинки для иконки

pg.init() # инициализация библиотеки

screen = pg.display.set_mode((600, 400)) # создание окна произвольного размера
# fullscreen = pg.display.set_mode((0, 0), pg.FULLSCREEN) # полноэкранный режим

pg.display.set_caption('Писька бобра') # заголовок окна
pg.display.set_icon(icon) # иконка окна

isGameStarted = True # состояние игры
while isGameStarted: # запуск основного игрового цикла

    # === 1. Обработка событий игры ===
    for event in pg.event.get(): # перебираем все события игры
        if event.type == pg.QUIT: # если событие - выход из игры
            isGameStarted = False # останавливаем игру

    # === 2. Вся игровая логика ===
        # просчеты столкновений (колизии)
        # движение персонажа, просчет текущей позиции

    # === 3. Отрисовка, обновление экрана ===
    pg.display.flip() # обновление экрана

pg.quit() # завершение работы, очистка памяти

