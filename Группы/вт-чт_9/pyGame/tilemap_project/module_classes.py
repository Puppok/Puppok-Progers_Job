import pygame as pg

class TilemapEditor:
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
            4: (255, 60, 60),  # Лава
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

class Tilemap:
    pass

class Player:
    pass
