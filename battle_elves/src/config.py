# Configuration settings for the game

GAME_WIDTH = 800
GAME_HEIGHT = 600
FPS = 60

# Player settings
PLAYER_SPEED = 5
PLAYER_HEALTH = 5

# Enemy settings
ENEMY_SPAWN_RATE = 3  # in seconds
ENEMY_TYPES = {
    "level1": {
        "health": 1,
        "speed": 2,
        "fire_rate": 3
    },
    "level2": {
        "health": 2,
        "speed": 3,
        "fire_rate": 3
    },
    "level3": {
        "health": 2,
        "speed": 3,
        "fire_rate": 1.5
    }
}

# Level settings
LEVEL_TIMES = {
    1: 90,  # 1.5 minutes in seconds
    2: 180  # 3 minutes in seconds
}

# Global dictionary to store frames
FRAMES = {}