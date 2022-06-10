from distutils.spawn import spawn
import pygame as py
import random
import time

py.init()

screen = py.display.set_mode([500,500])

speed = 5

p1X = 400
p1Y = 400
p1width = 10
p1height = 10
p1direction = 'UP'
p1change = 'UP'
p1body = [[400,400]]

p2X = 100
p2Y = 400
p2width = 10
p2height = 10
p2direction = 'UP'
p2change = 'UP'
p2body = [[100,400]]

speed = 10
spawn = True
blockX = 250
blockY = 250
winner = 3

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

    if p1X < 0 or p1X > 500: 
        winner = 2
        running = False
    if p1Y < 0 or p1Y > 500:
        winner = 2
        running = False
    if p2X < 0 or p2X > 500:
        winner = 1
        running = False
    if p2Y < 0 or p2Y > 500:
        winner = 1
        running = False
    
    p1body.insert(0, list([p1X, p1Y]))
    p2body.insert(0, list([p2X, p2Y]))

    if (p1X == blockX and p1Y == blockY):
        spawn = False
    else:
        p1body.pop()

    if (p2X == blockX and p2Y == blockY):
        spawn = False
    else:
        p2body.pop()

    if(p1X == p2X and p1Y == p2Y):
        py.quit()

    for pos in p1body:
        if p2X == pos[0] and p2Y == pos[1]:
            winner = 1
            running = False
    for pos in p2body:
        if p1X == pos[0] and p1Y == pos[1]:
            winner = 2
            running = False

    if not spawn:
        cont = True
        while cont:
            x = random.randrange(0,490,10)
            y = random.randrange(0,490,10)
            if (x != p1X and y != p1Y) and (x != p2X and y != p2Y):
                blockX = x
                blockY = y
                cont = False
        spawn = True

    screen.fill((0,0,0))
    py.draw.rect(screen, (255,255,0), (blockX,blockY,10,10))
    for pos in p1body:
        py.draw.rect(screen, (255,0,0), (pos[0], pos[1], p1width, p1height))
    for pos in p2body:    
        py.draw.rect(screen, (0, 0, 255), (pos[0], pos[1], p2width, p2height))
    py.display.update()

text = "tie"
if winner == 2:
    text = "blue"
elif winner == 1:
    text = "red"
font = py.font.SysFont('times new roman', 50)
display = font.render(text, True, py.Color(255,255,255))
rect = display.get_rect()
rect.midtop = (200,200)
screen.blit(display, rect)
print(text)
time.sleep(5)
py.quit()