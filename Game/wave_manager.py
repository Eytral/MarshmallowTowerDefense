from Constants import config  # Import game configuration settings
from Entities.Enemies.base_enemy import Enemy  # Import the base enemy class
from Game.spawning_data import SPAWNING_DATA, ENEMY_CLASS_MAP
import math
import random

class WaveManager:
    """
    Manages enemy waves in the game.

    Attributes:
        game: Reference to the main game object, allowing access to shared resources.
        initial_wave_count: Number of enemies in the first wave.
        wave_enemy_spawn_increase: Number of additional enemies per wave.
    """

    def __init__(self, game):
        """
        Initializes the WaveManager.

        Args:
            game: Reference to the main game object.
            initial_wave_count: Number of enemies in the first wave.
            wave_enemy_spawn_increase: Additional enemies added per wave.
        """
        self.wave_number = 0  # Tracks the current wave number
        self.spawn_interval = 50  # Time between enemy spawns (in frames/ticks)
        self.spawn_cooldown = 0  # Countdown timer for enemy spawning
        self.wave_ongoing = False  # Flag indicating whether a wave is currently active
        self.game = game  # Stores reference to the game instance
        self.difficulty = "Normal"

        self.accumulated_spawns = {enemy_name: count for enemy_name, count in SPAWNING_DATA[self.difficulty]["Default_Spawn"].items()}
        self.enemy_spawn_queue = []

    def create_enemy(self, enemy_name):
        enemy_class = ENEMY_CLASS_MAP.get(enemy_name)
        if enemy_class:
            return enemy_class(self.game.state_manager.current_state.map.enemy_start_pos, self.game.state_manager.current_state.map.enemy_path)

    def create_enemy_spawn_queue(self, spawn_wave):
        for enemy_name, count in spawn_wave.items():
            for _ in range(int(count)):
                self.enemy_spawn_queue.append(enemy_name)
        random.shuffle(self.enemy_spawn_queue)

    def initialise_next_spawn_wave(self):
            if self.wave_number != 1:
                for enemy_name, increment in SPAWNING_DATA[self.difficulty]["Increment"].items():
                    self.accumulated_spawns[enemy_name] += increment
                    print(f"accumulated spawns data straight after update is: {self.accumulated_spawns}")

            spawn_wave = {enemy_name: math.floor(count) for enemy_name, count in self.accumulated_spawns.items()}
            self.create_enemy_spawn_queue(spawn_wave)
            print(f"spawn wave is: {spawn_wave}, accumulated spawns data is: {self.accumulated_spawns}")

    def spawn_enemies(self):
        """
        Spawns enemies at regular intervals if there are more to be spawned.
        """
        if len(self.enemy_spawn_queue) > 0:
            if self.spawn_cooldown == 0:
                enemy_name = self.enemy_spawn_queue[0] # Spawn first enemy in queue
                del self.enemy_spawn_queue[0]
                enemy = self.create_enemy(enemy_name) # Create a new enemy at the designated start position
                self.game.state_manager.current_state.enemies.append(enemy)  # Add enemy to the game state
                self.spawn_cooldown = self.spawn_interval  # Reset cooldown timer
            else:
                self.spawn_cooldown -= 1  # Reduce cooldown timer until next spawn
        else:
            self.wave_ongoing = False  # Ends the wave once all enemies are spawned

    def start_wave(self):
        """
        Starts a new wave by Marking the wave as active.
        """
        self.initialise_next_spawn_wave()
        self.wave_ongoing = True  # Mark the wave as active

    def next_wave(self):
        """
        Increases difficulty and starts the next wave if the current one has ended.
        """
        if not self.wave_ongoing:
            print("Starting next wave")
            self.wave_number += 1  # Increment wave number
            self.start_wave()  # Begin the new wave
        else:
            print(f"Cannot start next wave yet! Current wave is still ongoing")  # Prevents starting a new wave mid-wave

    def update(self):
        """
        Updates the wave state and spawns enemies if a wave is ongoing.
        """
        if self.wave_ongoing:
            self.spawn_enemies()

    def reset_waves(self):
        """
        Resets all wave-related parameters, typically used when restarting the game.
        """
        self.wave_number = 1  # Reset wave number to the first wave
        self.spawn_interval = 200  # Reset the time between enemy spawns
        self.spawn_cooldown = 0  # Reset the cooldown for enemy spawning
        self.wave_ongoing = False  # Mark the wave as inactive
        self.accumulated_spawns = {enemy_name: count for enemy_name, count in SPAWNING_DATA[self.difficulty]["Default_Spawn"].items()} # Reset Spawn Counter
        self.enemy_spawn_queue = [] # Clear Spawn Queue
