import pygame as pg

pg.init()

class AnimatedSpriteSheet(pg.sprite.Sprite):
    def __init__(self, image_path: str,
                 frame_size: tuple[int, int],
                 animations_map: dict,
                 default: str = 'idle_down'):
        super().__init__()

        # загрузка картинки (спрайт лист)
        self.spritesheet = pg.image.load(image_path).convert_alpha()
        self.frame_w, self.frame_h = frame_size # установка размеров кадра (ширина, высота)

        # Нарезка анимаций
        self.animations = {} # анимации
        for name, info in animations_map.items(): # достаем настройки анимации из конфига
            frames = self._cut_frames(info["row"], info["count"]) # нарезаем каждую строку
            self.animations[name] = { # создаем информацию об анимации (название, скорость, цикличность)
                "frames": frames,
                "speed": info.get("speed", 0.1),
                "loop": info.get("loop", True),
            }

        # Состояние анимации

        # Состояние движения

        # Привязка клавиш

    def _cut_frames(self, row: int, frame_count: int):
        """Нарезка кадров по строке из спрайт листа"""
        frames = []
        for index in range(frame_count):
            rect = pg.Rect(
                index * self.frame_w,
                row * self.frame_h,
                self.frame_w,
                self.frame_h
            )
            frames.append(self.spritesheet.subsurface(rect))
        return frames