import pygame
import config
import component
import sys
from game import ReactionGame

pygame.init()
# game object
def main_menu():
    def start_game():
        ReactionGame().preparation_scene()
        print("Game Started")
    def quit_game():
        pygame.quit()
        sys.exit()
    font = "./asset/WESTG___.ttf"
    start_button = component.Button("Start Game", (config.screen_width // 6, 100), start_game,font)
    quit_button = component.Button("Quit Game", (config.screen_width // 6, 300), quit_game,font)

    config.screen.blit(component.background_image, (0, 0))
    start_button.draw(config.screen)
    quit_button.draw(config.screen)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            start_button.is_clicked(event)
            quit_button.is_clicked(event)

main_menu()