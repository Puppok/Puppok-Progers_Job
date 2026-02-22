import pygame as pg

class AnimatedCircleSprite(pg.sprite.Sprite):
    def __init__(self, coord_x, coord_y, frames, frame_duration):
        super().__init__()

        self.frames = frames # массив кадров
        self.current_frame = 0 # индекс текущего кадра
        self.frame_duration = frame_duration # длительность кадра
        self.frame_timer = 0 # таймер

        self.image = self.frames[self.current_frame] # картинка для отрисовки
        self.rect = self.image.get_rect() # достаем хит бокс
        self.rect.x = coord_x # задаем координату x и y
        self.rect.y = coord_y

    def update(self, dt):
        self.frame_timer += dt

        if self.frame_timer >= self.frame_duration:
            self.frame_timer = 0
            self.current_frame = ((self.current_frame + 1) % len(self.frames))
            self.image = self.frames[self.current_frame]

pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Анимации спрайтов')
clock = pg.time.Clock()

# Анимация спрайта (квадратик)
square_frames = []
for i in range(6):
    frame = pg.Surface((200, 200)) # создаем кадр (квадрат)
    color = (255, 50 * i, 0)       # создаем меняющийся цвет
    frame.fill(color)              # закрашиваем квадрат цветом
    square_frames.append(frame)    # добавляем кадр в массив

current_frame = 0     # индекс текущего кадра
frame_timer = 0       # счетчик кадров (сек)
frame_duration = 0.2  # время отрисовки кадра на экране
# -------------------------------

# Анимация класса (круг)
animated_circle_frames = []
for i in range(6):
    frame = pg.Surface((100, 100))
    frame.fill((255, 255, 255))
    frame.set_colorkey((255, 255, 255))

    radius = 15 + i * 5
    pg.draw.circle(frame, (255, 215, 0), (50, 50), radius)
    animated_circle_frames.append(frame)

circle_sprites = pg.sprite.Group()
for i in range(3):
    sprite = AnimatedCircleSprite(200 + i * 200, 270, animated_circle_frames, 0.1)
    circle_sprites.add(sprite)
#--------------------------

# === Работа со спрайт листом ===
spritesheet = pg.image.load('spritesheet.png').convert_alpha()

def get_frames(sheet, frame_width, frame_height, count):
    frames = []
    for i in range(count):
        rect = pg.Rect(i * frame_width, 0, frame_width, frame_height)
        frame = sheet.subsurface(rect) # вырезать область из картинки
        frames.append(frame)

    return frames

spritesheet_frames = get_frames(spritesheet,  # исходная картинка
                                spritesheet.get_width() // 8, # ширина кадра (ширина картинки / кол-во кадров)
                                spritesheet.get_height() // 2, # высота кадра (высота картинки / кол-во строк кадров)
                                8) # кол-во кадров в одной строке

running = True
while running:
    dt = clock.tick(60) / 1000

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Просчет анимации квадрата
    frame_timer += dt                                            # увеличиваем таймер по времени
    if frame_timer >= frame_duration:                            # если время таймера >= длительности анимации
        frame_timer = 0                                          # сбрасываем таймер
        current_frame = (current_frame + 1) % len(square_frames) # переключаем кадр анимации
    # ----------------

    circle_sprites.update(dt)

    screen.fill((0, 0, 0))
    screen.blit(square_frames[current_frame], (100, 100))
    circle_sprites.draw(screen)

    pg.display.flip()

pg.quit()
