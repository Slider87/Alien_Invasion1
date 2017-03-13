import pygame


class Ship:
    def __init__(self, screen):
        """Initialize the ship and its starting position"""
        self.screen = screen

        # load the ship image and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Movement flag
        self.moving_right = False

    def update(self):
        """Updating the ships position based on the movement flag."""
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        """Draw the ship a its current location"""
        self.screen.blit(self.image, self.rect)