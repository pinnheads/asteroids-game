import pygame
import random

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        """Draw an asteroid object on the screen"""
        pygame.draw.circle(screen, "white", self.position,
                           self.radius, LINE_WIDTH)

    def update(self, dt):
        """Move asteroid in a straight line"""
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        new_vel_1 = self.velocity.rotate(angle)
        new_vel_2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(
            self.position.x, self.position.y, new_radius)
        new_asteroid_2 = Asteroid(
            self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = new_vel_1 * 1.2
        new_asteroid_2.velocity = new_vel_2 * 1.2
