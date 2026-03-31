import pygame

from src.settings import (
    PLAYER_FRAME_W, PLAYER_FRAME_H,
    GRAVITY, PLAYER_SPEED, JUMP_FORCE, MAX_FALL_SPEED,
    ANIM_SPEED, LEVEL_WIDTH,
    WHITE, BLACK,
)
from src.utils.animation import Animation


# ------------------------------------------------------------------ #
#  Генератор кадров-заглушек                                           #
#  Заменить на SpriteSheet.get_strip() когда будут готовы ассеты.      #
# ------------------------------------------------------------------ #

def _build_placeholder_frames() -> dict[str, list[pygame.Surface]]:
    """Рисует простые векторные спрайты для каждого состояния анимации."""
    W, H = PLAYER_FRAME_W, PLAYER_FRAME_H

    BODY_COLOR = {
        "idle": (70,  120, 210),
        "run":  (70,  180,  90),
        "jump": (210, 190,  40),
        "fall": (210, 110,  40),
    }
    COUNTS = {"idle": 4, "run": 6, "jump": 2, "fall": 2}

    def shade(c, d):
        return tuple(max(0, min(255, v + d)) for v in c)

    def make_frame(state: str, idx: int, col: tuple) -> pygame.Surface:
        surf = pygame.Surface((W, H), pygame.SRCALPHA)

        bob = (idx % 2) if state == "idle" else 0   # лёгкое покачивание

        # Тело
        bx, by, bw, bh = 8, 4 + bob, W - 16, H - 22
        pygame.draw.rect(surf, col, (bx, by, bw, bh), border_radius=5)

        # Голова
        pygame.draw.rect(surf, shade(col, 25), (10, bob, W - 20, 14), border_radius=4)

        # Глаз (правая сторона = взгляд вправо)
        pygame.draw.circle(surf, WHITE, (W - 14, 6 + bob), 4)
        pygame.draw.circle(surf, BLACK, (W - 13, 7 + bob), 2)

        # Ноги
        lc  = shade(col, -50)
        top = by + bh

        if state == "run":
            shifts = [0, -5, -8, -5, 0, 5]
            off = shifts[idx % len(shifts)]
            pygame.draw.rect(surf, lc, (9,      top + off,  8, 10), border_radius=2)
            pygame.draw.rect(surf, lc, (W - 17, top - off,  8, 10), border_radius=2)
        elif state == "jump":
            pygame.draw.rect(surf, lc, (7,      top - 5, 10, 8), border_radius=2)
            pygame.draw.rect(surf, lc, (W - 17, top - 5, 10, 8), border_radius=2)
        elif state == "fall":
            pygame.draw.rect(surf, lc, (7,      top,     10, 12), border_radius=2)
            pygame.draw.rect(surf, lc, (W - 17, top,     10, 12), border_radius=2)
        else:  # idle
            pygame.draw.rect(surf, lc, (9,      top + bob, 8, 10), border_radius=2)
            pygame.draw.rect(surf, lc, (W - 17, top + bob, 8, 10), border_radius=2)

        return surf

    result: dict[str, list[pygame.Surface]] = {}
    for state, col in BODY_COLOR.items():
        result[state] = [make_frame(state, i, col) for i in range(COUNTS[state])]
    return result


# ------------------------------------------------------------------ #
#  Player                                                              #
# ------------------------------------------------------------------ #

