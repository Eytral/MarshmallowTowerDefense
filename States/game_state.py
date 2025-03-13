from States.base_state import State
from Game.map import Map 

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
        self.map = Map("Marsh_Mallows")


    def update(self, events):
        """
        Updates the game based on player input and game logic.
        
        Args:
            events: A list of input events (e.g., keyboard/mouse actions).
        """
        self.handle_events(events)  # Process player input and other events


    def enter(self, level_number):
        """
        Enters the Game_state, setting the level that will be played, and calling the load level function to load such level

        Args:
            level_number: integer number representing the level that is being loaded
        """
        self.level = level_number
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
        self.map.draw(screen, 0 ,0) #placeholder values for mouse grid position
        pass  # Placeholder for rendering logic

    def handle_events(self, events):
        """
        Handles user input and other event-driven behavior.
        
        Args:
            events: A list of events such as key presses or mouse clicks.
        """
        pass  # Placeholder for event handling logic
