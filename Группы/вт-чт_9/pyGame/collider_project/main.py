from classes import *

pg.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
score = 0
shoot_delay = 0

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('Стрелялка')
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
    enemy = Enemy(i * 80 + 10, 50)
    all_sprites.add(enemy)
    enemies.add(enemy)

is_running = True
while is_running:
    dt = clock.tick(60) / 1000

    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

    # Движение игрока
    keys = pg.key.get_pressed()
    player.update(SCREEN_WIDTH, keys)

    # Стрельба
    shoot_delay -= dt
    if keys[pg.K_SPACE] and shoot_delay <= 0:
        bullet = Bullet(player.rect.centerx, player.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        shoot_delay = .3

    # Передвижение всех
    enemies.update()
    bullets.update()

    # Столкновение пули и противника
    hits = pg.sprite.groupcollide(bullets, enemies, True, True)
    score += len(hits)
    if hits:
        print(f'Score: {score}')

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    pg.display.flip()

pg.quit()