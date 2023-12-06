# Pong 16
# Code With Mr Wagner
# Dany Christel
# Cleaning up the Code.

# Pong 15
# Code With Mr Wagner
# Dany Christel
# Game Over and Reset the Game.

import random
import time

import pygame
from pygame.locals import *

pygame.init()

# variables
ScreenWidth = 800
ScreenHeight = 600

BallX = random.randint(300, 600)
BallY = random.randint(100, 600)
BallLocation = (BallX, BallY)  # tuple
BallSize = 10
BallHalf = BallSize / 2
dx = random.choice([-3, 3])  # change in x
dy = random.choice([-3, 3])

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

RightScore = 0
LeftScore = 0
# tuple (x,y,y,q)
# Constant
#       (red, green, blue) 0 and 255
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)

# create a window
pygame.display.set_caption("Pong")
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
MyFont = pygame.font.SysFont(None, 100)
MySmallFont = pygame.font.SysFont(None, 40)
Message = ""  # This is an Empty string

CenterOfScreen = ScreenWidth / 2
NetWidth = 10
LeftSideOfNet = CenterOfScreen - (NetWidth / 2)

BallStopped = False
NewGame = False

# standard pygame game loop  while, for, if
GameRunning = True
while GameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRunning = False
        # keyboard events:
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                # print("Down Key")
                RPaddleUpOrDown = 3
            if event.key == K_UP:
                # print("Up Key")
                RPaddleUpOrDown = -3
            if event.key == K_SPACE:
                if BallStopped == True:
                    dx = random.choice([-3, 3])
                    dy = random.choice([-3, 3])
                    BallX = random.randint(300, 600)
                    BallY = random.randint(100, 600)
                    BallStopped = False
                    Message = ""
            if event.key == K_n:
                if BallStopped == True and NewGame == True:
                    dx = random.choice([-3, 3])
                    dy = random.choice([-3, 3])
                    BallX = random.randint(300, 600)
                    BallY = random.randint(100, 600)
                    BallStopped = False
                    Message = ""
                    LeftScore = 0
                    RightScore = 0
                    NewGame = False

        if event.type == KEYUP:
            if event.key == K_DOWN or event.key == K_UP:
                RPaddleUpOrDown = 0

    # == MEANS IS EQUAL TO  IF X == 10 RETURN TRUE OR FALSE
    # = MEANS ASSIGNED TO  X=10

    BallX += dx
    BallY += dy
    BallLocation = (BallX, BallY)  # tuple

    # bounce code
    # if BallX > ScreenWidth - BallHalf or BallX < BallHalf:
    # dx *= -1
    if BallY > ScreenHeight - BallHalf or BallY < BallHalf:
        dy *= -1
    # the ball goes off to the right side.
    if BallX > ScreenWidth - BallHalf:
        RightScore += 1
        BallStopped = True
    # The ball goes off to the left side.
    if BallX < BallHalf:
        LeftScore += 1
        BallStopped = True

    if BallStopped == True:  # Stops the ball.
        dx = 0
        dy = 0
        BallX = ScreenWidth / 2
        BallY = ScreenHeight / 2
        Message = "Press SPACE to continue"
        if RightScore == 10 or LeftScore == 10:
            Message = "GAME OVER! Press N for New game"
            NewGame = True

        # Collision detection w/ RPaddle
    if BallX + BallHalf > RPaddleX and \
            BallX - BallHalf < RPaddleX + RPaddleW and \
            BallY > RPaddleY and \
            BallY < RPaddleY + RPaddleH:
        dx *= -1

    # Collision detection w/ LPaddle
    if BallX - BallHalf < LPaddleX + LPaddleW and \
            BallX + BallHalf > LPaddleX and \
            BallY > LPaddleY and \
            BallY < LPaddleY + LPaddleH:
        dx *= -1

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, (LeftSideOfNet, 0, NetWidth, ScreenHeight))
    pygame.draw.circle(screen, RED, BallLocation, BallSize, BallSize)

    RPaddleY += RPaddleUpOrDown
    RPaddle = (RPaddleX, RPaddleY, RPaddleW, RPaddleH)
    pygame.draw.rect(screen, BLUE, RPaddle)

    if BallY > LPaddleY + LPaddleH / 2:  # below bottom half of left paddle
        LPaddleY += random.randint(-1, 5)
    else:  # above
        LPaddleY -= random.randint(-1, 5)

    LPaddle = (LPaddleX, LPaddleY, LPaddleW, LPaddleH)
    pygame.draw.rect(screen, GREEN, LPaddle)

    TextImg = MyFont.render(str(RightScore), True, BLUE, WHITE)
    TextRect = TextImg.get_rect()
    TextRect.midtop = (450, 10)
    screen.blit(TextImg, TextRect)

    TextImg = MyFont.render(str(LeftScore), True, GREEN, WHITE)
    TextRect = TextImg.get_rect()
    TextRect.midtop = (350, 10)
    screen.blit(TextImg, TextRect)

    TextImg = MySmallFont.render(Message, True, YELLOW, GRAY)
    TextRect = TextImg.get_rect()
    TextRect.midtop = (400, 300)
    screen.blit(TextImg, TextRect)


    pygame.display.update()
    time.sleep(0.01)
# end of the while loop

print("Game Over")
pygame.quit()
