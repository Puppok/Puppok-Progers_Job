import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Падающие звёзды")
clock = pygame.time.Clock()

star_img = pygame.Surface((40, 40))
star_img.fill((0, 0, 50))
star_img.set_colorkey((0, 0, 50))

points = []
for i in range(10):
    angle = i * 36 * 3.14159 / 180
    if i % 2 == 0:
        radius = 18
    else:
        radius = 8
    x = 20 + radius * pygame.math.Vector2(1, 0).rotate(angle * 180 / 3.14159).x
    y = 20 + radius * pygame.math.Vector2(1, 0).rotate(angle * 180 / 3.14159).y
    points.append((int(x), int(y)))

pygame.draw.polygon(star_img, (255, 255, 0), points)

stars = []
for _ in range(10):
    stars.append({
        "x": random.randint(0, 760),
        "y": random.randint(-600, 0),
        "speed": random.randint(100, 200)
    })

running = True
while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for star in stars:
        star["y"] += star["speed"] * dt

        if star["y"] > 600:
            star["y"] = -40
            star["x"] = random.randint(0, 760)
            star["speed"] = random.randint(100, 200)

    screen.fill((0, 0, 50))

    for star in stars:
        screen.blit(star_img, (star["x"], star["y"]))

    pygame.display.flip()

pygame.quit()