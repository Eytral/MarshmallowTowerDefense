import pygame
from Constants import config
from UI.button_class import Button
from Entities.Towers.base_tower import Tower

class TowerSelectionMenu():
    def __init__(self, game):
        self.title = "Select a Tower"
        self.buttons = []
        self.game = game
        self.title_font = pygame.font.Font(None, 34)  # Font for the title


        # Create button data: (button text, action)
        button_data = [
            (tower_type.__name__, lambda t=tower_type: self.select_tower(t))  
            for tower_type in Tower.__subclasses__()
        ]
        self.create_buttons(button_data)

    def create_buttons(self, button_data):
        for index, (text, action) in enumerate(button_data):
            self.buttons.append(Button(text,
                                       (config.SCREEN_WIDTH-config.SCREEN_SIDEBAR_WIDTH//1, config.SCREEN_TOPBAR_HEIGHT+config.BUTTON_OFFSET*index),
                                       action))

    def draw(self, screen):
        for button in self.buttons:
            button.draw(screen)
        
        title_surface = self.title_font.render(self.title, True, (255, 255, 255))  # White color for title text
        screen.blit(title_surface, (config.SCREEN_WIDTH-config.SCREEN_SIDEBAR_WIDTH, config.SCREEN_TOPBAR_HEIGHT//2))  # Draw the title on the screen

    def select_tower(self, tower_type):
        self.game.state_manager.current_state.select_tower(tower_type)
        print(f"Selected Tower: {tower_type.__name__}")  # Debugging feedback
