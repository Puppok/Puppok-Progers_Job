import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.load = pg.image.load('isaac.webp').convert_alpha()
        self.image = pg.transform.scale(self.load, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 550
        self.speed = 300

    def update(self, dt, keys):
        if keys[pg.K_LEFT]:
            self.rect.x -= self.speed * dt
        if keys[pg.K_RIGHT]:
            self.rect.x += self.speed * dt

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 800:
            self.rect.x = 800
