from UI.Menus.base_menu import Menu
from Constants import config
from UI.button_class import Button 
import pygame

class OptionsMenu(Menu):
    def __init__(self, game):
        """
        Initialize the options menu with title font, button font, and buttons.

        Args:
            game: The game object that holds the state manager and other game elements.
        """
        button_data = [
            ("Main Menu", self.back_to_main_menu),
            ("Easy Difficulty", lambda: self.change_difficulty("Easy")),
            ("Normal Difficulty", lambda: self.change_difficulty("Normal")),
            ("Hard Difficulty", lambda: self.change_difficulty("Hard"))
        ]
        super().__init__(game, "Options", button_data)  # Call the parent class's constructor
        self.title_font = pygame.font.Font(None, 74)  # Font for the title

    def draw(self, screen):
        """
        Draw the title and buttons on the screen.

        Args:
            screen: The Pygame surface to draw the menu on.
        """
        # Create and render the title text
        super().draw(screen)  # Call the draw method from the parent class to draw the buttons

        # Draw Difficulty Text
        difficulty_surface = self.body_font.render(f"Difficulty: {self.game.state_manager.states["Game_State"].wave_manager.difficulty}", True, (255, 255, 255))  # White color for title text
        text_rect = difficulty_surface.get_rect()  # Get the rect of the title text for positioning
        text_rect.center = (config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT-config.BUTTON_VERTICAL_OFFSET)  # Position the title at the center horizontally and near the top
        screen.blit(difficulty_surface, text_rect)  # Draw the title on the screen

    # ACTIONS (called when the respective buttons are clicked)
    def back_to_main_menu(self):
        """
        Action to return to the main menu when 'Main Menu' button is clicked.
        This changes the current menu to the "MainMenu".
        """
        self.game.state_manager.current_state.change_menu("MainMenu")

    def change_difficulty(self, difficulty):
        self.game.state_manager.states["Game_State"].change_difficulty(difficulty)
