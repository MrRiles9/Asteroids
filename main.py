import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import random

def main():
    pygame.init()
    import sys
    
    font = pygame.font.SysFont(None, 36)

    lives = 3

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable, drawable)

    AsteroidField.containers = (updateable,)

    asteroid_field = AsteroidField()

    Player.containers = (updateable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots_group)

    Shot.containers = (shots_group, updateable, drawable)

    clock = pygame.time.Clock()
    dt = 0  

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        dt = clock.tick(60) / 1000
    
        updateable.update(dt)
        
        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                lives -= 1
                if lives <= 0:
                    print("Game Over!")
                    sys.exit()
                else:
                    print(f"Lives remaining: {lives}")
                    player.position.x = SCREEN_WIDTH / 2
                    player.position.y = SCREEN_HEIGHT / 2
                    if hasattr(player, 'velocity'):
                        player.velocity.x = 0
                        player.velocity.y = 0
                    break
        
        for asteroid in list(asteroids):
            
            for bullet in list(shots_group):
                if bullet.is_colliding(asteroid):
                   asteroid.kill()
                   bullet.kill()
                   asteroid.split()
                   
                   break
        
        
        screen.fill((0, 0, 0))
        
        lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
        screen.blit(lives_text, (20, 20))

        
        for drawable_object in drawable:
            drawable_object.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
