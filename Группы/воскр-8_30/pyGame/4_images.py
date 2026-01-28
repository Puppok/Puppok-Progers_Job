import pygame as pg

pg.init()

screen = pg.display.set_mode((1500, 1000))
pg.display.set_caption('Клоака шимпанзе')
clock = pg.time.Clock()

# Загрузка картинки (форматы: .png .jpg .jpeg .bmp .gif .webp)
image_lays = pg.image.load('lays.jpg')

# Получение размеров картинки
image_size = image_lays.get_rect() # узнает размеры прямоугольника изображения
print(f'Image size: {image_size.width}x{image_size.height}')

# --- Размеры изображения ---
# до фиксированных значений
scaled_lays = pg.transform.scale(image_lays, (300, 300))

# изменение в x раз
# doubled_lays = pg.transform.scale2x(image_lays)
doubled_lays = pg.transform.scale_by(image_lays, 0.5) # >1 для увеличения, от 0 до 1 для уменьшения
sizes = doubled_lays.get_rect()
print(f'Image sizes: {sizes.width}x{sizes.height}')

# плавное масштабирование
smooth_lays = pg.transform.smoothscale(image_lays, (400, 400))


# --- Вращение изображения ---
# 1. Поворот на определенный угол
rotated_google = pg.transform.rotate(image_lays, 90)

# Зеркальное отражение (по х, по y, по обеим осям)
flipped_x = pg.transform.flip(rotated_google, True, False)
flipped_y = pg.transform.flip(rotated_google, False, True)
flipped_both = pg.transform.flip(rotated_google, True, True)



# отработка
coord_x, coord_y = 50, 200
speed = 200

isActive = True
while isActive:
    dt = clock.tick(60) / 1000

    for event in pg.event.get():
        if event.type == pg.QUIT:
            isActive = False

    coord_x += speed * dt

    if coord_x > 1500:
        coord_x = -800

    screen.fill((0, 0, 0))

    # Отрисовка картинки на экране
    # blit - Block Image Transfer (перенос блока изображения)
    screen.blit(smooth_lays, (coord_x, coord_y))

    pg.display.flip()


pg.quit()