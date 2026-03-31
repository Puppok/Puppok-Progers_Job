import pygame
import sys

from src.settings import (
    TITLE, FPS, WIDTH, HEIGHT,
    DEFAULT_SETTINGS,
)
from src.utils.sound_manager import SoundManager
from src.utils.parallax import ParallaxBackground
from src.utils.save_manager import load_settings, save_settings


class Game:
    """
    Главный класс приложения.

    Управляет:
    - инициализацией pygame и окном
    - стеком состояний (меню / настройки / геймплей)
    - главным циклом (events → update → draw)
    - хранением глобальных настроек
    """

    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        # Загружаем сохранённые настройки; используем дефолт если нет файла
        saved = load_settings()
        if saved:
            self.settings = saved
        else:
            self.settings = {
                "music_volume": DEFAULT_SETTINGS["music_volume"],
                "sfx_volume":   DEFAULT_SETTINGS["sfx_volume"],
                "fullscreen":   False,
                "controls":     dict(DEFAULT_SETTINGS["controls"]),
            }

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock   = pygame.time.Clock()
        self.running = True
        self.sounds  = SoundManager()

        # Общий параллакс-фон (создаём после set_mode — нужен Surface)
        self._bg = ParallaxBackground()

        # Стек состояний — импортируем здесь, чтобы избежать
        # циклических импортов на уровне модуля
        from src.states.menu_state import MenuState
        self._state_stack: list = []
        self.push_state(MenuState(self))

    # ------------------------------------------------------------------ #
    #  State Stack API                                                     #
    # ------------------------------------------------------------------ #

    def push_state(self, state) -> None:
        """Добавить новое состояние поверх стека (предыдущее засыпает)."""
        if self._state_stack:
            self._state_stack[-1].on_exit()
        self._state_stack.append(state)
        state.on_enter()

    def pop_state(self) -> None:
        """Убрать верхнее состояние и вернуться к предыдущему."""
        if self._state_stack:
            self._state_stack[-1].on_exit()
            self._state_stack.pop()
        if self._state_stack:
            self._state_stack[-1].on_resume()

    def change_state(self, state) -> None:
        """Очистить весь стек и перейти в новое состояние."""
        while self._state_stack:
            self._state_stack[-1].on_exit()
            self._state_stack.pop()
        self.push_state(state)

    # ------------------------------------------------------------------ #
    #  Helpers                                                             #
    # ------------------------------------------------------------------ #

    def apply_settings(self) -> None:
        """Применить текущие settings (fullscreen, громкость) и сохранить на диск."""
        flags = pygame.FULLSCREEN if self.settings.get("fullscreen") else 0
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), flags)
        self.sounds.set_music_volume(self.settings["music_volume"])
        self.sounds.set_sfx_volume(self.settings["sfx_volume"])
        save_settings(self.settings)

    # ------------------------------------------------------------------ #
    #  Main loop                                                           #
    # ------------------------------------------------------------------ #

    def run(self) -> None:
        while self.running:
            # delta time в секундах; cap 50 ms — защита от спайков при первом
            # кадре или после потери фокуса окна (иначе физика взрывается)
            dt = min(self.clock.tick(FPS) / 1000.0, 0.05)

            if not self._state_stack:
                break

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            state = self._state_stack[-1]
            state.handle_events(events)
            state.update(dt)
            state.draw(self.screen)

            pygame.display.flip()

        pygame.quit()
        sys.exit()
