# Asteroids
Asteroids Clone
A classic Asteroids arcade game clone built with Python and Pygame.

Game Description
This is a faithful recreation of the iconic Asteroids game where players control a triangular spaceship and must destroy asteroids while avoiding collisions. Features include:

Ship rotation and thrust-based movement
Screen wrapping for both the player ship and asteroids
Shooting mechanics with cooldown
Asteroid splitting - large asteroids break into medium ones, medium into small ones
Progressive difficulty as you clear asteroids
Requirements
Python 3.x
Pygame
Installation
Clone this repository:
git clone https://github.com/mrriles9/asteroids.git
cd asteroids

Install the required packages:
pip install pygame

How to Play
Run the game:

python main.py

Controls
W: Thrust forward
S: Thrust backward
A: Rotate counterclockwise
D: Rotate clockwise
SPACE: Fire
Game Rules
Destroy asteroids by shooting them with your ship's bullets
Large asteroids split into two medium asteroids when hit
Medium asteroids split into two small asteroids when hit
Small asteroids disappear when hit
Avoid colliding with asteroids to survive
Implementation Details
The game uses Pygame for rendering and collision detection. Key features:

Object-oriented design with separate classes for Player, Asteroid, Shot, etc.
Circular hitboxes for accurate collision detection
Vector-based physics for realistic movement
Screen wrapping to simulate infinite space
Asteroid splitting system with varied trajectories
Future Improvements
Potential enhancements could include:

Score tracking system
Lives and game over states
UFO enemies
Sound effects and music
Power-ups and special weapons
Acknowledgements
This game was created as a learning project following the classic arcade game Asteroids by Atari.

Feel free to modify and extend the game as you wish!
