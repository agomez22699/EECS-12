#Adrian Gomez
#20119988

from graphics import*


def main ():
    #creates graphic window for airline reservation 
    window=GraphWin("Airline Reservation", 600,600)
    nameentry = Entry(Point(65,60),11)
    nametext = Text(Point(60,80), "First Name")
    occupationentry = Entry(Point(175,60),11)
    occupationtext = Text(Point(175,80), "Occupation")
    lnameentry = Entry(Point(60,150), 11)
    lnametext = Text(Point(60,175), "Last Name")
    seatnumbertext = Text(Point(175,175), "Seat Number")
    cfx = Text(Point(175,160),  )
    jmn = Text(Point(65,325),   )
    tfti = Text(Point(200,375), )
    idk = Text(Point(200,400),  )
    reservet = Text(Point(350,60), "Reserve")
    rrect = Rectangle(Point(325,70), Point(375,50))
    downgradet = Text(Point(350, 110), "Downgrade")
    downgraderect = Rectangle(Point(315,120), Point(385,100))
    quittext = Text(Point(350,160), "Quit")
    quitrect = Rectangle(Point(325,170), Point(375,150))
    nameentry.draw(window)
    nametext.draw(window)
    occupationentry.draw(window)
    occupationtext.draw(window)
    lnameentry.draw(window)
    lnametext.draw(window)
    seatnumbertext.draw(window)
    reservet.draw(window)
    rrect.draw(window)
    downgradet.draw(window)
    downgraderect.draw(window)
    quittext.draw(window)
    quitrect.draw(window)
    cfx.draw(window)
    jmn.draw(window)
    tfti.draw(window)
    idk.draw(window)
    seating_list = [0]*51
    passen = open("passenger.txt", 'r')
    info = passen.readlines()
    for i in range(len(info)):
        laxa = line[i].split()
        for f in range(len(laxa)):
            opx = laxa[2]
            dcx = int(opx)
            seating_list[dcx] = 1
    passen.close()
    passeng = open("passenger.txt", 'a')

    while True:
        c1 = win.getMouse()
        occu = int(occupationentry.getText())
        fn = nameentry.getText()
        ln = lnameentry.getText()

        #click
        if c1.x>325 and c1.x<375 and c1.y>50 and c1.y<70:
            if occu == 1:
                yhg = seating_list[1:21]
                if 0 in yhg:
                    verify = seating_list[1:21].index(0)
                    jmn.setText((fn,ln,verify+1, 'First', 'Class'))
                    cfx.setText(verify+1)
                    sda = (fn,ln,verify+1, 'First', 'Class')
                    passeng.write(sda)
                else:
                    tfti.setText("All seats in First Class are taken.")
                    idk.setText('Select "Downgrade" to check availibity in Bussiness or Economy class')
                    if c1.x>315 and c1.x<385 and c1.y>100 and c1.y<120:
                        oli = seating_list[21:31]
                        if 0 in oli:
                                verify = seating_list[21:31].index(0)
                                jmn.setText((fn,ln,verify+21, 'Business', 'Class'))
                                cfx.setText(verify+21)
                                sda = (fn,ln,verify+1, 'Business', 'Class')
                                passeng.write(sda)
                        adr = seating_list[31:51]
                        if 0 in adr:
                                verify = seating_list[31:51].index(0)
                                jmn.setText((fn,ln,verify+31, 'Economy', 'Class'))
                                cfx.setText(verify+31)
                                sda = (fn,ln,verify+1, 'Economy', 'Class')
                                passeng.write(sda)
                        else:
                                tfti.setText("We are booked")
                                idk.setText(" ")
                        
            if occu == 2:
                oli = seating_list[21:31]
                if 0 in oli:
                    verify = seating_list[21:31].index(0)
                    jmn.setText((fn,ln,verify+21, 'Business', 'Class'))
                    cfx.setText(verify+21)
                    sda = (fn,ln,verify+1, 'Business', 'Class')
                    passeng.write(sda)
                else:
                    tfti.setText("All seats in Business Class are taken.")
                    idk.setText('Select "Downgrade" to check availibity in First or Economy class')
                    if c1.x>315 and c1.x<385 and c1.y>100 and c1.y<120:
                        yhg = seating_list[1:21]
                            if 0 in yhg:
                                verify = seating_list[1:21].index(0)
                                jmn.setText((fn,ln,verify+1, 'First', 'Class'))
                                cfx.setText(verify+1)
                                sda = (fn,ln,verify+1, 'First', 'Class')
                                passeng.write(sda)
                        adr = seating_list[31:51]
                            if 0 in adr:
                                verify = seating_list[31:51].index(0)
                                jmn.setText((fn,ln,verify+31, 'Economy', 'Class'))
                                cfx.setText(verify+31)
                                sda = (fn,ln,verify+1, 'Economy', 'Class')
                                passeng.write(sda)
                            else:
                                tfti.setText("We are booked")
                                idk.setText(" ")
            if occu == 3:
                adr = seating_list[31:51]
                if 0 in adr:
                    verify = seating_list[31:51].index(0)
                    jmn.setText((fn,ln,verify+31, 'Economy', 'Class'))
                    cfx.setText(verify+31)
                    sda = (fn,ln,verify+1, 'Economy', 'Class')
                    passeng.write(sda)
                else:
                    tfti.setText("All seats in Economy Class are taken.")
                    idk.setText('Select "Downgrade" to check availibity in Bussiness or First class')
                    if c1.x>315 and c1.x<385 and c1.y>100 and c1.y<120:
                        yhg = seating_list[1:21]
                            if 0 in yhg:
                                verify = seating_list[1:21].index(0)
                                jmn.setText((fn,ln,verify+1, 'First', 'Class'))
                                cfx.setText(verify+1)
                                sda = (fn,ln,verify+1, 'First', 'Class')
                                passeng.write(sda)
                        oli = seating_list[21:31]
                            if 0 in oli:
                                verify = seating_list[21:31].index(0)
                                jmn.setText((fn,ln,verify+21, 'Business', 'Class'))
                                cfx.setText(verify+21)
                                sda = (fn,ln,verify+1, 'Business', 'Class')
                                passeng.write(sda)
                            else:
                                tfti.setText("We are booked")
                                idk.setText(" ")
        if c1.x>325 and c1.x<375 and c1.y>150 and c1.y<170:
            win.close()
            
            
    
    
main()
