from UI.Menus.base_menu import Menu
class GameOverMenu(Menu):
    def __init__(self, game):
        button_data = [
            ("Main Menu", self.back_to_main_menu),
            ("Exit", self.exit_game)
        ]
        super().__init__(game, "Game Over", button_data)  # Call the parent class's constructor
    
    def back_to_main_menu(self):
        """
        Action to return to the main menu when 'Main Menu' button is clicked.
        This changes the current menu to the "MainMenu".
        """
        self.game.state_manager.states["Game_State"].exit(exiting_game=True)
        self.game.state_manager.change_state("Menu_State")
        self.game.state_manager.current_state.change_menu("MainMenu")

    def exit_game(self):
        """
        Action to exit the game when 'Exit' button is clicked.
        Sets the game’s running state to False, which will stop the game loop.
        """
        self.game.running = False
