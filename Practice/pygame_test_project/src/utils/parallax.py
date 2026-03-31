"""
Многослойный параллакс-фон.

Слои (от дальнего к ближнему):
  sky        factor=0.00  — статичный градиент неба
  clouds     factor=0.08  — размытые облака
  mountains  factor=0.12  — горы
  hills      factor=0.22  — холмы
  trees      factor=0.38  — деревья на переднем плане

Все поверхности генерируются процедурно с фиксированным seed.
"""

import math
import random

import pygame

from src.settings import WIDTH, HEIGHT, LEVEL_WIDTH


# ------------------------------------------------------------------ #
#  Ширина каждого тайлового слоя                                      #
# ------------------------------------------------------------------ #

_TILE_W = 1600   # слой рисуется кратно этой ширине и тайлится по X


# ------------------------------------------------------------------ #
#  Генераторы поверхностей                                             #
# ------------------------------------------------------------------ #

def _make_sky_surf() -> pygame.Surface:
    """Вертикальный градиент — рассвет/день."""
    surf = pygame.Surface((WIDTH, HEIGHT))
    for i in range(HEIGHT):
        t = i / HEIGHT
        r = int(80  + t * 55)
        g = int(160 + t * 35)
        b = int(235 - t * 55)
        pygame.draw.line(surf, (r, g, b), (0, i), (WIDTH - 1, i))
    return surf


def _make_clouds_surf(rng: random.Random) -> pygame.Surface:
    """Мягкие облака на прозрачном фоне."""
    surf = pygame.Surface((_TILE_W, HEIGHT), pygame.SRCALPHA)
    for _ in range(18):
        cx  = rng.randint(0, _TILE_W)
        cy  = rng.randint(30, 200)
        w   = rng.randint(110, 260)
        h   = rng.randint(40, 72)
        col = (245, 245, 255, rng.randint(140, 210))
        pygame.draw.ellipse(surf, col, (cx,         cy,        w,          h         ))
        pygame.draw.ellipse(surf, col, (cx + w//4,  cy - h//3, int(w*.60), int(h*.75)))
        pygame.draw.ellipse(surf, col, (cx + w//2,  cy + 4,    int(w*.50), int(h*.65)))
    return surf


def _make_mountains_surf(rng: random.Random) -> pygame.Surface:
    """Силуэты дальних гор."""
    surf = pygame.Surface((_TILE_W, HEIGHT), pygame.SRCALPHA)
    sky_bottom = HEIGHT - 50   # уровень земли примерно

    # Большие горы
    x = 0
    while x < _TILE_W + 200:
        peak_h = rng.randint(120, 280)
        w      = rng.randint(220, 420)
        poly = [
            (x - w // 2, sky_bottom),
            (x,          sky_bottom - peak_h),
            (x + w // 2, sky_bottom),
        ]
        col = (100 + rng.randint(-15, 15),
               120 + rng.randint(-15, 15),
               160 + rng.randint(-15, 15),
               180)
        pygame.draw.polygon(surf, col, poly)
        # снеговая шапка
        cap_h = int(peak_h * 0.25)
        snow = [
            (x - cap_h // 2, sky_bottom - peak_h + cap_h),
            (x,              sky_bottom - peak_h),
            (x + cap_h // 2, sky_bottom - peak_h + cap_h),
        ]
        pygame.draw.polygon(surf, (240, 245, 255, 200), snow)
        x += rng.randint(160, 320)
    return surf


def _make_hills_surf(rng: random.Random) -> pygame.Surface:
    """Мягкие зелёные холмы."""
    surf = pygame.Surface((_TILE_W, HEIGHT), pygame.SRCALPHA)
    sky_bottom = HEIGHT - 50

    x = -60
    while x < _TILE_W + 200:
        r = rng.randint(90, 160)
        cx = x + r
        col = (55 + rng.randint(-10, 20),
               130 + rng.randint(-15, 20),
               55  + rng.randint(-10, 20),
               210)
        pygame.draw.ellipse(surf, col,
                            (cx - r, sky_bottom - int(r * 0.65), r * 2, int(r * 1.3)))
        x += rng.randint(100, 220)
    return surf


def _make_trees_surf(rng: random.Random) -> pygame.Surface:
    """Силуэты деревьев."""
    surf = pygame.Surface((_TILE_W, HEIGHT), pygame.SRCALPHA)
    sky_bottom = HEIGHT - 50

    x = rng.randint(20, 80)
    while x < _TILE_W:
        h    = rng.randint(60, 120)
        tw   = rng.randint(30, 55)
        trunk_w = max(5, tw // 6)
        trunk_h = h // 3
        col = (30 + rng.randint(-10, 10),
               80 + rng.randint(-10, 20),
               30 + rng.randint(-10, 10),
               230)
        trunk_col = (60, 35, 15, 230)
        # ствол
        pygame.draw.rect(surf, trunk_col,
                         (x - trunk_w//2, sky_bottom - trunk_h, trunk_w, trunk_h))
        # крона (треугольник + круг)
        top_y = sky_bottom - h
        pygame.draw.polygon(surf, col, [
            (x,          top_y),
            (x - tw//2,  sky_bottom - trunk_h),
            (x + tw//2,  sky_bottom - trunk_h),
        ])
        pygame.draw.circle(surf, col, (x, top_y + h//6), tw//3)
        x += rng.randint(40, 120)
    return surf


# ------------------------------------------------------------------ #
#  Слой                                                                #
# ------------------------------------------------------------------ #

class ParallaxLayer:
    """Один тайлящийся слой параллакса."""

    def __init__(self, surf: pygame.Surface, factor: float) -> None:
        self._surf   = surf
        self._factor = factor   # 0 = статичный, 1 = двигается вместе с камерой
        self._w      = surf.get_width()

    def draw(self, screen: pygame.Surface, camera_x: float) -> None:
        if self._w == 0:
            return
        scroll = int(camera_x * self._factor)
        # стартовая позиция с учётом тайлинга
        start_x = -(scroll % self._w)
        x = start_x
        while x < WIDTH:
            screen.blit(self._surf, (x, 0))
            x += self._w


# ------------------------------------------------------------------ #
#  Фон целиком                                                         #
# ------------------------------------------------------------------ #

class ParallaxBackground:
    """
    Создаёт и хранит все слои.
    Вызов draw() каждый кадр.
    """

    def __init__(self) -> None:
        rng = random.Random(7)          # фиксированный seed → одинаковый фон

        sky_surf = _make_sky_surf()     # тайлится по WIDTH, не по _TILE_W
        self._layers: list[ParallaxLayer] = [
            ParallaxLayer(sky_surf,                  0.00),
            ParallaxLayer(_make_clouds_surf(rng),    0.08),
            ParallaxLayer(_make_mountains_surf(rng), 0.12),
            ParallaxLayer(_make_hills_surf(rng),     0.22),
            ParallaxLayer(_make_trees_surf(rng),     0.38),
        ]

    def draw(self, screen: pygame.Surface, camera_x: float) -> None:
        for layer in self._layers:
            layer.draw(screen, camera_x)
