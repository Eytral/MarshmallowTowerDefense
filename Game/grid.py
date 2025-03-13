import pygame
from Constants import config
class Grid():
    def __init__(self, grid):
        self.grid = grid

    def check_tile(self, grid_coords):
        grid_x, grid_y = grid_coords[0], grid_coords[1]
        if grid_x != None and grid_y != None:
            if self.grid[grid_y][grid_x] == 1 or self.grid[grid_y][grid_x] == 3:
                return "path"
            elif self.grid[grid_y][grid_x] == 2:
                return "tower"
            else:
                return "empty space"

    def determine_start_pos(self):
        start_pos = "undefined"
        for row_num, row in enumerate(self.grid):
            for column_num, space in enumerate(row):
                if space == 3: #starting position
                    start_pos = (column_num, row_num)
        return start_pos

    def draw(self, screen, grid_x, grid_y):
       self.draw_grid(screen)
       self.highlight_square(screen, grid_x, grid_y)

    def highlight_square(self, screen, grid_x, grid_y):
        if grid_x is not None and grid_y is not None:
            pygame.draw.rect(screen, (255, 0, 0), (grid_x * config.GRID_CELL_SIZE, grid_y * config.GRID_CELL_SIZE + config.SCREEN_TOPBAR_HEIGHT, config.GRID_CELL_SIZE, config.GRID_CELL_SIZE), 3)  # Red highlight

    def draw_grid(self, screen):
        for x in range(0, config.GRID_SIZE, config.GRID_CELL_SIZE):
            for y in range(config.SCREEN_TOPBAR_HEIGHT, config.GRID_SIZE + config.SCREEN_TOPBAR_HEIGHT, config.GRID_CELL_SIZE):
                pygame.draw.rect(screen, (200, 200, 200), (x, y, config.GRID_CELL_SIZE, config.GRID_CELL_SIZE), 1)

        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                rect = pygame.Rect(x * config.GRID_CELL_SIZE + config.OFFSET_FROM_GRID, y * config.GRID_CELL_SIZE + config.SCREEN_TOPBAR_HEIGHT + config.OFFSET_FROM_GRID, config.GRID_CELL_SIZE-config.OFFSET_FROM_GRID*2, config.GRID_CELL_SIZE-config.OFFSET_FROM_GRID*2)
                if cell == 1:
                    pygame.draw.rect(screen, (255, 165, 0), rect)  # Draw orange for 1

        border_rect = pygame.Rect(0, config.SCREEN_TOPBAR_HEIGHT, config.GRID_SIZE, config.GRID_SIZE)
        pygame.draw.rect(screen, (0,0,255), border_rect, 1)  # Draw a border (thickness = 1)


    def set_tile(self, tile, grid_x, grid_y):
        self.grid[grid_y][grid_x] = tile