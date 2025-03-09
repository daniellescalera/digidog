import pygame

class Kitchen:
    """Handles drawing the kitchen environment."""

    def __init__(self, screen):
        """Initialize kitchen background properties."""
        self.screen = screen

    def draw(self):
        """Draw the kitchen area."""
        self.screen.fill((230, 230, 230))  # Light gray kitchen walls
        pygame.draw.rect(self.screen, (180, 180, 180), (0, 400, 800, 200))  # Tiled floor

        # Fridge
        pygame.draw.rect(self.screen, (200, 200, 200), (50, 250, 100, 150))  # Fridge body
        pygame.draw.rect(self.screen, (180, 180, 180), (50, 250, 100, 75))  # Top fridge section
        pygame.draw.line(self.screen, (0, 0, 0), (50, 325), (150, 325), 2)  # Fridge door separation

        # Food Bowl (near fridge)
        pygame.draw.circle(self.screen, (200, 0, 0), (700, 470), 15)  # Red food bowl
        pygame.draw.circle(self.screen, (0, 0, 200), (730, 470), 15)  # Blue water bowl

        # Kitchen Counter
        pygame.draw.rect(self.screen, (170, 140, 120), (200, 300, 400, 80))  # Countertop
