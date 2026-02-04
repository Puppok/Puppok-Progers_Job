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

    # Управление персонажем
    keys = pg.key.get_pressed()
    player.update(keys)

    # Стрельба
    shoot_delay -= dt
    if keys[pg.K_SPACE] and shoot_delay <= 0:
        bullet = Bullet(player.rect.centerx, player.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        shoot_delay = 0.4

    # Движение пуль и противников
    bullets.update()
    enemies.update()

    # Столкновение пули и противника
    hits = pg.sprite.groupcollide(bullets, enemies, True, True)
    score += len(hits)
    if hits:
        print(f'Score: {score}')

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    pg.display.flip()

pg.quit()