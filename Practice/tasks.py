import pygame
import json

class TileMap:
    def __init__(self, tile_size):
        self.tile_size = tile_size
        self.map_data = []
        self.width = 0
        self.height = 0

        # Цвета тайлов
        self.tile_colors = {
            0: None,  # Пусто
            1: (139, 69, 19),  # Земля (твердая)
            2: (0, 200, 0),  # Трава (декор)
            3: (100, 100, 100),  # Камень (твердый)
            4: (255, 0, 0),  # Лава (опасная)
        }

        # Свойства тайлов
        self.solid_tiles = {1, 3}  # Твердые
        self.danger_tiles = {4}  # Опасные

    def load_from_file(self, filename):
        """Загрузка из JSON"""
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        self.map_data = data['map']
        self.width = data['width']
        self.height = data['height']

    def draw(self, screen, camera_x=0, camera_y=0):
        """Отрисовка с камерой"""
        for row in range(self.height):
            for col in range(self.width):
                tile_id = self.map_data[row][col]

                if tile_id != 0:
                    x = col * self.tile_size - camera_x
                    y = row * self.tile_size - camera_y

                    color = self.tile_colors.get(tile_id)
                    if color:
                        pygame.draw.rect(screen, color,
                                         (x, y, self.tile_size, self.tile_size))

    def is_solid(self, x, y):
        """Проверка твердости тайла"""
        col = int(x // self.tile_size)
        row = int(y // self.tile_size)

        if 0 <= row < self.height and 0 <= col < self.width:
            tile_id = self.map_data[row][col]
            return tile_id in self.solid_tiles
        return False

    def is_danger(self, x, y):
        """Проверка опасности тайла"""
        col = int(x // self.tile_size)
        row = int(y // self.tile_size)

        if 0 <= row < self.height and 0 <= col < self.width:
            tile_id = self.map_data[row][col]
            return tile_id in self.danger_tiles
        return False

class Player:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.width = 28
        self.height = 44
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = 200
        self.jump_power = 400
        self.on_ground = False
        self.alive = True

    def update(self, dt, keys, tilemap):
        if not self.alive:
            return

        # Управление
        self.velocity_x = 0
        if keys[pygame.K_LEFT]:
            self.velocity_x = -self.speed
        if keys[pygame.K_RIGHT]:
            self.velocity_x = self.speed

        # Движение X
        self.x += self.velocity_x * dt

        # Коллизия X
        corners_x = [
            (self.x, self.y + 5),
            (self.x + self.width, self.y + 5),
            (self.x, self.y + self.height - 5),
            (self.x + self.width, self.y + self.height - 5),
        ]

        for px, py in corners_x:
            if tilemap.is_solid(px, py):
                if self.velocity_x > 0:
                    self.x = int(px / tilemap.tile_size) * tilemap.tile_size - self.width - 1
                elif self.velocity_x < 0:
                    self.x = int(px / tilemap.tile_size) * tilemap.tile_size + tilemap.tile_size + 1
                break

        # Гравитация
        self.velocity_y += 1000 * dt
        self.y += self.velocity_y * dt

        # Коллизия Y
        self.on_ground = False
        corners_y = [
            (self.x + 5, self.y),
            (self.x + self.width - 5, self.y),
            (self.x + 5, self.y + self.height),
            (self.x + self.width - 5, self.y + self.height),
        ]

        for px, py in corners_y:
            if tilemap.is_solid(px, py):
                if self.velocity_y > 0:
                    self.y = int(py / tilemap.tile_size) * tilemap.tile_size - self.height - 1
                    self.velocity_y = 0
                    self.on_ground = True
                elif self.velocity_y < 0:
                    self.y = int(py / tilemap.tile_size) * tilemap.tile_size + tilemap.tile_size + 1
                    self.velocity_y = 0
                break

        # Прыжок
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = -self.jump_power

        # Проверка опасности
        for px, py in corners_y:
            if tilemap.is_danger(px, py):
                self.alive = False
                break

    def draw(self, screen, camera_x=0, camera_y=0):
        if self.alive:
            color = (0, 255, 0) if self.on_ground else (0, 200, 255)
            x = int(self.x - camera_x)
            y = int(self.y - camera_y)

            pygame.draw.rect(screen, color, (x, y, self.width, self.height))
            pygame.draw.rect(screen, (0, 0, 0), (x, y, self.width, self.height), 2)

# Инициализация
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tilemap Platformer")
clock = pygame.time.Clock()

# Загрузка карты
tilemap = TileMap(tile_size=32)
try:
    tilemap.load_from_file("tilemap.json")
except FileNotFoundError:
    print("Создайте карту в редакторе сначала!")
    # Создаем простую карту для примера
    tilemap.map_data = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 2, 2, 2, 2, 2, 0, 0, 0, 4, 4, 0, 0, 0, 2, 2, 2, 2, 2, 2],
        [1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1],
    ]
    tilemap.width = 20
    tilemap.height = 15

# Игрок
player = Player(100, 300)

# Камера (простая - следует за игроком)
camera_x = 0
camera_y = 0

running = True
while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and not player.alive:
                # Перезапуск
                player = Player(100, 300)

    keys = pygame.key.get_pressed()
    player.update(dt, keys, tilemap)

    # Камера следует за игроком
    camera_x = player.x + player.width / 2 - 400
    camera_y = player.y + player.height / 2 - 300

    # Ограничиваем камеру границами карты
    camera_x = max(0, min(camera_x, tilemap.width * tilemap.tile_size - 800))
    camera_y = max(0, min(camera_y, tilemap.height * tilemap.tile_size - 600))

    # Отрисовка
    screen.fill((135, 206, 235))

    tilemap.draw(screen, camera_x, camera_y)
    player.draw(screen, camera_x, camera_y)

    # UI
    font = pygame.font.Font(None, 36)

    if not player.alive:
        game_over = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(game_over, (300, 250))

        restart = pygame.font.Font(None, 28).render("Нажми R для перезапуска", True, (255, 255, 255))
        screen.blit(restart, (260, 300))

    pygame.display.flip()

pygame.quit()