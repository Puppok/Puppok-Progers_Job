import pygame as pg
import random

class Player(pg.sprite.Sprite):
    def __init__(self, screen_width, screen_height, speed):
        super().__init__()

        self.load = pg.image.load('assets/starship.png')
        self.image = pg.transform.scale(self.load, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.bottom = screen_height - 20

        self.speed = speed

    def update(self, keys):
        if keys[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed

class Enemy(pg.sprite.Sprite):
    def __init__(self, coord_x, coord_y):
        super().__init__()

        self.load = pg.image.load('assets/enemy.png')
        self.image = pg.transform.scale(self.load, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.x = coord_x
        self.rect.y = coord_y

        self.speed = random.choice([-2, 2])

    def update(self):
        self.rect.x += self.speed

        if self.rect.right >= 800 or self.rect.left <= 0:
            self.speed *= -1

class Bullet(pg.sprite.Sprite):
    def __init__(self, coord_x, coord_y):
        super().__init__()

        self.load = pg.image.load('assets/bullet.png')
        self.scale = pg.transform.scale(self.load, (20, 20))
        self.image = pg.transform.rotate(self.scale, 90)

        self.rect = self.image.get_rect()
        self.rect.x = coord_x
        self.rect.y = coord_y

        self.speed = -10

    def update(self):
        self.rect.y += self.speed

        if self.rect.bottom < 0:
            self.kill()

