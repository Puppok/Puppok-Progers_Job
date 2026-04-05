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

    def draw(self, screen, camera_x=0, camera_y=0):
        for row in range(self.height):
            for col in range(self.width):
                tile_id = self.map_data[row][col]

                if tile_id != 0:
                    x = col * self.tile_size - camera_x
                    y = row * self.tile_size - camera_y

                    color = self.tile_colors.get(tile_id)
                    if color:
                        pg.draw.rect(screen, color,
                                         (x, y, self.tile_size, self.tile_size))

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
