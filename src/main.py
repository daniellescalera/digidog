import pygame
import sys
import threading
from dog import Dog #orignal 
from dog_Vactions import DogVActions #visual effects version
from background.indoor import Indoor
from background.outdoor import Outdoor


def main():
    """Initialize Pygame and run the main game loop."""
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("DigiDog: Interactive Virtual Dog")

    clock = pygame.time.Clock()
    dog = DogVActions()
    print(f"Dog object created: {type(dog)}")
    indoor = Indoor(screen)
    outdoor = Outdoor(screen)

    current_location = "indoor"  # Start inside the home

    while True:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Handle user commands (feed, play, sleep, sit)
                if event.key == pygame.K_f:  # Press 'F' to feed
                    dog.perform_action("eating")
                elif event.key == pygame.K_p:  # Press 'P' to play
                    dog.perform_action("playing")
                elif event.key == pygame.K_s:  # Press 'S' to sleep
                    dog.perform_action("sleeping")
                elif event.key == pygame.K_c:  # Press 'C' to sit
                    dog.perform_action("sitting")

        dog.move(keys)

        if isinstance(dog, DogVActions) and dog.state == "playing":
            dog.move_during_playing()

        # 🚪 Room Switching Logic
        if current_location == "indoor":
            if dog.x > 750:  # Exit to outdoor
                current_location = "outdoor"
                dog.x = 50  
                dog.y = 450  # Keep dog on the ground

        elif current_location == "outdoor":
            if dog.x < 50:  # Return to indoor
                current_location = "indoor"
                dog.x = 750  
                dog.y = 450

        # Draw the correct background
        if current_location == "indoor":
            indoor.draw()
        elif current_location == "outdoor":
            outdoor.draw()

        dog.draw(screen)  # Draw the dog
        pygame.display.flip()
        clock.tick(30)  # Limit FPS


if __name__ == "__main__":
    main()
