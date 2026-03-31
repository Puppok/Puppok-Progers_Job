import pygame as pg
import json

class TileMap:
    def __init__(self, tile_size):
        self.tile_size = tile_size
        self.map_data = []
        self.width = 0
        self.height = 0

        # Цвета тайлов
        self.tile_colors = {
            0: (50, 50, 50),  # Пусто
            1: (139, 69, 19),  # Земля (твердая)
            2: (0, 200, 0),  # Трава (декор)
            3: (100, 100, 100),  # Камень (твердый)
            4: (255, 0, 0),  # Лава (опасная)
        }

        # Свойства тайлов
        self.solid_tiles = {1, 3}  # Твердые
        self.danger_tiles = {4}  # Опасные

    def load_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        self.map_data = data['map']
        self.width = data['width']
        self.height = data['height']

    def draw(self, screen, camera_x = 0, camera_y = 0):
        for row in range(self.height):
            for col in range(self.width):
                tile_id = self.map_data[row][col]

                if tile_id != 0:
                    x = col * self.tile_size - camera_x
                    y = row * self.tile_size - camera_y

                    color = self.tile_colors.get(tile_id)
                    if color:
                        pg.draw.rect(screen, color,(x, y, self.tile_size, self.tile_size))

    def is_solid(self, x, y):
        col = int(x // self.tile_size)
        row = int(y // self.tile_size)

        if 0 <= row < self.height and 0 <= col < self.width:
            tile_id = self.map_data[row][col]
            return tile_id in self.solid_tiles
        return False

    def is_danger(self, x, y):
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
        if keys[pg.K_LEFT]:
            self.velocity_x = -self.speed
        if keys[pg.K_RIGHT]:
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
        if keys[pg.K_SPACE] and self.on_ground:
            self.velocity_y = -self.jump_power

        # Проверка опасности
        for px, py in corners_y:
            if tilemap.is_danger(px, py):
                self.alive = False
                break

    def draw(self, screen, camera_x = 0, camera_y = 0):
        if self.alive:
            color = (0, 255, 0) if self.on_ground else (0, 200, 255)
            x = int(self.x - camera_x)
            y = int(self.y - camera_y)

            pg.draw.rect(screen, color, (x, y, self.width, self.height))
            pg.draw.rect(screen, (0, 0, 0), (x, y, self.width, self.height), 2)

class TileMapEditor:
    def __init__(self, width, height, tile_size):
        self.width = width  # В тайлах
        self.height = height
        self.tile_size = tile_size

        # Пустая карта
        self.map_data = [[0 for _ in range(width)] for _ in range(height)]

        # Текущий выбранный тайл
        self.current_tile = 1

        # Смещение карты на экране
        self.offset_x = 150
        self.offset_y = 60

        # Цвета тайлов
        self.tile_colors = {
            0: (50, 50, 50),  # Пусто (фон)
            1: (139, 69, 19),  # Земля
            2: (0, 200, 0),  # Трава
            3: (100, 100, 100),  # Камень
            4: (255, 0, 0),  # Вода
        }

    def handle_click(self, mouse_x, mouse_y, button):
        # Учитываем смещение карты
        adjusted_x = mouse_x - self.offset_x
        adjusted_y = mouse_y - self.offset_y

        col = adjusted_x // self.tile_size
        row = adjusted_y // self.tile_size

        if 0 <= col < self.width and 0 <= row < self.height:
            if button == 1:  # ЛКМ - рисовать
                self.map_data[row][col] = self.current_tile
            elif button == 3:  # ПКМ - стирать
                self.map_data[row][col] = 0

    def set_current_tile(self, tile_id):
        if tile_id in self.tile_colors:
            self.current_tile = tile_id

    def save_to_file(self, filename):
        data = {
            'width': self.width,
            'height': self.height,
            'tile_size': self.tile_size,
            'map': self.map_data
        }

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2)

        print(f"Карта сохранена в {filename}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)

            self.width = data['width']
            self.height = data['height']
            self.tile_size = data['tile_size']
            self.map_data = data['map']

            print(f"Карта загружена из {filename}")
            return True
        except FileNotFoundError:
            print(f"Файл {filename} не найден")
            return False

    def draw(self, screen):
        for row in range(self.height):
            for col in range(self.width):
                tile_id = self.map_data[row][col]
                x = col * self.tile_size
                y = row * self.tile_size

                # Фон тайла
                color = self.tile_colors.get(tile_id, (255, 0, 255))
                pg.draw.rect(screen, color, (x, y, self.tile_size, self.tile_size))

                # Сетка
                pg.draw.rect(screen, (100, 100, 100),
                                 (x, y, self.tile_size, self.tile_size), 1)

    def draw_ui(self, screen):
        font = pg.font.Font(None, 28)

        # Заголовок
        title = font.render("Tilemap Editor", True, (255, 255, 255))
        screen.blit(title, (10, 10))

        # Текущий тайл
        current_text = font.render(f"Тайл: {self.current_tile}", True, (255, 255, 255))
        screen.blit(current_text, (10, 40))

        # Палитра
        palette_y = 70
        for tile_id in range(1, 5):
            x = 10
            y = palette_y + (tile_id - 1) * 35

            # Квадрат тайла
            color = self.tile_colors[tile_id]
            pg.draw.rect(screen, color, (x, y, 30, 30))

            # Рамка (выделение текущего)
            border_color = (255, 255, 0) if tile_id == self.current_tile else (255, 255, 255)
            pg.draw.rect(screen, border_color, (x, y, 30, 30), 2)

            # Номер
            num_text = font.render(str(tile_id), True, (255, 255, 255))
            screen.blit(num_text, (x + 35, y + 5))

        # Подсказки
        hints = [
            "1-4: Выбор тайла",
            "ЛКМ: Рисовать",
            "ПКМ: Стирать",
            "S: Сохранить",
            "L: Загрузить"
        ]

        hint_y = 250
        for hint in hints:
            text = pg.font.Font(None, 22).render(hint, True, (200, 200, 200))
            screen.blit(text, (10, hint_y))
            hint_y += 25
