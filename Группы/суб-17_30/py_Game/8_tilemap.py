import pygame as pg

pg.init()
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()

# Размер тайла
TILE_SIZE = 32

# Карта (0 = пусто, 1 = земля, 2 = трава, 3 = вода)
tilemap = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 2, 2, 2, 2, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 3, 3, 3, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Цвета для типов тайлов
TILE_COLORS = {
    0: (135, 206, 235),  # Небо
    1: (139, 69, 19),  # Земля
    2: (0, 200, 0),  # Трава
    3: (0, 100, 255),  # Вода
}

running = True
while running:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Отрисовка
    screen.fill((135, 206, 235))

    # Рисуем каждый тайл
    for row in range(len(tilemap)):
        for col in range(len(tilemap[row])):
            tile_type = tilemap[row][col]

            if tile_type != 0:  # Не рисуем пустые тайлы
                x = col * TILE_SIZE
                y = row * TILE_SIZE
                color = TILE_COLORS[tile_type]

                pg.draw.rect(screen, color, (x, y, TILE_SIZE, TILE_SIZE))
                pg.draw.rect(screen, (0, 0, 0), (x, y, TILE_SIZE, TILE_SIZE), 1)

    pg.display.flip()

pg.quit()