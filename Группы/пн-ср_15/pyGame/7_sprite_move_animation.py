import pygame as pg

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
        self.current_anim = default
        self.frame_index = 0.0
        self.finished = False

        # Состояние движения
        self.move_speed = 3
        self.last_direction = "down"

        # Привязка клавиш (dx, dy, direction)
        self.controls = {
            pg.K_LEFT: (-1, 0, "left"),
            pg.K_RIGHT: (1, 0, "right"),
            pg.K_UP: (0, -1, "up"),
            pg.K_DOWN: (0, 1, "down"),
        }

        self.image = self.animations[self.current_anim]["frames"][0]
        self.rect = self.image.get_rect()

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

    def play(self, name, restart = False):
        if self.current_anim == name and not restart:
            return

        if name not in self.animations:
            return

        self.current_anim = name
        self.frame_index = 0.0
        self.finished = False

    def handle_input(self):
        keys = pg.key.get_pressed()
        moving = False

        for key, (dx, dy, direction) in self.controls.items():
            if keys[key]:
                self.rect.x += dx * self.move_speed
                self.rect.y += dy * self.move_speed
                self.last_direction = direction
                self.play(f"walk_{direction}")
                moving = True
                break  # одно направление за кадр

        if not moving:
            self.play(f"idle_{self.last_direction}")

    def update(self):
        self.handle_input()

        anim = self.animations[self.current_anim]
        frames = anim["frames"]

        if not self.finished:
            self.frame_index += anim["speed"]
            if self.frame_index >= len(frames):
                if anim["loop"]:
                    self.frame_index = 0.0
                else:
                    self.frame_index = len(frames) - 1
                    self.finished = True

        self.image = frames[int(self.frame_index)]

pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Miner Animation")
clock = pg.time.Clock()

animations = {
    "walk_down":  {"row": 0, "count": 4, "speed": 0.1},
    "walk_left":  {"row": 1, "count": 4, "speed": 0.1},
    "walk_right": {"row": 2, "count": 4, "speed": 0.1},
    "walk_up":    {"row": 3, "count": 4, "speed": 0.1},
    "idle_down":  {"row": 0, "count": 1, "speed": 0},
    "idle_left":  {"row": 1, "count": 1, "speed": 0},
    "idle_right": {"row": 2, "count": 1, "speed": 0},
    "idle_up":    {"row": 3, "count": 1, "speed": 0},
}

player = AnimatedSpriteSheet("spritesheet_miner.png", (64, 64), animations)
player.rect.center = (240, 160)

all_sprites = pg.sprite.Group(player)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    all_sprites.update()

    screen.fill((40, 42, 54))
    all_sprites.draw(screen)
    pg.display.flip()
    clock.tick(60)

pg.quit()