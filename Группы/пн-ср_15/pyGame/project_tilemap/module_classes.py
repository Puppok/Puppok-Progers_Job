import pygame as pg

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