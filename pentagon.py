#Adrian Gomez
#20119988

from graphics import*
from time import sleep
lower = Point(250, 475)
def main ():
    window=GraphWin("Pentagon",500,500)#creates drawing space
    #pentagon drawing
    textbox1=Text(lower,"Click 5 times and make a Pentagon")#textbox
    textbox1.draw(window)#draws textbox
    p0=window.getMouse()#stores mouseclick
    p1=window.getMouse()
    p2=window.getMouse()
    p3=window.getMouse()
    p4=window.getMouse()
    p01=Point(p0.getX(),p0.getY())#points of mouseclicks
    p10=Point(p1.getX(),p1.getY())
    p20=Point(p2.getX(),p2.getY())
    p30=Point(p3.getX(),p3.getY())
    p40=Point(p4.getX(),p4.getY())
    penta=Polygon(p01,p10,p20,p30,p40)#pentagon
    penta.draw(window)#draws pentagon
    textbox1.undraw()
    #red circle click portion
    textbox2=Text(lower, "Click to draw a Red Circle at your first click")
    textbox2.draw(window)
    p5=window.getMouse()
    circ = Circle(p01, 20)
    circ.draw(window)
    circ.setFill("Red")
    textbox2.undraw()
    #make the Red circle travel clockwise from first point
    textbox3 = Text(lower, "Click to make the Red Circle travel Clockwise from the first point")
    textbox3.draw(window)
    p6=window.getMouse()
    textbox3.undraw()
    ax = p1.getX() - p0.getX() #to move the red circle on the line
    ay = p1.getY() - p0.getY()
    for i in range(50): #to slow it down
        circ.move((ax/50),(ay/50))
        sleep(0.01)
    bx = p2.getX() - p1.getX()
    by = p2.getY() - p1.getY()
    for i in range(50):
        circ.move((bx/50),(by/50))
        sleep(0.01)
    cx = p3.getX() - p2.getX()
    cy = p3.getY() - p2.getY()
    for i in range(50):
        circ.move((cx/50),(cy/50))
        sleep(0.01)
    dx = p4.getX() - p3.getX()
    dy = p4.getY() - p3.getY()
    for i in range(50):
        circ.move((dx/50),(dy/50))
        sleep(0.01)
    ex = p0.getX() - p4.getX()
    ey = p0.getY() - p4.getY()
    for i in range(50):
        circ.move((ex/50),(ey/50))
        sleep(0.01)
    #click to close the window
    textbox4 = Text(lower, "Click to close Window")
    textbox4.draw(window)
    p6=window.getMouse()
    window.close()
    
    
         
    
main()
