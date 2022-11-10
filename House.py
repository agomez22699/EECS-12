#Adrian Gomez
#20119988

from graphics import*
lower = Point(250, 475)
def main():
    window=GraphWin("House",500,500)#creates drawing space
    #house stuff
    label=Text(lower, "Click on the lower left side of the window")#textbox
    label.draw(window)
    z=window.getMouse()#stores the mouseclick
    label.undraw()#erase textbox
    label2=Text(lower, "Click on the upper right of the window")
    label2.draw(window)
    w=window.getMouse()
    label2.undraw()
    house = Rectangle(Point(z.getX(),z.getY()),Point(w.getX(),w.getY()))#draws house
    house.draw(window)
    house.setFill("Green")
    house.setOutline("Brown")
    #door stuff
    label3=Text(lower, "Click inside the house to make the door")
    label3.draw(window)
    q=window.getMouse()
    label3.undraw()
    housewidth=abs(w.getX()-z.getX())
    househeight=abs(w.getY()-z.getY())
    doorwidth=(0.1*housewidth)
    doorq1=Point(q.getX()-(0.1*housewidth),q.getY())
    doorq2=Point(q.getX()+(0.1*housewidth),z.getY())
    door = Rectangle(doorq1,doorq2)
    door.draw(window)
    door.setFill("Blue")
    door.setOutline("Brown")
    #window stuff
    labelwindow = Text(lower, "Click inside the house to make a window")
    labelwindow.draw(window)
    b=window.getMouse()
    labelwindow.undraw()
    windowb1=Point(b.getX()-0.5*doorwidth,b.getY()-0.5*doorwidth)
    windowb2=Point(b.getY()+0.5*doorwidth,b.getY()+0.5*doorwidth)
    window2 = Rectangle(windowb1,windowb2)
    window2.draw(window)
    window2.setFill("Red")
    window2.setOutline("Brown")
    #roof stuff
    labelroof = Text(lower, "Click on top of the house to make a roof")
    labelroof.draw(window)
    ui=window.getMouse()
    labelroof.undraw()
    p5=Point(z.getX(),w.getY())
    p2=Point(w.getX(),w.getY())
    roof = Polygon(p5,ui,p2)
    roof.draw(window)
    roof.setFill("Green")
    roof.setOutline("Brown")
    textbox4 = Text(lower, "Click to close Window")
    textbox4.draw(window)
    p6=window.getMouse()
    window.close()
    
main()
    
