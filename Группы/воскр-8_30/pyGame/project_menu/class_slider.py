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
        ratio = (value - self.rect.x) / self.rect.width
        ratio = max(0, min(1, ratio))
        return self.rect.x + int(ratio * self.rect.width)

    def x_to_value(self, coord_x):
        ratio = (coord_x - self.rect.x) / self.rect.width
        ratio = max(0, min(1, ratio))
        return self.min_val + ratio * (self.max_val - self.min_val)

    def update(self, events, mouse_pos):
        pass