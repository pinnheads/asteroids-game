import pygame

from constants import (SCREEN_HEIGHT, SCREEN_WIDTH, ASTEROID_SCORES,
                       HIGH_SCORE_FILE)
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_state, log_event


def load_high_score():
    try:
        with open(HIGH_SCORE_FILE) as f:
            return int(f.read().strip())
    except (OSError, ValueError):
        return 0


def save_high_score(value):
    try:
        with open(HIGH_SCORE_FILE, "w") as f:
            f.write(str(value))
    except OSError:
        pass


def draw_text(screen, font, text, center, color="white"):
    surface = font.render(text, True, color)
    screen.blit(surface, surface.get_rect(center=center))


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
    title_font = pygame.font.Font(None, 96)
    menu_font = pygame.font.Font(None, 40)
    hud_font = pygame.font.Font(None, 36)
    center_x = SCREEN_WIDTH / 2
    center_y = SCREEN_HEIGHT / 2

    # Create Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    def new_game():
        """Clear the world and spawn a fresh player and asteroid field"""
        for group in (updatable, drawable, asteroids, shots):
            for sprite in group.sprites():
                sprite.kill()
        AsteroidField()
        return Player(center_x, center_y)

    player = new_game()
    score = 0
    high_score = load_high_score()
    # One of "start", "playing", "paused", "game_over"
    state = "start"

    # Use an infinite loop for the game loop
    # NOTE: Game Loop - https://gameprogrammingpatterns.com/game-loop.html
    while (True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type != pygame.KEYDOWN:
                continue
            if state == "start" and event.key in (pygame.K_RETURN, pygame.K_SPACE):
                state = "playing"
            elif state == "game_over" and event.key == pygame.K_RETURN:
                player = new_game()
                score = 0
                state = "playing"
            elif state == "playing" and event.key in (pygame.K_p, pygame.K_ESCAPE):
                state = "paused"
            elif state == "paused":
                if event.key in (pygame.K_p, pygame.K_ESCAPE, pygame.K_RETURN):
                    state = "playing"
                elif event.key == pygame.K_q:
                    return

        # Create screen
        screen.fill("black")

        if state == "playing":
            updatable.update(dt)

            # check if player collided with an asteroid
            for asteroid in asteroids:
                if player.collides_with(asteroid):
                    log_event("player_hit", score=score)
                    state = "game_over"
                    if score > high_score:
                        high_score = score
                        save_high_score(high_score)
                    break

            # check if asteroid is shot by player
            for asteroid in asteroids:
                for shot in shots:
                    if shot.collides_with(asteroid):
                        log_event("asteroid_shot")
                        shot.kill()
                        score += ASTEROID_SCORES.get(asteroid.radius, 10)
                        asteroid.split()

        # draw all objects in drawable group
        for sprite in drawable:
            sprite.draw(screen)

        # HUD
        screen.blit(hud_font.render(f"Score: {score}", True, "white"), (20, 15))
        high_surface = hud_font.render(
            f"High Score: {max(score, high_score)}", True, "white")
        screen.blit(high_surface, high_surface.get_rect(
            topright=(SCREEN_WIDTH - 20, 15)))

        # Overlays
        if state == "start":
            draw_text(screen, title_font, "ASTEROIDS",
                      (center_x, center_y - 80))
            draw_text(screen, menu_font, "Press ENTER or SPACE to start",
                      (center_x, center_y))
            draw_text(screen, hud_font,
                      "W/S thrust   A/D rotate   SPACE shoot   P pause",
                      (center_x, center_y + 60), "gray")
        elif state == "paused":
            draw_text(screen, title_font, "PAUSED", (center_x, center_y - 40))
            draw_text(screen, menu_font, "P / ESC / ENTER to resume   Q to quit",
                      (center_x, center_y + 30))
        elif state == "game_over":
            draw_text(screen, title_font, "GAME OVER",
                      (center_x, center_y - 60))
            draw_text(screen, menu_font, f"Final score: {score}",
                      (center_x, center_y + 10))
            draw_text(screen, menu_font, "Press ENTER to play again",
                      (center_x, center_y + 60))

        # Refersh the screen
        pygame.display.flip()

        # calculate delta time
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
