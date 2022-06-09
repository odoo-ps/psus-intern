import pygame as py
import random

py.init()

screen = py.display.set_mode([500,500])

speed = 5

class Drawer(object):
    def __init__(self):
        self.x = 400
        self.y = 400
        self.width = 5
        self.height = 5
        self.color = (255,255,255)
    def up(self):
        if self.x < 500 - speed - self.height:
            x += speed


def drawLine(ix, iy, nx, ny, color):
    py.draw.line(screen, color, (ix, iy), (nx, ny))
    py.display.flip()


p1X = 400
p1Y = 400
p2X = 100
p2Y = 100
width = 5
height = 5
speed = 5

running = True
while running:
    py.time.delay(50)
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    
    keys = py.key.get_pressed()

    if keys[py.K_UP] and p1Y > speed:
        a = p1X
        b = p1Y
        p1Y -= speed
        py.draw.line(screen, (255,255,255), (a, b), (p1X, p1Y))
        py.display.flip()
    if keys[py.K_DOWN] and p1Y < 500 - speed - height:
        a = p1X
        b = p1Y
        p1Y += speed
        drawLine(a,b,p1X, p1Y, (255,255,255))
    if keys[py.K_LEFT] and p1X > speed:
        p1X -= speed
    if keys[py.K_RIGHT] and p1X < 500 - speed - width:
        p1X += speed
    if keys[py.K_a] and p2X > speed:
        p2X -= speed
    if keys[py.K_d] and p2X < 500 - speed - width:
        p2X += speed
    if keys[py.K_w] and p2Y > speed2:
        p2Y -= speed
    if keys[py.K_s] and p2Y < 500 - speed - height:
        p2Y += speed

    
    screen.fill((0,0,0))
    py.draw.rect(screen, (255, 255, 255), (p1X, p1Y, width, height))
    py.draw.rect(screen, (194, 197, 204), (p2X, p2Y, width, height))
    py.display.update()

py.quit()