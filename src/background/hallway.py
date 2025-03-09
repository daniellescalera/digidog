import pygame

class Hallway:
    """Handles drawing the hallway with doors to other rooms."""

    def __init__(self, screen):
        """Initialize the hallway background properties."""
        self.screen = screen

    def draw(self):
        """Draw the hallway connecting all rooms."""
        self.screen.fill((190, 190, 190))  # Gray walls
        pygame.draw.rect(self.screen, (120, 120, 120), (0, 400, 800, 200))  # Darker floor

        # Doors leading to different rooms
        pygame.draw.rect(self.screen, (150, 100, 50), (50, 300, 80, 120))  # Door to outdoor
        pygame.draw.rect(self.screen, (150, 100, 50), (200, 300, 80, 120))  # Door to kitchen
        pygame.draw.rect(self.screen, (150, 100, 50), (350, 300, 80, 120))  # Door to bathroom
        pygame.draw.rect(self.screen, (150, 100, 50), (500, 300, 80, 120))  # Door to indoor

        # Labels for clarity
        font = pygame.font.Font(None, 24)
        text_outdoor = font.render("Outdoor", True, (0, 0, 0))
        text_kitchen = font.render("Kitchen", True, (0, 0, 0))
        text_bathroom = font.render("Bathroom", True, (0, 0, 0))
        text_indoor = font.render("Home", True, (0, 0, 0))

        self.screen.blit(text_outdoor, (65, 270))
        self.screen.blit(text_kitchen, (220, 270))
        self.screen.blit(text_bathroom, (370, 270))
        self.screen.blit(text_indoor, (525, 270))
