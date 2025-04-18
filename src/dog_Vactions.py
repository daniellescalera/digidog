import pygame
import threading
import time
import random

class DogVActions:
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

        # Tail wagging setup
        self.tail_offset = 0
        self.tail_direction = 1
        self.tail_counter = 0

    def move(self, keys):
        """Move the dog based on key presses, but prevent movement if busy."""
        if self.state not in ["idle", "walking"]:
            return

        self.state = "walking"
        moving = False

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

        if moving:
            self.wag_counter += 1
            if self.wag_counter >= 5:
                self.wag_counter = 0
                self.leg_offset = -self.leg_offset + 5
        self.state = "idle" if not moving else "walking"

    def perform_action(self, action):
        with self.lock:
            if self.state != "idle":
                print(f"Can't {action} right now, currently {self.state}.")
                return
            self.state = action

        threading.Thread(target=self._perform_action_thread, args=(action,)).start()

    def _perform_action_thread(self, action: str):
        with self.lock:
            print(f"Performing action: {action}")
            self.state = action
            self.action_start_time = time.time()
            self.action_duration = 30 if action == "sleeping" else 15  # sleeping is longer

    def move_during_playing(self):
        print("Dog is playing! Moving around...")
        clock = pygame.time.Clock()
        start_time = time.time()
        direction = 1

        while time.time() - start_time < 15:
            self.x += self.speed * direction
            if self.x > 700 or self.x < 100:
                direction *= -1

            self.wag_counter += 1
            if self.wag_counter >= 5:
                self.wag_counter = 0
                self.leg_offset = -self.leg_offset + 5

            self.screen.fill((200, 180, 150))  # wall
            pygame.draw.rect(self.screen, (100, 80, 60), (0, 400, 800, 200))  # floor
            self.draw(self.screen)
            pygame.display.update()
            clock.tick(30)

        self.leg_offset = 0

    def draw(self, screen):
        """Draw the dog based on its current state."""

        # Tail wagging logic
        if self.state == "idle":
            self.tail_counter += 1
            if self.tail_counter >= 5:
                self.tail_counter = 0
                self.tail_offset += self.tail_direction * 2
                if abs(self.tail_offset) > 10:
                    self.tail_direction *= -1
        else:
            self.tail_offset = 0

        # Body
        pygame.draw.ellipse(screen, (139, 69, 19), (self.x - 30, self.y, 60, 40))
        pygame.draw.circle(screen, (139, 69, 19), (self.x, self.y - 20), 20)

        # Ears
        pygame.draw.polygon(screen, (139, 69, 19), [(self.x - 12, self.y - 30), (self.x - 20, self.y - 45), (self.x - 5, self.y - 40)])
        pygame.draw.polygon(screen, (139, 69, 19), [(self.x + 12, self.y - 30), (self.x + 20, self.y - 45), (self.x + 5, self.y - 40)])

        # Tail (animated)
        pygame.draw.line(screen, (139, 69, 19),
                         (self.x + 30, self.y + 10),
                         (self.x + 45 + self.tail_offset, self.y), 5)

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

        # Extras based on state
        if self.state == "eating":
            pygame.draw.circle(screen, (200, 0, 0), (self.x + 20, self.y + 30), 15)  # red food
        elif self.state == "playing":
            pygame.draw.circle(screen, (255, 215, 0), (self.x + 40, self.y - 40), 10)  # ball
        elif self.state == "sleeping":
            pygame.draw.line(screen, (255, 255, 255), (self.x - 15, self.y - 20), (self.x - 5, self.y - 30), 2)
            pygame.draw.line(screen, (255, 255, 255), (self.x - 5, self.y - 20), (self.x + 5, self.y - 30), 2)
        elif self.state == "sitting":
            pygame.draw.rect(screen, (150, 75, 0), (self.x - 10, self.y + 20, 20, 5))  # seated tail stub
