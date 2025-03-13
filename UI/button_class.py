import pygame
from Constants import config

class Button:
    def __init__(self, text, position, action, normal_color=(50, 50, 50), hover_color=(255, 0, 0), font=None):
        """
        Initialize the button with text, position, action, and appearance options.
        
        Attributes:
            text: The text to display on the button.
            position: The (x, y) position to place the button on the screen.
            action: The function to call when the button is clicked.
            normal_color: The color of the button when not hovered (default: green).
            hover_color: The color of the button when hovered (default: yellow).
            font: The font to use for the button text (default: Arial, 24).
        """
        self.text = text
        self.position = position
        self.action = action

        # Create a rectangular area for the button based on position and size from config
        self.rect = pygame.Rect(position[0], position[1], config.BUTTON_WIDTH, config.BUTTON_HEIGHT)
        self.normal_color = normal_color  # Default button color when not hovered
        self.hover_color = hover_color  # Color when mouse hovers over button
        self.clicked_color = (255, 0, 0)  # Color when button is clicked (default is red)

        # Use the provided font or fall back to a default font
        self.font = font or pygame.font.SysFont('Arial', 24)

    def is_hovered(self):
        """
        Check if the mouse cursor is hovering over the button.

        Args:
            mouse_pos: The current position of the mouse (x, y).
        """
        return self.rect.collidepoint(pygame.mouse.get_pos()) #Returns True if the mouse is hovering over the button, False otherwise.

    def click(self):
        """
        Call the action function associated with the button when clicked.
        """
        self.action() # Call the action function associated with the button when clicked.

    def draw(self, screen):
        """
        Draw the button on the screen with the appropriate color and text.
        
        Args:
            screen: The Pygame surface where the button will be drawn.
            mouse_pos: The current position of the mouse (x, y), used to determine hover state.
        """
        # Determine which color to use based on whether the mouse is hovering over the button
        color = self.hover_color if self.is_hovered() else self.normal_color

        # Draw the button as a rectangle with the chosen color
        pygame.draw.rect(screen, color, self.rect)

        # Render the text in white and center it inside the button
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = self.rect.center

        # Blit the text onto the screen
        screen.blit(text_surface, text_rect)
