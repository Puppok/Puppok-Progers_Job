import pygame

from src.settings import WHITE, GRAY


class Slider:
    """
    Слайдер для настройки числового значения (например, громкости).

    Stage 1: геометрическая отрисовка, drag мышью.
    TODO Stage 5: PNG-трек и бегунок из assets/images/ui/.
    """

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        min_val: float = 0.0,
        max_val: float = 1.0,
        value: float   = 0.5,
    ):
        self.rect      = pygame.Rect(x, y, width, 20)
        self.min       = min_val
        self.max       = max_val
        self._value    = max(min_val, min(max_val, value))
        self._dragging = False

    # ------------------------------------------------------------------ #

    def get_value(self) -> float:
        return self._value

    def set_value(self, v: float) -> None:
        self._value = max(self.min, min(self.max, v))

    # ------------------------------------------------------------------ #

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self._dragging = True
        if event.type == pygame.MOUSEBUTTONUP:
            self._dragging = False
        if event.type == pygame.MOUSEMOTION and self._dragging:
            ratio = (event.pos[0] - self.rect.x) / self.rect.width
            self.set_value(self.min + ratio * (self.max - self.min))

    def draw(self, screen: pygame.Surface) -> None:
        # Трек
        pygame.draw.rect(screen, GRAY, self.rect, border_radius=4)
        # Заполненная часть
        ratio    = (self._value - self.min) / (self.max - self.min)
        fill_w   = int(ratio * self.rect.width)
        fill_rect = pygame.Rect(self.rect.x, self.rect.y, fill_w, self.rect.height)
        pygame.draw.rect(screen, (80, 160, 255), fill_rect, border_radius=4)
        # Бегунок
        thumb_x = self.rect.x + fill_w
        pygame.draw.circle(screen, WHITE, (thumb_x, self.rect.centery), 11)
        pygame.draw.circle(screen, GRAY,  (thumb_x, self.rect.centery), 11, 2)
