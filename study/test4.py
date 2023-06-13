import pygame
successes, fails = pygame.init()
print(successes, fails)

move_right = [pygame.image.load("D:\python\study\R1.png"), pygame.image.load("D:\python\study\R2.png"), pygame.image.load("D:\python\study\R3.png"), pygame.image.load("D:\python\study\R4.png"), pygame.image.load(
    "D:\python\study\R5.png"), pygame.image.load("D:\python\study\R6.png"), pygame.image.load("D:\python\study\R7.png"), pygame.image.load("D:\python\study\R8.png"), pygame.image.load("D:\python\study\R9.png")]
move_left = [pygame.image.load("D:\python\study\L1.png"), pygame.image.load("D:\python\study\L2.png"), pygame.image.load("D:\python\study\L3.png"), pygame.image.load("D:\python\study\L4.png"), pygame.image.load(
    "D:\python\study\L5.png"), pygame.image.load("D:\python\study\L6.png"), pygame.image.load("D:\python\study\L7.png"), pygame.image.load("D:\python\study\L8.png"), pygame.image.load("D:\python\study\L9.png")]

move_rightE = [pygame.image.load("D:\python\study\R1.png"), pygame.image.load("D:\python\study\R2.png"), pygame.image.load("D:\python\study\R3.png"), pygame.image.load("D:\python\study\R4.png"), pygame.image.load(
    "D:\python\study\R5.png"), pygame.image.load("D:\python\study\R6.png"), pygame.image.load("D:\python\study\R7.png"), pygame.image.load("D:\python\study\R8.png"), pygame.image.load("D:\python\study\R9.png")]
move_leftE = [pygame.image.load("D:\python\study\L1.png"), pygame.image.load("D:\python\study\L2.png"), pygame.image.load("D:\python\study\L3.png"), pygame.image.load("D:\python\study\L4.png"), pygame.image.load(
    "D:\python\study\L5.png"), pygame.image.load("D:\python\study\L6.png"), pygame.image.load("D:\python\study\L7.png"), pygame.image.load("D:\python\study\L8.png"), pygame.image.load("D:\python\study\L9.png")]



bg = pygame.image.load("D:\python\study/bg.jpg")
hero = pygame.image.load("D:\python\study\standing.png")

screenWidth = 700
screenHeight = 500
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("cs younes game")

BLACK = (0, 0, 0)  # RGB
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.step = 5
        self.left = False
        self.right = False
        self.moves = 0
        self.speed = 10
        self.isJumping = False
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
        pygame.draw.circle(screen, self.color,(self.x, self.y) ,self.radius)

class Enemy:
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.start = x
        self.step = 3
        self.moves = 0

    def draw(self, screen):
        self.move()
        if self.step < 0:
            screen.blit(move_leftE[self.moves // 2], (self.x, self.y))
            self.moves += 1
            if self.moves == 11 * 2:
                self.moves = 0
        else:
            screen.blit(move_rightE[self.moves // 2], (self.x, self.y))
            self.moves += 1
            if self.moves == 11 * 2:
                self.moves = 0




    def move(self):
        if self.step > 0:
            if self.x + self.step > self.end:
                self.step *= -1
            else:
                self.x += self.step
        else:
            if self.x - self.step < self.start:
                self.step *= -1
            else:
                self.x += self.step



man = Player(600, 400, 64, 64)
enemy = Enemy(100, 400, 64, 64, 500)


def redrawGame():
    global moves

    screen.blit(bg, (0, 0))
    man.draw(screen)
    enemy.draw(screen)
    for bullet in  bullets:
        bullet.draw(screen)

    pygame.display.update()
bullets = []

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if len(bullets) < 5:
                    direction = 0
                    if man.right:
                        direction = 1
                    else:
                        direction = -1
                    bullets.append(
                        Bullet(round(man.x + man.width // 2), round(man.y + man.height // 2), 5, RED, direction, 10))
    keys = pygame.key.get_pressed()

    for bullet in bullets:
        if bullet.x < screenWidth and bullet.x > 0:
            bullet.x += bullet.step
        else:
            bullets.remove(bullet)





    if keys[pygame.K_LEFT] and man.x - man.step >= 0:
        man.x -= man.step
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x + man.width + man.step <= screenWidth:
        man.x += man.step
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.moves = 0
    if not man.isJumping:
        if keys[pygame.K_SPACE]:
            man.isJumping = True
    else:
        if man.speed >= -10 :
            neg = 1
            if man.speed < 0:
                neg = -1
            man.y -= (man.speed ** 2) * 0.25 * neg
            man.speed -= 1
        else:
            man.speed = 10
            man.isJumping = False

    redrawGame()