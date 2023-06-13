import pygame
screen_width = 700
screen_hight = 500
screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption('My Game2')
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ORANGE = (255, 127, 0)
RED = (255, 0, 0)
x = 400
y = 400
hight = 64
width = 64
speed = 10
isjumping = False
step = 5
right = False
left = False
moves = 0
move_right = [pygame.image.load("D:\python\study\R1.png"), pygame.image.load("D:\python\study\R2.png"), pygame.image.load("D:\python\study\R3.png"), pygame.image.load("D:\python\study\R4.png"), pygame.image.load(
    "D:\python\study\R5.png"), pygame.image.load("D:\python\study\R6.png"), pygame.image.load("D:\python\study\R7.png"), pygame.image.load("D:\python\study\R8.png"), pygame.image.load("D:\python\study\R9.png")]
move_left = [pygame.image.load("D:\python\study\L1.png"), pygame.image.load("D:\python\study\L2.png"), pygame.image.load("D:\python\study\L3.png"), pygame.image.load("D:\python\study\L4.png"), pygame.image.load(
    "D:\python\study\L5.png"), pygame.image.load("D:\python\study\L6.png"), pygame.image.load("D:\python\study\L7.png"), pygame.image.load("D:\python\study\L8.png"), pygame.image.load("D:\python\study\L9.png")]

bg = pygame.image.load('D:\python\study/bg.jpg')
hero = pygame.image.load('D:\python\study\standing.png')
clock = pygame.time.Clock()

def show():
    global moves
    screen.blit(bg, (0, 0))
    if left:
        screen.blit(move_left[moves], (x,y))
        moves += 1 
        if moves == 9 :
            moves = 0
    elif right :
        screen.blit(move_right[moves], (x,y))
        moves += 1 
        if moves == 9 :
            moves = 0
    else:
         screen.blit(hero, (x, y))
   
   #  pygame.draw.rect(screen, ORANGE, (x, y, hight, width))
    pygame.display.update()



    


while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
   
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - step >= 0:
        x -= step
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x + width + step <= screen_width:
        x += step
        right = True
        left = False
    else :
        right = False
        left = False
        moves = 0    
    if not isjumping:
        if keys[pygame.K_SPACE]:
            isjumping = True
    else:
        if speed >= -10:
            neg = 1
            if speed < 0:
                neg = -1
            y -= (speed**2) * 0.25 * neg
            speed -= 1
        else:
            speed = 10
            isjumping = False

    show()
