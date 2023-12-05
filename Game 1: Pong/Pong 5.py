# pong5
# Code With Mr Wagner and
# Dany
# Bounce the ball

import time

import pygame

pygame.init()

# Variables
ScreenWidth = 800
ScreenHeight = 600
BallX = 100
BallY = 100
BallLocation = (BallX, BallY)  # tuple
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

# standard pygame game loo while , for , if

GameRunning = True
while GameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRunning = False
    # New Value = Old Value + 1
    BallX = BallX + dx
    BallY = BallY + dy
    BallLocation = (BallX, BallY)  # Tuple

    if BallY > 600 or BallY < 0:
        dy = dy * -1

    if BallX > 800 or BallX < 0:
        dx = dx * -1
    #if BallX < 0:
       # dx = dx * -1

    screen.fill(white)
    pygame.draw.circle(screen, lime, BallLocation, 10, 5)
    pygame.draw.rect(screen, black, (395, 0, 10, 600))

    pygame.display.update()
    time.sleep(0.01)
# end of the while loop
print("Game Over")
pygame.quit()
