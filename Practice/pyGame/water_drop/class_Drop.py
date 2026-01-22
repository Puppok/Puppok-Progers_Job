import random
import pygame as pg

class Drop(pg.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.load = pg.image.load('drop.webp').convert_alpha()
        self.image = pg.transform.scale(self.load, (30, 30))

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = 0

        self.speed = random.randint(100, 250)

    def update(self, dt):
        self.rect.y += self.speed * dt

        if self.rect.y > 600:
            self.kill()