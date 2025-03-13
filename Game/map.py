import pygame
from Constants import config
from Constants import sprites
from Game.grid import Grid
from Game.maps import MAP_DATA

class Map():
    def __init__(self, name):
        self.name = name

        if name not in MAP_DATA:
            raise ValueError(f"Map {name} not found")
        
        self.map_grid = Grid(MAP_DATA[name]["grid"])

        self.background_image = sprites.MARSH_MALLOWS_SPRITE
        self.music = MAP_DATA[name]["music"]

    def draw(self, screen, grid_x, grid_y):
        screen.blit(self.background_image, (0, config.SCREEN_TOPBAR_HEIGHT))
        self.map_grid.draw(screen, grid_x, grid_y)

    def check_tile(self, grid_coords):
        return self.map_grid.check_tile(grid_coords)

    #Attemps to place tower at given coordinate
    def place_tower(self, x, y):
        self.map_grid.set_tile(2, x, y)
        
    def remove_tower(self, x, y):
        self.map_grid.set_tile(0, x, y)

    #Sets the grid to the default map (removing towers etc)
    def reset_map(self):
        self.map_grid.grid = MAP_DATA[self.name]["grid"]


