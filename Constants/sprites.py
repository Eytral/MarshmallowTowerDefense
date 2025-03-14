import pygame
from Constants import config

marsh_mallows_img = pygame.image.load("Assets/Maps/placeholder_map.png")
MARSH_MALLOWS_SPRITE = pygame.transform.scale(marsh_mallows_img, (config.GRID_SIZE, config.GRID_SIZE))

birdflamethrower_sprite = pygame.image.load("Assets/Sprites/birdflamethrower.png")
BIRDFLAMETHROWER_SPRITE = pygame.transform.scale(birdflamethrower_sprite, (config.GRID_CELL_SIZE, config.GRID_CELL_SIZE))

mine_sprite = pygame.image.load("Assets/Sprites/mine.png")
MINE_SPRITE = pygame.transform.scale(mine_sprite, (config.GRID_CELL_SIZE, config.GRID_CELL_SIZE))


tower_default = pygame.image.load("Assets/Sprites/placeholder_sprite.png")
TOWER_DEFAULT_SPRITE = pygame.transform.scale(tower_default, (config.GRID_CELL_SIZE, config.GRID_CELL_SIZE))