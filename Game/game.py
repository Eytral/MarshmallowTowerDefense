import pygame
from Constants import config

# Manages main game loop and window management
class Game():
    def __init__(self):
        # Initialize pygame and set up the game window
        pygame.init() 
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption("Marsh Tower Defense") 
        self.clock = pygame.time.Clock() # Initialise Clock to manage frame rate
        self.running = True # Run game
    
    def run(self):
        # Main game loop
        while self.running:
            try:
                events = pygame.event.get()  # Get all the events that have occurred
                for event in events:
                    if event.type == pygame.QUIT:  # Closes window
                        self.running = False

                self.screen.fill((0, 0, 0))  # Clears Screen (black)

                pygame.display.flip()  # Update Screen
                self.clock.tick(60)  # Maintain 60fps frame rate

            except Exception as e:
                # Stops game and prints error if error detected
                print(f"Error: {e} has occurred")
                self.running = False
