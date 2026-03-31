import math

import pygame

from src.states.base_state import BaseState
from src.settings import WIDTH, HEIGHT, WHITE, YELLOW, GRAY
from src.ui.button import Button


def _fmt(t: float) -> str:
    return f"{int(t)//60:02d}:{int(t)%60:02d}.{int((t%1)*100):02d}"


class WinState(BaseState):
    """Экран победы — появляется когда игрок достигает финальной платформы."""

    def __init__(self, game, score: int, total: int, elapsed: float):
        super().__init__(game)
        self._score   = score
        self._total   = total
        self._elapsed = elapsed
        self._time    = 0.0

    def on_enter(self) -> None:
        fb = pygame.font.SysFont("Arial", 28, bold=True)
        bw, bh = 220, 52
        mid = WIDTH // 2
        self._btn_again = Button(mid - bw - 16, HEIGHT // 2 + 110, bw, bh, "Play Again", fb)
        self._btn_menu  = Button(mid + 16,       HEIGHT // 2 + 110, bw, bh, "Main Menu",  fb)
        self._f_big  = pygame.font.SysFont("Arial", 78, bold=True)
        self._f_mid  = pygame.font.SysFont("Arial", 30)
        self._f_hint = pygame.font.SysFont("Arial", 20)

    def handle_events(self, events: list) -> None:
        for event in events:
            if self._btn_again.handle_event(event):
                self._replay()
                return
            if self._btn_menu.handle_event(event):
                self._to_menu()
                return
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    self._replay()
                elif event.key == pygame.K_ESCAPE:
                    self._to_menu()

    def update(self, dt: float) -> None:
        self._time += dt

    def _replay(self) -> None:
        from src.states.game_state import GameState
        self.game.change_state(GameState(self.game))

    def _to_menu(self) -> None:
        from src.states.menu_state import MenuState
        self.game.change_state(MenuState(self.game))

    def draw(self, screen: pygame.Surface) -> None:
        screen.fill((12, 22, 12))

        # Пульсирующий заголовок
        bob = math.sin(self._time * 3.0) * 5
        sh = self._f_big.render("YOU WIN!", True, (20, 80, 20))
        screen.blit(sh, sh.get_rect(center=(WIDTH // 2 + 3, int(HEIGHT // 2 - 110 + bob) + 3)))
        title = self._f_big.render("YOU WIN!", True, YELLOW)
        screen.blit(title, title.get_rect(center=(WIDTH // 2, int(HEIGHT // 2 - 110 + bob))))

        # Статистика
        all_done  = self._score == self._total
        coin_col  = (100, 255, 120) if all_done else (180, 220, 180)
        coin_val  = f"{self._score} / {self._total}" + ("  ✓ All!" if all_done else "")
        for i, (label, val, col) in enumerate([
            ("Coins",  coin_val,           coin_col),
            ("Time",   _fmt(self._elapsed), (180, 220, 180)),
        ]):
            line = self._f_mid.render(f"{label}:  {val}", True, col)
            screen.blit(line, line.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20 + i * 50)))

        self._btn_again.draw(screen)
        self._btn_menu.draw(screen)

        hint = self._f_hint.render("ENTER — Play Again   ESC — Menu", True, (80, 120, 80))
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT - 26)))
