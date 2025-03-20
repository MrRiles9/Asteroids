import pygame
import math

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, powerup_type, lifespan=10):
        super().__init__()
        self.position = pygame.math.Vector2(x, y)
        self.type = powerup_type
        self.active = True
        self.timer = lifespan
        if self.type == "extra_life":
             self.radius = 15
        elif self.type == "no_fire_rate_cap":
             self.radius = 10

        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self._render_powerup()

    def _render_powerup(self):
        if self.type == "extra_life":
            
            size = self.radius
            center = self.radius
            pygame.draw.rect(self.image, (0, 255, 0), (center - size, center - 4, size * 2, 8))
            pygame.draw.rect(self.image, (0, 255, 0), (center - 4, center - size, 8, size * 2))

        elif self.type == "no_fire_rate_cap":
            size = self.radius
            center = self.radius
            points = [
                (center, center - 5),      # Top of pistol
                (center + 15, center - 5), # Front barrel top
                (center + 15, center + 5), # Front barrel bottom
                (center + 5, center + 5),  # Handle start
                (center + 5, center + 15), # Handle bottom
                (center - 5, center + 15), # Back of handle
                (center - 5, center - 5)   # Back of gun
            ]
            pygame.draw.polygon(self.image, (255, 0, 0), points)

    def update(self, dt):
        self.timer -= dt
        if self.timer <= 0:
            self.active = False
