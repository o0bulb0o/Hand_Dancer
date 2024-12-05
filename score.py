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

    def display_scores(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.back_button.is_clicked(event)

            self.screen.fill((0, 0, 0))
            scores = [
                "Player 1: 3",
                "Player 2: 4",
                "Player 3: 2"
            ]
            y = 100
            for score in scores:
                score_text = self.font.render(score, True, (255, 255, 255))
                self.screen.blit(score_text, (100, y))
                y += 50

            self.back_button.draw(self.screen)
            pygame.display.flip()