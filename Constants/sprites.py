import pygame
from Constants import config

# Map Sprites------------------------------------------------------------------------------------------------------------------------
marsh_mallows_img = pygame.image.load("Assets/Maps/placeholder_map.jpeg")
MARSH_MALLOWS_SPRITE = pygame.transform.scale(marsh_mallows_img, (config.GRID_SIZE, config.GRID_SIZE))

# Tower Sprites------------------------------------------------------------------------------------------------------------------------

birdflamethrower_sprite = pygame.image.load("Assets/Sprites/Towers/birdflamethrower.jpg")
BIRDFLAMETHROWER_SPRITE = pygame.transform.scale(birdflamethrower_sprite, (config.GRID_CELL_SIZE, config.GRID_CELL_SIZE))

mine_sprite = pygame.image.load("Assets/Sprites/Towers/mine.jpg")
MINE_SPRITE = pygame.transform.scale(mine_sprite, (config.GRID_CELL_SIZE, config.GRID_CELL_SIZE))

tower_default = pygame.image.load("Assets/Sprites/Towers/tower_placeholder_sprite.jpg")
TOWER_DEFAULT_SPRITE = pygame.transform.scale(tower_default, (config.GRID_CELL_SIZE, config.GRID_CELL_SIZE))

# Enemy Sprites------------------------------------------------------------------------------------------------------------------------
enemy_default = pygame.image.load("Assets/Sprites/Enemies/enemy_placeholder_sprite.jpg")
ENEMY_DEFAULT_SPRITE = pygame.transform.scale(enemy_default, (config.GRID_CELL_SIZE, config.GRID_CELL_SIZE))

marshmallow = pygame.image.load("Assets/Sprites/Enemies/marshmallow.jpg")
MARSHMALLOW_SPRITE = pygame.transform.scale(marshmallow, (config.GRID_CELL_SIZE, config.GRID_CELL_SIZE))

cracker = pygame.image.load("Assets/Sprites/Enemies/cracker.jpg")
CRACKER_SPRITE = pygame.transform.scale(cracker, (config.GRID_CELL_SIZE, config.GRID_CELL_SIZE))

white_chocolate = pygame.image.load("Assets/Sprites/Enemies/white_chocolate.jpg")
WHITE_CHOCOLATE_SPRITE = pygame.transform.scale(white_chocolate, (config.GRID_CELL_SIZE, config.GRID_CELL_SIZE))

dark_chocolate = pygame.image.load("Assets/Sprites/Enemies/dark_chocolate.jpg")
DARK_CHOCOLATE_SPRITE = pygame.transform.scale(dark_chocolate, (config.GRID_CELL_SIZE, config.GRID_CELL_SIZE))

smore = pygame.image.load("Assets/Sprites/Enemies/smore.jpg")
SMORE_SPRITE = pygame.transform.scale(smore, (config.GRID_CELL_SIZE, config.GRID_CELL_SIZE))


# Projectile Sprites------------------------------------------------------------------------------------------------------------------------
bullet_img = pygame.image.load("Assets/Sprites/Projectiles/bullet.jpg")
BULLET_SPRITE = pygame.transform.scale(bullet_img, (config.GRID_CELL_SIZE//3, config.GRID_CELL_SIZE//3))