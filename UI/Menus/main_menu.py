from UI.Menus.base_menu import Menu
import pygame
from Constants import config
from UI.button_class import Button

class MainMenu(Menu):
    def __init__(self, game):
        """
        Initialize the main menu with title font, button font, and buttons.

        Args:
            game: The game object that holds the state manager and other game elements.
        """
        button_data = [
            ("Start Game", self.start_game),
            ("Options", self.open_options),
            ("Exit", self.exit_game)
        ]
        super().__init__(game, "MainMenu", button_data)  # Call the parent class's constructor
        self.title_font = pygame.font.Font(None, 74)  # Font for the title
        self.button_font = pygame.font.Font(None, 36)  # Font for the buttons

    def draw(self, screen):
        """
        Draw the title and buttons on the screen.

        Args:
            screen: The Pygame surface to draw the menu on.
        """
        # Create and render the title text
        title_surface = self.title_font.render("Main Menu", True, (255, 255, 255))
        text_rect = title_surface.get_rect()
        text_rect.center = (config.SCREEN_WIDTH//2, 150)  # Center the title on the screen
        screen.blit(title_surface, text_rect)  # Position the title
        super().draw(screen)  # Call the draw method from the parent class to draw the buttons

    # ACTIONS (called when the respective buttons are clicked)
    def start_game(self):
        """
        Action to switch to level select menu when clicking play game.
        """
        self.game.state_manager.current_state.change_menu("LevelSelectMenu")

    def open_options(self):
        """
        Action to open the options menu when 'Options' button is clicked.
        Updates the current menu to "OptionsMenu".
        """
        self.game.state_manager.current_state.change_menu("OptionsMenu")

    def exit_game(self):
        """
        Action to exit the game when 'Exit' button is clicked.
        Sets the game’s running state to False, which will stop the game loop.
        """
        self.game.running = False
