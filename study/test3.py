import pygame
pygame.joystick.init()
if pygame.joystick.get_count() == 0:
    print("No joystick found.")
else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
move_right = [pygame.image.load("D:\python\study\R1.png"), pygame.image.load("D:\python\study\R2.png"), pygame.image.load("D:\python\study\R3.png"), pygame.image.load("D:\python\study\R4.png"), pygame.image.load(
    "D:\python\study\R5.png"), pygame.image.load("D:\python\study\R6.png"), pygame.image.load("D:\python\study\R7.png"), pygame.image.load("D:\python\study\R8.png"), pygame.image.load("D:\python\study\R9.png")]
move_left = [pygame.image.load("D:\python\study\L1.png"), pygame.image.load("D:\python\study\L2.png"), pygame.image.load("D:\python\study\L3.png"), pygame.image.load("D:\python\study\L4.png"), pygame.image.load(
    "D:\python\study\L5.png"), pygame.image.load("D:\python\study\L6.png"), pygame.image.load("D:\python\study\L7.png"), pygame.image.load("D:\python\study\L8.png"), pygame.image.load("D:\python\study\L9.png")]

bg = pygame.image.load('D:\python\study/bg.jpg')
hero = pygame.image.load('D:\python\study\standing.png')
clock = pygame.time.Clock()
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


class player():
    def __init__(self, x, y, hight, width):
        self.x = x
        self.y = y
        self.width = width
        self.hight = hight
        self.step = 5
        self.left = False
        self.right = False
        self.moves = 0
        self.speed = 10
        self.isjumping = False
        self.standing = True

    def draw(self, screen):
        if not self.standing:
            if self.left:
                screen.blit(move_left[self.moves // 2], (self.x, self.y))
                self.moves += 1
                if self.moves == 18:
                    self.moves = 0
            elif self.right:
                screen.blit(move_right[self.moves // 2], (self.x, self.y))
                self.moves += 1
                if self.moves == 18:
                    self.moves = 0
        else:
            if self.right:
                screen.blit(move_right[0], (self.x, self.y))
            else:
                screen.blit(move_left[0], (self.x, self.y))


class Bullet:
    def __init__(self, x, y, radius, color, direction, step):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.direction = direction
        self.step = step * direction

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


man = player(600, 400, 64, 64)


def show():
    global moves
    screen.blit(bg, (0, 0))
    man.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    pygame.display.update()


bullets = []

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    if pygame.joystick.get_count() != 0:
        horizontal_axis = joystick.get_axis(0)
        vertical_axis = joystick.get_axis(1)
        bullet_shoot = joystick.get_button(1)

        for bullet in bullets:
            if bullet.x < screen_width and bullet.x > 0:
                bullet.x += bullet.step
            else:
                bullets.remove(bullet)
        if  bullet_shoot:
            if len(bullets) < 5:
                direction = 0
                if man.right:
                    direction = 1
                else:
                    direction = -1
                bullets.append(Bullet(round(man.x + man.width//2),
                               round(man.y + man.hight//2), 5, RED, direction, 10))

        if horizontal_axis < -0.2 and man.x - man.step >= 0:
            man.x -= man.step
            man.left = True
            man.right = False
            man.standing = False
        elif horizontal_axis > 0.2 and man.x + man.width + man.step <= screen_width:
            man.x += man.step
            man.right = True
            man.left = False
            man.standing = False
        else:
            man.standing = True
            man.moves = 0

        if not man.isjumping:
            if joystick.get_button(4):
                man.isjumping = True

        else:
            if man.speed >= -10:
                neg = 1
                if man.speed < 0:
                    neg = -1
                man.y -= (man.speed**2) * 0.25 * neg
                man.speed -= 1
            else:
                man.isjumping = False
                man.speed = 10

    show()
