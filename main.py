import pygame
import sys
from game import ReactionGame
from score import ScoreChecker

# 初始化 Pygame
pygame.init()

# 設置窗口大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Main Menu")

# 加載背景圖片
background_image = pygame.image.load("./img/bg_interface.png")

# 定義按鈕類
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

# 定義按鈕回調函數
def start_game():
    ReactionGame(screen, main_menu)

def check_score():
    ScoreChecker(screen, main_menu)

def quit_game():
    pygame.quit()
    sys.exit()

# 創建按鈕
start_button = Button("Start Game", (screen_width // 2, 200), start_game)
score_button = Button("Check the Score", (screen_width // 2, 300), check_score)
quit_button = Button("Quit Game", (screen_width // 2, 400), quit_game)

# 主菜單循環
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            start_button.is_clicked(event)
            score_button.is_clicked(event)
            quit_button.is_clicked(event)

        screen.blit(background_image, (0, 0))
        start_button.draw(screen)
        score_button.draw(screen)
        quit_button.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main_menu()