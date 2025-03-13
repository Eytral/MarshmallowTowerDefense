import pygame
from Constants import config

marsh_mallows_img = pygame.image.load("Assets\Maps\placeholder_map.png")
MARSH_MALLOWS_SPRITE = pygame.transform.scale(marsh_mallows_img, (config.GRID_SIZE, config.GRID_SIZE))