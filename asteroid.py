from circleshape import *
import pygame
import random
import math
from constants import *

class Asteroid(CircleShape):
    containers = None
    def __init__(self, x, y, radius=None, size=None):
        if radius is not None:
            self.size = "LARGE"
            if radius >= 40:
                self.size = "LARGE"
            elif radius >= 25:
                self.size = "MEDIUM"
            else:
                self.size = "SMALL"
        elif size is not None:
            if size == "LARGE":
                self.radius = 40
                self.size = "LARGE"
            elif size == "MEDIUM":
                self.radius = 25
                self.size = "MEDIUM"
            elif size == "SMALL":
                self.radius = 15
                self.size = "SMALL"
        else:
            self.radius = 40
            self.size = "LARGE"
        
        super().__init__(x, y, radius)
        
        # Add self to container groups
        if Asteroid.containers:
            for container in Asteroid.containers:
                container.add(self)

        self.shape = self.generate_asteroid_shape(self.radius)
        
        if self.velocity.x == 0 and self.velocity.y == 0:
            speed = random.uniform(20, 50)
            angle = random.uniform(0, 2 * math.pi)   
            self.velocity.x = math.cos(angle) * speed
            self.velocity.y = math.sin(angle) * speed
    

    def generate_asteroid_shape(self, radius, jaggedness=0.4, num_points=8):
        points = []
        for i in range(num_points):
            angle = (i / num_points) * math.pi * 2
            distance = radius + random.uniform(-radius * jaggedness, radius * jaggedness)
            x = math.cos(angle) * distance
            y = math.sin(angle) * distance
            points.append((x, y))
        return points


    def draw(self, surface):
        
        shifted_points = [
            (self.position.x + x, self.position.y + y) for x, y in self.shape
        ]
        pygame.draw.polygon(surface, (255, 255, 255), shifted_points, 2)
        
        
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
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        

        # Create two smaller asteroids
        new_asteroid1 = Asteroid(self.position.x, self.position.y, radius=new_radius)
        new_asteroid1.velocity = new_velocity1

        new_asteroid2 = Asteroid(self.position.x, self.position.y, radius=new_radius)
        new_asteroid2.velocity = new_velocity2
        
