import pygame as pg

pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Писька бобра')
clock = pg.time.Clock()

# Работа с картинками
# Форматы: .jpg .jpeg .png .bmp .webp .gif
frog_image = pg.image.load('./assets/Crazy_Frog.jpg')

# Получение размеров картинки
frog_size = frog_image.get_size() # размер в виде (width, height)
frog_size_width = frog_image.get_width()
frog_size_height = frog_image.get_height()

print(f'Полный размер: {frog_size} \n'
      f'Только ширина: {frog_size_width} \n'
      f'Только высота: {frog_size_height}')

# Создание изображений программно
surface_image = pg.Surface((100, 100)) # создание пустой поверхности
surface_image.fill((255, 140, 20)) # заливка цветом
# рисуем фигуры на области
pg.draw.rect(surface_image, (0, 255, 0), (30, 30, 20, 40))
pg.draw.circle(surface_image, (0, 0, 255), (50, 50), 10)

# Картинки с альфа каналом (прозрачность)
google_logo = pg.image.load('./assets/google_logo.png').convert_alpha()
google_logo.set_alpha(255) # уровень прозрачности (0 - прозрачно, 255 - нет)
google_logo.set_colorkey((235, 64, 50)) # фильтр прозрачности цвета

# Движение картинки
moving_surface = pg.Surface((100, 100)) # создаем поверхность / картинку
moving_surface.fill((255, 0, 0))

# Вращение картинки
# 1. Поворот на определенный угол
rotated_google = pg.transform.rotate(google_logo, 90)

# Зеркальное отражение (по х, по y, по обеим осям)
flipped_x = pg.transform.flip(rotated_google, True, False)
flipped_y = pg.transform.flip(rotated_google, False, True)
flipped_both = pg.transform.flip(rotated_google, True, True)

# Стартовая позиция + скорость
start_x, start_y = 100, 300
speed = 300

isActive = True
while isActive:
    dt = clock.tick(60) / 1000 # привязка просчетов ко времени

    for event in pg.event.get():
        if event.type == pg.QUIT:
            isActive = False

    # управление
    keys = pg.key.get_pressed() # отслеживаем состояние нажатия клавиш
    if keys[pg.K_a] or keys[pg.K_LEFT]: # нажатие буквы или стрелки
        start_x -= speed * dt
    if keys[pg.K_d]:
        start_x += speed * dt
    if keys[pg.K_w]:
        start_y -= speed * dt
    if keys[pg.K_s]:
        start_y += speed * dt

    screen.fill((0,0,0))

    # blit - Block Image Transfer (Перенос блока изображения)
    # .blit(image, (start_x, start_y))
    screen.blit(frog_image,(0, 0))
    screen.blit(surface_image, (30, 30)) # отрисовка области на экране
    screen.blit(flipped_both, (50, 50))
    screen.blit(moving_surface, (start_x, start_y)) # отрисовка движущейся поверхности

    pg.display.flip()

pg.quit()