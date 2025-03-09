import pygame

class Bathroom:
    """Handles drawing the bathroom environment."""

    def __init__(self, screen):
        """Initialize bathroom background properties."""
        self.screen = screen

    def draw(self):
        """Draw the bathroom area."""
        self.screen.fill((190, 190, 190))  # Light gray walls
        pygame.draw.rect(self.screen, (220, 220, 220), (0, 400, 800, 200))  # Tiled floor

        # Toilet
        pygame.draw.rect(self.screen, (255, 255, 255), (600, 350, 70, 80))  # Toilet base
        pygame.draw.circle(self.screen, (255, 255, 255), (635, 340), 30)  # Toilet seat
        pygame.draw.rect(self.screen, (180, 180, 180), (620, 300, 30, 40))  # Tank

        # Sink
        pygame.draw.rect(self.screen, (200, 200, 200), (100, 350, 100, 50))  # Sink base
        pygame.draw.circle(self.screen, (230, 230, 230), (150, 330), 30)  # Sink bowl
        pygame.draw.rect(self.screen, (150, 150, 150), (140, 270, 20, 60))  # Faucet
