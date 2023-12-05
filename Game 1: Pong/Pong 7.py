# pong 7
# Code With Mr Wagner and
# Dany
# Create a Right Paddle and Catch Keyboard Event.

import time

import pygame
from pygame.locals import *

pygame.init()

# Variables
ScreenWidth = 800
ScreenHeight = 600
BallX = 100
BallY = 100
BallLocation = (BallX, BallY)  # tuple
BallSize = 10
BallHalf = BallSize / 2
dx = 1  # Change in X
dy = 1  # Change in Y

RPaddleX = 700
RPaddleY = 100
RPaddleW = 20
RPaddleH = 80
RPaddle = (RPaddleX, RPaddleY, RPaddleW, RPaddleH)

# tuple (x,y,y,q)
# Constant (red, green, blue, white, yellow) 0 to 255
white = (255, 255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
lime = (0, 255, 0)
blue = (0, 0, 255)
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

        # == MEANS IS EQUAL TO IF X == 10 RETURN TRUE OR FALSE
        # MEANS ASSIGN TO X=10
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                print("Down Key")
            if event.key == K_UP:
                print("Up Key")

    # New Value = Old Value + 1
    # Variable += 1
    BallX += dx
    BallY += dy
    BallLocation = (BallX, BallY)  # Tuple

    # Bounce Code

    if BallX > ScreenWidth - BallHalf or BallX < BallHalf:
        dx *= -1
    if BallY > ScreenHeight - BallHalf or BallY < BallHalf:
        dy *= -1

    # if BallX < 0:
    # dx = dx * -1

    screen.fill(white)
    pygame.draw.rect(screen, red, (LeftSideOfNet, 0, NetWidth, ScreenHeight))
    pygame.draw.circle(screen, lime, BallLocation, BallSize, 5)
    pygame.draw.rect(screen, blue, RPaddle)

    pygame.display.update()
    time.sleep(0.01)
# end of the while loop
print("Game Over")
pygame.quit()
