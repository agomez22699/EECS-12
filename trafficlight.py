#Adrian Gomez
#20119988


from time import sleep
from graphics import*

def main():
    #Lines for street
    window=GraphWin("Traffic Light",500,500)
    window.setCoords(-500,-500,500,500)
    aline = Line(Point(100,125),Point(100,500))
    aline.draw(window)
    bline = Line(Point(-100,125),Point(-100,500))
    bline.draw(window)
    cline = Line(Point(100,-125),Point(100,-500))
    cline.draw(window)
    dline = Line(Point(-100,-125),Point(-100,-500))
    dline.draw(window)
    eline = Line(Point(100,125),Point(500,125))
    eline.draw(window)
    fline = Line(Point(-100,125),Point(-500,125))
    fline.draw(window)
    gline = Line(Point(100,-125),Point(500,-125))
    gline.draw(window)
    hline = Line(Point(-100,-125),Point(-500,-125))
    hline.draw(window)
    he = Entry(Point(400,325),10)
    he.draw(window)
    he.setText("0")
    circ1 = Circle(Point(125,105),10)
    circ1.draw(window)
    circ2 = Circle(Point(-82,150),10)
    circ2.draw(window)
    circ3 = Circle(Point(82,-150),10)
    circ3.draw(window)
    circ4 = Circle(Point(-125,-105),10)
    circ4.draw(window)
    #Text for streets
    campusdr = Text(Point(180,-480), "Campus Dr.")
    campusdr.draw(window)
    culverdr = Text(Point(-420,150), "Culver Dr.")
    culverdr.draw(window)
    pedtext = Text(Point(200,325),"Pedestrain(0 or 1):")
    pedtext.draw(window)
    #Under the hood stuff lol
    #filling opposite lights with same color
    while True:
        circ2.setFill("Green")
        circ3.setFill("Green")
        circ1.setFill("Red")
        circ4.setFill("Red")
        sleep(1)#pauses the code for 1 second
        circ1.setFill("Green")
        circ4.setFill("Green")
        circ2.setFill("Red")
        circ3.setFill("Red")
        sleep(1)#pauses the code for 1 second
     
        if he.getText() == '1':#if there is a pedestrain, stop all lights for 2 seconds
            circ2.setFill("Red")
            circ3.setFill("Red")
            circ1.setFill("Red")
            circ4.setFill("Red")
            sleep(2)#sleeps for 2 seconds
            he.setText("0") #resets user input  
main()
    
