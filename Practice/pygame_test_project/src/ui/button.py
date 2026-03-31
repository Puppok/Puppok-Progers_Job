import pygame

from src.settings import WHITE, GRAY, DARK_GRAY


class Button:
    """
    Кликабельная кнопка.

    Stage 1: базовая геометрическая отрисовка + hover-эффект.
    TODO Stage 5: поддержка PNG-изображений для normal/hover состояний.
    """

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        text: str,
        font: pygame.font.Font | None = None,
    ):
        self.rect    = pygame.Rect(x, y, width, height)
        self.text    = text
        self._font   = font or pygame.font.SysFont("Arial", 28)
        self.hovered = False

    def handle_event(self, event: pygame.event.Event) -> bool:
        """Возвращает True при клике левой кнопкой мыши."""
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False

    def set_text(self, text: str) -> None:
        self.text = text

    def draw(self, screen: pygame.Surface) -> None:
        color = GRAY if self.hovered else DARK_GRAY
        pygame.draw.rect(screen, color, self.rect, border_radius=8)
        pygame.draw.rect(screen, WHITE, self.rect, 2, border_radius=8)
        label = self._font.render(self.text, True, WHITE)
        screen.blit(label, label.get_rect(center=self.rect.center))
