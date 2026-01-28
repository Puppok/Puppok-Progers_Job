import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Галерея")
clock = pygame.time.Clock()

image1 = pygame.Surface((200, 200))
pygame.draw.circle(image1, (255, 0, 0), (100, 100), 90)

image2 = pygame.Surface((200, 200))
pygame.draw.rect(image2, (0, 255, 0), (20, 20, 160, 160))

image3 = pygame.Surface((200, 200))
points = [(100, 20), (20, 180), (180, 180)]
pygame.draw.polygon(image3, (0, 0, 255), points)

image4 = pygame.Surface((200, 200))
pygame.draw.ellipse(image4, (255, 255, 0), (30, 50, 140, 100))

images = [image1, image2, image3, image4]

current_index = 0

print(f"Показано изображение: {current_index + 1}")

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_index = 0
                print(f"Показано изображение: {current_index + 1}")
            elif event.key == pygame.K_2:
                current_index = 1
                print(f"Показано изображение: {current_index + 1}")
            elif event.key == pygame.K_3:
                current_index = 2
                print(f"Показано изображение: {current_index + 1}")
            elif event.key == pygame.K_4:
                current_index = 3
                print(f"Показано изображение: {current_index + 1}")

    screen.fill((255, 255, 255))

    current_image = images[current_index]
    x = 400 - current_image.get_width() // 2
    y = 300 - current_image.get_height() // 2

    screen.blit(current_image, (x, y))

    pygame.display.flip()

pygame.quit()