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
    large_font = pygame.font.SysFont(None, 64)
    GAME_STATE_PLAYING = 0
    GAME_STATE_GAME_OVER = 1
    game_state = GAME_STATE_PLAYING
    lives = 3
    score = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    leaderboard = []
    try:
        with open("leaderboard.txt", "r") as f:
            for line in f:
                leaderboard.append(int(line.strip()))
    except FileNotFoundError:
        pass

    def reset_game():
        nonlocal lives, game_state, player, asteroid_field
        lives = 3
        game_state = GAME_STATE_PLAYING

        updateable.empty()
        drawable.empty()
        asteroids.empty()
        shots_group.empty()

        asteroid_field = AsteroidField()
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots_group)

    def draw_game_over_screen():
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        is_new_high_score = False
        if not leaderboard or score > max(leaderboard, default=0):
            is_new_high_score = True

        game_over_text = large_font.render("GAME OVER", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(game_over_text, game_over_rect)

        if is_new_high_score:
            score_text = font.render(f"NEW HIGH SCORE! {score}", True, (255, 255, 0))
        else:
            score_text = font.render(f"Your score: {score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 2 // 3))
        screen.blit(score_text, score_rect)

        restart_text = font.render("Press ENTER to play again", True, (255, 255, 255))
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 4))
        screen.blit(restart_text, restart_rect)

        if leaderboard or is_new_high_score:
            displayed_scores = list(leaderboard) if leaderboard else []

            if is_new_high_score and score not in displayed_scores:
                displayed_scores.append(score)

            top_scores = sorted(leaderboard, reverse=True)[:3]
            top_y = SCREEN_HEIGHT // 8
            leaderboard_text = font.render("Top Scores:", True, (255, 255, 255))
            leaderboard_rect = leaderboard_text.get_rect(center=(SCREEN_WIDTH // 2, top_y))
            screen.blit(leaderboard_text, leaderboard_rect)

            y_offset = top_y + 40
            for i, top_score in enumerate(top_scores):
                entry = font.render(f"{i+1}. {top_score}", True, (255, 255, 0))
                entry_rect = entry.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
                screen.blit(entry, entry_rect)
                y_offset += 30

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
                if score > 0:
                    leaderboard.append(score)
                    with open("leaderboard.txt", "w") as f:
                        for s in leaderboard:
                            f.write(f"{s}\n")
                running = False
        
            if game_state == GAME_STATE_GAME_OVER and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if score > 0:
                        leaderboard.append(score)
                        with open("leaderboard.txt", "w") as f:
                            for s in leaderboard:
                                f.write(f"{s}\n")
                    score = 0
                    reset_game()

        dt = clock.tick(60) / 1000
    
        if game_state == GAME_STATE_PLAYING:

            updateable.update(dt)
        
            for asteroid in asteroids:
                if player.is_colliding(asteroid):
                    lives -= 1
                    if lives <= 0:
                        print("Game Over!")
                        game_state = GAME_STATE_GAME_OVER
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
                       
                       bullet.kill()
                       
                       if asteroid.radius > ASTEROID_MIN_RADIUS * 2:
                           score += 20
                       elif asteroid.radius > ASTEROID_MIN_RADIUS:
                           score += 50
                       else:
                           score += 100

                       asteroid.split()
                   
                       break
        
        
        screen.fill((0, 0, 0))
        
        lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
        screen.blit(lives_text, (20, 20))

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (20, 60))        

        for drawable_object in drawable:
            drawable_object.draw(screen)

        if game_state == GAME_STATE_GAME_OVER:
            draw_game_over_screen()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
