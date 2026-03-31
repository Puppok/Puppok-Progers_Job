import pygame

from src.states.base_state import BaseState
from src.settings import WIDTH, HEIGHT, WHITE, GRAY, YELLOW
from src.ui.button import Button


class PauseState(BaseState):
    """
    Пауза поверх игры.
    Получает скриншот экрана в момент паузы → рисует его затемнённым.
    """

    def __init__(self, game, screenshot: pygame.Surface):
        super().__init__(game)
        self._screenshot = screenshot

    def on_enter(self) -> None:
        self._font_title = pygame.font.SysFont("Arial", 52, bold=True)
        self._font_hint  = pygame.font.SysFont("Arial", 20)

        # Затемнённый фон
        self._overlay = self._screenshot.copy()
        dim = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        dim.fill((0, 0, 0, 160))
        self._overlay.blit(dim, (0, 0))

        bw, bh = 260, 52
        cx = WIDTH // 2 - bw // 2
        font_btn = pygame.font.SysFont("Arial", 26, bold=True)

        self._btn_resume   = Button(cx, 310, bw, bh, "Resume",          font_btn)
        self._btn_settings = Button(cx, 378, bw, bh, "Settings",        font_btn)
        self._btn_menu     = Button(cx, 446, bw, bh, "Quit to Menu",    font_btn)

    # ------------------------------------------------------------------ #

    def handle_events(self, events: list) -> None:
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_p):
                    self.game.pop_state()
                    return

            if self._btn_resume.handle_event(event):
                self.game.pop_state()
                return

            if self._btn_settings.handle_event(event):
                from src.states.settings_state import SettingsState
                self.game.push_state(SettingsState(self.game))
                return

            if self._btn_menu.handle_event(event):
                from src.states.menu_state import MenuState
                self.game.change_state(MenuState(self.game))
                return

    # ------------------------------------------------------------------ #

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self._overlay, (0, 0))

        # Заголовок
        shadow = self._font_title.render("PAUSED", True, (20, 20, 40))
        title  = self._font_title.render("PAUSED", True, YELLOW)
        screen.blit(shadow, shadow.get_rect(center=(WIDTH // 2 + 3, 233)))
        screen.blit(title,  title.get_rect(center=(WIDTH // 2,     230)))

        self._btn_resume.draw(screen)
        self._btn_settings.draw(screen)
        self._btn_menu.draw(screen)

        hint = self._font_hint.render("P / ESC — resume", True, GRAY)
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT - 28)))
