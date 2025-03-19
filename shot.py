import pygame
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = velocity

    def update(self, time_delta):
        self.position.x += self.velocity.x * time_delta
        self.position.y += self.velocity.y * time_delta

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), SHOT_RADIUS)
