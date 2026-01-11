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


isActive = True
while isActive:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isActive = False

    screen.fill((0, 0, 0))

    # Отрисовка картинки на экране
    # blit - Block Image Transfer (перенос блока изображения)
    screen.blit(smooth_lays, (50, 50))

    pg.display.flip()

pg.quit()