import pygame as pg

pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Test Game')
clock = pg.time.Clock()
font = pg.font.Font(None, 36)

isGameStarted = True
while isGameStarted:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isGameStarted = False

    screen.fill((0, 0, 0))

    fps = int(clock.get_fps())
    fps_text = font.render(f'FPS: {fps}', True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))

    pg.display.flip()
    clock.tick(60)

pg.quit()
