import pygame

from Game import Game
import numpy as np


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 30


player_score = 0
player_x = SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2  # Center the player horizontally
player_y = SCREEN_HEIGHT - PLAYER_HEIGHT - \
    10   # Position the player near the bottom
player_speed = 10


game = Game(screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT,
            player_width=PLAYER_WIDTH, player_height=PLAYER_HEIGHT,
            player_hover_level=10, player_speed=player_speed, ball_count=1,
            ball_radius=10, ball_speed=10, ball_cooldown_range=[10, 30], FPS=30)


game.start()

game.quit()

# pygame setup
