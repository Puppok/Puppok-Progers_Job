import pygame as pg
import random

# Спрайты
class Player(pg.sprite.Sprite):
    def __init__(self, coord_x, coord_y):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface((250, 250))
        self.image.fill((28, 252, 3))

        # получение исходных границ изображения
        self.rect = self.image.get_rect()
        self.rect.x = coord_x
        self.rect.y = coord_y

# Группы спрайтов
class Coins(pg.sprite.Sprite):
    def __init__(self, coord_x, coord_y):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface((50, 50)) # создаем поверхность
        self.image.fill((255, 255, 255)) # закрашиваем в белый
        self.image.set_colorkey((255, 255, 255)) # делаем белый прозрачным

        pg.draw.circle(self.image, (252, 211, 3), (25, 25), 25)

        self.rect = self.image.get_rect()
        self.rect.x = coord_x
        self.rect.y = coord_y

# Движение спрайтов
class MovingEnemy(pg.sprite.Sprite):
    def __init__(self, coord_x, coord_y):
        super().__init__()

        self.image = pg.Surface((100, 100))
        self.image.fill((88, 74, 217))

        self.rect = self.image.get_rect()
        self.rect.x = coord_x
        self.rect.y = coord_y

        self.speed = 5

    # функция движения спрайта
    def update(self):
        self.rect.x += self.speed # смещение по оси x

        # если касается правого или левого края экрана, отскакивает в обратную сторону
        if self.rect.right >= 800 or self.rect.left <= 0:
            self.speed *= -1

# Столкновения спрайтов
# pygame.sprite.spritecollide(sprite, group, dokill)
# pygame.sprite.groupcollide(group_1, group_2, dokill_1, dokill_2)

pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Спрайты письки бобра йопта')
clock = pg.time.Clock()

player = Player(10, 10) # создание объекта персонажа

coins = pg.sprite.Group() # создание группы спрайтов
for _ in range(50):
    random_x = random.randint(50, 750)
    random_y = random.randint(50, 550)

    coin = Coins(random_x, random_y) # создание спрайта
    coins.add(coin) # добавление спрайта в группу

enemies = pg.sprite.Group()
for _ in range(10):
    random_x = random.randint(100, 700)
    random_y = random.randint(100, 500)

    enemy = MovingEnemy(random_x, random_y)
    enemies.add(enemy)

isActive = True
while isActive:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            isActive = False

    enemies.update() # вызываем функцию для движения спрайтов

    screen.fill((0, 0 ,0))
    # рисуем картинку в координатах его исходного прямоугольника
    screen.blit(player.image, player.rect)
    coins.draw(screen) # отрисовка группы спрайтов
    enemies.draw(screen) # отрисовка движущейся группы спрайтов

    pg.display.flip()

pg.quit()