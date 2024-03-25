import pygame
import random

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shooting Gallery')
icon = pygame.image.load("images/Тир.jpg")
pygame.display.set_icon(icon)


target_img = pygame.image.load("images/target.png")
target_size = (80, 80)
target_x = random.randint(0, SCREEN_WIDTH - target_size[0])
target_y = random.randint(0, SCREEN_HEIGHT - target_size[1])
target_speed_x = 2
target_speed_y = 2
background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

score = 0
font = pygame.font.Font(None, 36)

running = True
clock = pygame.time.Clock()
while running:
    screen.fill(background_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_size[0] and target_y < mouse_y < target_y + target_size[1]:
                score += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_size[0])
                target_y = random.randint(0, SCREEN_HEIGHT - target_size[1])
                background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


    target_x += target_speed_x
    target_y += target_speed_y


    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_size[0]:
        target_speed_x = -target_speed_x
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_size[1]:
        target_speed_y = -target_speed_y

    screen.blit(target_img, (target_x, target_y))


    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()