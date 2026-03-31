import pygame

from src.utils.animation import Animation

COIN_SIZE = 22   # пиксели


def build_coin_frames() -> list[pygame.Surface]:
    """
    6 кадров вращения монеты вокруг вертикальной оси.
    x-радиус меняется как |cos(θ)|, имитируя объём.
    """
    S  = COIN_SIZE
    cx = cy = S // 2
    ry = S // 2 - 1

    x_scales = [1.0, 0.68, 0.36, 0.08, 0.36, 0.68]
    frames: list[pygame.Surface] = []

    for xw in x_scales:
        surf = pygame.Surface((S, S), pygame.SRCALPHA)
        rx   = max(1, int(ry * xw))

        # Тело монеты
        pygame.draw.ellipse(surf, (255, 182, 0),
                            (cx - rx, cy - ry, rx * 2, ry * 2))
        # Блик
        if xw > 0.25:
            hr = max(1, int(rx * 0.44))
            pygame.draw.ellipse(surf, (255, 232, 110),
                                (cx - hr, cy - ry + 2, hr * 2, ry - 3))
        # Обводка
        pygame.draw.ellipse(surf, (195, 130, 0),
                            (cx - rx, cy - ry, rx * 2, ry * 2), 1)
        frames.append(surf)

    return frames


class Coin(pygame.sprite.Sprite):

    def __init__(self, x: int, y: int):
        super().__init__()
        self._anim = Animation(build_coin_frames(), frame_duration=0.08, loop=True)
        self.image = self._anim.get_current_frame()
        self.rect  = self.image.get_rect(center=(x, y))

    def update(self, dt: float) -> None:
        self._anim.update(dt)
        self.image = self._anim.get_current_frame()
