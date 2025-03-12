class StateManager:
    """
    Manages different game states and handles state transitions.
    """

    def __init__(self):
        """
        Initializes the state manager.
        
        Attributes:
            states (dict): A dictionary storing available states by name.
            current_state (State or None): The active game state.
        """
        self.states = {}  # Stores states with their names as keys
        self.current_state = None  # Tracks the active state

    def add_state(self, state_name, state):
        """
        Adds a new state to the state manager.

        Args:
            state_name (str): The name of the state.
            state (State): The state object to add.
        """
        self.states[state_name] = state

    def change_state(self, new_state):
        """
        Changes the current game state.

        Args:
            new_state (str): The name of the new state to switch to.

        If a state transition occurs, it calls `exit()` on the old state
        and `enter()` on the new state.
        """
        if new_state in self.states:
            if self.current_state:
                self.current_state.exit()  # Exit the current state
            self.current_state = self.states[new_state]  # Switch to the new state
            self.current_state.enter()  # Initialize the new state

    def update(self, events):
        """
        Updates the current state.

        Args:
            events (list): A list of events (e.g., input events).
        """
        if self.current_state:
            self.current_state.update(events)  # Call the state's update method

    def draw(self, screen):
        """
        Draws the current state to the screen.

        Args:
            screen: The surface where the game is rendered.
        """
        if self.current_state:
            self.current_state.draw(screen)  # Call the state's draw method