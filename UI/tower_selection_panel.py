import pygame
from Constants import config
from UI.button_class import Button
from Entities.Towers.base_tower import Tower

class TowerSelectionMenu():
    """
    A menu for selecting a tower to place or remove.

    Attributes:
        title: The title of the menu displayed at the top.
        buttons: List of Button objects representing different tower options and removal.
        game: Reference to the main game object, used to interact with the game's current state.
        title_font: Font object used for rendering the title text.
    """

    def __init__(self, game):
        """
        Initializes the TowerSelectionMenu with the given game object.

        Args:
            game: Reference to the main game object, used to manage the current state and mouse actions.
        """
        self.title = "Select a Tower"  # Title of the menu
        self.buttons = []  # List to store buttons for selecting towers
        self.game = game  # Game reference to interact with the game state
        self.title_font = pygame.font.Font(None, 34)  # Font for the title text

        # Create button data with text and corresponding action
        button_data = []
        for tower_type in Tower.__subclasses__():
            button_data.append((tower_type.__name__, lambda t=tower_type: self.select_tower(t)))
        button_data.append(("Remove Tower", self.remove_tower))  # Add remove tower button
        
        # Create buttons using the provided button data
        self.create_buttons(button_data)

    def create_buttons(self, button_data):
        """
        Creates buttons based on provided button data.

        Args:
            button_data: List of tuples containing button text and corresponding action to bind.
        """
        for index, (text, action) in enumerate(button_data):
            # Create each button and add it to the buttons list
            self.buttons.append(Button(text,
                                       (config.SCREEN_WIDTH - config.SCREEN_SIDEBAR_WIDTH // 1, config.SCREEN_TOPBAR_HEIGHT + config.BUTTON_VERTICAL_OFFSET * index),
                                       action))

    def draw(self, screen):
        """
        Draws the TowerSelectionMenu on the screen.

        Args:
            screen: The pygame display surface where the menu is drawn.
        """
        for button in self.buttons:
            button.draw(screen)  # Draw each button

        # Render and draw the title of the menu
        title_surface = self.title_font.render(self.title, True, (255, 255, 255))  # White color for title text
        screen.blit(title_surface, (config.SCREEN_WIDTH - config.SCREEN_SIDEBAR_WIDTH, config.SCREEN_TOPBAR_HEIGHT // 2))  # Position the title

    def select_tower(self, tower_type):
        """
        Selects the tower type to place in the game.

        Args:
            tower_type: The type of tower to place, passed as a class reference (e.g., a subclass of Tower).
        """
        self.game.state_manager.current_state.mouse.change_current_action("Placing Tower", tower_type)

    def remove_tower(self):
        """
        Allows the player to remove a tower.
        """
        self.game.state_manager.current_state.mouse.change_current_action("Removing Tower", None)
