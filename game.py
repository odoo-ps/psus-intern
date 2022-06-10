from distutils.spawn import spawn
import pygame as py
import random

py.init()

screen = py.display.set_mode([500,500])

speed = 5

p1X = 400
p1Y = 400
p1width = 25
p1height = 25
p1direction = 'UP'
p1change = 'UP'
p1body = [[400,400]]

p2X = 100
p2Y = 400
p2width = 25
p2height = 25
p2direction = 'UP'
p2change = 'UP'
p2body = [[100,400]]

speed = 5
spawn = False
blockX = 0
blockY = 0

def gameOver():
    py.quit()

def spawnBlock():
    while True:
        x = random.randint(0,500)
        y = random.randint(0,500)
        if (x > p1X + p1width  and y > p1Y + p1height) or (x < p1X and y < p1Y):
            if(x > p2X + p2width and y > p2Y + p2height) or (x < p2X and y < p2Y):
                py.draw.rect(screen, (255,255,0), (x,y,25,25))
                blockX = x
                blockY = y
                return

def checkCollision():
    if p1X < 0 or p1X > 500: 
        gameOver()
    if p1Y < 0 or p1Y > 500:
        gameOver()
    if p2X < 0 or p2X > 500:
        gameOver()
    if p2Y < 0 or p2Y > 500:
        gameOver


running = True
while running:
    py.time.delay(50)
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    
    keys = py.key.get_pressed()

    if keys[py.K_UP]:
        p1change = 'UP'
    if keys[py.K_DOWN]:
        p1change = 'DOWN'
    if keys[py.K_LEFT]:
        p1change = 'LEFT'
    if keys[py.K_RIGHT]:
        p1change = 'RIGHT'

    if keys[py.K_a]:
        p2change = 'LEFT'
    if keys[py.K_d]:
        p2change = 'RIGHT'
    if keys[py.K_w]:
        p2change = 'UP'
    if keys[py.K_s]:
        p2change = 'DOWN'

    if p1change == 'UP' and p1direction != 'DOWN':
        p1direction = 'UP'
    if p1change == 'DOWN' and p1direction != 'UP':
        p1direction = 'DOWN'
    if p1change == 'LEFT' and p1direction != 'RIGHT':
        p1direction = 'LEFT'
    if p1change == 'RIGHT' and p1direction != 'LEFT':
        p1direction = 'RIGHT'

    if p2change == 'UP' and p2direction != 'DOWN':
        p2direction = 'UP'
    if p2change == 'DOWN' and p2direction != 'UP':
        p2direction = 'DOWN'
    if p2change == 'LEFT' and p2direction != 'RIGHT':
        p2direction = 'LEFT'
    if p2change == 'RIGHT' and p2direction != 'LEFT':
        p2direction = 'RIGHT'
        
    if p1direction == 'UP':
        p1Y -= speed
    if p1direction == 'DOWN':
        p1Y += speed
    if p1direction == 'LEFT':
        p1X -= speed
    if p1direction == 'RIGHT':
        p1X += speed
    
    if p2direction == 'UP':
        p2Y -= speed
    if p2direction == 'DOWN':
        p2Y += speed
    if p2direction == 'LEFT':
        p2X -= speed
    if p2direction == 'RIGHT':
        p2X += speed

    checkCollision()

    if not spawn:
        spawnBlock()
        spawn = True

    screen.fill((0,0,0))
    py.draw.rect(screen, (255, 255, 255), (p1X, p1Y, p1width, p1height))
    py.draw.rect(screen, (194, 197, 204), (p2X, p2Y, p2width, p2height))
    py.display.update()

py.quit()