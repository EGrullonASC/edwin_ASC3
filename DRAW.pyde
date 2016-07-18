from random import *

def setup():
    size(600,600)
    background(255,255,255)
    frameRate(100)
    
def draw():
    drawEllipse()
        

def drawEllipse():
    if mousePressed:
        fill(0,255,0)
        rect(mouseX,mouseY,150,150)
    else:
        fill(255,0,0)
        rect(mouseX,mouseY,150,150)
    
    
    