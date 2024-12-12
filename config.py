import pygame
import sys

screen_width = 900
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Anicent Ritual")

Level1Recipe = [["sword", 4], ["fist", 6], ["fist", 7.4], ["fist", 9], ["sword", 10.4], ["sword", 12.8], ["sword", 14.8], ["fist", 16.4], ["sword", 18], ["fist", 20],["fist", 22],["sword", 24],["sword", 26],["sword", 28] ]
Level1UpdateFreq = 5  # 10 ticks move 1 px