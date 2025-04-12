import pygame
import threading
import time
import random

class DogVActions:  # Renamed class for visual actions
    """Represents DigiDog with visual effects for different actions."""

    def __init__(self, screen, background=None):
        self.x = 100
        self.y = 300
        self.speed = 5
        self.state = "idle"
        self.lock = threading.Lock()
        self.wag_counter = 0
        self.leg_offset = 0
        self.screen = screen



    def move(self, keys):
        """Move the dog based on key presses, but prevent movement if busy."""
        if self.state not in ["idle", "walking"]:  # Don't allow movement if performing an action
            return

        self.state = "walking"
        moving = False  # Track if the dog is actually moving

        if keys[pygame.K_LEFT]:
            self.x -= self.speed
            moving = True
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
            moving = True
        if keys[pygame.K_UP]:
            self.y -= self.speed
            moving = True
        if keys[pygame.K_DOWN]:
            self.y += self.speed
            moving = True

        # Animate legs only if moving
        if moving:
            self.wag_counter += 1
            if self.wag_counter >= 5:  # Adjust animation speed
                self.wag_counter = 0
                self.leg_offset = -self.leg_offset + 5  # Moves legs back and forth

        self.state = "idle" if not moving else "walking"

    def perform_action(self, action):
        with self.lock:
            if self.state != "idle":
                print(f"Can't {action} right now, currently {self.state}.")
                return
            self.state = action  # Set the state before starting the thread

        threading.Thread(target=self._perform_action_thread, args=(action,)).start()

    def _perform_action_thread(self, action: str):
        with self.lock:
            print(f"Performing action: {action}")
            self.state = action
            self.action_start_time = time.time()
            self.action_duration = 15  # seconds


    def move_during_playing(self):
        print("Dog is playing! Moving around...")
        import pygame
        clock = pygame.time.Clock()

        start_time = time.time()
        direction = 1

        while time.time() - start_time < 15:
            self.x += self.speed * direction

            # Bounce off edges
            if self.x > 700 or self.x < 100:
                direction *= -1

        # Animate legs
            self.wag_counter += 1
            if self.wag_counter >= 5:
                self.wag_counter = 0
                self.leg_offset = -self.leg_offset + 5
                print(f"Leg offset updated to: {self.leg_offset}")

            # Redraw scene
            self.screen.fill((200, 180, 150))  # wall
            pygame.draw.rect(self.screen, (100, 80, 60), (0, 400, 800, 200))  # floor

            self.draw(self.screen)
            pygame.display.update()
            clock.tick(30)

        # Reset leg position after playing
        self.leg_offset = 0



    def draw(self, screen):
        """Draw the dog based on its current state."""

        # Body
        pygame.draw.ellipse(screen, (139, 69, 19), (self.x - 30, self.y, 60, 40))
        pygame.draw.circle(screen, (139, 69, 19), (self.x, self.y - 20), 20)

        # Ears
        pygame.draw.polygon(screen, (139, 69, 19), [(self.x - 12, self.y - 30), (self.x - 20, self.y - 45), (self.x - 5, self.y - 40)])
        pygame.draw.polygon(screen, (139, 69, 19), [(self.x + 12, self.y - 30), (self.x + 20, self.y - 45), (self.x + 5, self.y - 40)])

        # Tail
        pygame.draw.line(screen, (139, 69, 19), (self.x + 30, self.y + 10), (self.x + 45, self.y), 5)

        # Legs
        pygame.draw.rect(screen, (100, 50, 20), (self.x - 20, self.y + 25 + self.leg_offset, 10, 20))
        pygame.draw.rect(screen, (100, 50, 20), (self.x - 5, self.y + 25 - self.leg_offset, 10, 20))
        pygame.draw.rect(screen, (100, 50, 20), (self.x + 5, self.y + 25 + self.leg_offset, 10, 20))
        pygame.draw.rect(screen, (100, 50, 20), (self.x + 20, self.y + 25 - self.leg_offset, 10, 20))

        # Eyes and Nose
        if self.state != "sleeping":
            pygame.draw.circle(screen, (255, 255, 255), (self.x - 8, self.y - 25), 5)
            pygame.draw.circle(screen, (255, 255, 255), (self.x + 8, self.y - 25), 5)
            pygame.draw.circle(screen, (0, 0, 0), (self.x - 8, self.y - 25), 2)
            pygame.draw.circle(screen, (0, 0, 0), (self.x + 8, self.y - 25), 2)
            pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y - 15), 4)

        if self.state == "eating":
            pygame.draw.circle(screen, (200, 0, 0), (self.x + 20, self.y + 30), 15)
        elif self.state == "playing":
            pygame.draw.circle(screen, (255, 215, 0), (self.x + 40, self.y - 40), 10)
        elif self.state == "sleeping":
            pygame.draw.line(screen, (255, 255, 255), (self.x - 15, self.y - 20), (self.x - 5, self.y - 30), 2)
            pygame.draw.line(screen, (255, 255, 255), (self.x - 5, self.y - 20), (self.x + 5, self.y - 30), 2)
        elif self.state == "sitting":
            pygame.draw.rect(screen, (150, 75, 0), (self.x - 10, self.y + 20, 20, 5))
