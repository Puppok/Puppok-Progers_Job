import pygame as pg

class Button:
    def __init__(self, coord_x, coord_y, width, height, text):
        self.rect = pg.Rect(coord_x, coord_y, width, height)
        self.text = text

        self.color = (100, 100, 100)
        self.hover_color = (150, 150, 255)
        self.clicked_color = (200, 200, 255)
        self.text_color = (255, 255, 255)

        self.is_hovered = False
        self.is_clicked = False

    def update(self, mouse_pos, mouse_pressed):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

        if self.is_hovered and mouse_pressed:
            self.is_clicked = True
        else:
            self.is_clicked = False

        return self.is_clicked

    def draw(self, surface):
        if self.is_clicked:
            color = self.clicked_color
        elif self.is_hovered:
            color = self.hover_color
        else:
            color = self.color

        pg.draw.rect(surface, color, self.rect, border_radius = 5)
        pg.draw.rect(surface, (0, 0, 0), self.rect, 2, border_radius = 5)

        font = pg.font.Font(None, 32)
        text = font.render(self.text, True, self.text_color)
        text_rect = text.get_rect(center = self.rect.center)
        surface.blit(text, text_rect)


pg.init()
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()

button = Button(300, 250, 200, 100, 'Hello')

running = True
while running:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    mouse_pos = pg.mouse.get_pos()
    mouse_pressed = pg.mouse.get_pressed()[0]

    if button.update(mouse_pos, mouse_pressed):
        print('pressed')

    screen.fill((0, 0, 0))
    button.draw(screen)

    pg.display.flip()

pg.quit()