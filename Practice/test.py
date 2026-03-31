import pygame


class AnimatedButton:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

        self.base_size = 200
        self.current_size = self.base_size
        self.growing = True
        self.pulse_speed = 30

        self.hovered = False
        self.clicking = False
        self.click_blink_count = 0
        self.blink_timer = 0

    def update(self, dt, mouse_pos):
        half_size = self.current_size // 2
        rect = pygame.Rect(self.x - half_size, self.y - half_size,
                           self.current_size, self.current_size)

        self.hovered = rect.collidepoint(mouse_pos)

        if self.clicking:
            self.blink_timer += dt
            if self.blink_timer >= 0.15:
                self.blink_timer = 0
                self.click_blink_count += 1

                if self.click_blink_count >= 6:
                    self.clicking = False
                    self.click_blink_count = 0

        elif not self.hovered:
            if self.growing:
                self.current_size += self.pulse_speed * dt
                if self.current_size >= self.base_size + 20:
                    self.growing = False
            else:
                self.current_size -= self.pulse_speed * dt
                if self.current_size <= self.base_size - 20:
                    self.growing = True
        else:
            target = self.base_size + 30
            if self.current_size < target:
                self.current_size += self.pulse_speed * 2 * dt
                if self.current_size > target:
                    self.current_size = target

    def click(self):
        self.clicking = True
        self.click_blink_count = 0
        self.blink_timer = 0
        print(f"Нажата кнопка: {self.text}")

    def draw(self, screen):
        if self.clicking and self.click_blink_count % 2 == 1:
            return

        half_size = int(self.current_size) // 2

        if self.clicking:
            color = (255, 255, 0)
        elif self.hovered:
            color = (100, 255, 100)
        else:
            color = (100, 150, 255)

        pygame.draw.rect(screen, color,
                         (self.x - half_size, self.y - half_size,
                          int(self.current_size), int(self.current_size)),
                         border_radius=15)

        pygame.draw.rect(screen, (0, 0, 0),
                         (self.x - half_size, self.y - half_size,
                          int(self.current_size), int(self.current_size)),
                         3, border_radius=15)


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Анимированное меню")
clock = pygame.time.Clock()

buttons = [
    AnimatedButton(400, 150, "Играть"),
    AnimatedButton(400, 300, "Настройки"),
    AnimatedButton(400, 450, "Выход")
]

running = True
while running:
    dt = clock.tick(60) / 1000.0

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.hovered:
                    button.click()

    for button in buttons:
        button.update(dt, mouse_pos)

    screen.fill((50, 50, 80))

    for button in buttons:
        button.draw(screen)

    pygame.display.flip()

pygame.quit()