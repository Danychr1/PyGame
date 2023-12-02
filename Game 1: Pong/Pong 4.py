# pong4
# Code With Mr Wagner and
# Dany
import time

import pygame

pygame.init()

# Variables
ScreenWidth = 800
ScreenHeight = 600
BallX = 100
BallY = 100
BallLocation = (BallX, BallY)  # tuple

# tuple (x,y,y,q)
# Constant (red, green, blue, white, yellow) 0 to 255
white = (255, 255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
lime = (0, 255, 0)
# create a window
pygame.display.set_caption("Pong")
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))

# standard pygame game loo while , for , if

GameRunning = True
while GameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRunning = False
    # New Value = Old Value + 1 
    BallX = BallX + 1
    BallY = BallY + 1
    BallLocation = (BallX, BallY)

    screen.fill(white)
    pygame.draw.circle(screen, lime, BallLocation, 10, 5)
    pygame.draw.rect(screen, black, (395, 0, 10, 600))

    pygame.display.update()
    time.sleep(0.01)
# end of the while loop
print("Game Over")
pygame.quit()
