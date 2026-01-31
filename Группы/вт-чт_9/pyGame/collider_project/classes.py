import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, screen_width, screen_height, speed_x):
        super().__init__()

        self.load_image = pg.image.load('./assets/starship.png')
        self.image = pg.transform.scale(self.load_image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.bottom = screen_height - 20

        self.speed_x = speed_x

    def update(self, screen_width, keys):
        if keys[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed_x

        if keys[pg.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed_x

class Bullet(pg.sprite.Sprite):
    pass

class Enemy(pg.sprite.Sprite):
    pass