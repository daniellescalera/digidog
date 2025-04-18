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
        self.busy_animating = False

        self.tail_offset = 0
        self.tail_direction = 1
        self.tail_counter = 0

        self.head_bob_offset = 0
        self.last_bob_time = 0
        self.action_end_time = 0
        self.sleep_zzz_offset = 0
        self.last_zzz_time = 0
        self.showing_zzz = False
        self.last_play_time = 0

    def move(self, keys):
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
        self.busy_animating = True
        with self.lock:
            print(f"Performing action: {action}")
            self.state = action
            self.action_start_time = time.time()
            if action == "sleeping":
                self.action_duration = 30
            elif action == "sitting":
                self.action_duration = 5
            else:
                self.action_duration = 15

        if action == "eating":
            self.last_bob_time = time.time()
            self.action_end_time = self.action_start_time + self.action_duration
            self.state = "eating_animating"

        elif action == "sitting":
            time.sleep(self.action_duration)
            print("✅ Done sitting!")
            self.state = "idle"

        elif action == "sleeping":
            self.last_zzz_time = time.time()
            self.action_end_time = self.action_start_time + self.action_duration
            while time.time() < self.action_end_time:
                now = time.time()
                if now - self.last_zzz_time > 0.8:
                    self.showing_zzz = not self.showing_zzz
                    self.last_zzz_time = now
                time.sleep(0.05)
            print("💤 Done sleeping!")
            self.state = "idle"

        elif action == "playing":
            self.action_end_time = self.action_start_time + self.action_duration
            self.last_play_time = time.time()
            while time.time() < self.action_end_time:
                self.x += self.speed
                if self.x > 700 or self.x < 100:
                    self.speed *= -1
                self.wag_counter += 1
                if self.wag_counter >= 5:
                    self.wag_counter = 0
                    self.leg_offset = -self.leg_offset + 5
                time.sleep(0.05)
            print("🎾 Done playing!")
            self.state = "idle"

        self.busy_animating = False

    def draw(self, screen, head_offset=None):
        if head_offset is None:
            head_offset = self.head_bob_offset

        if self.state == "idle":
            self.tail_counter += 1
            if self.tail_counter >= 5:
                self.tail_counter = 0
                self.tail_offset += self.tail_direction * 2
                if abs(self.tail_offset) > 8:
                    self.tail_direction *= -1
        else:
            self.tail_offset = 0

        body_color = (139, 69, 19)
        leg_color = (100, 50, 20)

        pygame.draw.ellipse(screen, body_color, (self.x - 30, self.y, 60, 40))

        y_head = self.y - 20 + head_offset
        if self.state == "sleeping":
            y_head += 10

        pygame.draw.circle(screen, body_color, (self.x, y_head), 20)

        pygame.draw.polygon(screen, body_color, [(self.x - 12, self.y - 30), (self.x - 20, self.y - 45), (self.x - 5, self.y - 40)])
        pygame.draw.polygon(screen, body_color, [(self.x + 12, self.y - 30), (self.x + 20, self.y - 45), (self.x + 5, self.y - 40)])

        pygame.draw.line(screen, body_color,
                         (self.x + 30, self.y + 10),
                         (self.x + 45, self.y + self.tail_offset), 5)

        pygame.draw.rect(screen, leg_color, (self.x - 20, self.y + 25 + self.leg_offset, 10, 20))
        pygame.draw.rect(screen, leg_color, (self.x - 5, self.y + 25 - self.leg_offset, 10, 20))
        pygame.draw.rect(screen, leg_color, (self.x + 5, self.y + 25 + self.leg_offset, 10, 20))
        pygame.draw.rect(screen, leg_color, (self.x + 20, self.y + 25 - self.leg_offset, 10, 20))

        if self.state != "sleeping":
            pygame.draw.circle(screen, (255, 255, 255), (self.x - 8, self.y - 25), 5)
            pygame.draw.circle(screen, (255, 255, 255), (self.x + 8, self.y - 25), 5)
            pygame.draw.circle(screen, (0, 0, 0), (self.x - 8, self.y - 25), 2)
            pygame.draw.circle(screen, (0, 0, 0), (self.x + 8, self.y - 25), 2)
            pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y - 15), 4)

        if self.state == "eating_animating":
            pygame.draw.rect(screen, (255, 255, 255), (self.x + 25, self.y + 15, 20, 10))
        elif self.state == "playing":
            pygame.draw.circle(screen, (255, 215, 0), (self.x + 40, self.y - 40), 10)
        elif self.state == "sleeping" and self.showing_zzz:
            font = pygame.font.Font(None, 30)
            z_text = font.render("Zzz", True, (255, 255, 255))
            screen.blit(z_text, (self.x + 30, self.y - 40))
        elif self.state == "sitting":
            pygame.draw.rect(screen, (150, 75, 0), (self.x - 10, self.y + 20, 20, 5))
