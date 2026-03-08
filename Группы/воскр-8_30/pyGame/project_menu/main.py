import pygame as pg
from class_slider import Slider
from class_button import Button
from class_checkbox import Checkbox

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Меню настроек")
clock = pg.time.Clock()

# Настройки
music_volume = 70
sfx_volume = 50
fullscreen = False
show_fps = True

# UI элементы
music_slider = Slider(200, 150, 400, 0, 100, music_volume, "Музыка")
sfx_slider = Slider(200, 230, 400, 0, 100, sfx_volume, "Эффекты")

fullscreen_check = Checkbox(200, 310, 30, "Полный экран")
fullscreen_check.checked = fullscreen

fps_check = Checkbox(200, 360, 30, "Показывать FPS")
fps_check.checked = show_fps

apply_button = Button(200, 450, 180, 60, "Применить")
cancel_button = Button(420, 450, 180, 60, "Отмена")

# Сохранённые значения
saved_music = music_volume
saved_sfx = sfx_volume
saved_fullscreen = fullscreen
saved_fps = show_fps

running = True
while running:
    clock.tick(60)

    mouse_pos = pg.mouse.get_pos()
    events = pg.event.get()

    for event in events:
        if event.type == pg.QUIT:
            running = False

        # Кнопки
        if apply_button.is_clicked(event):
            saved_music = music_slider.value
            saved_sfx = sfx_slider.value
            saved_fullscreen = fullscreen_check.checked
            saved_fps = fps_check.checked
            print(f"Настройки применены: Музыка={saved_music:.0f}, Эффекты={saved_sfx:.0f}")

        if cancel_button.is_clicked(event):
            music_slider.value = saved_music
            music_slider.handle_x = music_slider.value_to_x(saved_music)
            sfx_slider.value = saved_sfx
            sfx_slider.handle_x = sfx_slider.value_to_x(saved_sfx)
            fullscreen_check.checked = saved_fullscreen
            fps_check.checked = saved_fps
            print("Изменения отменены")

    # Обновление
    music_slider.update(events, mouse_pos)
    sfx_slider.update(events, mouse_pos)
    fullscreen_check.update(events, mouse_pos)
    fps_check.update(events, mouse_pos)
    apply_button.update(mouse_pos)
    cancel_button.update(mouse_pos)

    # Отрисовка
    screen.fill((240, 240, 250))

    # Заголовок
    font = pg.font.Font(None, 56)
    title = font.render("Настройки", True, (0, 0, 0))
    screen.blit(title, (320, 40))

    music_slider.draw(screen)
    sfx_slider.draw(screen)
    fullscreen_check.draw(screen)
    fps_check.draw(screen)
    apply_button.draw(screen)
    cancel_button.draw(screen)

    pg.display.flip()

pg.quit()