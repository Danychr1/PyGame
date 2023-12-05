# pong 6
# Code With Mr Wagner and
# Dany
# Bounce the ball and Cleaning the Code.

import time

import pygame

pygame.init()

# Variables
ScreenWidth = 800
ScreenHeight = 600
BallX = 100
BallY = 100
BallLocation = (BallX, BallY)  # tuple
BallSize = 15
dx = 1  # Change in X
dy = 1  # Change in Y

# tuple (x,y,y,q)
# Constant (red, green, blue, white, yellow) 0 to 255
white = (255, 255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
lime = (0, 255, 0)
# create a window
pygame.display.set_caption("Pong")
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))

CenterOfScreen = ScreenWidth / 2
NetWidth = 9
LeftSideOfNet = CenterOfScreen - (NetWidth / 2)

# standard pygame game loo while , for , if

GameRunning = True
while GameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRunning = False
    # New Value = Old Value + 1
    # Variable += 1
    BallX += dx
    BallY += dy
    BallLocation = (BallX, BallY)  # Tuple

    # Bounce Code

    if BallX > ScreenWidth - BallSize / 2 or BallX < BallSize / 2:
        dx *= -1
    if BallY > ScreenHeight - BallSize / 2 or BallY < BallSize / 2:
        dy *= -1

    # if BallX < 0:
    # dx = dx * -1

    screen.fill(white)
    pygame.draw.rect(screen, red, (LeftSideOfNet, 0, NetWidth, ScreenHeight))
    pygame.draw.circle(screen, lime, BallLocation, BallSize, 5)

    pygame.display.update()
    time.sleep(0.01)
# end of the while loop
print("Game Over")
pygame.quit()
