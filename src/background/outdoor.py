import pygame

class Outdoor:
    """Handles drawing the outdoor environment."""

    def __init__(self, screen):
        """Initialize outdoor background properties."""
        self.screen = screen

    def draw(self):
        """Draw the backyard where the dog goes outside."""
        # Sky and Grass
        self.screen.fill((135, 206, 250))  # Blue sky
        pygame.draw.rect(self.screen, (34, 139, 34), (0, 400, 800, 200))  # Green grass

        # Trees
        pygame.draw.rect(self.screen, (139, 69, 19), (100, 300, 40, 100))  # Tree trunk
        pygame.draw.circle(self.screen, (34, 139, 34), (120, 250), 50)  # Tree top

        # Doghouse
        pygame.draw.polygon(self.screen, (150, 75, 0), [(500, 350), (600, 350), (550, 270)])  # Roof
        pygame.draw.rect(self.screen, (165, 42, 42), (520, 350, 60, 50))  # House base
        pygame.draw.circle(self.screen, (0, 0, 0), (550, 375), 15)  # Door hole

        # Bathroom Area (small fenced section)
        pygame.draw.rect(self.screen, (139, 69, 19), (700, 400, 50, 100))  # Fence
        pygame.draw.rect(self.screen, (180, 180, 180), (720, 420, 30, 30))  # Small "bathroom" area
