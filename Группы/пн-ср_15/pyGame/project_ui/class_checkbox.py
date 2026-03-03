import pygame as pg

class CheckBox:
    def __init__(self, coord_x, coord_y, size, label):
        self.rect = pg.Rect(coord_x, coord_y, size, size)
        self.label = label
        self.checked = False

    def update(self, events, mouse_pos):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1 and self.rect.collidepoint(mouse_pos):
                    self.checked = not self.checked

    def draw(self, surface):
        pg.draw.rect(surface, (200, 200, 200), self.rect)
        pg.draw.rect(surface, (0, 0, 0), self.rect, 2)

        if self.checked:
            points = [
                (self.rect.x + 5, self.rect.centery),
                (self.rect.centerx - 3 , self.rect.bottom - 5),
                (self.rect.right - 5, self.rect.y + 5)
            ]
            pg.draw.lines(surface, (0, 200, 0), False, points, 3)

        font = pg.font.Font(None, 28)
        text = font.render(self.label, True, (0, 0, 0))
        surface.blit(text, (self.rect.right + 10, self.rect.y + 2))

# TODO: чуваки запишут и дальше слайдер