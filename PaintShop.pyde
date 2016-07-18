
def setup():
    frameRate(800)
    size(480,600)
    background(255,255,255)
    fill(255,0,0)
    rect(0,0,80,80)
    fill(0,255,0)
    rect(80,0,80,80)
    fill(0,0,255)
    rect(160,0,80,80)
    fill(255,0,255)
    rect(240,0,80,80)
    fill(0,255,255)
    rect(320,0,80,80)
    fill(255,255,0)
    rect(400,0,80,80)
    stroke(255,255,255)
    fill(255,255,255)
    
def draw():
    #RED
    if mouseButton == LEFT:
        if mouseY < 80 and mouseX < 80:
            fill(255,0,0)
        if mouseY > 80 and mouseX > 0:
            if mousePressed:
                stroke(255,0,0)
                ellipse(mouseX,mouseY,15,15)
    #GREEN
    if mouseButton == LEFT:
        if mouseY < 80 and mouseX > 160:
            fill(0,255,0)
        if mouseY > 80 and mouseX > 0:
            if mousePressed:
                stroke(0,255,0)
                ellipse(mouseX,mouseY,15,15)

    
               
                    
    
                
            
        
        
    

    