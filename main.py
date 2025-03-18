import pygame
from constants import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

print("Starting Asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

def __main__():
	if __name__ == "__main__":
    		main()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	screen.fill((0, 0, 0))
	pygame.display.flip()

pygame.quit()
