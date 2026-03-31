"""
Звуковая система.

Все звуки генерируются процедурно при старте (numpy не нужен).
При отсутствии аудиоустройства автоматически деактивируется.

Звуки:
  jump  — восходящий свип 350 → 750 Гц, 0.14 с
  coin  — звонкий «динь» 880 Гц с экспоненциальным затуханием, 0.15 с
  land  — глухой удар 60 Гц, 0.12 с

Музыка:
  Ambient-петля 4 с (два слоистых тона 110 + 165 Гц), очень тихая.
"""

import math
import struct

import pygame


# ------------------------------------------------------------------ #
#  Генератор семплов                                                   #
# ------------------------------------------------------------------ #

def _make_sound(n: int, fn, vol: float = 0.45) -> pygame.mixer.Sound:
    """
    Создаёт стерео 16-bit Sound из n семплов.
    fn(i, n) → float в диапазоне [-1, 1]
    """
    buf = bytearray(n * 4)          # stereo 16-bit: 4 байта на фрейм
    for i in range(n):
        v = int(fn(i, n) * vol * 32767)
        v = max(-32768, min(32767, v))
        struct.pack_into('<hh', buf, i * 4, v, v)
    return pygame.mixer.Sound(buffer=bytes(buf))


# ------------------------------------------------------------------ #
#  SoundManager                                                        #
# ------------------------------------------------------------------ #

class SoundManager:
    _RATE = 44100

    def __init__(self):
        self._ok       = bool(pygame.mixer.get_init())
        self._sfx_vol  = 0.7
        self._music_vol = 0.5
        self._music_ch: pygame.mixer.Channel | None = None
        self._sfx: dict[str, pygame.mixer.Sound] = {}
        self._music: pygame.mixer.Sound | None = None

        if self._ok:
            self._build()

    # ------------------------------------------------------------------ #
    #  Генерация                                                           #
    # ------------------------------------------------------------------ #

    def _build(self) -> None:
        R = self._RATE

        # ── Jump: свип 350 → 750 Гц ────────────────────────────────
        def jump(i, n):
            t   = i / R
            prg = i / n
            env = (1.0 - prg) * min(1.0, 15 * t)
            return math.sin(2 * math.pi * (350 + 400 * prg) * t) * env

        # ── Coin: «динь» 880 Гц + гармоника ───────────────────────
        def coin(i, n):
            t   = i / R
            env = math.exp(-12 * t)
            return (math.sin(2 * math.pi * 880 * t) * 0.7
                  + math.sin(2 * math.pi * 1320 * t) * 0.3) * env

        # ── Land: низкий удар 60 Гц ────────────────────────────────
        def land(i, n):
            t   = i / R
            env = math.exp(-20 * t)
            return math.sin(2 * math.pi * 60 * t) * env

        # ── Ambient музыка: 4 с, два тона ─────────────────────────
        def music(i, n):
            t    = i / R
            fade = min(1.0, 8 * t, 8 * (4.0 - t))
            return (math.sin(2 * math.pi * 110 * t) * 0.55
                  + math.sin(2 * math.pi * 165 * t) * 0.35
                  + math.sin(2 * math.pi * 220 * t) * 0.10) * fade

        self._sfx['jump']  = _make_sound(int(R * 0.14), jump,  0.50)
        self._sfx['coin']  = _make_sound(int(R * 0.15), coin,  0.55)
        self._sfx['land']  = _make_sound(int(R * 0.12), land,  0.35)
        self._music        = _make_sound(int(R * 4.0),  music, 0.15)

    # ------------------------------------------------------------------ #
    #  API                                                                 #
    # ------------------------------------------------------------------ #

    def play(self, name: str) -> None:
        """Воспроизвести SFX по имени (не блокирует)."""
        if not self._ok or name not in self._sfx:
            return
        ch = self._sfx[name].play()
        if ch:
            ch.set_volume(self._sfx_vol)

    def start_music(self) -> None:
        if not self._ok or self._music is None:
            return
        if self._music_ch is None:
            self._music_ch = pygame.mixer.Channel(0)
        if not self._music_ch.get_busy():
            self._music_ch.play(self._music, loops=-1)
            self._music_ch.set_volume(self._music_vol)

    def stop_music(self) -> None:
        if self._music_ch and self._music_ch.get_busy():
            self._music_ch.stop()

    def set_sfx_volume(self, v: float) -> None:
        self._sfx_vol = max(0.0, min(1.0, v))

    def set_music_volume(self, v: float) -> None:
        self._music_vol = max(0.0, min(1.0, v))
        if self._music_ch:
            self._music_ch.set_volume(self._music_vol)
