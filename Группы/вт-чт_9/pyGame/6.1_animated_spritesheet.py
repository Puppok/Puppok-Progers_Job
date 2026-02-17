import pygame as pg

class AnimatedSpritesheet(pg.sprite.Sprite):
    def __init__(self, image_path: str, frame_size: tuple, animation_map: dict, default: str = 'idle_down'):
        super().__init__()

        self.spritesheet = pg.image.load(image_path).convert_alpha() # спрайтлист картинка
        self.frame_w, self.frame_h = frame_size # размеры кадра

        # нарезка всех анимаций
        self.animations = {}
        for name, info in animation_map.items():
            frames = self._cut_frames(info['row'], info['count'])
            self.animations[name] = {
                'frames': frames,
                'speed': info.get('speed', 0.1),
                'loop': info.get('loop', True),
            }

        # состояние анимации
        self.current_animation = default
        self.frame_index = 0
        self.finished = False

        # состояние движения
        self.move_speed = 3
        self.last_direction = 'down'

        # привязка клавиш: key -> (dx, dy, dir)
        self.controls = {
            pg.K_LEFT:  (-1, 0, 'left'),
            pg.K_RIGHT: (1, 0, 'right'),
            pg.K_UP:    (0, -1, 'up'),
            pg.K_DOWN:  (0, 1, 'down'),
        }

        self.image = self.animations[self.current_animation]['frames'][0]
        self.rect = self.image.get_rect()

    def _cut_frames(self, row: int, count: int):
        """Нарезка кадров"""
        frames = []
        for col in range(count):
            rect = pg.Rect(col * self.frame_w, row * self.frame_h, self.frame_w, self.frame_h)
            frames.append(self.spritesheet.subsurface(rect))

        return frames

    def handle_input(self):
        """Обработка клавиатуры"""
        keys = pg.key.get_pressed()
        moving = False

        for key, (dx, dy, direction) in self.controls.items():
            if keys[key]:
                self.rect.x += dx * self.move_speed
                self.rect.y += dy * self.move_speed
                self.last_direction = direction
                moving = True
                break

            if not moving:
                self.play(f'idle_{self.last_direction}')

    def play(self, name, restart = False):
        pass

    def update(self):
        pass

