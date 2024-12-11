import pygame
import time
import sys
import component
import config
from hand_tracker import HandTracker  # Import the HandTracker class

class ReactionGame:

    def __init__(self):
        self.screen = config.screen
        self.pointing_to = -1
        self.sword = False
        self.amulet = False
        self.shield = False
        self.eyeball = False

    def preparation_scene(self):
        def quit_game():
            pygame.quit()
            sys.exit()

        config.screen.blit(component.preparation_image, (0, 0))
        pygame.display.flip()

        level1_button = component.Button("Level 1", [845, 500], self.level1)
        level2_button = component.Button("Level 2", [760, 400], self.level2)
        level3_button = component.Button("Level 3", [865, 240], self.level3)
        level4_button = component.Button("Level 4", [730, 90], self.level4)

        level1_button.draw(config.screen)
        level2_button.draw(config.screen)
        level3_button.draw(config.screen)
        level4_button.draw(config.screen)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game()
                elif event.type == pygame.MOUSEMOTION:
                    x = event.pos[0]
                    y = event.pos[1]
                    if 800 < x < 1000 and 465 < y < 550:
                        self.pointing_to = 1
                    elif 720 < x < 800 and 345 < y < 450:
                        self.pointing_to = 2
                    elif 830 < x < 900 and 195 < y < 285:
                        self.pointing_to = 3
                    elif 700 < x < 760 and 50 < y < 125:
                        self.pointing_to = 4
                    else:
                        self.pointing_to = -1

                    config.screen.blit(component.preparation_image, (0, 0))
                    level1_button.draw(config.screen)
                    level2_button.draw(config.screen)
                    level3_button.draw(config.screen)
                    level4_button.draw(config.screen)

                    if self.pointing_to == 1:
                        pygame.draw.circle(self.screen, (255, 255, 255), [845, 500], 60, 5)
                    elif self.pointing_to == 2:
                        pygame.draw.circle(self.screen, (255, 255, 255), [760, 400], 60, 5)
                    elif self.pointing_to == 3:
                        pygame.draw.circle(self.screen, (255, 255, 255), [865, 240], 60, 5)
                    elif self.pointing_to == 4:
                        pygame.draw.circle(self.screen, (255, 255, 255), [730, 90], 60, 5)

                level1_button.is_clicked(event)
                level2_button.is_clicked(event)
                level3_button.is_clicked(event)
                level4_button.is_clicked(event)

            pygame.display.update()

    def level1(self):
        print("Level 1")
        config.screen.blit(component.level1_image, (0, 0))
        pygame.display.flip()

        hand_tracker = HandTracker()  # Initialize the hand tracker

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    hand_tracker.release()  # Release the hand tracker resources
                    pygame.quit()
                    sys.exit()
            if not hand_tracker.process_frame():  # Process the frame and check if 'q' is pressed
                break
            pygame.display.update()

    def level2(self):
        print("Level 2")
    def level3(self):
        print("Level 3")
    def level4(self):
        print("Level 4")