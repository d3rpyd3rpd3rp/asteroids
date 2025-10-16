import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.x, self.y), 2)
    
    def update(self, dt):
        self.x = self.velocity.x * dt
        self.y = self.velocity.y * dt