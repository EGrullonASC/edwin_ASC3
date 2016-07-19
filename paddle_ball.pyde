from random import *

xPos = 250
xSpeed = 2
yPos = 250
ySpeed = -4
paddle = rect 

def setup():
    size (500,500)
    background (255,255,255)
    
def draw():
    global xPos
    global xSpeed
    global yPos
    global ySpeed
    xPos += xSpeed
    yPos += ySpeed
    background(255,255,255)
    #BALL
    fill(255,0,0)
    ellipse(xPos,yPos,30,30)
    #PADDLE
    fill(0,0,0)
    paddle(mouseX,480,80,120)
    if xPos > 485 or xPos < 5:
        xSpeed *= -1
    if yPos > 485 or yPos < 5:
        ySpeed *= -1
    if ellipse > 475 and ellipse < 480:
        ySpeed *= -4
if 490 > mouseX and 10 < mouseY:
        ySpeed
    