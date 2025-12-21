import sys
import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_state, log_event


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Start pygame
    pygame.init()

    # Create screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    # Create Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()

    # Create Player instance
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Use an infinite loop for the game loop
    # NOTE: Game Loop - https://gameprogrammingpatterns.com/game-loop.html
    while (True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Create screen
        screen.fill("black")

        updatable.update(dt)

        # check if player collided with an asteroid
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game Over!")
                sys.exit(1)

        # check if asteroid is shot by player
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

        # draw all objects in drawable group
        for sprite in drawable:
            sprite.draw(screen)

        # Refersh the screen
        pygame.display.flip()

        # calculate delta time
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
