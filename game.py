import pygame
import random
import time
import sys

class Button:
    def __init__(self, text, pos, callback):
        self.text = text
        self.pos = pos
        self.callback = callback
        self.font = pygame.font.Font(None, 36)
        self.rendered_text = self.font.render(self.text, True, (255, 255, 255))
        self.rect = self.rendered_text.get_rect(center=self.pos)

    def draw(self, screen):
        screen.blit(self.rendered_text, self.rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.callback()

class ReactionGame:
    def __init__(self, screen, back_to_menu_callback):
        self.screen = screen
        self.back_to_menu_callback = back_to_menu_callback
        self.levels = {
            "Level 1": [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d],
            "Level 2": [pygame.K_d, pygame.K_c, pygame.K_b, pygame.K_a]
        }
        self.font = pygame.font.Font(None, 36)
        self.time_limit = 2  # seconds
        self.current_round = 0
        self.score = 0
        self.results = []
        self.selected_level = None
        self.sequence = []
        self.buttons = []
        self.create_buttons()
        screen = pygame.display.set_mode((800, 600))
        self.run()

    def create_buttons(self):
        y = 100
        for level in self.levels:
            button = Button(level, (self.screen.get_width() // 2, y), lambda l=level: self.start_level(l))
            self.buttons.append(button)
            y += 60
        back_button = Button("Back to Menu", (self.screen.get_width() // 2, y), self.back_to_menu_callback)
        self.buttons.append(back_button)

    def select_level(self):
        self.screen.fill((0, 0, 0))  # bg color
        for button in self.buttons:
            button.draw(self.screen)
        pygame.display.flip()

        selecting = True
        while selecting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        button.is_clicked(event)

    def start_level(self, level):       
        self.selected_level = level
        self.sequence = self.levels[self.selected_level]
        print(f"Starting {self.selected_level}")
        self.current_round = 0
        self.start_time = pygame.time.get_ticks()
        self.next_round()

    def next_round(self):
        if self.current_round < len(self.sequence):
            self.target_key = self.sequence[self.current_round]
            self.start_time = time.time()
            self.remaining_time = self.time_limit
            self.run_round()
        else:
            self.end_game()
    
    def run_round(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))
            current_time = time.time()
            if current_time - self.start_time > self.time_limit:
                print("Time's up!")
                running = False
                self.end_game()
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == self.target_key:
                        self.current_round += 1
                        self.start_time = time.time()  # reset timer
                        if self.current_round >= len(self.sequence):
                            print("Level completed!")
                            running = False
                            self.end_game()
                            break
                    else:
                        print("Wrong key!")
                        running = False
                        self.end_game()
                        break

            pygame.display.flip()

    def update_score_list(self):
        # print(f"Current Score: {self.score}")
        current_high_score = self.load_high_score()
        if self.score > current_high_score:
            self.save_high_score(self.score)

    def load_high_score(self):
        try:
            with open('./score/score_list.txt', 'r') as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def save_high_score(self, score):
        with open('./score/score_list.txt', 'w') as file:
            file.write(str(score))

    def end_game(self):
            back_button = Button("Back to Menu", (self.screen.get_width() // 2, 500), self.back_to_menu_callback)
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        self.back_to_menu_callback()
                        return
                    back_button.is_clicked(event)

                self.screen.fill((0, 0, 0))
                result_message = "\n".join(self.results)
                lines = [
                    f"Game Over",
                    f"Your score: {self.score}",
                    "",
                    "Results:",
                    result_message
                ]
                y = 100
                for line in lines:
                    for subline in line.split('\n'):
                        result_text = self.font.render(subline, True, (255, 255, 255))
                        self.screen.blit(result_text, (100, y))
                        y += 40  # 調整行間距

                self.update_score_list()     #send the score to score.py

                back_button.draw(self.screen)
                pygame.display.flip()

    def back_to_menu(self):
        pass

    def run(self):
        self.select_level()