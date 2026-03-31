import pygame

from src.states.base_state import BaseState

# Человекочитаемые имена для SDL2 scan-кодов (значения event.scancode).
# Хардкод SDL2-констант — не зависит от версии pygame и раскладки клавиатуры.
_KSCAN_NAMES: dict[int, str] = {
     4: "A",   5: "B",   6: "C",   7: "D",   8: "E",   9: "F",  10: "G",
    11: "H",  12: "I",  13: "J",  14: "K",  15: "L",  16: "M",  17: "N",
    18: "O",  19: "P",  20: "Q",  21: "R",  22: "S",  23: "T",  24: "U",
    25: "V",  26: "W",  27: "X",  28: "Y",  29: "Z",
    44: "SPACE", 40: "ENTER",
    79: "RIGHT", 80: "LEFT", 81: "DOWN", 82: "UP",
    225: "LSHIFT", 229: "RSHIFT", 224: "LCTRL", 228: "RCTRL",
}
from src.settings import WIDTH, HEIGHT, WHITE, GRAY, DARK_GRAY, YELLOW
from src.ui.button import Button
from src.ui.slider import Slider
from src.utils.save_manager import save_settings


# Позиции элементов
_LX  = 100    # x меток (левая колонка)
_CX  = 480    # x контролов (правая колонка)
_VX  = 800    # x значений (слайдеры)
_SLW = 300    # ширина слайдера


