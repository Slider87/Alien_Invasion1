import sys

import pygame


def check_events(ship):
    """Respond to key presses and mouse events."""
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_RIGHT:
                # Move ship to the right
                ship.moving_right = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                # Stop ship moving
                ship.moving_right = False


def update_screen(ai_settings, screen, ship):
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
