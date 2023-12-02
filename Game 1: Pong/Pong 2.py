# pong 2
# Code with Mr Wagner
# Your name

import pygame

pygame.init()

# Variables
ScreenWidth = 800
ScreenHeight = 600

# create a window
pygame.display.set_caption("Pong")
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
# print("open window")
# Standard pygame game loop "while, for , if"
GameRunning = True
while GameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRunning = False

# end of the while loop
print("Game Over")
pygame.quit()
