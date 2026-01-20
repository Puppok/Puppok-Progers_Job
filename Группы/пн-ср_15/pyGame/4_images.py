import pygame as pg

pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Бобровые картинки йопта')
clock = pg.time.Clock()

# === Работа с изображениями ===
# Форматы: .png .jpg .jpeg .gif .bmp .webp
lays_image = pg.image.load('assets/lays.jpg') # загрузка картинки в программу

# --- Размеры ---
# получение размеров изображения
image_size = lays_image.get_rect()
print(image_size)
print(f'Image size: {image_size.width}x{image_size.height}')

# Изменение размеров изображения
scaled_lays = pg.transform.scale(lays_image, (350, 100)) # фиксированные значения

doubled_lays = pg.transform.scale2x(lays_image) # увеличивает размер вдвое

# меняет размер по значению factor (0-1 для уменьшения, >1 для увеличения)
relative_scale = pg.transform.scale_by(lays_image, 0.3)

# плавное изменение размера
smooth_scale = pg.transform.smoothscale(lays_image, (500, 200))

# --- Вращение ---
# по градусу
rotate_lays = pg.transform.rotate(lays_image, 45)

# отзеркалить по горизонтали
flip_horizontal = pg.transform.flip(relative_scale, True, False)

# отзеркалить по вертикали
flip_vertical = pg.transform.flip(relative_scale, False, True)

# отзеркалить по обеим осям
flip_both = pg.transform.flip(relative_scale, True, True)


# --- Изображения с альфа каналом (прозрачность) ---
# .png с прозрачностью
google_logo = pg.image.load('assets/google_logo.png').convert_alpha()

# установка прозрачности
google_logo.set_alpha(128) # полупрозрачное изображение


# --- Работа с Rect ---
image_lays = pg.image.load('assets/lays.jpg')
image_lays_rect = lays_image.get_rect() # <rect(0, 0, 825, 1024)>
print(image_lays_rect)

# стартовая позиция прямоугольника на экране
image_lays_rect.topleft = (50, 50)
image_lays_rect.midtop = (40, 45)

# === Базовая анимация ===
surface = pg.Surface((200, 200)) # создаем поверхность
surface.fill((255, 0, 0))

coord_x, coord_y = 100, 100
speed = 400 # скорость перемещения

isActive = True
while isActive:
    dt = clock.tick(60) / 1000 # привязка ко времени

    for event in pg.event.get():
        if event.type == pg.QUIT:
            isActive = False

    keys = pg.key.get_pressed() # отслеживание состояния нажатости клавиш
    if keys[pg.K_w]: # если нажата w, идем вверх
        coord_y -= speed * dt
    if keys[pg.K_s]:
        coord_y += speed * dt
    if keys[pg.K_a]:
        coord_x -= speed * dt
    if keys[pg.K_d]:
        coord_x += speed * dt

    screen.fill((0,0,0))

    # blit - Block Image Transfer (перенос блока изображения)
    # .blit(image, (start_x, start_y))
    screen.blit(google_logo, (100, 100)) # отрисовка на экран
    screen.blit(surface, (coord_x, coord_y)) # отрисовка поверхности

    pg.display.flip()

pg.quit()