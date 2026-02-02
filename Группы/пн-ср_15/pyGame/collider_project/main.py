import pygame as pg
from classes import * # импортируем все классы (Player, Bullet, Enemy)

pg.init()

score = 0
shoot_delay = 0

screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Писька бобра')
clock = pg.time.Clock()

# Создание групп спрайтов
all_sprites = pg.sprite.Group()
bullets = pg.sprite.Group()
enemies = pg.sprite.Group()

# Создание игрока
player = Player(10)
all_sprites.add(player)

# Создание противников
for i in range(10):
    enemy = Enemy(10 + (i * 60), 50)
    enemies.add(enemy)
    all_sprites.add(enemy)

isActive = True
while isActive:
    dt = clock.tick(60) / 1000

    for event in pg.event.get():
        if event.type == pg.QUIT:
            isActive = False

    pg.display.flip()

pg.quit()