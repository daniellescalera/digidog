import pygame

class Indoor:
    """Handles drawing the indoor home environment."""

    def __init__(self, screen):
        """Initialize indoor background properties."""
        self.screen = screen

    def draw(self):
        """Draw the main home room where the dog lives."""
        # Background Wall and Floor
        self.screen.fill((200, 180, 150))  # Beige wall
        pygame.draw.rect(self.screen, (100, 80, 60), (0, 400, 800, 200))  # Wooden floor

        # Bed
        pygame.draw.rect(self.screen, (220, 190, 230), (500, 250, 200, 100))  # Pink bed
        pygame.draw.rect(self.screen, (180, 180, 180), (500, 250, 200, 40))  # Gray mattress

        # Small Dog Bed
        pygame.draw.ellipse(self.screen, (150, 100, 50), (350, 450, 120, 60))  # Brown dog bed

        # Food & Water Bowls
        pygame.draw.circle(self.screen, (200, 0, 0), (700, 470), 15)  # Red food bowl
        pygame.draw.circle(self.screen, (0, 0, 200), (730, 470), 15)  # Blue water bowl

        # Small Kitchen (Cabinets)
        pygame.draw.rect(self.screen, (170, 140, 120), (50, 250, 150, 100))  # Brown cabinets
        pygame.draw.rect(self.screen, (220, 220, 220), (100, 260, 50, 30))  # Silver handles

        # TV
        pygame.draw.rect(self.screen, (30, 30, 30), (300, 180, 150, 90))  # TV screen
        pygame.draw.rect(self.screen, (50, 50, 50), (320, 270, 110, 10))  # TV stand

        # Door to go outside
        pygame.draw.rect(self.screen, (120, 100, 80), (750, 250, 50, 150))  # Brown door
