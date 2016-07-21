#Beta Battleship Game
#TRY USING FOR LOOPS
#REMOVE HARDCODING/ADD MORE VARIABLES
from random import *
grid = []
side = 50            #side length of sqaure
boatCoord= [0,0]    #boat coordinates [x,y])
turn = 3            #maximum turns for player
queue = []          #to store graphics from hits and misses
result = 0          #0 for misses, 1 for hits
def setup():
    size(500,500)
    print("Guess which tile the boat is in!")
    noLoop()
def draw():
    global grid
    global side
    global boatCoord 
    global turn
    global queue
    global result
    for i in range(10):          #creating board (range(rows) and append(coloumns))
        grid.append(["0"]*10)
    for i in range(len(grid)):         #for each row in grid
        for y in range (len(grid[i])):         #for each tile in each row
            fill(0,0,255)
            rect(i*side, y*side,side,side)         #tile
    #for i in range(2):
        #boatCoord[i] = randrange(100)      #getting random x,y coord for boat                  <------temporary delete
    print (boatCoord)
    if mouseButton==LEFT:
        if int(mouseX/side)*side+.5*side<boatCoord[0] and int(mouseY/side)*side+.5*side<boatCoord[1]:
            fill(255,0,0)
            ellipse(int(mouseX/side)*side+.5*side,int(mouseY/side)*side+.5*side, side,side)
            print("Direct Hit! You win!")
            result = 1
        else:
            fill(255,0,0)
            ellipse(int(mouseX/side*side+.5*side),int(mouseY/side*side+.5*side), side,side)         #mouseX/100 creates a float (i.e. 2.5), then int()rounds that number down (2), and *100 creates the proper coordinates (200) 
            print("You Missed! You have "+str(turn)+" turn(s) left!")
            result = 0
        turn -= 1
        queue.append([int(mouseX/side*side+.5*side),int(mouseY/side*side+.5*side),result])    #stores tile graphic for next frame
        if turn<1:
            print("GAME OVER Try again!")
            turn = 3
        for i in range(len(queue)):                    #redraw stored objects with proper color/position
            if queue[i][2]==1:
                fill(255,0,0)
                ellipse(queue[i][0],queue[i][1],side,side)
            else:
                fill(255)
                ellipse(queue[i][0],queue[i][1],side,side)
def mousePressed():
    redraw()    #forces our tile image to appear

    
    
    
    