import pygame as pg
import random

# Спрайты
class Player(pg.sprite.Sprite):
    def __init__(self, coord_x, coord_y):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface((200, 200))
        self.image.fill((66, 69, 245)) # красим в цвет

        self.rect = self.image.get_rect() # получение класса прямоугольника (хитбокс)
        self.rect.x = coord_x
        self.rect.y = coord_y

class Coin(pg.sprite.Sprite):
    def __init__(self, coord_x, coord_y):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface((30, 30))
        self.image.fill((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))
        pg.draw.circle(self.image, (255, 209, 3), (15, 15), 15)

        self.rect = self.image.get_rect() # получение класса прямоугольника
        self.rect.x = coord_x
        self.rect.y = coord_y

class Enemy(pg.sprite.Sprite): # движущийся спрайт
    def __init__(self, coord_x, coord_y):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface((100, 100))
        self.image.fill((32, 255, 3))

        self.rect = self.image.get_rect() # получение класса прямоугольника
        self.rect.x = coord_x
        self.rect.y = coord_y

        self.speed_x = 5 # скорость для движения

    def update(self):
        self.rect.x += self.speed_x # движение

        # отскок от стен
        if self.rect.x >= 800 - self.rect.width or self.rect.x <= 0:
            self.speed_x *= -1

# Столкновения спрайтов
# pygame.sprite.spritecollide(sprite, group, dokill)
# pygame.sprite.groupcollide(group_1, group_2, dokill_1, dokill_2)



pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Писька бобра')
clock = pg.time.Clock()

player = Player(200, 200) # создание объекта класса
coins = pg.sprite.Group() # создание группы для множества спрайтов
for i in range(50):
    random_x = random.randint(50, 750)
    random_y = random.randint(50, 550)

    coin = Coin(random_x, random_y)
    coins.add(coin) # наполняем группу монетками

enemies = pg.sprite.Group() # группа врагов скакунов
for i in range(5):
    random_x = random.randint(100, 700)
    random_y = random.randint(100, 500)

    enemy = Enemy(random_x, random_y)
    enemies.add(enemy)

isActive = True
while isActive:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            isActive = False

    enemies.update()

    screen.fill((0, 0 ,0))
    screen.blit(player.image, player.rect)
    coins.draw(screen) # отрисовка всей группы спрайтов
    enemies.draw(screen) # рисуем движущиеся спрайты

    pg.display.flip()

pg.quit()