#Beta Battleship Game
grid = []
side=100
def setup():
    size(500,500)
def draw():
    global grid
    global side
    for i in range(5):          #creating board (range(rows) and append(coloumns))
        grid.append(["0"]*5)
    for i in range(len(grid)):
        for y in range (len(grid[i])):
            fill(0,0,255)
            rect(i*side, y*side,side,side)
            grid[i].insert(y,[[i*side,i+(2*side)],[y*side,y+(2*side)]])    #grid[column][row]
            print(grid[i][y])
        if box[0][0]<mouseX<box[0][1] and box[1][0]<mouseY<box[1][1]:    ##tile<x1>  tile<x2>  tile<y1> tile<y2>  
            
            

            