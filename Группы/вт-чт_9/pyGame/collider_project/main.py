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
