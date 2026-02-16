from classes import *

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
score = 0
shoot_delay = 0

pg.init()

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('Collider project')
bg_image = pg.image.load('./assets/BG.jpeg')
clock = pg.time.Clock()

# Группы спрайтов
all_sprites = pg.sprite.Group()
bullets = pg.sprite.Group()
enemies = pg.sprite.Group()

# Игрок
player = Player(SCREEN_WIDTH, SCREEN_HEIGHT, 10)
all_sprites.add(player)

# Создание противников
for i in range(10):
    enemy = Enemy(i * 70, 50)
    all_sprites.add(enemy)
    enemies.add(enemy)

isActive = True
while isActive:
    dt = clock.tick(60) / 1000

    for event in pg.event.get():
        if event.type == pg.QUIT:
            isActive = False

    # Управление игроком
    keys = pg.key.get_pressed()
    player.update(keys)

    # Стрельба
    shoot_delay -= dt
    if keys[pg.K_SPACE] and shoot_delay <= 0:
        bullet = Bullet(player.rect.centerx, player.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        shoot_delay = 0.2

    # Обновление состояния
    bullets.update()
    enemies.update()

    # Просчет столкновений
    hits = pg.sprite.groupcollide(bullets, enemies, True, True)
    score += len(hits)
    if hits:
        print(f'Score: {score}')

    screen.blit(bg_image,(0,0))
    all_sprites.draw(screen)
    pg.display.flip()

pg.quit()