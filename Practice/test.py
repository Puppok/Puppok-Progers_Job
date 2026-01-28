import pygame
import pymunk
import pymunk.pygame_util
import math


def create_bird(space, x, y):
    """Создание птицы"""
    mass = 5
    radius = 15
    moment = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, moment)
    body.position = x, y

    shape = pymunk.Circle(body, radius)
    shape.friction = 0.5
    shape.elasticity = 0.3
    shape.color = (255, 0, 0, 255)

    space.add(body, shape)
    return body, shape


def create_block(space, x, y, width, height):
    """Создание блока"""
    mass = 2
    moment = pymunk.moment_for_box(mass, (width, height))
    body = pymunk.Body(mass, moment)
    body.position = x, y

    shape = pymunk.Poly.create_box(body, (width, height))
    shape.friction = 0.8
    shape.elasticity = 0.2
    shape.color = (139, 69, 19, 255)

    space.add(body, shape)
    return body, shape


def create_pig(space, x, y):
    """Создание свиньи (цель)"""
    mass = 3
    radius = 20
    moment = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, moment)
    body.position = x, y

    shape = pymunk.Circle(body, radius)
    shape.friction = 0.5
    shape.elasticity = 0.3
    shape.color = (0, 255, 0, 255)

    space.add(body, shape)
    return body, shape


pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Angry Birds Physics")
clock = pygame.time.Clock()

# Физический мир
space = pymunk.Space()
space.gravity = (0, 900)

# Земля
ground = pymunk.Segment(space.static_body, (0, 580), (1000, 580), 5)
ground.friction = 0.9
space.add(ground)

# Стены
left_wall = pymunk.Segment(space.static_body, (0, 0), (0, 600), 5)
right_wall = pymunk.Segment(space.static_body, (1000, 0), (1000, 600), 5)
space.add(left_wall, right_wall)

# Построение башни
tower_x = 700
blocks = []

# Основание
for i in range(3):
    body, shape = create_block(space, tower_x + i * 60, 530, 50, 100)
    blocks.append((body, shape))

# Второй уровень
for i in range(2):
    body, shape = create_block(space, tower_x + 30 + i * 60, 420, 50, 100)
    blocks.append((body, shape))

# Верх
body, shape = create_block(space, tower_x + 60, 310, 50, 100)
blocks.append((body, shape))

# Свинья на вершине
pig_body, pig_shape = create_pig(space, tower_x + 60, 250)

# Рогатка
slingshot_pos = (150, 500)
slingshot_power = 0
dragging = False
bird_body = None
bird_shape = None

draw_options = pymunk.pygame_util.DrawOptions(screen)

score = 0
game_started = False

running = True
while running:
    dt = clock.tick(60) / 1000.0

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Проверка клика на рогатку
                dx = mouse_pos[0] - slingshot_pos[0]
                dy = mouse_pos[1] - slingshot_pos[1]
                if math.sqrt(dx ** 2 + dy ** 2) < 50 and not game_started:
                    dragging = True
                    bird_body, bird_shape = create_bird(space, slingshot_pos[0], slingshot_pos[1])

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and dragging:
                # Запуск птицы
                dx = slingshot_pos[0] - bird_body.position.x
                dy = slingshot_pos[1] - bird_body.position.y
                force = (dx * 50, dy * 50)
                bird_body.apply_impulse_at_local_point(force)

                dragging = False
                game_started = True

    # Перетаскивание птицы
    if dragging and bird_body:
        # Ограничение расстояния
        dx = mouse_pos[0] - slingshot_pos[0]
        dy = mouse_pos[1] - slingshot_pos[1]
        distance = math.sqrt(dx ** 2 + dy ** 2)
        max_distance = 100

        if distance > max_distance:
            dx = dx / distance * max_distance
            dy = dy / distance * max_distance

        bird_body.position = slingshot_pos[0] + dx, slingshot_pos[1] + dy
        bird_body.velocity = 0, 0

    # Обновление физики
    space.step(dt)

    # Проверка упавших блоков
    for body, shape in blocks[:]:
        if body.position.y > 700:
            space.remove(body, shape)
            blocks.remove((body, shape))
            score += 10

    # Проверка свиньи
    if pig_body.position.y > 700:
        score += 100
        print("Свинья уничтожена!")
        # Можно создать новую свинью или завершить уровень

    # Отрисовка
    screen.fill((135, 206, 235))

    # Рогатка
    pygame.draw.circle(screen, (139, 69, 19), slingshot_pos, 10)
    pygame.draw.line(screen, (80, 40, 10),
                     (slingshot_pos[0] - 20, slingshot_pos[1] - 30),
                     (slingshot_pos[0] - 20, slingshot_pos[1]), 8)
    pygame.draw.line(screen, (80, 40, 10),
                     (slingshot_pos[0] + 20, slingshot_pos[1] - 30),
                     (slingshot_pos[0] + 20, slingshot_pos[1]), 8)

    # Линии натяжения
    if dragging and bird_body:
        pygame.draw.line(screen, (100, 50, 20),
                         (slingshot_pos[0] - 20, slingshot_pos[1] - 30),
                         bird_body.position, 3)
        pygame.draw.line(screen, (100, 50, 20),
                         (slingshot_pos[0] + 20, slingshot_pos[1] - 30),
                         bird_body.position, 3)

    # Физические объекты
    space.debug_draw(draw_options)

    # UI
    font = pygame.font.Font(None, 42)
    score_text = font.render(f"Счёт: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    if not game_started:
        hint = pygame.font.Font(None, 28).render(
            "Перетащите и отпустите для запуска", True, (0, 0, 0))
        screen.blit(hint, (300, 50))

    pygame.display.flip()

pygame.quit()