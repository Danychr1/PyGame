# pong 11
# Code With Mr Wagner and
# Dany
# using Random Gameplay.

import pygame
import time
import random

from pygame.locals import *

pygame.init()

# Variables
ScreenWidth = 800
ScreenHeight = 600

BallX = random.randint(300,500)
BallY = random.randint(100,500)
BallLocation = (BallX, BallY)  # tuple
BallSize = 10
BallHalf = BallSize / 2
dx = 2  # Change in X
dy = 2  # Change in Y

RPaddleX = 700
RPaddleY = 100
RPaddleW = 20
RPaddleH = 80
RPaddle = (RPaddleX, RPaddleY, RPaddleW, RPaddleH)
RPaddleUpOrDown = 0

LPaddleX = 100
LPaddleY = 100
LPaddleW = 20
LPaddleH = 80
LPaddle = (LPaddleX, LPaddleY, LPaddleW, LPaddleH)

# tuple (x,y,y,q)
# Constant (red, green, blue, white, yellow) 0 to 255
black = (0, 0, 0)
white = (255, 255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
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
                RPaddleUpOrDown = 3
            if event.key == K_UP:
                print("Up Key")
                RPaddleUpOrDown = -3
    if event.type == KEYUP:
        if event.key == K_DOWN or event.key == K_UP:
            RPaddleUpOrDown = 0

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
    # Collision detection w/RPaddle
    if BallX + BallHalf > RPaddleX and \
            BallY > RPaddleY and \
            BallY < RPaddleY + RPaddleH:
        dx *= -1

    # Collision detection w/LPaddle
    if BallX - BallHalf < LPaddleX + LPaddleW / 2 and \
            BallY > RPaddleY and \
            BallY < LPaddleY + LPaddleH:
        dx *= -1

    screen.fill(white)
    pygame.draw.rect(screen, red, (LeftSideOfNet, 0, NetWidth, ScreenHeight))
    pygame.draw.circle(screen, black, BallLocation, BallSize)

    RPaddleY += RPaddleUpOrDown
    RPaddle = (RPaddleX, RPaddleY, RPaddleW, RPaddleH)
    pygame.draw.rect(screen, blue, RPaddle)

    if BallY > LPaddleY + LPaddleH / 2: # Below botton half of LpaddleY
        LPaddleY += random.randint(-1,5)
    else: #Above
        LPaddleY -= random.randint(-1,5)

    LPaddle = (LPaddleX, LPaddleY, LPaddleW, LPaddleH)
    pygame.draw.rect(screen, green, LPaddle)

    pygame.display.update()
    time.sleep(0.01)
# end of the while loop
print("Game Over")
pygame.quit()
