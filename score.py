import pygame
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

class ScoreChecker:
    def __init__(self, screen, back_to_menu_callback):
        self.screen = screen
        self.back_to_menu_callback = back_to_menu_callback
        self.font = pygame.font.Font(None, 36)
        self.back_button = Button("Back to Menu", (screen.get_width() // 2, 500), self.back_to_menu_callback)
        self.display_scores()

    def load_score(self):
        try:
            with open('score_list.txt', 'r') as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def save_highest_score(self):
        with open('score_list.txt', 'w') as file:
            file.write(str(self.highest_score))
    
    def accept_new_score(score):
        # score_checker = ScoreChecker(None, None)
        current_high_score =load_score()
        if score > current_high_score:
            score_checker.update_high_score(score)

    def display_scores(self):
        high_score_text = self.font.render(f"High Score: {self.load_score}", True, (255, 255, 255))
        self.screen.blit(high_score_text, (10, 10))
        pygame.display.flip()
