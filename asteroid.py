from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        random_angle1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
        random_angle2 = pygame.math.Vector2.rotate(self.velocity, -abs(random_angle))
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        new_asteroid1.velocity = random_angle1 * 1.2
        new_asteroid2.velocity = random_angle2 * 1.2

        

