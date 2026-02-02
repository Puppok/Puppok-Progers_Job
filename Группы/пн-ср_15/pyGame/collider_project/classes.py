import random
import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()

        self.load = pg.image.load('./assets/starship.png')
        self.image = pg.transform.scale(self.load, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.bottom = 580
        self.rect.centerx = 400

        self.speed = speed

    def update(self, keys):
        if keys[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed

class Enemy(pg.sprite.Sprite):
    def __init__(self, coord_x, coord_y):
        super().__init__()

        self.load = pg.image.load('./assets/enemy.png')
        self.image = pg.transform.scale(self.load, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.x = coord_x
        self.rect.y = coord_y

        self.speed = random.choice([-2, 2])

    def update(self):
        self.rect.x += self.speed

        if self.rect.left < 0 or self.rect.right > 800:
            self.speed *= -1

class Bullet(pg.sprite.Sprite):
    def __init__(self, coord_x, coord_y):
        super().__init__()

        self.load = pg.image.load('./assets/bullet.png')
        self.scale_load = pg.transform.scale(self.load, (50, 50))
        self.image = pg.transform.rotate(self.scale_load, 90)

        self.rect = self.image.get_rect()
        self.rect.x = coord_x
        self.rect.y = coord_y

        self.speed = -10

    def update(self):
        self.rect.y += self.speed

        if self.rect.bottom < 0:
            self.kill()