class SettingsState(BaseState):
    """
    Экран настроек.
    Разделы: Sound · Display · Controls
    """

    def on_enter(self) -> None:
        self._f_title  = pygame.font.SysFont("Arial", 36, bold=True)
        self._f_sect   = pygame.font.SysFont("Arial", 22, bold=True)
        self._f_label  = pygame.font.SysFont("Arial", 22)
        self._f_small  = pygame.font.SysFont("Arial", 18)

        s = self.game.settings

        # Сохраняем оригинальные значения для возможной отмены
        self._orig_music_vol = s["music_volume"]
        self._orig_sfx_vol   = s["sfx_volume"]

        # ── Sound ──────────────────────────────────────────────────
        self._sl_music = Slider(_CX, 136, _SLW, value=s["music_volume"])
        self._sl_sfx   = Slider(_CX, 184, _SLW, value=s["sfx_volume"])

        # ── Display ────────────────────────────────────────────────
        self._fullscreen = s.get("fullscreen", False)

        # ── Controls ───────────────────────────────────────────────
        self._controls  = dict(s["controls"])   # рабочая копия
        self._rebinding = None                  # action ожидающий клавишу

        _rb_font = pygame.font.SysFont("Arial", 20, bold=True)
        self._rbind_btns: dict[str, Button] = {
            "left":  Button(_CX, 362, 190, 36, self._key_label("left"),  _rb_font),
            "right": Button(_CX, 408, 190, 36, self._key_label("right"), _rb_font),
            "jump":  Button(_CX, 454, 190, 36, self._key_label("jump"),  _rb_font),
        }

        # ── Footer ─────────────────────────────────────────────────
        _f_btn = pygame.font.SysFont("Arial", 24, bold=True)
        self._btn_back  = Button(100,       HEIGHT - 72, 160, 46, "Back",  _f_btn)
        self._btn_apply = Button(WIDTH - 260, HEIGHT - 72, 160, 46, "Apply", _f_btn)

    # ------------------------------------------------------------------ #
    #  Helpers                                                             #
    # ------------------------------------------------------------------ #

    def _key_label(self, action: str) -> str:
        code = self._controls[action]
        return _KSCAN_NAMES.get(code, f"SC:{code}")

    def _toggle_fullscreen(self) -> None:
        self._fullscreen = not self._fullscreen

    def _cancel(self) -> None:
        """Отмена без сохранения — восстанавливаем громкость как было."""
        self.game.sounds.set_music_volume(self._orig_music_vol)
        self.game.sounds.set_sfx_volume(self._orig_sfx_vol)
        self.game.pop_state()

    def _apply(self) -> None:
        s = self.game.settings
        s["music_volume"] = self._sl_music.get_value()
        s["sfx_volume"]   = self._sl_sfx.get_value()
        s["fullscreen"]   = self._fullscreen
        s["controls"]     = self._controls
        self.game.apply_settings()   # внутри вызывает save_settings()

    # ------------------------------------------------------------------ #
    #  Events                                                              #
    # ------------------------------------------------------------------ #

    def handle_events(self, events: list) -> None:
        for event in events:

            # Перехватить нажатие клавиши при rebinding
            if self._rebinding and event.type == pygame.KEYDOWN:
                if event.scancode != 41:   # не ESC
                    self._controls[self._rebinding] = event.scancode
                    self._rbind_btns[self._rebinding].set_text(
                        self._key_label(self._rebinding)
                    )
                self._rebinding = None
                continue

            if event.type == pygame.KEYDOWN and event.scancode == 41:   # ESC
                self._cancel()
                return

            # Слайдеры — обновляют громкость в реальном времени
            self._sl_music.handle_event(event)
            self._sl_sfx.handle_event(event)
            self.game.sounds.set_music_volume(self._sl_music.get_value())
            self.game.sounds.set_sfx_volume(self._sl_sfx.get_value())

            # Rebind buttons
            for action, btn in self._rbind_btns.items():
                if btn.handle_event(event):
                    self._rebinding = action

            # Fullscreen toggle (два прямоугольника, обрабатываем вручную)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i, fs_val in enumerate([False, True]):
                    r = pygame.Rect(_CX + i * 210, 266, 195, 36)
                    if r.collidepoint(event.pos):
                        self._fullscreen = fs_val

            # Footer buttons
            if self._btn_back.handle_event(event):
                self._cancel()
                return
            if self._btn_apply.handle_event(event):
                self._apply()
                self.game.pop_state()
                return

    # ------------------------------------------------------------------ #
    #  Draw                                                                #
    # ------------------------------------------------------------------ #

    def draw(self, screen: pygame.Surface) -> None:
        screen.fill((25, 30, 45))

        # Заголовок
        t = self._f_title.render("SETTINGS", True, WHITE)
        screen.blit(t, t.get_rect(center=(WIDTH // 2, 46)))

        self._draw_sound_section(screen)
        self._draw_display_section(screen)
        self._draw_controls_section(screen)

        # Footer
        pygame.draw.line(screen, (60, 65, 80), (60, HEIGHT - 86), (WIDTH - 60, HEIGHT - 86))
        self._btn_back.draw(screen)
        self._btn_apply.draw(screen)

        hint = self._f_small.render("ESC — cancel without saving", True, GRAY)
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT - 20)))

    # ── SOUND ──────────────────────────────────────────────────────────

    def _draw_sound_section(self, screen: pygame.Surface) -> None:
        self._sect_header(screen, "SOUND", 100)

        # Music
        self._draw_label(screen, "Music Volume", _LX, 140)
        self._sl_music.draw(screen)
        pct = int(self._sl_music.get_value() * 100)
        self._draw_value(screen, f"{pct}%", _VX, 140)

        # SFX
        self._draw_label(screen, "SFX Volume", _LX, 188)
        self._sl_sfx.draw(screen)
        pct = int(self._sl_sfx.get_value() * 100)
        self._draw_value(screen, f"{pct}%", _VX, 188)

    # ── DISPLAY ────────────────────────────────────────────────────────

    def _draw_display_section(self, screen: pygame.Surface) -> None:
        self._sect_header(screen, "DISPLAY", 240)
        self._draw_label(screen, "Window Mode", _LX, 270)

        for i, (label, is_fs) in enumerate([("Windowed", False), ("Fullscreen", True)]):
            r     = pygame.Rect(_CX + i * 210, 266, 195, 36)
            active = (self._fullscreen == is_fs)
            bg     = (50, 80, 130) if active else DARK_GRAY
            border = YELLOW if active else WHITE
            pygame.draw.rect(screen, bg,     r, border_radius=6)
            pygame.draw.rect(screen, border, r, 2, border_radius=6)
            lbl = self._f_label.render(label, True, YELLOW if active else WHITE)
            screen.blit(lbl, lbl.get_rect(center=r.center))

    # ── CONTROLS ───────────────────────────────────────────────────────

    def _draw_controls_section(self, screen: pygame.Surface) -> None:
        self._sect_header(screen, "CONTROLS", 330)

        rows = [
            ("left",  "Move Left",  _LX, 366),
            ("right", "Move Right", _LX, 412),
            ("jump",  "Jump",       _LX, 458),
        ]
        for action, label, lx, ly in rows:
            self._draw_label(screen, label, lx, ly)
            btn = self._rbind_btns[action]

            # Особый вид когда ожидаем нажатие
            if self._rebinding == action:
                pygame.draw.rect(screen, (60, 50, 15), btn.rect, border_radius=6)
                pygame.draw.rect(screen, YELLOW,       btn.rect, 2, border_radius=6)
                wait = self._f_small.render("▶ Press a key…", True, YELLOW)
                screen.blit(wait, wait.get_rect(center=btn.rect.center))
            else:
                btn.draw(screen)

    # ── Helpers ────────────────────────────────────────────────────────

    def _sect_header(self, screen: pygame.Surface, text: str, y: int) -> None:
        lbl = self._f_sect.render(f"▸  {text}", True, (130, 180, 255))
        screen.blit(lbl, (_LX, y))
        pygame.draw.line(screen, (60, 65, 80),
                         (_LX, y + 28), (WIDTH - _LX, y + 28))

    def _draw_label(self, screen: pygame.Surface, text: str, x: int, y: int) -> None:
        lbl = self._f_label.render(text, True, GRAY)
        screen.blit(lbl, (x, y))

    def _draw_value(self, screen: pygame.Surface, text: str, x: int, y: int) -> None:
        val = self._f_label.render(text, True, WHITE)
        screen.blit(val, (x, y))
