import random

def generate_random_array(rows=10, cols=10):
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]


MAP_DATA = {
    "Marsh_Mallows": {
        "grid": [
            [0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ],
        "background": "motivational_quote.png",
        "music": "forest_theme.mp3"
    },
    "Rando_Mallows": {
        "grid": generate_random_array(),
        "background": "motivational_quote.png",
        "music": "forest_theme.mp3"
    }
}

