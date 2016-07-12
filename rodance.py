from Myro import *
x=100
y=1
counter = 0
while counter < 5:
    forward(x,y)
    turnBy(90)
    counter = counter + 1
backward(1,.5)
backward(1,.5)
motors(6,0)