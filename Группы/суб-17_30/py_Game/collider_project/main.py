from classes import *

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()

# Создание групп
all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()
bullets = pg.sprite.Group()

# Игрок
player = Player(SCREEN_WIDTH, SCREEN_HEIGHT, 10)
all_sprites.add(player)

# Враги
for i in range(10):
    enemy = Enemy(30 + i * 70, 50)
    all_sprites.add(enemy)
    enemies.add(enemy)

score = 0
shoot_delay = 0

running = True
while running:
    dt = clock.tick(60) / 1000.0

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Управление персонажем
    keys = pg.key.get_pressed()
    player.update(keys)

    # Стрельба
    shoot_delay -= dt
    if keys[pg.K_SPACE] and shoot_delay <= 0:
       bullet = Bullet(player.rect.centerx, player.rect.top)
       all_sprites.add(bullet)
       bullets.add(bullet)
       shoot_delay = 0.3

    # Обновление состояния пуль и противника
    bullets.update()
    enemies.update()

    # Столкновения пуль с врагами
    hits = pg.sprite.groupcollide(bullets, enemies, True, True)
    score += len(hits)
    if hits:
        print(f'Score: {score}')

    # Отрисовка
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    pg.display.flip()

pg.quit()



