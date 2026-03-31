import pygame

from src.settings import WIDTH, HEIGHT

_LERP_SPEED = 10.0   # чем выше — тем быстрее камера догоняет игрока


class Camera:
    """
    Следит за целевым спрайтом и предоставляет смещение для отрисовки.

    update(target, dt) — плавное следование с lerp
    apply(sprite)      — rect со смещением для blit
    apply_rect(rect)   — то же для голых Rect
    """

    def __init__(self, level_width: int, level_height: int):
        self.offset   = pygame.math.Vector2(0, 0)
        self._level_w = level_width
        self._level_h = level_height

    def update(self, target: pygame.sprite.Sprite, dt: float) -> None:
        """Плавно центрирует камеру на target (lerp)."""
        tx = target.rect.centerx - WIDTH  // 2
        ty = target.rect.centery - HEIGHT // 2

        # Зажать по краям уровня
        tx = max(0, min(tx, self._level_w - WIDTH))
        ty = max(0, min(ty, self._level_h - HEIGHT))

        # Линейная интерполяция
        factor = min(1.0, _LERP_SPEED * dt)
        self.offset.x += (tx - self.offset.x) * factor
        self.offset.y += (ty - self.offset.y) * factor

    def reset(self) -> None:
        self.offset.update(0, 0)

    def apply(self, sprite: pygame.sprite.Sprite) -> pygame.Rect:
        """Rect спрайта со смещением камеры (для blit)."""
        return sprite.rect.move(-int(self.offset.x), -int(self.offset.y))

    def apply_rect(self, rect: pygame.Rect) -> pygame.Rect:
        return rect.move(-int(self.offset.x), -int(self.offset.y))
