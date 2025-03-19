from circleshape import *
import pygame
import random
import math
from constants import *

class Asteroid(CircleShape):
    containers = None
    def __init__(self, x, y, size="LARGE", radius=None):
        if size == "LARGE":
            radius = 40
        elif size == "MEDIUM":
            radius = 25
        elif size == "SMALL":
            radius = 15
        else:
            radius = 40 
        self.size = size
        
        super().__init__(x, y, radius)
        
        # Add self to container groups
        if Asteroid.containers:
            for container in Asteroid.containers:
                container.add(self)
        
        if self.velocity.x == 0 and self.velocity.y == 0:
            speed = random.uniform(20, 50)
            angle = random.uniform(0, 2 * math.pi)   
            self.velocity.x = math.cos(angle) * speed
            self.velocity.y = math.sin(angle) * speed
    
    def draw(self, surface):
        pygame.draw.circle(
            surface,
            (255, 255, 255), 
            (self.position.x,
            self.position.y),
            self.radius,
            2
        )
        
    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
        
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH  
        elif self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT  
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y = 0

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(random_angle) * 1.2
        new_velocity2 = self.velocity.rotate(-random_angle) * 1.2

        if self.size == "LARGE":
            new_size = "MEDIUM"
        elif self.size == "MEDIUM":
            new_size = "SMALL"
        else:
            new_size = "SMALL"

        # Create two smaller asteroids
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_size)
        new_asteroid1.velocity = new_velocity1

        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_size)
        new_asteroid2.velocity = new_velocity2
        
