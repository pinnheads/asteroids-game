import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_state


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
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Create Player instance
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    asteroid_field = AsteroidField()

    # Use an infinite loop for the game loop
    # NOTE: Game Loop - https://gameprogrammingpatterns.com/game-loop.html
    while (True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # calculate delta time
        time_passed = clock.tick(60)
        dt = time_passed / 1000

        # Create screen
        screen.fill("black")

        # Draw player on screen
        updatable.update(dt)
        for player in drawable:
            player.draw(screen)

        # Refersh the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
