class BaseState:
    """
    Абстрактный базовый класс для всех состояний игры.

    Дочерние классы переопределяют нужные методы.
    Ссылка self.game позволяет вызывать push/pop/change_state.
    """

    def __init__(self, game):
        self.game = game

    def on_enter(self) -> None:
        """Вызывается при переходе в это состояние (первый вход)."""
        pass

    def on_resume(self) -> None:
        """Вызывается когда дочернее состояние снято со стека и это стало активным.
        По умолчанию ведёт себя как on_enter; переопределите если нужно иначе."""
        self.on_enter()

    def on_exit(self) -> None:
        """Вызывается при выходе из этого состояния."""
        pass

    def handle_events(self, events: list) -> None:
        """Обработка pygame-событий."""
        pass

    def update(self, dt: float) -> None:
        """Обновление логики. dt — delta time в секундах."""
        pass

    def draw(self, screen) -> None:
        """Отрисовка состояния на экран."""
        pass
