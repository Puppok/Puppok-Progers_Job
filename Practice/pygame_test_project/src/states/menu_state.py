import math

import pygame

from src.states.base_state import BaseState
from src.settings import WIDTH, HEIGHT, WHITE, GRAY, DARK_GRAY, YELLOW
from src.ui.button import Button


class MenuState(BaseState):
    """
    Главное меню.
    Stage 8: параллакс-фон вместо статичного неба; автоскролл.
    """

    def on_enter(self) -> None:
        self._font_title = pygame.font.SysFont("Arial", 78, bold=True)
        self._font_sub   = pygame.font.SysFont("Arial", 28)
        self._font_hint  = pygame.font.SysFont("Arial", 20)
        self._time       = 0.0
        self._scroll     = 0.0   # виртуальная позиция камеры для параллакса

        bw, bh = 300, 58
        cx = WIDTH // 2 - bw // 2
        font_btn = pygame.font.SysFont("Arial", 30, bold=True)
        self._btn_play     = Button(cx, 370, bw, bh, "Play",     font_btn)
        self._btn_settings = Button(cx, 448, bw, bh, "Settings", font_btn)
        self._btn_quit     = Button(cx, 526, bw, bh, "Quit",     font_btn)

        self.game.sounds.start_music()

    def on_exit(self) -> None:
        self.game.sounds.stop_music()

    # ------------------------------------------------------------------ #

    def handle_events(self, events: list) -> None:
        for event in events:
            # Кнопки мышью
            if self._btn_play.handle_event(event):
                self._start_game()
            if self._btn_settings.handle_event(event):
                self._open_settings()
            if self._btn_quit.handle_event(event):
                self.game.running = False

            # Клавиатурные шорткаты
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    self._start_game()
                if event.key == pygame.K_ESCAPE:
                    self.game.running = False

    def _start_game(self) -> None:
        from src.states.game_state import GameState
        self.game.push_state(GameState(self.game))

    def _open_settings(self) -> None:
        from src.states.settings_state import SettingsState
        self.game.push_state(SettingsState(self.game))

    # ------------------------------------------------------------------ #

    def update(self, dt: float) -> None:
        self._time   += dt
        self._scroll += 40 * dt   # медленный автоскролл фона

    def draw(self, screen: pygame.Surface) -> None:
        # Параллакс-фон с автоскроллом
        self.game._bg.draw(screen, self._scroll)
        self._draw_ground_strip(screen)

        # Тень заголовка (глубина)
        bob = math.sin(self._time * 2.2) * 7
        ty  = int(220 + bob)
        shadow = self._font_title.render("PLATFORMER", True, (20, 40, 80))
        screen.blit(shadow, shadow.get_rect(center=(WIDTH // 2 + 3, ty + 3)))
        title  = self._font_title.render("PLATFORMER", True, YELLOW)
        screen.blit(title,  title.get_rect(center=(WIDTH // 2, ty)))

        # Подзаголовок
        sub = self._font_sub.render("Pygame 2D Platformer", True, WHITE)
        screen.blit(sub, sub.get_rect(center=(WIDTH // 2, ty + 62)))

        # Кнопки
        self._btn_play.draw(screen)
        self._btn_settings.draw(screen)
        self._btn_quit.draw(screen)

        # Подсказка снизу
        hint = self._font_hint.render(
            "ENTER — Play   ESC — Quit", True, GRAY
        )
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT - 28)))

    def _draw_ground_strip(self, screen: pygame.Surface) -> None:
        """Декоративная полоска земли внизу меню."""
        pygame.draw.rect(screen, (139, 90, 43), (0, HEIGHT - 50, WIDTH, 50))
        pygame.draw.rect(screen, (72, 160, 56),  (0, HEIGHT - 50, WIDTH, 8))
        pygame.draw.line(screen, (120, 210, 100), (0, HEIGHT - 50), (WIDTH - 1, HEIGHT - 50))
