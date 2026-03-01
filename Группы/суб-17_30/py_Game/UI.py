import pygame as pg

class Button:
    def __init__(self, coord_x, coord_y, width, height, text):
        self.text = text

        self.color = (100, 100, 100)
        self.hover_color = (150, 150, 255)
        self.clicked_color = (200, 200, 255)
        self.text_color = (255, 255, 255)

        self.is_hovered = False
        self.is_clicked = False

    def update(self, mouse_pos, mouse_pressed):
        pass

    def draw(self, screen):
        pass