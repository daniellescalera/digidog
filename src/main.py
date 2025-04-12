import pygame
import sys
import time
from dog import Dog  # original (unused here)
from dog_Vactions import DogVActions  # visual effects version
from background.indoor import Indoor
from background.outdoor import Outdoor


def main():
    """Initialize Pygame and run the main game loop."""
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("DigiDog: Interactive Virtual Dog")

    clock = pygame.time.Clock()

    indoor = Indoor(screen)
    outdoor = Outdoor(screen)

    #Pass screen and background into the dog
    dog = DogVActions(screen)

    print(f"Dog object created: {type(dog)}")
    print(f"Available methods: {dir(dog)}")

    current_location = "indoor"  # Start inside the home

    while True:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    dog.perform_action("eating")
                elif event.key == pygame.K_p:
                    dog.perform_action("playing")
                elif event.key == pygame.K_s:
                    dog.perform_action("sleeping")
                elif event.key == pygame.K_c:
                    dog.perform_action("sitting")

        # Check if action is done
        if dog.state in ["playing", "eating", "sitting"]:
            if hasattr(dog, 'action_start_time') and hasattr(dog, 'action_duration'):
                if time.time() - dog.action_start_time > dog.action_duration:
                    dog.state = "idle"

        # If playing, move the dog left/right
        if dog.state == "playing":
            dog.x += dog.speed
            if dog.x > 700 or dog.x < 100:
                dog.speed *= -1

        dog.move(keys)

        # Room Switching Logic
        if current_location == "indoor":
            if dog.x > 750:
                current_location = "outdoor"
                dog.x = 50
                dog.y = 450
        elif current_location == "outdoor":
            if dog.x < 50:
                current_location = "indoor"
                dog.x = 750
                dog.y = 450

        # Draw background
        if current_location == "indoor":
            indoor.draw()
        elif current_location == "outdoor":
            outdoor.draw()

        # Draw the dog
        dog.draw(screen)

        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()
