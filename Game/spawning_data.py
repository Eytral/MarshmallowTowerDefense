SPAWNING_DATA = {

# EASY /////////////////////////////////

    "Easy": {

    "Default_Spawn": {
        "marshmallow enemy": 3,
        "cracker enemy": 2,
        "white_chocolate enemy": 0,
        "dark_chocolate enemy": 0,
        "smore enemy": 0
        },

    "Increment": {
        "marshmallow enemy": 2,
        "cracker enemy": 1,
        "white_chocolate enemy": 0.5,
        "dark_chocolate enemy": 0.1,
        "smore enemy": 0.1
    }
    },

# NORMAL /////////////////////////////////

    "Normal": {

    "Default_Spawn": {
        "marshmallow enemy": 4,
        "cracker enemy": 3,
        "white_chocolate enemy": 1,
        "dark_chocolate enemy": 0,
        "smore enemy": 0
        },

    "Increment": {
        "marshmallow enemy": 3,
        "cracker enemy": 1.5,
        "white_chocolate enemy": 1,
        "dark_chocolate enemy": 0.2,
        "smore enemy": 0.2
    }

    },

# HARD /////////////////////////////////

        "Hard": {

        "Default_Spawn": {
        "marshmallow enemy": 5,
        "cracker enemy": 4,
        "white_chocolate enemy": 1.5,
        "dark_chocolate enemy": 0.5,
        "smore enemy": 0.25
        },

        "Increment": {

        "marshmallow enemy": 3.5,
        "cracker enemy": 2,
        "white_chocolate enemy": 1.25,
        "dark_chocolate enemy": 0.25,
        "smore enemy": 0.25
    }
    },
}

from Entities.Enemies.marshmallow_enemy import Marshmallow
from Entities.Enemies.cracker_enemy import Cracker
from Entities.Enemies.white_chocolate_enemy import WhiteChocolate
from Entities.Enemies.dark_chocolate_enemy import DarkChocolate
from Entities.Enemies.smore_enemy import Smore

ENEMY_CLASS_MAP = {
    "marshmallow enemy": Marshmallow,
    "cracker enemy": Cracker,
    "white_chocolate enemy": WhiteChocolate,
    "dark_chocolate enemy": DarkChocolate,
    "smore enemy": Smore,
}
