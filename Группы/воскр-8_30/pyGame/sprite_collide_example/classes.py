import pygame as pg
import random

class Player(pg.sprite.Sprite):
    def __init__(self, screen_width, screen_height, speed_x):
        pg.sprite.Sprite.__init__(self)

        self.load = pg.image.load('./assets/starship.png')
        self.image = pg.transform.scale(self.load, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2 # выставляем игрока по центру экрана
        self.rect.bottom = screen_height - 20 # делаем отступ снизу, чтобы не прилипал к полу

        self.speed_x = speed_x

    def update(self, keys):
        if keys[pg.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed_x
        if (key
                and self.rect.right < 800):
            self.rect.x += self.speed_x

class Enemy(pg.sprite.Sprite):
    def __init__(self, coord_x, coord_y):
        super().__init__()

        self.load = pg.image.load('./assets/enemy.png')
        self.image = pg.transform.scale(self.load, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.x = coord_x
        self.rect.y = coord_y

        self.speed_x = random.choice([-3, 3])

    def update(self):
        self.rect.x += self.speed_x

        if self.rect.right > 800 or self.rect.left < 0:
            self.speed_x *= -1

class Bullet(pg.sprite.Sprite):
    def __init__(self, coord_x, coord_y):
        super().__init__()

        self.load = pg.image.load('./assets/bullet.png')
        self.scale = pg.transform.scale(self.load, (20, 20))
        self.image = pg.transform.rotate(self.scale, 90)

        self.rect = self.image.get_rect()
        self.rect.centerx = coord_x
        self.rect.bottom = coord_y

        self.speed_y = -10

    def update(self):
        self.rect.y += self.speed_y

        if self.rect.bottom < 0:
            self.kill()
