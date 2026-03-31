import math
import random

import pygame

from src.states.base_state import BaseState
from src.settings import (
    WIDTH, HEIGHT,
    LEVEL_WIDTH, LEVEL_HEIGHT,
    LIVES,
    DARK_GRAY, WHITE, YELLOW,
    PLAYER_FRAME_H,
)
from src.entities.player   import Player
from src.entities.platform import Platform
from src.entities.coin     import Coin, build_coin_frames
from src.utils.camera      import Camera
from src.utils.animation   import Animation


# ------------------------------------------------------------------ #
#  Утилиты                                                             #
# ------------------------------------------------------------------ #

def _fmt_time(t: float) -> str:
    return f"{int(t)//60:02d}:{int(t)%60:02d}.{int((t%1)*100):02d}"


def _draw_heart(screen: pygame.Surface, cx: int, cy: int,
                size: int = 14, color: tuple = (210, 50, 65)) -> None:
    r = max(2, int(size * 0.34))
    pygame.draw.circle(screen, color, (cx - r + 1, cy),     r)
    pygame.draw.circle(screen, color, (cx + r - 1, cy),     r)
    pygame.draw.polygon(screen, color, [
        (cx - size // 2,     cy + 1),
        (cx + size // 2,     cy + 1),
        (cx,                 cy + size // 2 + 2),
    ])


# ------------------------------------------------------------------ #
#  Данные уровня  (x, y, width, height, kind)                         #
# ------------------------------------------------------------------ #

_G = HEIGHT - 40

_LEVEL: list[tuple] = [
    # ── Земля ──────────────────────────────────────────────────────
    (0,    _G,  LEVEL_WIDTH, 40, "stone"),

    # ── Зона 1 ─────────────────────────────────────────────────────
    (60,   560, 220, 18, "grass"),
    (360,  568, 185, 18, "grass"),
    (630,  555, 200, 18, "grass"),
    (910,  563, 175, 18, "grass"),
    (1120, 558, 210, 18, "grass"),

    (150,  430, 195, 18, "grass"),
    (450,  422, 180, 18, "grass"),
    (720,  435, 190, 18, "grass"),
    (980,  428, 185, 18, "grass"),

    (80,   300, 170, 18, "stone"),
    (330,  292, 180, 18, "stone"),
    (590,  305, 165, 18, "stone"),
    (850,  298, 180, 18, "stone"),
    (1080, 302, 170, 18, "stone"),

    # ── Зона 2 ─────────────────────────────────────────────────────
    (1380, 558, 165, 18, "grass"),
    (1630, 568, 150, 18, "grass"),
    (1880, 552, 170, 18, "grass"),
    (2090, 562, 155, 18, "grass"),
    (2320, 555, 165, 18, "grass"),
    (2490, 560, 160, 18, "grass"),

    (1460, 428, 160, 18, "grass"),
    (1710, 418, 155, 18, "grass"),
    (1950, 430, 170, 18, "stone"),
    (2180, 422, 160, 18, "grass"),
    (2400, 432, 155, 18, "stone"),

    (1360, 298, 155, 18, "stone"),
    (1620, 288, 160, 18, "stone"),
    (1870, 302, 150, 18, "stone"),
    (2110, 292, 158, 18, "stone"),
    (2360, 300, 155, 18, "stone"),

    # ── Зона 3 ─────────────────────────────────────────────────────
    (2620, 548, 135, 18, "stone"),
    (2860, 560, 120, 18, "stone"),
    (3080, 545, 135, 18, "stone"),
    (3290, 555, 120, 18, "stone"),
    (3510, 548, 140, 18, "stone"),
    (3720, 555, 120, 18, "stone"),

    (2700, 420, 130, 18, "stone"),
    (2930, 410, 125, 18, "stone"),
    (3150, 425, 130, 18, "stone"),
    (3380, 415, 125, 18, "stone"),
    (3600, 420, 130, 18, "stone"),

    (2640, 292, 125, 18, "stone"),
    (2870, 282, 120, 18, "stone"),
    (3090, 296, 130, 18, "stone"),
    (3310, 285, 120, 18, "stone"),
    (3540, 292, 120, 18, "stone"),

    # Финальная платформа — цель
    (3720, 220, 100, 18, "stone"),
]

_SPAWN_X = 120
_SPAWN_Y = _G - PLAYER_FRAME_H


def _generate_coin_positions() -> list[tuple[int, int]]:
    positions = []
    for x, y, w, h, _ in _LEVEL:
        if w > 400:
            continue
        count = max(2, min(4, w // 55))
        step  = w // (count + 1)
        for i in range(1, count + 1):
            positions.append((x + step * i, y - 28))
    return positions


# ------------------------------------------------------------------ #
#  State                                                               #
# ------------------------------------------------------------------ #

class GameState(BaseState):

    def on_enter(self) -> None:
        self._font_hud   = pygame.font.SysFont("Arial", 20)
        self._font_score = pygame.font.SysFont("Arial", 26, bold=True)
        self._font_time  = pygame.font.SysFont("Arial", 22, bold=True)
        self.camera      = Camera(LEVEL_WIDTH, LEVEL_HEIGHT)
        self._coin_icon  = Animation(build_coin_frames(), frame_duration=0.08)
        self._debug      = False
        self._lives      = LIVES
        self._pending_pause = False
        self._setup_level()

    def on_resume(self) -> None:
        """Возврат из паузы/настроек — уровень не сбрасываем."""
        self._pressed_scans.clear()   # клавиши могли отпустить пока был pause

    def _setup_level(self) -> None:
        self.platforms = pygame.sprite.Group()
        for x, y, w, h, kind in _LEVEL:
            self.platforms.add(Platform(x, y, w, h, kind))

        self.coins        = pygame.sprite.Group()
        for cx, cy in _generate_coin_positions():
            self.coins.add(Coin(cx, cy))

        self._score         = 0
        self._total_coins   = len(self.coins)
        self._elapsed       = 0.0
        self._particles: list = []
        self._state_pushed  = False
        self._pending_pause = False
        self._pressed_scans: set = set()   # физические scan-коды зажатых клавиш

        self.player = Player(_SPAWN_X, _SPAWN_Y)
        self.camera.reset()

    # ------------------------------------------------------------------ #
    #  Events                                                              #
    # ------------------------------------------------------------------ #

    def handle_events(self, events: list) -> None:
        for event in events:
            # Трекаем физические scan-коды для layout-независимого ввода
            if event.type == pygame.KEYDOWN:
                self._pressed_scans.add(event.scancode)
            elif event.type == pygame.KEYUP:
                self._pressed_scans.discard(event.scancode)

            if event.type == pygame.KEYDOWN:
                sc = event.scancode
                if sc == 41:   # ESC
                    self.game.pop_state()
                    return   # прекратить обработку: стек уже изменился
                if sc == 21:   # R
                    self._lives = LIVES
                    self._setup_level()
                if sc == 43:   # Tab
                    self._debug = not self._debug
                if sc == 19:   # P
                    self._pending_pause = True

    # ------------------------------------------------------------------ #
    #  Update                                                              #
    # ------------------------------------------------------------------ #

    def update(self, dt: float) -> None:
        if self._state_pushed or self._pending_pause:
            return

        self._elapsed += dt

        # Ввод и физика
        self.player.just_jumped = False
        self.player.handle_input(self._pressed_scans, self.game.settings["controls"])
        self.player.update(dt, self.platforms)
        self.camera.update(self.player, dt)

        # Звуки движения
        if self.player.just_jumped:
            self.game.sounds.play('jump')
        if self.player.just_landed:
            self.game.sounds.play('land')

        # Монеты
        self.coins.update(dt)
        collected = pygame.sprite.spritecollide(self.player, self.coins, True)
        if collected:
            self._score += len(collected)
            self.game.sounds.play('coin')
            self._emit_particles(collected)

        # Иконка монеты
        self._coin_icon.update(dt)

        # Частицы
        self._update_particles(dt)

        # Падение
        if self.player.rect.top > HEIGHT + 50:
            self._lives -= 1
            if self._lives <= 0:
                self._push_game_over()
            else:
                self.player = Player(_SPAWN_X, _SPAWN_Y)
                self.camera.reset()
            return

        # Победа: финальная платформа (3720, 220)
        if (self.player.on_ground
                and self.player.rect.centerx > 3700
                and self.player.rect.bottom <= 222):
            self._push_win()

    def _push_game_over(self) -> None:
        self._state_pushed = True
        from src.states.game_over_state import GameOverState
        self.game.push_state(
            GameOverState(self.game, self._score, self._total_coins, self._elapsed)
        )

    def _push_win(self) -> None:
        self._state_pushed = True
        from src.states.win_state import WinState
        self.game.push_state(
            WinState(self.game, self._score, self._total_coins, self._elapsed)
        )

    # ------------------------------------------------------------------ #
    #  Particles                                                           #
    # ------------------------------------------------------------------ #

    def _emit_particles(self, sprites) -> None:
        for sp in sprites:
            for _ in range(10):
                angle = random.uniform(0, math.tau)
                speed = random.uniform(60, 200)
                self._particles.append([
                    float(sp.rect.centerx),
                    float(sp.rect.centery),
                    math.cos(angle) * speed,
                    math.sin(angle) * speed,
                    random.uniform(0.30, 0.55),   # lifetime
                    0.0,                           # age
                    (255, random.randint(155, 210), random.randint(0, 40)),
                ])

    def _update_particles(self, dt: float) -> None:
        live = []
        for p in self._particles:
            p[5] += dt
            if p[5] < p[4]:
                p[0] += p[2] * dt
                p[1] += p[3] * dt
                p[3] += 280 * dt   # гравитация
                live.append(p)
        self._particles = live

    def _draw_particles(self, screen: pygame.Surface) -> None:
        for p in self._particles:
            alpha = 1.0 - p[5] / p[4]
            size  = max(1, int(5 * alpha))
            sx = int(p[0] - self.camera.offset.x)
            sy = int(p[1] - self.camera.offset.y)
            pygame.draw.circle(screen, p[6], (sx, sy), size)

    # ------------------------------------------------------------------ #
    #  Draw                                                                #
    # ------------------------------------------------------------------ #

    def draw(self, screen: pygame.Surface) -> None:
        self.game._bg.draw(screen, self.camera.offset.x)

        for plat in self.platforms:
            screen.blit(plat.image, self.camera.apply(plat))

        for coin in self.coins:
            screen.blit(coin.image, self.camera.apply(coin))

        self._draw_particles(screen)

        screen.blit(self.player.image, self.camera.apply(self.player))

        # HUD
        self._draw_score_panel(screen)
        self._draw_timer(screen)
        self._draw_lives(screen)
        self._draw_progress(screen)

        if self._debug:
            self._draw_debug(screen)
        else:
            self._draw_hints(screen)

        # Пауза — открываем после отрисовки, чтобы был скриншот
        if self._pending_pause:
            self._pending_pause = False
            from src.states.pause_state import PauseState
            self.game.push_state(PauseState(self.game, screen.copy()))

    # ── HUD helpers ────────────────────────────────────────────────────

    def _draw_score_panel(self, screen: pygame.Surface) -> None:
        panel = pygame.Surface((190, 40), pygame.SRCALPHA)
        panel.fill((0, 0, 0, 130))
        screen.blit(panel, (WIDTH - 200, 6))
        screen.blit(self._coin_icon.get_current_frame(), (WIDTH - 192, 15))
        all_done = (self._score == self._total_coins)
        color = (100, 255, 120) if all_done else YELLOW
        text  = self._font_score.render(
            f"× {self._score} / {self._total_coins}", True, color)
        screen.blit(text, (WIDTH - 166, 13))

    def _draw_timer(self, screen: pygame.Surface) -> None:
        surf = self._font_time.render(_fmt_time(self._elapsed), True, WHITE)
        screen.blit(surf, (10, 10))

    def _draw_lives(self, screen: pygame.Surface) -> None:
        for i in range(self._lives):
            _draw_heart(screen, 18 + i * 26, HEIGHT - 28)

    def _draw_progress(self, screen: pygame.Surface) -> None:
        ratio = min(1.0, self.player.rect.centerx / LEVEL_WIDTH)
        pygame.draw.rect(screen, (30, 30, 30),   (0, HEIGHT - 8, WIDTH, 8))
        pygame.draw.rect(screen, (80, 200, 110), (0, HEIGHT - 8, int(WIDTH * ratio), 8))
        mx = int(WIDTH * ratio)
        pygame.draw.rect(screen, YELLOW,         (mx - 2, HEIGHT - 10, 4, 10))

    def _draw_debug(self, screen: pygame.Surface) -> None:
        lines = [
            f"state  : {self.player.anim_state}",
            f"vel    : ({self.player.vel.x:+.0f}, {self.player.vel.y:+.0f})",
            f"pos    : {self.player.rect.x} / {LEVEL_WIDTH}",
            f"cam    : {int(self.camera.offset.x)}",
            f"parts  : {len(self._particles)}",
            "",
            "Tab — hide debug   R — restart   ESC — menu",
        ]
        for i, line in enumerate(lines):
            color = YELLOW if i == 0 else WHITE if i < 5 else DARK_GRAY
            surf = self._font_hud.render(line, True, color)
            screen.blit(surf, (10, 38 + i * 22))

    def _draw_hints(self, screen: pygame.Surface) -> None:
        hint = self._font_hud.render(
            "A/D — move   SPACE — jump   P — pause   R — restart   Tab — debug   ESC — menu",
            True, DARK_GRAY,
        )
        screen.blit(hint, (10, 38))
