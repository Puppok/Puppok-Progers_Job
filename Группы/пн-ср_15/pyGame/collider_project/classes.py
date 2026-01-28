import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.load = pg.image.load('./assets/starship.png')
        self.image = pg.transform.scale(self.load, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.bottom = 580
        self.rect.centerx = 400

        self.speed = 5

    def update(self, keys):
        if keys[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed



class Enemy(pg.sprite.Sprite):
    pass

class Bullet(pg.sprite.Sprite):
    pass