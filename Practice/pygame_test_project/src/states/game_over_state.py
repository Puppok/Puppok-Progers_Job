import pygame

from src.states.base_state import BaseState
from src.settings import WIDTH, HEIGHT, WHITE, YELLOW, GRAY
from src.ui.button import Button


def _fmt(t: float) -> str:
    return f"{int(t)//60:02d}:{int(t)%60:02d}.{int((t%1)*100):02d}"


class GameOverState(BaseState):
    """Экран Game Over — поверх стека после потери всех жизней."""

    def __init__(self, game, score: int, total: int, elapsed: float):
        super().__init__(game)
        self._score   = score
        self._total   = total
        self._elapsed = elapsed

    def on_enter(self) -> None:
        fb = pygame.font.SysFont("Arial", 28, bold=True)
        bw, bh = 220, 52
        mid = WIDTH // 2
        self._btn_retry = Button(mid - bw - 16, HEIGHT // 2 + 90, bw, bh, "Retry",     fb)
        self._btn_menu  = Button(mid + 16,       HEIGHT // 2 + 90, bw, bh, "Main Menu", fb)
        self._f_big  = pygame.font.SysFont("Arial", 72, bold=True)
        self._f_mid  = pygame.font.SysFont("Arial", 30)
        self._f_hint = pygame.font.SysFont("Arial", 20)

    def handle_events(self, events: list) -> None:
        for event in events:
            if self._btn_retry.handle_event(event):
                self._retry()
                return
            if self._btn_menu.handle_event(event):
                self._to_menu()
                return
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    self._retry()
                elif event.key == pygame.K_ESCAPE:
                    self._to_menu()

    def _retry(self) -> None:
        from src.states.game_state import GameState
        self.game.change_state(GameState(self.game))

    def _to_menu(self) -> None:
        from src.states.menu_state import MenuState
        self.game.change_state(MenuState(self.game))

    def draw(self, screen: pygame.Surface) -> None:
        screen.fill((28, 8, 8))

        # Заголовок с тенью
        sh = self._f_big.render("GAME OVER", True, (70, 15, 15))
        screen.blit(sh, sh.get_rect(center=(WIDTH // 2 + 3, HEIGHT // 2 - 95 + 3)))
        title = self._f_big.render("GAME OVER", True, (215, 55, 55))
        screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 95)))

        # Статистика
        for i, (label, val, col) in enumerate([
            ("Coins",  f"{self._score} / {self._total}", (190, 130, 130)),
            ("Time",   _fmt(self._elapsed),              (190, 130, 130)),
        ]):
            line = self._f_mid.render(f"{label}:  {val}", True, col)
            screen.blit(line, line.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 10 + i * 46)))

        self._btn_retry.draw(screen)
        self._btn_menu.draw(screen)

        hint = self._f_hint.render("ENTER — Retry   ESC — Menu", True, (100, 60, 60))
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT - 26)))
