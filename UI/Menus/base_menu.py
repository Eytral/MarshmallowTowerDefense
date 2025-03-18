from abc import ABC, abstractmethod
from UI.button_class import Button
from Constants import config
import pygame

class Menu(ABC):
    def __init__(self, game, title, button_data):
        self.game = game
        self.buttons = []
        self.title = title
        self.create_buttons(button_data)
        self.title_font = pygame.font.Font(None, 74)  # Font for the title
        self.body_font = pygame.font.Font(None, 37)  # Font for the title


    def draw(self, screen):
        """Draw the menu and its buttons."""
        for button in self.buttons:
            button.draw(screen)

        title_surface = self.title_font.render(self.title, True, (255, 255, 255))  # White color for title text
        text_rect = title_surface.get_rect()  # Get the rect of the title text for positioning
        text_rect.center = (config.SCREEN_WIDTH // 2, 150)  # Position the title at the center horizontally and near the top
        screen.blit(title_surface, text_rect)  # Draw the title on the screen
        

    def add_button(self, button):
        """Add a button to the menu."""
        self.buttons.append(button)

    def create_buttons(self, button_data):
        x_pos = config.SCREEN_WIDTH//2 - config.BUTTON_WIDTH//2
        for index, (text, action) in enumerate(button_data):
            y_pos = config.BUTTON_DEFAULT_Y_POS + config.BUTTON_VERTICAL_OFFSET*index
            self.buttons.append(Button(text, (x_pos ,y_pos), action))