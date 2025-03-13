import pygame
from Constants import config

class Mouse():
    def __init__(self):
        self.map_grid_x = None
        self.map_grid_y = None
        self.current_selection = None
        self.current_action = None
    
    def update_mouse_pos(self):
        x,y = pygame.mouse.get_pos()
        y -= config.SCREEN_TOPBAR_HEIGHT
        map_grid_x = x // config.GRID_CELL_SIZE
        if map_grid_x >= config.GRID_CELL_COUNT:
            map_grid_x = None
        map_grid_y = y // config.GRID_CELL_SIZE
        if map_grid_y >= config.GRID_CELL_COUNT or map_grid_y < 0:
            map_grid_y = None
        self.map_grid_x, self.map_grid_y = map_grid_x, map_grid_y

    def is_on_grid(self):
        if self.map_grid_x != None and self.map_grid_y != None: #if neither value is None
            return True
        else:
            return False

    def change_current_selection(self, selection):
        self.current_selection = selection

    def change_current_action(self, action):
        self.current_action = action

    def no():
        pass
