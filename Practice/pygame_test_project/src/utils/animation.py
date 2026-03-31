import pygame


class Animation:
    """
    Контроллер покадровой анимации.

    Использование:
        anim = Animation(frames, frame_duration=0.08, loop=True)
        anim.update(dt)
        screen.blit(anim.get_current_frame(), rect)
    """

    def __init__(
        self,
        frames: list[pygame.Surface],
        frame_duration: float = 0.1,
        loop: bool = True,
    ):
        self.frames         = frames
        self.frame_duration = frame_duration
        self.loop           = loop

        self._index    = 0
        self._elapsed  = 0.0
        self.finished  = False   # True, если loop=False и дошли до конца

    def reset(self) -> None:
        self._index   = 0
        self._elapsed = 0.0
        self.finished = False

    def update(self, dt: float) -> None:
        if self.finished:
            return
        self._elapsed += dt
        while self._elapsed >= self.frame_duration:
            self._elapsed -= self.frame_duration
            self._index += 1
            if self._index >= len(self.frames):
                if self.loop:
                    self._index = 0
                else:
                    self._index = len(self.frames) - 1
                    self.finished = True
                    break

    def get_current_frame(self) -> pygame.Surface:
        return self.frames[self._index]
