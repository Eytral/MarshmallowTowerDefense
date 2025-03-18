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
        button_data = [
            ("Resume", self.resume_game),
            ("Main Menu", self.back_to_main_menu),
            ("Exit", self.exit_game)
        ]
        super().__init__(game, "Pause", button_data)  # Call the parent class's constructor

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
        self.game.state_manager.states["Game_State"].exit(exiting_game=True)
        self.game.state_manager.change_state("Menu_State")
        self.game.state_manager.current_state.change_menu("MainMenu")

    def exit_game(self):
        """
        Action to exit the game when 'Exit' button is clicked.
        Sets the game’s running state to False, which will stop the game loop.
        """
        self.game.running = False
