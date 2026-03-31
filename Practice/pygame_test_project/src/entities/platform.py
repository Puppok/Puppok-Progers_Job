import pygame


# Цвета для разных «слоёв» платформ
_DIRT  = (139, 90,  43)
_GRASS = (72,  160, 56)
_STONE = (110, 110, 120)
_EDGE  = (50,  50,  55)


class Platform(pygame.sprite.Sprite):
    """
    Статичная платформа.

    kind="grass" — земляная с зелёным верхом (по умолчанию)
    kind="stone" — каменная

    TODO Stage 3: заменить на тайлы из TileSet по индексу.
    """

    def __init__(self, x: int, y: int, width: int, height: int, kind: str = "grass"):
        super().__init__()
        self.image = pygame.Surface((width, height))

        if kind == "stone":
            self.image.fill(_STONE)
            pygame.draw.rect(self.image, _EDGE, (0, 0, width, height), 2)
        else:  # grass
            self.image.fill(_DIRT)
            top_h = min(6, height)
            pygame.draw.rect(self.image, _GRASS, (0, 0, width, top_h))
            # Highlight на траве
            pygame.draw.line(self.image, (120, 210, 100), (0, 0), (width - 1, 0))

        self.rect = self.image.get_rect(topleft=(x, y))
