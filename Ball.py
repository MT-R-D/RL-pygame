import pygame
import random


class Ball:
    def __init__(self, x, y, radius, color, speed, cooldown_range):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.cooldown_range = cooldown_range
        self.cooldown = 0

    def render(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def spawn(self, screen_width):
        self.cooldown = random.randint(
            self.cooldown_range[0], self.cooldown_range[1])
        self.y = 0
        self.x = random.randint(self.radius, screen_width - self.radius)

    def move(self, screen_width, screen_height) -> int:
        if self.cooldown != 0:
            self.cooldown -= 1
            return
        self.y += self.speed
        if self.y >= screen_height:
            self.spawn(screen_width)
            return -1
        return 0


__all__ = ['Ball']
