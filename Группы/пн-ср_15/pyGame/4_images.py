import pygame as pg

# === Работа с изображениями ===
# Форматы: .png .jpg .jpeg .gif .bmp .webp
lays_image = pg.image.load('lays.jpg') # загрузка картинки в программу

# получение размеров изображения
image_size = lays_image.get_rect()
print(f'Image size: {image_size.width}x{image_size.height}')

# Изменение размеров изображения
scaled_lays = pg.transform.scale(lays_image, (350, 100)) # фиксированные значения

doubled_lays = pg.transform.scale2x(lays_image) # увеличивает размер вдвое

# меняет размер по значению factor (0-1 для уменьшения, >1 для увеличения)
relative_scale = pg.transform.scale_by(lays_image, 0.005)

pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Бобровые картинки йопта')
clock = pg.time.Clock()

isActive = True
while isActive:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isActive = False

    screen.fill((0,0,0))

    # blit - Block Image Transfer (перенос блока изображения)
    # .blit(image, (start_x, start_y))
    screen.blit(relative_scale, (100, 100)) # отрисовка на экран


    pg.display.flip()
    clock.tick(60)

pg.quit()