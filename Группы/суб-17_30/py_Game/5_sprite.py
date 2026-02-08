import pygame as pg
import random

class Player(pg.sprite.Sprite):
    def __init__(self, coord_x, coord_y):
        super().__init__()

        self.image = pg.Surface((250, 250))
        self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.x = coord_x
        self.rect.y = coord_y

class Coin(pg.sprite.Sprite):
    def __init__(self, coord_x, coord_y):
        super().__init__()

        self.image = pg.Surface((20, 20))
        self.image.fill((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))
        pg.draw.circle(self.image, (255, 255, 0), (10, 10), 10)

        self.rect = self.image.get_rect()
        self.rect.x = coord_x
        self.rect.y = coord_y

class MovingMan(pg.sprite.Sprite):
    def __init__(self, coord_x, coord_y, speed):
        super().__init__()

        self.image = pg.Surface((150, 150))
        self.image.fill((0, 0, 255))

        self.rect = self.image.get_rect()
        self.rect.x = coord_x
        self.rect.y = coord_y

        self.speed_x = speed

    def update(self):
        self.rect.x += self.speed_x

        if self.rect.right > 800 or self.rect.left < 0:
            self.speed_x *= -1

# Отслеживание столкновений
# .spritecollide(sprite, group, dokill)
# .groupcollide(group_1, group_2, dokill_1, dokill_2)

pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Спрайты')
clock = pg.time.Clock()

# создание объекта спрайта
player = Player(100, 200)

# Создание группы монеток
coins = pg.sprite.Group()
for _ in range(50):
    random_x = random.randint(100, 700)
    random_y = random.randint(50, 550)

    coin = Coin(random_x, random_y)
    coins.add(coin)

# Создаем группу движущихся спрайтов
moving_people = pg.sprite.Group()
for _ in range(5):
    random_x = random.randint(200, 600)
    random_y = random.randint(200, 400)

    moving_man = MovingMan(random_x, random_y, 5)
    moving_people.add(moving_man)

isActive = True
while isActive:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isActive = False

    moving_people.update() # заставляем спрайты двигаться

    screen.fill((0, 0, 0))

    screen.blit(player.image, player.rect) # отрисовка спрайта
    coins.draw(screen) # отрисовка группы
    moving_people.draw(screen) # рисуем движущиеся спрайты

    pg.display.flip()
    clock.tick(60)

pg.quit()