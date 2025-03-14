import pygame
from Constants import config

class Grid:
    """
    Represents a grid structure that stores map data and handles rendering.
    """
    
    def __init__(self, grid):
        """
        Initializes the Grid instance.
        
        Args:
            grid: A 2D list representing the grid structure.
        """
        self.grid = grid

    def check_tile(self, grid_coords):
        """
        Determines the type of tile at the given grid coordinates.
        
        Args:
            grid_coords: Tuple (x, y) representing the grid position.
        
        Returns:
            A string indicating the tile type ("path", "tower", or "empty space").
        """
        grid_x, grid_y = grid_coords[0], grid_coords[1]
        if grid_x is not None and grid_y is not None:
            if self.grid[grid_y][grid_x] == 1 or self.grid[grid_y][grid_x] == 3:
                return "path"
            elif self.grid[grid_y][grid_x] == 2:
                return "tower"
            else:
                return "empty space"

    def determine_start_pos(self):
        """
        Finds and returns the starting position of the path.
        
        Returns:
            A tuple (x, y) representing the start position, or "undefined" if not found.
        """
        start_pos = "undefined"
        for row_num, row in enumerate(self.grid):
            for column_num, space in enumerate(row):
                if space == 3:  # Starting position
                    start_pos = (column_num, row_num)
        return start_pos

    def draw(self, screen, grid_x, grid_y):
        """
        Renders the grid and highlights the selected cell.
        
        Args:
            screen: pygame display surface.
            grid_x: X-coordinate of the highlighted grid cell.
            grid_y: Y-coordinate of the highlighted grid cell.
        """
        self.draw_grid(screen)
        self.highlight_square(screen, grid_x, grid_y)

    def highlight_square(self, screen, grid_x, grid_y):
        """
        Highlights the selected grid square.
        
        Args:
            screen: pygame display surface.
            grid_x: X-coordinate of the grid cell.
            grid_y: Y-coordinate of the grid cell.
        """
        if grid_x is not None and grid_y is not None:
            pygame.draw.rect(screen, (255, 0, 0), (grid_x * config.GRID_CELL_SIZE, grid_y * config.GRID_CELL_SIZE + config.SCREEN_TOPBAR_HEIGHT, config.GRID_CELL_SIZE, config.GRID_CELL_SIZE), 3)  # Red highlight

    def draw_grid(self, screen):
        """
        Draws the grid lines and visualizes tile types.
        
        Args:
            screen: pygame display surface.
        """
        for x in range(0, config.GRID_SIZE, config.GRID_CELL_SIZE):
            for y in range(config.SCREEN_TOPBAR_HEIGHT, config.GRID_SIZE + config.SCREEN_TOPBAR_HEIGHT, config.GRID_CELL_SIZE):
                pygame.draw.rect(screen, (200, 200, 200), (x, y, config.GRID_CELL_SIZE, config.GRID_CELL_SIZE), 1)

        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                rect = pygame.Rect(x * config.GRID_CELL_SIZE + config.OFFSET_FROM_GRID, y * config.GRID_CELL_SIZE + config.SCREEN_TOPBAR_HEIGHT + config.OFFSET_FROM_GRID, config.GRID_CELL_SIZE-config.OFFSET_FROM_GRID*2, config.GRID_CELL_SIZE-config.OFFSET_FROM_GRID*2)
                if cell == 1:
                    pygame.draw.rect(screen, (255, 165, 0), rect)  # Draw orange for path tiles
                if cell == 3:
                    pygame.draw.rect(screen, (255, 0, 0), rect)  # Draw red for starting point tile

        border_rect = pygame.Rect(0, config.SCREEN_TOPBAR_HEIGHT, config.GRID_SIZE, config.GRID_SIZE)
        pygame.draw.rect(screen, (0, 0, 255), border_rect, 1)  # Draw a border (thickness = 1)

    def set_tile(self, tile, grid_x, grid_y):
        """
        Sets the specified tile type at the given grid coordinates.
        
        Args:
            tile: The tile type to place.
            grid_x: X-coordinate of the grid.
            grid_y: Y-coordinate of the grid.
        """
        self.grid[grid_y][grid_x] = tile

    def find_path(self):
    # Find the start position (3)
        start = None
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if self.grid[r][c] == 3:  # Look for the start marker
                    start = (r, c)
                    break
            if start:
                break

        if not start:
            print("Start position (3) not found in the grid.")
            return []  # Return an empty list if start not found

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Movement directions

        path = [start]
        visited = set([start])
        current_position = start

        while True:
            found_next_step = False
            possible_moves = []

            # Check all possible directions
            for dr, dc in directions:
                nr, nc = current_position[0] + dr, current_position[1] + dc

                # Ensure we stay within bounds, check for valid path (1), and avoid revisiting cells
                if 0 <= nr < len(self.grid) and 0 <= nc < len(self.grid[0]):
                    if self.grid[nr][nc] == 1 and (nr, nc) not in visited:
                        possible_moves.append((nr, nc))

            if not possible_moves:
                print(f"Dead end reached at {current_position}, breaking out.")
                break  # No valid path found, exit loop

            next_position = possible_moves[0]  # Pick the first valid move

            # Add the next position to the path and mark it as visited
            visited.add(next_position)
            path.append(next_position)
            current_position = next_position

            print(f"Moving from {current_position} to {next_position}")

        print(f"Enemy grid path: {path}")
        # Convert the path coordinates into screen positions
        path_positions = []
        for coordinate in path:
            x, y = (coordinate[1]) * config.GRID_CELL_SIZE, coordinate[0] * config.GRID_CELL_SIZE + config.SCREEN_TOPBAR_HEIGHT
            path_positions.append((x, y))

        print(f"Enemy path (screen positions): {path_positions}")
        return path_positions





        
    def find_enemy_start_pos(self):
        for row_num, row in enumerate(self.grid):
            for column_num, space in enumerate(row):
                if space == 3:
                    x, y = column_num*config.GRID_CELL_SIZE, row_num*config.GRID_CELL_SIZE + config.SCREEN_TOPBAR_HEIGHT 
                    return (x, y)
        return (0,0)