import pygame as pg
from module_classes import TileMapEditor

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Tilemap Editor")
clock = pg.time.Clock()

# Создание редактора
editor = TileMapEditor(width = 20, height = 15, tile_size = 32)

# Попытка загрузить сохраненную карту
editor.load_from_file("tilemap.json")

# Состояние мыши
mouse_pressed = False

running = True
while running:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # Клавиши
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                editor.set_current_tile(1)
            elif event.key == pg.K_2:
                editor.set_current_tile(2)
            elif event.key == pg.K_3:
                editor.set_current_tile(3)
            elif event.key == pg.K_4:
                editor.set_current_tile(4)
            elif event.key == pg.K_s:
                editor.save_to_file("tilemap.json")
            elif event.key == pg.K_l:
                editor.load_from_file("tilemap.json")

        # Мышь
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pressed = True
            editor.handle_click(*event.pos, event.button)

        if event.type == pg.MOUSEBUTTONUP:
            mouse_pressed = False

    # Рисование при удержании мыши
    if mouse_pressed:
        mouse_buttons = pg.mouse.get_pressed()
        mouse_pos = pg.mouse.get_pos()

        if mouse_buttons[0]:  # ЛКМ
            editor.handle_click(*mouse_pos, 1)
        elif mouse_buttons[2]:  # ПКМ
            editor.handle_click(*mouse_pos, 3)

    # Отрисовка
    screen.fill((30, 30, 40))

    # Сдвиг для UI
    pg.draw.rect(screen, (20, 20, 30), (0, 0, 150, 600))

    # Карта
    map_surface = pg.Surface((640, 480))
    editor.draw(map_surface)
    screen.blit(map_surface, (editor.offset_x, editor.offset_y))

    # UI
    editor.draw_ui(screen)

    pg.display.flip()

pg.quit()