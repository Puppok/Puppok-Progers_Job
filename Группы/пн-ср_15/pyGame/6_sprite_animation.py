import pygame as pg

class AnimatedSprite(pg.sprite.Sprite):
    def __init__(self, coord_x, coord_y, frames, frame_duration):
        super().__init__()

        self.frames = frames
        self.current_frame = 0
        self.frame_duration = frame_duration
        self.frame_timer = 0

        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.x = coord_x
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

# === Работа со спрайт листом ===
spritesheet = pg.image.load('spritesheet.png').convert_alpha()

def get_frames(sheet, frame_width, frame_height, count):
    frames = []
    for i in range(count):
        rect = pg.Rect(i * frame_width, 0, frame_width, frame_height)
        frame = sheet.subsurface(rect)
        frames.append(frame)
    return frames

spritesheet_frames = get_frames(spritesheet, spritesheet.get_width() // 8,
                                spritesheet.get_height() // 2, 8)

cur_fr = 0
anim_speed = 0.2
anim_timer = 0
# --------------------

arr_frames = [] # список для хранения кадров
for i in range(5):
    frame = pg.Surface((100, 100)) # создаем поверхность (кадр)
    color = (255, 50 * i, 0) # создаем цвет для кадра (меняется в ходе цикле)
    frame.fill(color) # закрашиваем поверхность в текущий цвет
    arr_frames.append(frame) # добавляем получившийся кадр в массив кадров

current_frame = 0

frame_timer = 0
frame_duration = 0.2

# Для класса AnimatedSprite
animated_sprite_frames = []
for i in range(6):
    frame = pg.Surface((100, 100))
    frame.fill((255, 255, 255))
    frame.set_colorkey((255, 255, 255))

    raduis = 15 + i * 5
    pg.draw.circle(frame, (255, 215, 0), (50, 50), raduis)
    animated_sprite_frames.append(frame)

sprites = pg.sprite.Group()
for i in range(3):
    sprite = AnimatedSprite(200 + i * 200, 270, animated_sprite_frames, 0.1)
    sprites.add(sprite)

isActive = True
while isActive:
    dt = clock.tick(60) / 1000

    for event in pg.event.get():
        if event.type == pg.QUIT:
            isActive = False

    # --- Анимация спрайт листа ---
    anim_timer += anim_speed
    if anim_timer >= 1:
        anim_timer = 0
        cur_fr = (cur_fr + 1) % len(spritesheet_frames)
    # -----------


    frame_timer += dt # таймер отсчитывает время в секундах
    if frame_timer >= frame_duration: # если время таймера превышает длительность анимации
        frame_timer = 0 # обнуление таймера
        current_frame = (current_frame + 1) % len(arr_frames) # смена кадра

    sprites.update(dt) # обновление группы спрайтов

    screen.fill((0, 0, 0))
    screen.blit(arr_frames[current_frame], (100, 100)) # отрисовка картинки с определенным кадром
    sprites.draw(screen) # отрисовка группы спрайтов
    screen.blit(spritesheet_frames[cur_fr], (100, 100))

    pg.display.flip()

pg.quit()
