import pygame as pg

pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Анимации спрайтов')
clock = pg.time.Clock()

frames = []
for i in range(5):
    frame = pg.Surface((100, 100)) # создаем поверхность (кадр)
    color = (255, 50 * i, 0) # создаем цвет для кадра (меняется в ходе цикле)
    frame.fill(color) # закрашиваем поверхность в текущий цвет
    frames.append(frame) # добавляем получившийся кадр в массив кадров

current_frame = 0
frame_timer = 0
frame_duration = 0.2

isActive = True
while isActive:
    dt = clock.tick(60) / 1000

    for event in pg.event.get():
        if event.type == pg.QUIT:
            isActive = False

    frame_timer += dt
    if frame_timer >= frame_duration:
        frame_timer = 0
        current_frame = (current_frame + 1) % len(frames)

    screen.fill((0, 0, 0))
    screen.blit(frames[current_frame], (100, 100))

    pg.display.flip()

pg.quit()
