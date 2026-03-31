import pygame
import json


class TileEditor:
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
            4: (0, 100, 255),  # Вода
        }

    def handle_click(self, mouse_x, mouse_y, button):
        """Обработка клика мыши"""
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
        """Установить текущий тайл для рисования"""
        if tile_id in self.tile_colors:
            self.current_tile = tile_id

    def save_to_file(self, filename):
        """Сохранить карту в JSON"""
        data = {
            'width': self.width,
            'height': self.height,
            'tile_size': self.tile_size,
            'map': self.map_data
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

        print(f"Карта сохранена в {filename}")

    def load_from_file(self, filename):
        """Загрузить карту из JSON"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)

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
        """Отрисовка карты"""
        for row in range(self.height):
            for col in range(self.width):
                tile_id = self.map_data[row][col]
                x = col * self.tile_size
                y = row * self.tile_size

                # Фон тайла
                color = self.tile_colors.get(tile_id, (255, 0, 255))
                pygame.draw.rect(screen, color, (x, y, self.tile_size, self.tile_size))

                # Сетка
                pygame.draw.rect(screen, (100, 100, 100),
                                 (x, y, self.tile_size, self.tile_size), 1)

    def draw_ui(self, screen):
        """Отрисовка UI (палитра)"""
        font = pygame.font.Font(None, 28)

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
            pygame.draw.rect(screen, color, (x, y, 30, 30))

            # Рамка (выделение текущего)
            border_color = (255, 255, 0) if tile_id == self.current_tile else (255, 255, 255)
            pygame.draw.rect(screen, border_color, (x, y, 30, 30), 2)

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
            text = pygame.font.Font(None, 22).render(hint, True, (200, 200, 200))
            screen.blit(text, (10, hint_y))
            hint_y += 25

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tilemap Editor")
clock = pygame.time.Clock()

# Создание редактора
editor = TileEditor(width=20, height=15, tile_size=32)

# Попытка загрузить сохраненную карту
editor.load_from_file("tilemap.json")

# Состояние мыши
mouse_pressed = False

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Клавиши
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                editor.set_current_tile(1)
            elif event.key == pygame.K_2:
                editor.set_current_tile(2)
            elif event.key == pygame.K_3:
                editor.set_current_tile(3)
            elif event.key == pygame.K_4:
                editor.set_current_tile(4)
            elif event.key == pygame.K_s:
                editor.save_to_file("tilemap.json")
            elif event.key == pygame.K_l:
                editor.load_from_file("tilemap.json")

        # Мышь
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True
            editor.handle_click(*event.pos, event.button)

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False

    # Рисование при удержании мыши
    if mouse_pressed:
        mouse_buttons = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        if mouse_buttons[0]:  # ЛКМ
            editor.handle_click(*mouse_pos, 1)
        elif mouse_buttons[2]:  # ПКМ
            editor.handle_click(*mouse_pos, 3)

    # Отрисовка
    screen.fill((30, 30, 40))

    # Сдвиг для UI
    pygame.draw.rect(screen, (20, 20, 30), (0, 0, 150, 600))

    # Карта
    map_surface = pygame.Surface((640, 480))
    editor.draw(map_surface)
    screen.blit(map_surface, (editor.offset_x, editor.offset_y))

    # UI
    editor.draw_ui(screen)

    pygame.display.flip()

pygame.quit()