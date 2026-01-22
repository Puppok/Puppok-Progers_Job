import random
import pygame as pg

from Practice.pyGame.water_drop.class_Drop import Drop
from Practice.pyGame.water_drop.class_Player import Player

pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Писька бобра')
clock = pg.time.Clock()
font = pg.font.Font(None, 48)
background_load = pg.image.load('background.webp')
background_image = pg.transform.scale(background_load, (800, 600))

all_sprites = pg.sprite.Group()
drops = pg.sprite.Group()

player = Player()
all_sprites.add(player)

drop_timer = 0
drop_interval = 0.5

score = 0

isActive = True
while isActive:
    dt = clock.tick(60) / 1000

    for event in pg.event.get():
        if event.type == pg.QUIT:
            isActive = False

    keys = pg.key.get_pressed()
    player.update(dt, keys)

    drop_timer += dt
    if drop_timer >= drop_interval:
        drop = Drop(random.randint(20, 700))
        all_sprites.add(drop)
        drops.add(drop)
        drop_timer = 0

    drops.update(dt)

    hits = pg.sprite.spritecollide(player, drops, True)
    score += len(hits)
    score_text = font.render(f'Score: {str(score)}', True, (255, 255, 255))

    screen.fill((0, 0, 0))
    screen.blit(background_image, (0,0))
    all_sprites.draw(screen)
    screen.blit(score_text, [10, 10])

    pg.display.flip()

pg.quit()