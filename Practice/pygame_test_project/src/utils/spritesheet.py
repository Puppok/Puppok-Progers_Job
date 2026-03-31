import pygame


class SpriteSheet:
    """
    Загружает PNG со множеством кадров и нарезает их.

    Использование:
        sheet = SpriteSheet("assets/images/player/player_sheet.png")
        frames = sheet.get_strip(row=0, count=4, frame_w=48, frame_h=48)
    """

    def __init__(self, path: str):
        self.sheet = pygame.image.load(path).convert_alpha()

    def get_image(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        colorkey=None,
    ) -> pygame.Surface:
        """Вырезает один кадр по координатам пикселей."""
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), (x, y, width, height))
        if colorkey is not None:
            image.set_colorkey(colorkey)
        return image

    def get_strip(
        self,
        row: int,
        count: int,
        frame_w: int,
        frame_h: int,
        colorkey=None,
    ) -> list[pygame.Surface]:
        """Возвращает список кадров из горизонтальной полосы (row)."""
        return [
            self.get_image(i * frame_w, row * frame_h, frame_w, frame_h, colorkey)
            for i in range(count)
        ]
