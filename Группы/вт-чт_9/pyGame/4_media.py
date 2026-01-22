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


# --- Работа с rect ---
image_icon = pg.image.load('./assets/penguin.png')
image_icon_rect = image_icon.get_rect() # достаем rect область из картинки
print(f'Vinni rect: {image_icon_rect}') # <rect(0, 0, 32, 32)>

# Установка позиции через разные вариации точек
image_icon_rect.center = (400, 300)

# Доступные параметры rect
# x, y - координаты левого верхнего угла
print(f'\nIcon coords: {image_icon_rect.x}, {image_icon_rect.y}')

# width, height - размеры (ширина, высота)
print(f'\nIcon size: {image_icon_rect.width}x{image_icon_rect.height}')

# centerx, centery - координаты центра
print(f'\nIcon center coords: {image_icon_rect.centerx}, {image_icon_rect.centery}')

# top, left, right, bottom - границы rect
print(f'\nIcon border: \n'
      f'Left: {image_icon_rect.left}, \n'
      f'Right: {image_icon_rect.right}, \n'
      f'Top: {image_icon_rect.top}, \n'
      f'Bottom: {image_icon_rect.bottom}')

# Движение rect
# Сдвинуть на 100 вправо, на 50 вниз (move in-place) .move(x, y)
image_icon_rect.move_ip(100, 50)

# Создать новый, сразу сдвинутый rect
new_rect = image_icon_rect.move(50, 300)

# Пример работы
# Скорость движения
speed = 200

isActive = True
while isActive:
    dt = clock.tick(60) / 1000

    for event in pg.event.get():
        if event.type == pg.QUIT:
            isActive = False

    # массив нажатых клавиш
    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT]:
        image_icon_rect.x -= speed * dt
    if keys[pg.K_RIGHT]:
        image_icon_rect.x += speed * dt
    if keys[pg.K_UP]:
        image_icon_rect.y -= speed * dt
    if keys[pg.K_DOWN]:
        image_icon_rect.y += speed * dt

    # ограничение области движения по размерам экрана
    image_icon_rect.clamp_ip(screen.get_rect())

    screen.fill((0, 0, 0))

    # blit - Block Image Transfer (перенос блока изображения)
    # .blit(image, (start_x, start_y))
    # screen.blit(relative_frog, (50, 50))
    # screen.blit(google_logo, (300, 50))
    screen.blit(image_icon, image_icon_rect)

    pg.display.flip()


pg.quit()