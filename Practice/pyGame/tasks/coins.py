import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Сбор монет")
clock = pygame.time.Clock()

# Создаем игрока
player_img = pygame.Surface((50, 50))
player_img.fill((0, 200, 0))

# Создаем монету
coin_img = pygame.Surface((40, 40))
coin_img.fill((255, 255, 255))
coin_img.set_colorkey((255, 255, 255))
pygame.draw.circle(coin_img, (255, 215, 0), (20, 20), 20)
pygame.draw.circle(coin_img, (255, 180, 0), (20, 20), 20, 3)

# Позиция игрока
player_x = 400.0
player_y = 300.0
speed = 250

# Монеты
coins = []
for _ in range(5):
    coins.append({
        "x": random.randint(50, 750),
        "y": random.randint(50, 550)
    })

score = 0

running = True
while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= speed * dt
    if keys[pygame.K_RIGHT]:
        player_x += speed * dt
    if keys[pygame.K_UP]:
        player_y -= speed * dt
    if keys[pygame.K_DOWN]:
        player_y += speed * dt

    # Проверка сбора монет
    coins_to_remove = []
    for i, coin in enumerate(coins):
        # Проверка пересечения прямоугольников
        if (player_x < coin["x"] + 40 and
                player_x + 50 > coin["x"] and
                player_y < coin["y"] + 40 and
                player_y + 50 > coin["y"]):
            coins_to_remove.append(i)
            score += 1
            print(f"Собрано монет: {score}")

    # Удаляем собранные монеты
    for i in reversed(coins_to_remove):
        coins.pop(i)

    # Отрисовка
    screen.fill((255, 255, 255))

    # Рисуем монеты
    for coin in coins:
        screen.blit(coin_img, (coin["x"], coin["y"]))

    # Рисуем игрока
    screen.blit(player_img, (player_x, player_y))

    pygame.display.flip()

pygame.quit()