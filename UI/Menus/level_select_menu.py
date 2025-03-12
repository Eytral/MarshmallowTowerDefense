from UI.Menus.base_menu import Menu
from Constants import config
from UI.button_class import Button 
import pygame

class LevelSelectMenu(Menu):
    def __init__(self, game):
        """
        Initialize the options menu with title font, button font, and buttons.

        Args:
            game: The game object that holds the state manager and other game elements.
        """
        super().__init__(game)  # Call the parent class's constructor
        self.title_font = pygame.font.Font(None, 74)  # Font for the title
        self.button_font = pygame.font.Font(None, 36)  # Font for the buttons
        self.create_buttons()  # Create buttons for the level select menu

    def create_buttons(self):
        """
        Create the buttons for the OptionsMenu, positioning them and binding actions.

        This method adds the buttons to the menu's list by calling add_button.
        """
        # Add a button to choose each level (currently hardcoded)
        self.add_button(Button("Level 1", 
                               (config.SCREEN_WIDTH // 2 - config.BUTTON_WIDTH // 2,  # Center button horizontally
                                200),
                               lambda: self.set_level(1)))  # Action to return to the main menu
        
        self.add_button(Button("Level 2", 
                               (config.SCREEN_WIDTH // 2 - config.BUTTON_WIDTH // 2,  # Center button horizontally
                                300),  # Center button vertically
                               lambda: self.set_level(2)))  # Action to return to the main menu

    def draw(self, screen):
        """
        Draw the title and buttons on the screen.

        Args:
            screen: The Pygame surface to draw the menu on.
        """
        # Create and render the title text
        title_surface = self.title_font.render("Level Select", True, (255, 255, 255))  # White color for title text
        text_rect = title_surface.get_rect()  # Get the rect of the title text for positioning
        text_rect.center = (config.SCREEN_WIDTH // 2, 150)  # Position the title at the center horizontally and near the top
        screen.blit(title_surface, text_rect)  # Draw the title on the screen
        super().draw(screen)  # Call the draw method from the parent class to draw the buttons

    # ACTIONS (called when the respective buttons are clicked)
    def set_level(self, level_number):
        self.game.state_manager.change_state("Game_State", level_number)
        return level_number
