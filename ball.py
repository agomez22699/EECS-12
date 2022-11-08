#Adrian Gomez
#20119988

from graphics import*
from time import sleep
r = 30
z = 40
def main():
    window=GraphWin("Ball")#opens a seperate window for ball to be drawn
    d = Circle(Point(40,0),z)
    c = Circle(Point(40,0),r)#gives coordinates for ball and how big
    d.draw(window)
    c.draw(window)#draws the ball
    c.setFill("red")
    d.setFill("blue")
    for i in range(500):#repeats the code 500 times
        c.move(0,10), d.move(0,10) #moving in positive direction
        sleep(0.2)#slows the ball down so we can see it
        c.move(0,20), d.move(0,20)
        sleep(0.2)
        c.move(0,30), d.move(0,30)
        sleep(0.2)
        c.move(0,40), d.move(0,40)
        sleep(0.2)
        c.move(0,50), d.move(0,50)
        sleep(0.2)
        c.move(0,60), d.move(0,60)
        sleep(0.2)
        c.move(0,-10), d.move(0,-10)#Starts moving the ball in the opposite direction it came from
        sleep(0.2)
        c.move(0,-20), d.move(0,-20)
        sleep(0.2)
        c.move(0,-30), d.move(0,-30)
        sleep(0.2)
        c.move(0,-40), d.move(0,-40)
        sleep(0.2)
        c.move(0,-50), d.move(0,-50)
        sleep(0.2)
        c.move(0,-60), d.move(0,-60)
    window.close()
main()

        


