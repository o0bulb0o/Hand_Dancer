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
        self.keys = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g]
        self.font = pygame.font.Font(None, 36)
        self.time_limit = 2  # seconds
        self.level = 0
        self.score = 0
        self.results = []
        self.next_level()

    def next_level(self):
        if self.level < 4:
            self.target_key = random.choice(self.keys)
            self.start_time = time.time()
            self.remaining_time = self.time_limit
            self.run_level()
        else:
            self.end_game()

    def run_level(self):
        while self.remaining_time > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == self.target_key:
                        reaction_time = time.time() - self.start_time
                        if reaction_time <= self.time_limit:
                            self.score += 1
                            self.results.append(f"Level {self.level + 1}: Passed")
                        else:
                            self.results.append(f"Level {self.level + 1}: Failed (Time out)")
                        self.level += 1
                        self.next_level()
                        return
                    else:
                        self.results.append(f"Level {self.level + 1}: Failed (Wrong key)")
                        self.level += 1
                        self.next_level()
                        return

            self.remaining_time = self.time_limit - (time.time() - self.start_time)
            self.screen.fill((0, 0, 0))
            instruction_text = self.font.render(f"Press the key: {pygame.key.name(self.target_key).upper()}", True, (255, 255, 255))
            time_text = self.font.render(f"Time left: {self.remaining_time:.1f}s", True, (255, 255, 255))
            self.screen.blit(instruction_text, (100, 100))
            self.screen.blit(time_text, (100, 200))
            pygame.display.flip()

    def load_score_list(self):
        try:
            with open('./score/score_list.txt', 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "No scores yet"
    
    def update_score_list(self):
        highest_score = self.load_score_list()
        print(highest_score)
        if self.score > int(highest_score):
            with open('./score/score_list.txt', 'w') as file:
                file.write(str(self.score))
            # print("New high score!")
        # print(f"Current Score: {self.score}")

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
            #testing