from random import *

xPos = 250
xSpeed = 1
yPos = 250
ySpeed = -2

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
    fill(50,50,50)
    ellipse(xPos,yPos,100,100)
    if xPos > 450 or xPos < 50:
        xSpeed *= -1
    if yPos > 450 or yPos < 50:
        ySpeed *= -1
        
        
    
    
        
        
        
        
    
    