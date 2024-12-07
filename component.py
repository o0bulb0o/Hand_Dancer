import pygame
import config

class Button:
    def __init__(self, text, pos, callback, font = None, font_size = 36):
        self.text = text
        self.pos = pos
        self.callback = callback
        self.font = pygame.font.Font(font, font_size)
        self.rendered_text = self.font.render(self.text, True, (255, 255, 255))
        self.rect = self.rendered_text.get_rect(center=self.pos)

    def draw(self, screen):
        screen.blit(self.rendered_text, self.rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.callback()
class CameraMonitor:
    def __init__(self):
        pass

background_image = pygame.image.load("./img/OpenMenuBg.jpg")
background_image = pygame.transform.scale(background_image, (config.screen_width, config.screen_height))
preparation_image = pygame.image.load("./img/PreparationSceneBG.png")
preparation_image = pygame.transform.scale(preparation_image, (config.screen_width, config.screen_height))
level1_image = pygame.image.load("./img/Level1BG.jpg")
level1_image = pygame.transform.scale(level1_image, (config.screen_width, config.screen_height))