class Player(pygame.sprite.Sprite):

    def __init__(self, x: int, y: int):
        super().__init__()

        # Анимации
        frames = _build_placeholder_frames()
        self._anims: dict[str, Animation] = {
            key: Animation(f, ANIM_SPEED.get(key, 0.1), loop=key in ("idle", "run"))
            for key, f in frames.items()
        }
        self._anim_key    = "idle"
        self._facing_right = True

        # Физика
        self.pos         = pygame.math.Vector2(x, y)
        self.vel         = pygame.math.Vector2(0.0, 0.0)
        self.on_ground   = False
        self.just_jumped = False   # сбрасывается в game_state после проверки
        self.just_landed = False   # True в первый тик приземления

        # Спрайт
        self.image = self._anims["idle"].get_current_frame()
        self.rect  = self.image.get_rect(topleft=(x, y))

    # ------------------------------------------------------------------ #
    #  Ввод                                                                #
    # ------------------------------------------------------------------ #

    def handle_input(self, pressed: set, controls: dict) -> None:
        self.vel.x = 0.0
        if controls["left"] in pressed:
            self.vel.x = -PLAYER_SPEED
            self._facing_right = False
        if controls["right"] in pressed:
            self.vel.x = PLAYER_SPEED
            self._facing_right = True
        if controls["jump"] in pressed and self.on_ground:
            self.vel.y    = JUMP_FORCE
            self.on_ground = False
            self.just_jumped = True

    # ------------------------------------------------------------------ #
    #  Обновление                                                          #
    # ------------------------------------------------------------------ #

    def update(self, dt: float, platforms) -> None:
        # Гравитация
        self.vel.y += GRAVITY * dt
        self.vel.y  = min(self.vel.y, MAX_FALL_SPEED)

        # Движение по X + коллизии со стенками экрана
        self.pos.x += self.vel.x * dt
        self.rect.x = round(self.pos.x)
        self._collide_x(platforms)
        # Не выходить за края уровня
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > LEVEL_WIDTH:
            self.rect.right = LEVEL_WIDTH
        self.pos.x = self.rect.x

        # Движение по Y + коллизии (платформы — одностороннее приземление)
        self.pos.y += self.vel.y * dt
        self.rect.y = round(self.pos.y)
        was_grounded   = self.on_ground
        self.on_ground = False
        self._collide_y(platforms)
        self.just_landed = self.on_ground and not was_grounded
        self.pos.y = self.rect.y

        # Анимация
        self._update_animation(dt)

    # ------------------------------------------------------------------ #
    #  Коллизии                                                            #
    # ------------------------------------------------------------------ #

    def _collide_x(self, platforms) -> None:
        for plat in platforms:
            if self.rect.colliderect(plat.rect):
                if self.vel.x > 0:
                    self.rect.right = plat.rect.left
                elif self.vel.x < 0:
                    self.rect.left  = plat.rect.right
                self.vel.x = 0.0
                self.pos.x = self.rect.x

    def _collide_y(self, platforms) -> None:
        for plat in platforms:
            # Горизонтальное перекрытие — общее условие для обоих направлений
            if not (self.rect.right > plat.rect.left
                    and self.rect.left < plat.rect.right):
                continue

            if (self.vel.y >= 0
                    and self.rect.bottom >= plat.rect.top
                    and self.rect.top < plat.rect.bottom):
                # Падение вниз: приземление на верх платформы
                self.rect.bottom = plat.rect.top
                self.on_ground   = True
                self.vel.y       = 0.0
                self.pos.y       = self.rect.y

            elif (self.vel.y < 0
                    and self.rect.top <= plat.rect.bottom
                    and self.rect.bottom > plat.rect.top):
                # Прыжок вверх: удар о нижнюю сторону платформы
                self.rect.top = plat.rect.bottom
                self.vel.y    = 0.0
                self.pos.y    = self.rect.y

    # ------------------------------------------------------------------ #
    #  Анимация                                                            #
    # ------------------------------------------------------------------ #

    def _update_animation(self, dt: float) -> None:
        if not self.on_ground:
            new_key = "jump" if self.vel.y < 0 else "fall"
        elif abs(self.vel.x) > 10:
            new_key = "run"
        else:
            new_key = "idle"

        if new_key != self._anim_key:
            self._anim_key = new_key
            self._anims[self._anim_key].reset()

        self._anims[self._anim_key].update(dt)
        frame = self._anims[self._anim_key].get_current_frame()

        if not self._facing_right:
            frame = pygame.transform.flip(frame, True, False)

        self.image = frame

    # ------------------------------------------------------------------ #

    @property
    def anim_state(self) -> str:
        return self._anim_key
