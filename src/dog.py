import pygame
import threading
import time

class Dog:
    """Represents DigiDog and its behaviors with multithreading and synchronization."""

    def __init__(self):
        """Initialize the dog's position, state, and thread lock for synchronization."""
        self.x = 400
        self.y = 300
        self.speed = 5
        self.state = "idle"  # Dog starts in an idle state
        self.lock = threading.Lock()  # Prevent conflicting actions
        self.leg_offset = 0  # Controls leg animation
        self.wag_counter = 0  # Controls walking animation speed

    def move(self, keys):
        """Move the dog based on key presses, but prevent movement if busy."""
        if self.state not in ["idle", "walking"]:  # Don't allow movement if performing an action
            return

        moving = False  # Track if the dog is actually moving

        if keys[pygame.K_RIGHT]:  # RIGHT arrow moves right
            self.x += self.speed
            moving = True
        if keys[pygame.K_LEFT]:  # LEFT arrow moves left
            self.x -= self.speed
            moving = True
        if keys[pygame.K_UP]:  # UP arrow moves up
            self.y -= self.speed
            moving = True
        if keys[pygame.K_DOWN]:  # DOWN arrow moves down
            self.y += self.speed
            moving = True

        # Animate legs if moving
        if moving:
            self.state = "walking"
            self.wag_counter += 1
            if self.wag_counter >= 5:  # Adjust animation speed
                self.wag_counter = 0
                self.leg_offset = -self.leg_offset + 5  # Moves legs back and forth
        else:
            self.state = "idle"

    def draw(self, screen):
        """Draw the dog with a full body, legs, and tail."""
        # Body
        pygame.draw.ellipse(screen, (139, 69, 19), (self.x - 30, self.y, 60, 40))  # Brown oval body
        pygame.draw.circle(screen, (139, 69, 19), (self.x, self.y - 20), 20)  # Head

        # Eyes
        pygame.draw.circle(screen, (255, 255, 255), (self.x - 8, self.y - 25), 5)  # Left eye
        pygame.draw.circle(screen, (255, 255, 255), (self.x + 8, self.y - 25), 5)  # Right eye
        pygame.draw.circle(screen, (0, 0, 0), (self.x - 8, self.y - 25), 2)  # Left pupil
        pygame.draw.circle(screen, (0, 0, 0), (self.x + 8, self.y - 25), 2)  # Right pupil

        # Ears
        pygame.draw.polygon(screen, (139, 69, 19), [(self.x - 12, self.y - 30), (self.x - 20, self.y - 45), (self.x - 5, self.y - 40)])  # Left ear
        pygame.draw.polygon(screen, (139, 69, 19), [(self.x + 12, self.y - 30), (self.x + 20, self.y - 45), (self.x + 5, self.y - 40)])  # Right ear

        # Nose
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y - 15), 4)  # Black nose

        # Tail
        pygame.draw.line(screen, (139, 69, 19), (self.x + 30, self.y + 10), (self.x + 45, self.y), 5)

        # Legs
        pygame.draw.rect(screen, (100, 50, 20), (self.x - 20, self.y + 25 + self.leg_offset, 10, 20))  # Front left leg
        pygame.draw.rect(screen, (100, 50, 20), (self.x - 5, self.y + 25 - self.leg_offset, 10, 20))   # Back left leg
        pygame.draw.rect(screen, (100, 50, 20), (self.x + 5, self.y + 25 + self.leg_offset, 10, 20))   # Front right leg
        pygame.draw.rect(screen, (100, 50, 20), (self.x + 20, self.y + 25 - self.leg_offset, 10, 20))  # Back right leg

    def perform_action(self, action):
        """Perform a long-running action (eating, playing, etc.) in a thread-safe way."""
        with self.lock:
            if self.state != "idle":
                print(f"Can't {action} right now, currently {self.state}.")
                return
            self.state = action
            threading.Thread(target=self._perform_action_thread, args=(action,)).start()

    def _perform_action_thread(self, action):
        print(f'The dog is {action}...')
        duration = {
            "eating": 20,
            "playing": 20,
            "sleeping": 45,
            "sitting": 20
        }.get(action, 10)

        time.sleep(duration)
        print(f"Ok done {action}!")

        with self.lock:
            self.state = "idle"
