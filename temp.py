#Adrian Gomez
#20119988

from graphics import*
errormessage=Point(150,430)
def main():
    #Text in front of rectangles
    window=GraphWin("Temperature Conversion Calculator",500,500)
    unitstext=Text(Point(80,40),"Enter C or F or K")
    unitstext.draw(window)
    temperaturetext=Text(Point(80,100),"Enter Temperature")
    temperaturetext.draw(window)
    tempinc=Text(Point(80,160),"Temperature in C")
    tempinc.draw(window)
    tempinf=Text(Point(80,220),"Temperature in F")
    tempinf.draw(window)
    tempink=Text(Point(80,280),"Temperature in K")
    tempink.draw(window)
    calculatetext=Text(Point(80,340),"Click here to Calculate")
    calculatetext.draw(window)
    quittext=Text(Point(80,400),"Quit")
    quittext.draw(window)
    #rectangle boxes/ entry objects
    rect1 = Entry(Point(300,40), 15)
    rect1.draw(window)
    rect2 = Entry(Point(300,90), 15)
    rect2.draw(window)
    rect3 = Rectangle(Point(250,150),Point(350,170))
    rect3.draw(window)
    rect4 = Rectangle(Point(250,210),Point(350,230))
    rect4.draw(window)
    rect5 = Rectangle(Point(250,270),Point(350,290))
    rect5.draw(window)
    rect6 = Rectangle(Point(250,330),Point(350,350))
    rect6.draw(window)
    rect7 = Rectangle(Point(250,390),Point(350,410))
    rect7.draw(window)
    #click for calculate
    click1=window.getMouse()
    a1x = click1.getX()
    a1y = click1.getY()
    if a1x > 250 and a1x < 350 and a1y > 310 and a1y < 360:
        #error message for units
        error99=Text(errormessage, " ")
        error99.draw(window)
        error99.setFill("Red")
        rect1input=(rect1.getText())
        if rect1input == "C" or rect1input == "F" or rect1input == "K":
            error99.setText(" ")
        else:           
            error99.setText("Please enter either C, F, or K")
        #error message for integers
        error9 = Text(Point(150,450), " ")
        error9.draw(window)
        error9.setFill("Red")
        rect2input =eval(rect2.getText())
        if type(rect2input) != int:           
            error9.setText("Temperature should be an integer")
        error91 = Text(Point(150,470), " ")
        error91.draw(window)
        error91.setFill("Red")
        if (rect2input)<0 or (rect2input)>50 :           
            error91.setText("Temperature should be less than 50 and greater than 0")
            #conversion of input/ print into respextive boxes
        if rect1input == "C":
            C=rect2input
            K=C + 273.15
            F=((C)*(9/5))+32
            tempincresult=Text(Point(300,160), C)
            tempinfresult=Text(Point(300,220), F)
            tempinkresult=Text(Point(300,280), K)
            tempincresult.draw(window)
            tempinfresult.draw(window)
            tempinkresult.draw(window)
        if rect1input == "F":
            F=rect2input
            C=(F-32)*(5/9)
            K=C + 273.15
            tempincresult=Text(Point(300,160), C)
            tempinfresult=Text(Point(300,220), F)
            tempinkresult=Text(Point(300,280), K)
            tempincresult.draw(window)
            tempinfresult.draw(window)
            tempinkresult.draw(window)
        if rect1input == "K":
            K=rect2input
            C=K - 273.15
            F=(C)*(9/5)+32
            tempincresult=Text(Point(300,160), C)
            tempinfresult=Text(Point(300,220), F)
            tempinkresult=Text(Point(300,280), K)
            tempincresult.draw(window)
            tempinfresult.draw(window)
            tempinkresult.draw(window)
    #to close window
    click2=window.getMouse()
    a2x = click2.getX()
    a2y = click2.getY()
    if a2x > 250 and a2x < 350 and a2y > 380 and a2y < 420:
        window.close()

                                 
            
    
main()
