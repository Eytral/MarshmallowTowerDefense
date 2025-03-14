import pygame
from Constants import config
from UI.button_class import Button
from Entities.Towers.base_tower import Tower

class TowerSelectionMenu():
    def __init__(self):
        self.title = "Select a Tower"
        self.buttons = []

        # Create button data: (button text, action)
        button_data = [
            (tower_type.__name__, lambda t=tower_type: self.select_tower(t))  
            for tower_type in Tower.__subclasses__()
        ]
        self.create_buttons(button_data)

    def create_buttons(self, button_data):
        for index, (text, action) in enumerate(button_data):
            self.buttons.append(Button(text,
                                       (config.SCREEN_WIDTH-config.SCREEN_SIDEBAR_WIDTH, config.SCREEN_TOPBAR_HEIGHT),
                                       action))

    def draw(self, screen):
        for button in self.buttons:
            button.draw(screen)

    def select_tower(self, tower_type):
        """Handle tower selection logic."""
        print(f"Selected Tower: {tower_type.__name__}")  # Debugging feedback
