import pygame as pg
import random

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.load = pg.image.load('./assets/starship.png')
        self.image = pg.transform.scale(self.load, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.bottom = 580

    def update(self, keys):
        if keys[pg.K_a] and self.rect.left > 0:
            self.rect.x -= 10
        if keys[pg.K_d] and self.rect.right < 800:
            self.rect.x += 10

class Enemy:
    pass

class Bullet:
    pass