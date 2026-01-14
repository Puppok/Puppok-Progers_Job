import pygame as pg

pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Писька бобра')
clock = pg.time.Clock()


# === Работа с изображениями ===
# Форматы: .jpg .jpeg .png .gif .webp .bmp

# Загрузка картинки
crazy_frog_image = pg.image.load('./assets/Crazy_Frog.jpg')

# Получение текущих размеров картинки
frog_size = crazy_frog_image.get_rect()
print(f'Image size: {frog_size.width}x{frog_size.height}')

# -- Размеры картинки ---
# фиксированный размер .scale(image, (width, height))
scaled_frog = pg.transform.scale(crazy_frog_image, (700, 500))

# увеличение в 2 раза
doubled_frog = pg.transform.scale2x(crazy_frog_image)

# изменение размера относительно числа factor
# 0-1 для уменьшения, >1 для увеличения
relative_frog = pg.transform.scale_by(crazy_frog_image, 0.5)

# плавное изменение размера (работает как .scale(), но плавно)
smooth_frog = pg.transform.smoothscale(crazy_frog_image, (100, 100))

# --- Вращение картинки ---
# поворот на определенный градус
rotate_frog = pg.transform.rotate(crazy_frog_image, 90)

# отражение по горизонтали
horizontal_frog = pg.transform.flip(crazy_frog_image, True, False)

# отражение по вертикали
vertical_frog = pg.transform.flip(crazy_frog_image, False, True)

# отражение по обеим осям
flipped_frog = pg.transform.flip(crazy_frog_image, True, True)

# --- Картинки с альфа каналом (прозрачность) ---
# загрузка картинки с альфа каналом
google_logo = pg.image.load('./assets/google_logo.png').convert_alpha()

# установка прозрачности (0-255)
# 0 - полностью прозрачно, 255 - полностью непрозрачно
google_logo.set_alpha(128) # полупрозрачное


isActive = True
while isActive:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isActive = False

    screen.fill((0, 0, 0))

    # blit - Block Image Transfer (перенос блока изображения)
    # .blit(image, (start_x, start_y))
    screen.blit(relative_frog, (50, 50))
    screen.blit(google_logo, (300, 50))


    pg.display.flip()
    clock.tick(60)

pg.quit()