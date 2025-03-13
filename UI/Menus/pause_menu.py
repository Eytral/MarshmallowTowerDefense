from UI.Menus.base_menu import Menu
from Constants import config
from UI.button_class import Button
import pygame

class PauseMenu(Menu):
    def __init__(self, game):
        """
        Initialize the pause menu with title font, button font, and buttons.

        Args:
            game: The game object that holds the state manager and other game elements.
        """
        super().__init__(game)  # Call the parent class's constructor
        self.title_font = pygame.font.Font(None, 74)  # Font for the title
        self.button_font = pygame.font.Font(None, 36)  # Font for the buttons
        self.create_buttons()  # Create buttons for the pause menu

    def create_buttons(self):
        """
        Create the buttons for the PauseMenu, positioning them and binding actions.

        This method adds the buttons to the menu's list by calling add_button.
        """
        # Add a button to resume the game
        self.add_button(Button("Resume", 
                               (config.SCREEN_WIDTH // 2 - config.BUTTON_WIDTH // 2, 
                                config.BUTTON_DEFAULT_Y_POS),  # Center button horizontally
                               self.resume_game))  # Action to resume the game
        
        # Add a button to return to the main menu
        self.add_button(Button("Main Menu", 
                               (config.SCREEN_WIDTH // 2 - config.BUTTON_WIDTH // 2, 
                                config.BUTTON_DEFAULT_Y_POS+config.BUTTON_OFFSET),  # Center button horizontally
                               self.back_to_main_menu))  # Action to go to the main menu

        # Add a button to exit the game
        self.add_button(Button("Exit", 
                               (config.SCREEN_WIDTH // 2 - config.BUTTON_WIDTH // 2, 
                                config.BUTTON_DEFAULT_Y_POS+config.BUTTON_OFFSET*2),  # Center button horizontally
                               self.exit_game))  # Action to exit the game

    def draw(self, screen):
        """
        Draw the title and buttons on the screen.

        Args:
            screen: The Pygame surface to draw the menu on.
        """
        # Create and render the title text
        title_surface = self.title_font.render("Pause Menu", True, (255, 255, 255))  # White color for title text
        text_rect = title_surface.get_rect()  # Get the rect of the title text for positioning
        text_rect.center = (config.SCREEN_WIDTH // 2, 150)  # Position the title at the center horizontally and near the top
        screen.blit(title_surface, text_rect)  # Draw the title on the screen
        super().draw(screen)  # Call the draw method from the parent class to draw the buttons

    # ACTIONS (called when the respective buttons are clicked)
    def resume_game(self):
        """
        Action to resume the game when 'Resume' button is clicked.
        This changes the state back to the "Game_State".
        """
        self.game.state_manager.change_state("Game_State")

    def back_to_main_menu(self):
        """
        Action to return to the main menu when 'Main Menu' button is clicked.
        This changes the current menu to the "MainMenu".
        """
        self.game.state_manager.change_state("Menu_State")
        self.game.state_manager.current_state.change_menu("MainMenu")

    def exit_game(self):
        """
        Action to exit the game when 'Exit' button is clicked.
        Sets the game’s running state to False, which will stop the game loop.
        """
        self.game.running = False
