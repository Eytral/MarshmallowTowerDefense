from abc import ABC, abstractmethod

class Menu(ABC):
    def __init__(self, game):
        self.game = game
        self.buttons = []

    def draw(self, screen):
        """Draw the menu and its buttons."""
        for button in self.buttons:
            button.draw(screen)

    def add_button(self, button):
        """Add a button to the menu."""
        self.buttons.append(button)