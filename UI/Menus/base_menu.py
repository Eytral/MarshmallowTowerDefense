from abc import ABC, abstractmethod
from UI.button_class import Button
from Constants import config

class Menu(ABC):
    def __init__(self, game, title, button_data):
        self.game = game
        self.buttons = []
        self.title = title
        self.create_buttons(button_data)

    def draw(self, screen):
        """Draw the menu and its buttons."""
        for button in self.buttons:
            button.draw(screen)

    def add_button(self, button):
        """Add a button to the menu."""
        self.buttons.append(button)

    def create_buttons(self, button_data):
        x_pos = config.SCREEN_WIDTH//2 - config.BUTTON_WIDTH//2
        for index, (text, action) in enumerate(button_data):
            y_pos = config.BUTTON_DEFAULT_Y_POS + config.BUTTON_OFFSET*index
            self.buttons.append(Button(text, (x_pos ,y_pos), action))