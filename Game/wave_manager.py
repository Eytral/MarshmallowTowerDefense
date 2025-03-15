from Constants import config  # Import game configuration settings
from Entities.Enemies.base_enemy import Enemy  # Import the base enemy class

class WaveManager:
    """
    Manages enemy waves in the game.

    Attributes:
        game: Reference to the main game object, allowing access to shared resources.
        initial_wave_count: Number of enemies in the first wave.
        wave_enemy_spawn_increase: Number of additional enemies per wave.
    """

    def __init__(self, game, initial_wave_count=5, wave_enemy_spawn_increase=2):
        """
        Initializes the WaveManager.

        Args:
            game: Reference to the main game object.
            initial_wave_count: Number of enemies in the first wave.
            wave_enemy_spawn_increase: Additional enemies added per wave.
        """
        self.wave_number = 1  # Tracks the current wave number
        self.enemy_count = initial_wave_count  # Number of enemies in the current wave
        self.initial_wave_count = initial_wave_count  # Stores the initial enemy count for resets
        self.wave_enemy_spawn_increase = wave_enemy_spawn_increase  # Defines how many more enemies spawn per wave
        self.enemies_spawned = 0  # Tracks how many enemies have been spawned so far
        self.spawn_interval = 200  # Time between enemy spawns (in frames/ticks)
        self.spawn_cooldown = 0  # Countdown timer for enemy spawning
        self.wave_ongoing = False  # Flag indicating whether a wave is currently active
        self.game = game  # Stores reference to the game instance

    def spawn_enemies(self):
        """
        Spawns enemies at regular intervals if there are more to be spawned.
        """
        if self.enemies_spawned < self.enemy_count:
            if self.spawn_cooldown == 0:
                # Create a new enemy at the designated start position
                enemy = Enemy(
                    self.game.state_manager.current_state.map.enemy_start_pos,
                    self.game.state_manager.current_state.map.enemy_path
                )
                self.game.state_manager.current_state.enemies.append(enemy)  # Add enemy to the game state
                self.enemies_spawned += 1  # Increase the count of spawned enemies
                self.spawn_cooldown = self.spawn_interval  # Reset cooldown timer
            else:
                self.spawn_cooldown -= 1  # Reduce cooldown timer until next spawn
        else:
            self.wave_ongoing = False  # Ends the wave once all enemies are spawned

    def start_wave(self):
        """
        Starts a new wave by resetting enemy count and marking the wave as active.
        """
        self.enemies_spawned = 0  # Reset the count of spawned enemies
        self.wave_ongoing = True  # Mark the wave as active

    def next_wave(self):
        """
        Increases difficulty and starts the next wave if the current one has ended.
        """
        if not self.wave_ongoing:
            print("Starting next wave")
            if self.wave_number != 1:
                self.wave_number += 1  # Increment wave number
                self.enemy_count += self.wave_enemy_spawn_increase  # Increase the number of enemies for this wave
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
        self.enemy_count = self.initial_wave_count  # Reset enemy count to its initial value
        self.enemies_spawned = 0  # Reset the number of spawned enemies
        self.spawn_interval = 200  # Reset the time between enemy spawns
        self.spawn_cooldown = 0  # Reset the cooldown for enemy spawning
        self.wave_ongoing = False  # Mark the wave as inactive
