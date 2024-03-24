import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
pygame.display.set_caption('Игра "Тир"')
icon = pygame.image.load("images/Тир.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("images/target.png")
target_width = 80
target_heigth = 80
target_x = random.randint(0, SCREEN_WIDTH-target_width)
target_y = random.randint(0, SCREEN_HEIGTH-target_heigth)
color = (random.randint(0, 255), random.randint(0, 255).random.randint(0, 255))



running = True
while running:
    pass


pygame.quit()