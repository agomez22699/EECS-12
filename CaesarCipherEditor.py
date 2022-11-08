#Adrian Gomez
#20119988

from graphics import*
def main():
    #Design Graphic Window
    window=GraphWin("Caesar Cipher",600,600)
    enterfilename = Text(Point(80,40), 'Enter the File Name:')
    enterfilename.draw(window)
    filenametextbox = Text(Point(90,80), "Filename:")
    filenametextbox.draw(window)
    filenameentry = Entry(Point(275,80), 45)
    filenameentry.draw(window)
    steptext = Text(Point(100,120), "Step:")
    steptext.draw(window)
    stepentry = Entry(Point(275,120), 45)
    stepentry.draw(window)
    stepentryguide = Text(Point(500,120), "(Step must be a Positive integer)")
    stepentryguide.draw(window)
    stepentryguide.setFill("Blue")
    originalmessagetext = Text(Point(80,200), "Original Message:")
    originalmessagetext.draw(window)
    encodedmessagetext = Text(Point(80,400), "Encoded Message:")
    encodedmessagetext.draw(window)
    clickanywhere = Text(Point(250,150),"(Click anywhere to encode message)")
    clickanywhere.draw(window)
    clickanywhere.setFill("Blue")
    clickexit = Text(Point(250,175), "(Click a second time to close window)")
    clickexit.draw(window)
    clickexit.setFill("Blue")
     #Get User Click
    click1 = window.getMouse()
    #Open File
    fileIn = open(filenameentry.getText(), 'r')
    if fileIn != None:
        content = fileIn.read()
    fileIn.close()
    #print content of .txt
    content2 = Text(Point(180,200), content)
    content2.draw(window)
    content2.setFill("Red")
    #Read Value for Step
    step = eval(stepentry.getText())
    #Converting character into ASCII and adding step, and converting back to character
    message = ""
    for character in content:
        if character.isalpha() == True:
            encoded = ord(character) - 97
            encoded += -step
            encoded = encoded % 26
            message += chr(encoded + 97)
            
        else:
            message += character
    jmessage = Text(Point(180,400), message)
    jmessage.draw(window)
    jmessage.setFill("Green")
    #write to encrypted file
    fileout=open("encrypt.txt", 'w')
    fileout.write(message)
    fileout.close()
    #close the window
    click2 = window.getMouse()
    window.close()
main()
