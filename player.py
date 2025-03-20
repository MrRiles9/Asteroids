import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, shots_group):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots_group = shots_group
        self.shoot_cooldown = 0
        self.shoot_delay = 0.3

        self.shield_active = True
        self.shield_duration = 3.0
        self.shield_timer = 0
        self.shield_max_breaks = 10       

    def triangle(self):
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
            a = self.position + forward * self.radius
            b = self.position - forward * self.radius - right
            c = self.position - forward * self.radius + right
            return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)


        if self.shield_active:
            shield_radius = self.radius * 1.5
            pygame.draw.circle(screen, "cyan", self.position, shield_radius, 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:
                self.rotate(-dt)
            if keys[pygame.K_d]:
                self.rotate(dt)
            if keys[pygame.K_w]:
                self.move(dt)
            if keys[pygame.K_s]:
                self.move(-dt)    
  
            if self.shoot_cooldown >0:
                self.shoot_cooldown -= dt
            if keys[pygame.K_SPACE] and self.shoot_cooldown <= 0:
                self.shoot()
                self.shoot_cooldown = self.shoot_delay
                
            if self.shield_active:
                self.shield_timer -= dt
                if self.shield_timer <= 0:
                    self.shield_active = False
                    self.shield_break_count = 0
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y = 0

    def shoot(self):
        shot_position = pygame.Vector2(self.position)
        velocity = pygame.Vector2(0, 1)
        velocity = velocity.rotate(self.rotation)
        velocity = velocity * PLAYER_SHOOT_SPEED
        
        new_shot = Shot(shot_position, velocity)
        self.shots_group.add(new_shot)

    def collides_with(self, other):
        distance = (self.position - other.position).length()
        return distance < self.radius + other.radius

    def handle_collision(self):
        if self.shield_active:
            self.shield_active = False
            self.shield_timer = 0
        else:
            self.respawn_with_shield()

    def respawn_with_shield(self):
        self.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.rotation = 0
        self.shield_active = True
        self.shield_timer = self.shield_duration
