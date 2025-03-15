from States.base_state import State
from Game.map import Map 
from Game.mouse import Mouse
import pygame
from Constants import config
from Entities.Towers.base_tower import Tower
from UI.tower_selection_panel import TowerSelectionMenu
from Game.wave_manager import WaveManager
from UI.in_game_buttons import GameButtons

class Game_State(State):
    """Main game engine - Manages the in-game logic, events, and rendering"""

    def __init__(self, game):
        """
        Initializes the Game_State.
        
        Args:
            game: Reference to the main game object, allowing access to shared resources.
        """

        super().__init__(game)  # Call the parent State class constructor
        self.map = None
        self.mouse = Mouse()
        self.towers = {}
        self.towerselectionpanel = TowerSelectionMenu(self.game)
        self.gamebuttons = GameButtons(self.game)
        self.enemies = []
        self.wave_manager = WaveManager(self.game)


    # -- STATE HANDLING --
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

    def exit(self, **kwargs):
        exiting_game = kwargs.get("exiting_game", True)
        if exiting_game:
            self.map.reset_map()
            self.enemies = []
            self.towers = {}
            self.wave_manager.reset_waves()
            print("Game successfully exited")



    # -- RENDERING --
    def draw(self, screen):
        """
        Handles rendering the game to the screen.

        Args:
            screen: pygame display surface
        """
        self.map.draw(screen, self.mouse.map_grid_x, self.mouse.map_grid_y) #placeholder values for mouse grid position
        self.draw_towers(screen)
        self.draw_enemies(screen)
        self.towerselectionpanel.draw(screen)
        self.gamebuttons.draw(screen)


    def draw_towers(self, screen):
        for _, tower in self.towers.items():
            tower.draw(screen)

    def draw_enemies(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def draw_debug_info(self, screen):
        """
        Draws debug information relevant to game state:
        Mouse map_grid_pos: Shows the grid index the mouse is hovering over

        Args:
            screen: pygame display surface
        """
        super().draw_debug_info(screen)
        mouse_map_grid_text = self.debug_font.render(f"Mouse map_grid_pos: {(self.mouse.map_grid_x, self.mouse.map_grid_y)}", True, (255, 255, 255))
        screen.blit(mouse_map_grid_text, (config.DEBUG_TEXT_X,config.DEBUG_MOUSEGRIDTEXT_POS))


    # -- EVENT HANDLING --
    def update(self, events):
            """
            Updates the game based on player input and game logic.
            
            Args:
                events: A list of input events (e.g., keyboard/mouse actions).
            """
            self.mouse.update_mouse_pos()
            self.handle_events(events)  # Process player input and other events
            self.update_enemies()
            self.wave_manager.update()
            self.update_towers()


    def handle_events(self, events):
        """
        Handles user input and other event-driven behavior.
        
        Args:
            events: A list of events such as key presses or mouse clicks.
        """
        for event in events:
    
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.towerselectionpanel.buttons:
                    if button.is_hovered():
                        button.click()
                
                for button in self.gamebuttons.buttons:
                    if button.is_hovered():
                        button.click()

                if self.mouse.current_action == "Placing Tower":
                    self.place_tower()

                if self.mouse.current_action == "Removing Tower":
                    self.remove_tower()

    def update_enemies(self):
        for enemy in self.enemies:
            enemy.update()
            if enemy.is_dead or enemy.reached_end:
                self.enemies.remove(enemy)
                print(f"Enemy has been removed")

    def update_towers(self):
        for _, tower in self.towers.items():
            tower.update(self.enemies)

    def place_tower(self):
        """
        Places a tower on the map grid and adds the selected tower to the game_state tower dict
        """
        if self.map.place_tower(self.mouse.map_grid_x, self.mouse.map_grid_y): # If able to place tower
            self.towers[(self.mouse.map_grid_x, self.mouse.map_grid_y)] = self.mouse.current_selection(self.mouse.map_grid_x, self.mouse.map_grid_y) # Create new tower object
            print(f"successfully placed tower, tower list is{self.towers}") # print dictionary of towers for debugging purposes
            self.mouse.change_current_action(None, None) # Reset mouse action and selection


    def remove_tower(self): # If able to remove tower
        """
        Removes a tower on the map grid and removes the selected tower from the game_state tower dict
        """
        if self.map.remove_tower(self.mouse.map_grid_x, self.mouse.map_grid_y):
            del self.towers[(self.mouse.map_grid_x, self.mouse.map_grid_y)] # Delete selected tower object (at selected map coordinate)
            print(f"successfully deleted tower, tower list is{self.towers}") # print dictionary of towers for debugging purposes
            self.mouse.change_current_action(None, None) # Reset mouse action and selection