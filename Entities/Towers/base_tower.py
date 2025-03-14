from Constants import config, sprites

class Tower():
    def __init__(self, x_grid_pos, y_grid_pos):
        self.sprite = sprites.TOWER_DEFAULT_SPRITE
        self.x_grid_pos = x_grid_pos
        self.y_grid_pos = y_grid_pos

        self.x_pos = x_grid_pos * config.GRID_CELL_SIZE
        self.y_pos = y_grid_pos * config.GRID_CELL_SIZE + config.SCREEN_TOPBAR_HEIGHT
    
    def draw(self, screen):
        screen.blit(self.sprite, (self.x_pos, self.y_pos))


class BirdFlamethrower(Tower):
    def __init__(self, x_grid_pos, y_grid_pos):
        super().__init__(x_grid_pos, y_grid_pos)
        self.sprite = sprites.BIRDFLAMETHROWER_SPRITE

class LandMine(Tower):
    def __init__(self, x_grid_pos, y_grid_pos):
        super().__init__(x_grid_pos, y_grid_pos)
        self.sprite = sprites.MINE_SPRITE
