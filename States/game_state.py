from States.base_state import State
from Game.map import Map 
from Game.mouse import Mouse
import pygame

class Game_State(State):
    """Main game engine - Manages the in-game logic, events, and rendering"""

    def __init__(self, game):
        """
        Initializes the Game_State.
        
        Args:
            game: Reference to the main game object, allowing access to shared resources.
        """

        super().__init__(game)  # Call the parent State class constructor
        self.level = None
        self.map = None
        self.mouse = Mouse()


    def update(self, events):
        """
        Updates the game based on player input and game logic.
        
        Args:
            events: A list of input events (e.g., keyboard/mouse actions).
        """
        self.mouse.update_mouse_pos()
        self.handle_events(events)  # Process player input and other events


    def enter(self, *args):
        """
        Enters the Game_state, setting the level that will be played, and calling the load level function to load such level

        Args:
            level_number: integer number representing the level that is being loaded
        """
        if args:
            level_name = args[0]
            self.level = level_name
            self.map = Map(level_name)
            print(f"Entering level {self.level}")

        self.load_level()

    def load_level(self):
        pass

    def draw(self, screen):
        """
        Handles rendering the game to the screen.

        Args:
            screen: pygame display surface
        """
        self.map.draw(screen, self.mouse.map_grid_x, self.mouse.map_grid_y) #placeholder values for mouse grid position
        pass  # Placeholder for rendering logic

    def handle_events(self, events):
        """
        Handles user input and other event-driven behavior.
        
        Args:
            events: A list of events such as key presses or mouse clicks.
        """
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.game.state_manager.change_state("Pause_State")
        pass  # Placeholder for event handling logic
