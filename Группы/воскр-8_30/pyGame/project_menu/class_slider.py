import pygame as pg

class Slider:
    def __init__(self, coord_x, coord_y, width, min_val, max_val, init_val, label):
        self.rect = pg.Rect(coord_x, coord_y, width, 15)

        self.min_val = min_val
        self.max_val = max_val
        self.value = init_val
        self.label = label

        self.handle_radius = 10
        self.handle_x = self.value_to_x(init_val)
        self.dragging = False

    def value_to_x(self, value):
        ratio = (value - self.min_val) / (self.max_val - self.min_val)
        return self.rect.x + int(ratio * self.rect.width)

    def x_to_value(self, coord_x):
        ratio = (coord_x - self.rect.x) / self.rect.width
        ratio = max(0, min(1, ratio))
        return self.min_val + ratio * (self.max_val - self.min_val)

    def update(self, events, mouse_pos):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    handle_rect = pg.Rect(self.handle_x - self.handle_radius,
                                          self.rect.centery - self.handle_radius,
                                          self.handle_radius * 2, self.handle_radius * 2)
                    if handle_rect.collidepoint(mouse_pos):
                        self.dragging = True

            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    self.dragging = False

        if self.dragging:
            self.handle_x = max(self.rect.x, min(mouse_pos[0], self.rect.right))
            self.value = self.x_to_value(self.handle_x)

    def draw(self, surface):
        # Текст
        font = pg.font.Font(None, 28)
        text = font.render(f"{self.label}: {int(self.value)}", True, (0, 0, 0))
        surface.blit(text, (self.rect.x, self.rect.y - 30))

        # Линия
        pg.draw.rect(surface, (150, 150, 150), self.rect, border_radius=8)

        # Заполнение
        fill_rect = pg.Rect(self.rect.x, self.rect.y, self.handle_x - self.rect.x, self.rect.height)
        pg.draw.rect(surface, (100, 200, 100), fill_rect, border_radius=8)

        # Ручка
        pg.draw.circle(surface, (100, 150, 255), (self.handle_x, self.rect.centery), self.handle_radius)
        pg.draw.circle(surface, (0, 0, 0), (self.handle_x, self.rect.centery), self.handle_radius, 2)
