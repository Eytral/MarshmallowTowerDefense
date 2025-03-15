from Constants import config
from Entities.Enemies.base_enemy import Enemy

class WaveManager:
    def __init__(self, game, initial_wave_count=5, wave_enemy_spawn_increase=2):
        self.map = map
        self.wave_number = 1
        self.enemy_count = initial_wave_count
        self.wave_enemy_spawn_increase = wave_enemy_spawn_increase
        self.enemies_spawned = 0
        self.spawn_interval = 200  # Time between enemy spawns
        self.spawn_cooldown = 0
        self.wave_ongoing = False
        self.game = game

    def spawn_enemies(self):
        """Spawn enemies at regular intervals."""
        print("Spawning enemy")

        if self.enemies_spawned < self.enemy_count:
            if self.spawn_cooldown == 0:
                enemy = Enemy(self.game.state_manager.current_state.map.enemy_start_pos, self.game.state_manager.current_state.map.enemy_path)  # Spawn enemy at the start point
                self.game.state_manager.current_state.enemies.append(enemy)
                self.enemies_spawned += 1
                self.spawn_cooldown = self.spawn_interval
            else:
                self.spawn_cooldown -= 1
        else:
            self.wave_ongoing = False


    def start_wave(self):
        """Begin spawning enemies for the current wave."""
        self.enemies_spawned = 0
        self.wave_ongoing = True

    def next_wave(self):
        """Increase difficulty for the next wave."""
        print("starting next wave")
        if self.wave_number != 1:
            self.wave_number += 1
            self.enemy_count += self.wave_increase  # Increase number of enemies per wave
        self.start_wave()

    def update(self):
        if self.wave_ongoing:
            self.spawn_enemies()
