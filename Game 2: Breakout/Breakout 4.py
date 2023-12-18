# breakout12

# Dany Christel
#

# what this code does

# import for the pygame stuff
import pygame
from pygame.locals import *


# all of my classes
class Brick:
    '''This class defines a brick
    the attributes for the brick are as follows
    rect - rectangle
    color - color of the brick
    points - how many points the brick is worth
    '''

    # constructor - makes the object
    def __init__(self, rect, color, points):
        self.rect = rect
        self.color = color
        self.points = points

    def __str__(self):
        return f"Brick: {self.rect} {self.color} {self.points}"

    def draw(self, screen):
        return pygame.draw.rect(screen, self.color, self.rect)


class TextBox:
    def __init__(self, x, y, size, \
                 color=pygame.Color("white"), \
                 bg_color=pygame.Color("black")):
        self.x = x
        self.y = y
        self.font = pygame.font.Font(None, size)
        self.color = color
        self.bg_color = bg_color

    def draw(self, screen, text):
        text_bitmap = self.font.render(text, True, self.color, self.bg_color)
        screen.blit(text_bitmap, (self.x, self.y))


# Here are all the funcitons
def MakeBricks(rows, cols):
    myColors = ["green", "red", "orange", "yellow", "violet", "blue"]
    # print(myColors[0])
    mybricks = []
    BrickWidth = 35
    BrickHeight = 20
    BrickSpacing = 5
    BrickInitialShift = 20
    for r in range(rows):
        for c in range(cols):
            BrickRect = (c * (BrickWidth + BrickSpacing) + BrickInitialShift, \
                         r * (BrickHeight + BrickSpacing) + BrickInitialShift, \
                         BrickWidth, BrickHeight)
            NewBrick = Brick(BrickRect, myColors[r], (rows - r) * 10)
            mybricks.append(NewBrick)
    return mybricks


# initializing our pygame stuff
pygame.init()
clock = pygame.time.Clock()
fps = 60

# defining our pygame screen
ScreenHeight = 600
ScreenWidth = 800
pygame.display.set_caption("Breakout")
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))

# defining the paddle
PaddleX = 400
PaddleY = 530
PaddleW = 80
PaddleH = 20
Paddle_dx = 0
PaddleLocation = (PaddleX, PaddleY, PaddleW, PaddleH)

# defining the ball
BallX = PaddleX + PaddleW // 2
BallY = PaddleY - 10
BallLocation = (BallX, BallY)
dx = 0
dy = 0
BallRadius = 6

# makeing our bricks
bricks = MakeBricks(5, 19)

# initial drawing commands
BallRect = pygame.draw.circle(screen, pygame.Color("green"), BallLocation, BallRadius)
PaddleRect = pygame.draw.rect(screen, pygame.Color("black"), PaddleLocation)

score = 0
txtScore = TextBox(20, 560, 30)
balls = 5
txtBalls = TextBox(700, 560, 30)
txtMessage = TextBox(300, 560, 30, pygame.Color("black"), pygame.Color("white"))

NewGame = True
NewBall = False

# game loop
GameRunning = True
while GameRunning:
    # events... keyboard
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # == means is equal to
            GameRunning = False  # = means Gets... GameRunning variable gets the value false
        if event.type == pygame.KEYDOWN:
            if event.key == K_RIGHT:
                Paddle_dx = 7
            if event.key == K_LEFT:
                Paddle_dx = -7
            if event.key == K_n and NewGame:
                dx = 6
                dy = -6
                score = 0
                balls = 5
                bricks = MakeBricks(5, 19)
                NewGame = False
            if event.key == K_SPACE and NewBall:
                dx = 6
                dy = -6
                NewBall = False

        if event.type == pygame.KEYUP:
            if event.key == K_RIGHT or event.key == K_LEFT:
                Paddle_dx = 0

    # check for ball/brick interaction
    for b in bricks:
        if pygame.Rect.colliderect(BallRect, b.rect):
            dy *= -1
            score += b.points
            bricks.remove(b)
            break

    # bounce ball off walls and floor and ceiling
    if BallX > ScreenWidth - BallRadius or BallX < BallRadius:
        dx *= -1
    if BallY < BallRadius:
        dy *= -1

    if BallY > ScreenHeight - BallRadius:
        balls -= 1
        dx = 0
        dy = 0
        BallX = PaddleX + PaddleW // 2
        BallY = PaddleY - 10
        if balls == 0:
            NewGame = True
        else:
            NewBall = True

    # ball / paddle interaction
    TempWidth = PaddleRect.w // 6
    dxList = [-7, -5, -3, 3, 5, 7]
    for i in range(6):
        TempRect = PaddleRect.copy()
        TempRect.w = TempWidth
        TempRect.x = TempRect.x + TempWidth * i
        if pygame.Rect.colliderect(BallRect, TempRect):
            dy *= -1
            dx = dxList[i]
            break

    # updating the ball position
    if NewBall or NewGame:
        BallX = PaddleX + PaddleW // 2
        BallY = PaddleY - 10
    else:
        BallX += dx
        BallY += dy
    BallLocation = (BallX, BallY)

    # update the paddle position
    PaddleX += Paddle_dx
    if PaddleX > ScreenWidth - PaddleW:
        PaddleX = ScreenWidth - PaddleW
    if PaddleX < 0:
        PaddleX = 0
    PaddleLocation = (PaddleX, PaddleY, PaddleW, PaddleH)

    # drawing commands
    screen.fill(pygame.Color("white"))
    BallRect = pygame.draw.circle(screen, pygame.Color("green"), BallLocation, BallRadius)
    PaddleRect = pygame.draw.rect(screen, pygame.Color("black"), PaddleLocation)

    txtScore.draw(screen, f"Score: {score}")
    txtBalls.draw(screen, f"Balls: {balls}")
    if NewGame:
        txtMessage.draw(screen, "Press N for new game.")
    if NewBall:
        txtMessage.draw(screen, "Press SPACE for new ball.")

    for b in bricks:
        # pygame.draw.rect(screen, b.color, b.rect)
        b.draw(screen)

    # final update
    pygame.display.update()
    clock.tick(fps)  # for every second at most 60 frames (loops) can pass
    # print(clock.get_fps())

# out of the while loop
print("Game over")
pygame.quit()