# pong3
# Code With Mr Wagner and
# Dany

import time

import pygame

pygame.init()

# Variables
ScreenWidth = 800
ScreenHeight = 600

# tuple (x, y, y, q)
# Constant (red, green, blue, white) 0 and 255
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Create a window
pygame.display.set_caption("Pong")
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))

# Standart pygame game loop while, for, if
GameRunning = True
while GameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRunning = False
    screen.fill("yellow")
    pygame.draw.circle(screen, red, (100, 100), 10, 5)
    pygame.draw.rect(screen, black, (395, 0, 10, 600))

    pygame.display.update()
    time.sleep(0.01)
# end of the while loop
print("Game Over")
pygame.quit()
