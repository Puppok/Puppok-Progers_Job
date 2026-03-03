import pygame as pg

class Button:
    def __init__(self, coord_x, coord_y, width, height, text):
        self.rect = pg.Rect(coord_x, coord_y, width, height)
        self.text = text

        self.color = (100, 150, 200)
        self.hover_color = (150, 200, 255)
        self.text_color = (255, 255, 255)

        self.is_hovered = False

    def update(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and self.is_hovered:
                return True
        return False

    def draw(self, surface):
        color = self.hover_color if self.is_hovered else self.color

        pg.draw.rect(surface, color, self.rect, border_radius = 5)
        pg.draw.rect(surface, (0, 0, 0), self.rect, 2, border_radius = 5)

        font = pg.font.Font(None, 32)
        text = font.render(self.text, True, self.text_color)
        text_rect = text.get_rect(center = self.rect.center)
        surface.blit(text, text_rect)
