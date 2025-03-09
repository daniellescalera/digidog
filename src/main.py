import pygame
import sys
import threading
from dog import Dog
from background.indoor import Indoor
from background.outdoor import Outdoor
from background.kitchen import Kitchen
from background.bathroom import Bathroom
from background.hallway import Hallway

def main():
    """Initialize Pygame and run the main game loop."""
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("DigiDog: Interactive Virtual Dog")

    clock = pygame.time.Clock()
    dog = Dog()
    indoor = Indoor(screen)
    outdoor = Outdoor(screen)
    kitchen = Kitchen(screen)
    bathroom = Bathroom(screen)
    hallway = Hallway(screen)

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

        # 🚪 **Room Switching Logic**
        if current_location == "indoor":
            if dog.x > 750:  # Exit to outdoor
                current_location = "outdoor"
                dog.x = 50  
                dog.y = 450  # Keep dog on the ground
            elif dog.x < 50:  # Enter hallway (go LEFT)
                current_location = "hallway"
                dog.x = 700  # Enter hallway from the right
                dog.y = 450  # Enter at floor level

        elif current_location == "hallway":
            if dog.x > 700:  # Return to indoor
                current_location = "indoor"
                dog.x = 50  
                dog.y = 450  # Keep dog on the ground
            elif 150 < dog.x < 250:  # Enter kitchen
                current_location = "kitchen"
                dog.x = 400
                dog.y = 450  
            elif 300 < dog.x < 400:  # Enter bathroom
                current_location = "bathroom"
                dog.x = 400
                dog.y = 450  

        elif current_location == "kitchen":
            if dog.y > 450:  # Return to hallway
                current_location = "hallway"
                dog.x = 200  
                dog.y = 450  

        elif current_location == "bathroom":
            if dog.y > 450:  # Return to hallway
                current_location = "hallway"
                dog.x = 350  
                dog.y = 450  

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
        elif current_location == "kitchen":
            kitchen.draw()
        elif current_location == "bathroom":
            bathroom.draw()
        elif current_location == "hallway":
            hallway.draw()

        dog.draw(screen)  # Draw the dog
        pygame.display.flip()
        clock.tick(30)  # Limit FPS

if __name__ == "__main__":
    main()
