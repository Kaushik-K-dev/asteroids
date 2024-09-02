from circleshape import CircleShape
import pygame
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        vec1 = self.velocity.rotate(angle)
        vec2 = self.velocity.rotate(-angle)
        Ast1 = Asteroid(self.position[0], self.position[1], self.radius-ASTEROID_MIN_RADIUS)
        Ast1.velocity = vec1 * 1.2
        Ast2 = Asteroid(self.position[0], self.position[1], self.radius-ASTEROID_MIN_RADIUS)
        Ast2.velocity = vec2 * 1.2      

    
    