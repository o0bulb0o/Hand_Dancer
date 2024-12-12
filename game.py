import pygame
import time
import sys
import component
import config

class ReactionGame:

    def __init__(self):
        self.screen = config.screen
        self.pointing_to = -1
        self.sword = True
        self.amulet = False
        self.shield = False
        self.eyeball = False

    SetHealth = pygame.event.custom_type()
    SetGesture = pygame.event.custom_type()

    def set_health(self, health):
        health_event = pygame.event.Event(self.SetHealth, health = health)
        pygame.event.post(health_event)
    
    def set_gesture(self, gesture):
        gesture_event = pygame.event.Event(self.SetGesture, gesture = gesture)
        pygame.event.post(gesture_event)

    def preparation_scene(self):
        def quit_game():
            pygame.quit()
            sys.exit()

        config.screen.blit(component.preparation_image, (0, 0))
        pygame.display.flip()

        level1_button = component.Button("Level 1", [845,500] , self.level1)
        level2_button = component.Button("Level 2", [760,400] , self.level2)
        level3_button = component.Button("Level 3", [865,240] , self.level3)
        level4_button = component.Button("Level 4", [730,90]  , self.level4)

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
                    if ( x > 800 and x < 1000 and y > 465 and y < 550):
                        self.pointing_to = 1
                    elif ( x > 720 and x < 800 and y > 345 and y < 450):
                        self.pointing_to = 2
                    elif ( x > 830 and x < 900 and y > 195 and y < 285):
                        self.pointing_to = 3
                    elif ( x > 700 and x < 760 and y > 50 and y < 125):
                        self.pointing_to = 4
                    else:
                        self.pointing_to = -1

                    if self.pointing_to == 1:
                        pygame.draw.circle(self.screen, (255,255,255),[845,500],60,width=5)
                    elif self.pointing_to == 2:
                        pygame.draw.circle(self.screen, (255,255,255),[760,400],60,width=5)
                    elif self.pointing_to == 3:
                        pygame.draw.circle(self.screen, (255,255,255),[865,240],60,width=5)
                    elif self.pointing_to == 4:
                        pygame.draw.circle(self.screen, (255,255,255),[730,90],60,width=5)
                    else:
                        config.screen.blit(component.preparation_image, (0, 0))
                        pygame.display.flip()
                level1_button.is_clicked(event)
                level2_button.is_clicked(event)
                level3_button.is_clicked(event)
                level4_button.is_clicked(event)
                    
            pygame.display.update()

    def level1(self):
        print("Level 1")

        def init():
            self.health = 5
            self.gesture = "None"
            self.objects = []
            self.spawn_times = [item[1] * 1000 for item in config.Level1Recipe]  # Convert seconds to milliseconds
            self.spawn_index = 0
            self.enemy_health = 10
            self.level_start_time = pygame.time.get_ticks()  # Record the start time of the level

        def updateVisual():
            config.screen.blit(component.level1_image, (550, 0))
            component.HealthStatusBar().draw(config.screen, self.health)
            component.GestureStatusBar().draw(config.screen, self.gesture)
            component.EnemyHealthStatusBar().draw(config.screen, self.enemy_health)
            component.TuneBoard().draw(config.screen)
            component.Enemy().draw(config.screen)
            for obj in self.objects:
                obj.draw(config.screen)
            pygame.display.flip()

        def checkwin():
            if self.health <= 0:
                print("You lose")
                self.spawn_index = 0
                self.objects = []
                self.preparation_scene()
            if self.enemy_health <= 0:
                print("You win !")
                print(" You have unlocked the amulet ")
                self.amulet = True
                self.spawn_index = 0
                self.objects = []
                self.preparation_scene()

        init()
        last_update_time = pygame.time.get_ticks()  # Reset last update time when the level starts

        while True:
            current_time = pygame.time.get_ticks()
            if current_time - last_update_time > config.Level1UpdateFreq:
                for obj in self.objects:
                    obj.move(1)
                    if obj.rect.y > 830:
                        self.objects.remove(obj)
                        if obj.__class__.__name__ == "Sword":
                            if self.gesture == "Sword":
                                self.enemy_health -= 1
                            else:
                                self.health -= 1
                        elif obj.__class__.__name__ == "Fist":
                            if self.gesture == "Fist":
                                self.enemy_health -= 1
                            else:
                                self.health -= 1
                        checkwin()
                last_update_time = current_time

            if self.spawn_index < len(self.spawn_times) and current_time - self.level_start_time >= self.spawn_times[self.spawn_index]:
                item = config.Level1Recipe[self.spawn_index]
                if item[0] == "sword":
                    self.objects.append(component.Sword((300, 0)))
                    print("Sword")
                elif item[0] == "fist":
                    self.objects.append(component.Fist((300, 0)))
                    print("Fist")
                self.spawn_index += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    print(event.pos)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.gesture = "Sword"
                    if event.key == pygame.K_f:
                        self.gesture = "Fist"

            updateVisual()
            pygame.display.update()

    def level2(self):
        print("Level 2")

        def init():
            self.health = 5
            self.gesture = "None"
            self.objects = []
            self.spawn_times = [item[1] * 1000 for item in config.Level2Recipe]  # Convert seconds to milliseconds
            self.spawn_index = 0
            self.enemy_health = 10
            self.level_start_time = pygame.time.get_ticks()  # Record the start time of the level

        def updateVisual():
            config.screen.blit(component.level1_image, (550, 0))
            component.HealthStatusBar().draw(config.screen, self.health)
            component.GestureStatusBar().draw(config.screen, self.gesture)
            component.EnemyHealthStatusBar().draw(config.screen, self.enemy_health)
            component.TuneBoard().draw(config.screen)
            component.Enemy().draw(config.screen)
            for obj in self.objects:
                obj.draw(config.screen)
            pygame.display.flip()

        def checkwin():
            if self.health <= 0:
                print("You lose")
                self.spawn_index = 0
                self.objects = []
                self.preparation_scene()
            if self.enemy_health <= 0:
                print("You win !")
                self.shield = True
                self.spawn_index = 0
                self.objects = []
                self.preparation_scene()

        init()
        last_update_time = pygame.time.get_ticks()  # Reset last update time when the level starts

        while True:
            current_time = pygame.time.get_ticks()
            if current_time - last_update_time > config.Level2UpdateFreq:
                for obj in self.objects:
                    obj.move(1)
                    if obj.rect.y > 830:
                        self.objects.remove(obj)
                        if obj.__class__.__name__ == "Sword":
                            if self.gesture == "Sword":
                                self.enemy_health -= 1
                            else:
                                self.health -= 1
                        elif obj.__class__.__name__ == "Fist":
                            if self.gesture == "Fist":
                                self.enemy_health -= 1
                            else:
                                self.health -= 1
                        elif obj.__class__.__name__ == "ok":
                            if self.gesture == "Ok":
                                self.enemy_health -= 1
                            else:
                                self.health -= 1
                        elif obj.__class__.__name__ == "Shield":
                            if self.gesture == "Shield":
                                self.enemy_health -= 1
                            else:
                                self.health -= 1
                        checkwin()
                last_update_time = current_time

            if self.spawn_index < len(self.spawn_times) and current_time - self.level_start_time >= self.spawn_times[self.spawn_index]:
                item = config.Level2Recipe[self.spawn_index]
                if item[0] == "sword":
                    self.objects.append(component.Sword((300, 0)))
                    print("Sword")
                elif item[0] == "fist":
                    self.objects.append(component.Fist((300, 0)))
                    print("Fist")
                elif item[0] == "ok":
                    self.objects.append(component.ok((300, 0)))
                    print("Ok")
                elif item[0] == "shield":
                    self.objects.append(component.Shield((300, 0)))
                    print("Shield")
                self.spawn_index += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    print(event.pos)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.gesture = "Sword"
                    if event.key == pygame.K_f:
                        self.gesture = "Fist"
                    if event.key == pygame.K_o:
                        self.gesture = "Ok"
                    if event.key == pygame.K_b:
                        self.gesture = "Shield"

            updateVisual()
            pygame.display.update()

    def level3(self):
        print("Level 3")
    def level4(self):
        print("Level 4")