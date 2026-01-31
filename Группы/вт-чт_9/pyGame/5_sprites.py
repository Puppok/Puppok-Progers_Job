import pygame as pg
import random

# Спрайты
class Player(pg.sprite.Sprite):
    def __init__(self, coord_x, coord_y):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface((100, 100)) # создаем картинку / поверхность
        self.image.fill((0, 200, 150))

        self.rect = self.image.get_rect() # получаем хитбокс картинки
        self.rect.x = coord_x
        self.rect.y = coord_y

# Группы спрайтов
class Coin(pg.sprite.Sprite):
    def __init__(self, coord_x, coord_y):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface((50, 50))
        self.image.fill((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))

        pg.draw.circle(self.image, (252, 194, 3), (25, 25), 25)

        self.rect = self.image.get_rect()
        self.rect.x = coord_x
        self.rect.y = coord_y

# Движущийся спрайт
class MovingEnemy(pg.sprite.Sprite):
    def __init__(self, coord_x, coord_y, speed):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface((50, 50))
        self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.x = coord_x
        self.rect.y = coord_y

        self.speed_x = speed

    def update(self):
        self.rect.x += self.speed_x

        if self.rect.right >= 800 or self.rect.left <= 0:
            self.speed_x *= -1

# Столкновения спрайтов
# pygame.sprite.spritecollide(sprite, group, dokill)
# pygame.sprite.groupcollide(group_1, group_2, dokill_1, dokill_2)

pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Писька бобра')
clock = pg.time.Clock()

player = Player(100, 100) # создание объекта спрайта

coins = pg.sprite.Group() # создание группы спрайтов
for _ in range(50):
    random_x = random.randint(50, 750)
    random_y = random.randint(50, 550)

    coin = Coin(random_x, random_y) # создание спрайта
    coins.add(coin) # добавление спрайта в группу

enemies = pg.sprite.Group()
for _ in range(100):
    random_x = random.randint(50, 750)
    random_y = random.randint(50, 550)
    random_speed = random.randint(5, 15)

    enemy = MovingEnemy(random_x, random_y, random_speed)
    enemies.add(enemy)

isActive = True
while isActive:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            isActive = False

    enemies.update() # вызов метода update для каждого объекта класса

    screen.fill((3, 252, 252))

    screen.blit(player.image, player.rect) # отрисовка спрайта
    coins.draw(screen) # отрисовка группы спрайтов
    enemies.draw(screen) # отрисовка движущихся объектов

    pg.display.flip()

pg.quit()