import pygame as pg

pg.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('Писька бобра')
clock = pg.time.Clock()

cloud = pg.image.load('./assets/cloud.png').convert_alpha()
scaled_cloud = pg.transform.scale_by(cloud, .2)

cloud_coords_start = [
    {'x': 80, 'y': 2, 'speed': 250},
    {'x': 300, 'y': 70, 'speed': 280},
    {'x': 10, 'y': 150, 'speed': 220},
]

cloud_speed = 200

isActive = True
while isActive:
    dt = clock.tick(60) / 1000

    for event in pg.event.get():
        if event.type == pg.QUIT:
            isActive = False

    for cloud in cloud_coords_start:
        cloud['x'] += cloud['speed'] * dt

        if cloud['x'] > SCREEN_WIDTH:
            cloud['x'] = -SCREEN_WIDTH

    screen.fill((33, 214, 255))

    for cloud in cloud_coords_start:
        screen.blit(scaled_cloud, (cloud['x'], cloud['y']))

    pg.display.flip()

pg.quit()