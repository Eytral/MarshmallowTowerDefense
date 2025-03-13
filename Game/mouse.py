import pygame
from Constants import config

class Mouse():
    """
    Represents the mouse input and its interaction with the grid in the game.

    Attributes:
        map_grid_x: The x-coordinate of the mouse position on the grid.
        map_grid_y: The y-coordinate of the mouse position on the grid.
        current_selection: The currently selected object or tower for placement.
        current_action: The current action (e.g., placing a tower, selecting an object) that the user is performing.
    """
    
    def __init__(self):
        """
        Initializes the Mouse object with default values.
        Sets map_grid_x and map_grid_y to None, representing no position on the grid.
        Initializes current_selection and current_action to None, representing no selection or action.
        """
        self.map_grid_x = None  # X position on the grid (None means no position yet)
        self.map_grid_y = None  # Y position on the grid (None means no position yet)
        self.current_selection = None  # The object or tower selected (None means no selection)
        self.current_action = None  # The action being performed (None means no action)

    def update_mouse_pos(self):
        """
        Updates the mouse's grid position based on the current mouse coordinates.
        
        Adjusts the mouse position to take the screen's top bar height into account
        and maps the mouse position to the grid based on the defined grid cell size.
        """
        x, y = pygame.mouse.get_pos()  # Get current mouse position
        y -= config.SCREEN_TOPBAR_HEIGHT  # Adjust for the screen top bar height
        map_grid_x = x // config.GRID_CELL_SIZE  # Calculate the grid column the mouse is on
        if map_grid_x >= config.GRID_CELL_COUNT:  # If out of bounds, set to None
            map_grid_x = None
        map_grid_y = y // config.GRID_CELL_SIZE  # Calculate the grid row the mouse is on
        if map_grid_y >= config.GRID_CELL_COUNT or map_grid_y < 0:  # If out of bounds, set to None
            map_grid_y = None
        self.map_grid_x, self.map_grid_y = map_grid_x, map_grid_y  # Update the grid position attributes

    def is_on_grid(self):
        """
        Checks if the mouse is currently positioned within the grid boundaries.
        
        Returns:
            bool: True if the mouse is on the grid, False otherwise.
        """
        if self.map_grid_x != None and self.map_grid_y != None:  # If both grid positions are valid
            return True
        else:
            return False  # If either grid position is None, return False

    def change_current_selection(self, selection):
        """
        Changes the current selection to the new selection provided.
        
        Args:
            selection: The new selection (e.g., a tower or object to place).
        """
        self.current_selection = selection  # Set the new selection

    def change_current_action(self, action):
        """
        Changes the current action to the new action provided.
        
        Args:
            action: The new action to perform (e.g., place tower, select object).
        """
        self.current_action = action  # Set the new action

    def no(self):
        """
        A placeholder method that does nothing.
        This can be used as a placeholder for future functionality or removed if not needed.
        """
        pass
