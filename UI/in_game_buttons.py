import pygame
from Constants import config
from UI.button_class import Button

class GameButtons():
    """
    A menu for selecting a tower to place or remove.

    Attributes:
        buttons: List of Button objects representing different game options.
        game: Reference to the main game object, used to interact with the game's current state.
    """

    def __init__(self, game):
        """
        Initializes the TowerSelectionMenu with the given game object.

        Args:
            game: Reference to the main game object, used to manage the current state and mouse actions.
        """
        self.buttons = []  # List to store buttons for selecting towers
        self.game = game  # Game reference to interact with the game state

        # Create button data with text and corresponding action
        button_data = [
            ("Start", self.start_wave),
            ("Pause", self.pause_game)
        ]
        
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
                                       (10 + config.BUTTON_HORIZONTAL_OFFSET * index, config.SCREEN_TOPBAR_HEIGHT//4),
                                       action))

    def draw(self, screen):
        """
        Draws the TowerSelectionMenu on the screen.

        Args:
            screen: The pygame display surface where the menu is drawn.
        """
        for button in self.buttons:
            button.draw(screen)  # Draw each button

    def start_wave(self):
        """
        Starts the next game enemy wave
        """
        self.game.state_manager.current_state.wave_manager.next_wave()

    def pause_game(self):
        """
        Allows the player to remove a tower.
        """
        self.game.state_manager.change_state("Pause_State")
