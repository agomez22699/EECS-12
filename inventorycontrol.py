#Adrian Gomez
#20119988

from graphics import*
def _init_(self,pid,pname,quantity):#given
        self.pid = pid
        self.name = name
        self.quantity = quantity
def READ_INVENTORY(fname):#opens the given file to read inventory
    ifile = open(fname,'r')
    inventory = [ ] 
    for line in infile.readlines():
        pid, name, quantity = line.strip().split("\t")
        inventory.append(Item(pid,name,quantity))
    ifile.close()
    return inventory
def INDEX_RECORD(inventory, pid):# finds pid
    for b in range (len(inventory)):
        item = inventory[b]
        if item.pid == pid:
            return b
        return None
def ADD_RECORD(inventory, pid, stuname, quantity):#adds to inventory list
    x = Item(pid, stuname, quantity)
    inventory.append(x)
def WRITE_INVENTORY(inventory, fnet):#writes to inventory
    ofile = open(fnet, 'w')
    sinvent = ''
    for item in inventory:
        sinvent += item.pid + '\t' + item.name + '\t' + item.quantity + '\n'
    ofile.write(sinvent)
    ofile.close
def FILE_OPEN(fnet, sfn):#opens given file and asks if there isnt a file 
    if fnet == "":
        sfn.setText("Please set a File Name")
    else:
        inventory = READ_INVENTORY(fnet)
        sfn.setText("Inventory has loaded")
        return inventory
def UPDATE_RECORD(inventory, pid, stuname, quantity):#updates an item
    location = INDEX_RECORD(inventory,pid)
    if location is None:
        return None
    else:
        item = inventory[location]
        item.name = stuname
        item.quantity = quantity
        return item.name, item.quantity
def main():
    #draw GUI
    win=GraphWin("Inventory",500,475)
    fnt = Text(Point(50,50), "File Name:")
    fnt.draw(win)
    fne = Entry(Point(140,50), 13)
    fne.draw(win)
    iidt = Text(Point(50,150), "Item ID:")
    iidt.draw(win)
    iiddte = Entry(Point(140,150), 13)
    iiddte.draw(win)
    itnt = Text(Point(50,250), "Item Name:")
    itnt.draw(win)
    itnte = Entry(Point(140,250), 13)
    itnte.draw(win)
    qt = Text(Point(50,350), "Quantity:")
    qt.draw(win)
    qte = Entry(Point(140,350), 13)
    qte.draw(win)
    ro = Rectangle(Point(300,35), Point(375,65))
    ro.draw(win)
    ra = Rectangle(Point(300,100), Point(375,130))
    ra.draw(win)
    rfi = Rectangle(Point(300,165), Point(375,195))
    rfi.draw(win)
    uq = Rectangle(Point(300,230),Point(385,260))
    uq.draw(win)
    qb = Rectangle(Point(300,295),Point(375,325))
    qb.draw(win)
    rot = Text(Point(330,45), "Open")
    rot.draw(win)
    rat = Text(Point(330,110), "Add")
    rat.draw(win)
    rfit = Text(Point(330,175), "Find Item")
    rfit.draw(win)
    uqt = Text(Point(343,240), "Update Quantity")
    uqt.draw(win)
    qbt = Text(Point(330,305), "Quit")
    qbt.draw(win)
    sfn = Text(Point(100,400), "Specify the file name of an inventory")
    sfn.draw(win)
    #if statements for clicks on buttons and other functions
    while True:
        c1 = win.getMouse()
        fnet = fne.getText()
        pid = iiddte.getText()
        stuname = itnte.getText()
        quantity = qte.getText() 
        if c1.x>300 and c1.x<375 and c1.y>35 and c1.y<65:
            #read
            FILE_OPEN(fnet, sfn)
        if c1.x>300 and c1.x<375 and c1.y>100 and c1.y<130:
            #add items
            if pid == '' or fnet == '' or stuname == '' or quantity == '':
                sfn.setText("Missing required field(s) to add an item!")
            else:
                inventory = FILE_OPEN(fnet, sfn)
                pch = INDEX_RECORD(inventory,pid)
                dlr = fnet + '\t' + pid + '\t' + stuname + '\t' + quantity
                if pch is not None:
                    sfn.setText('Item ID already exists!')
                else:
                    ADD_RECORD(inventory, pid, stuname, quantity)
                    lmu = 'Record has been added\n' +dlr
                    sfn.setText(lmu)
                    WRITE_INVENTORY(inventory, fnet)
        if c1.x>300 and c1.x<375 and c1.y>165 and c1.y<195:
            #find item
            inventory = FILE_OPEN(fnet, sfn)
            location = INDEX_RECORD(inventory, pid)
            m = 'row' + " " + str(location)
            if location is None:
                sfn.setText("Unable to find location with given ID")
            else:
                sfn.setText(m)
        if c1.x>300 and c1.x<385 and c1.y>230 and c1.y<260:
            #update quantity
            if fnet == '' or stuname == '' or quantity == '' or pid == '':
                sfn.setText('Missing required field(s) to update item!')
            else:
                inventory = FILE_OPEN(fnet, sfn)
                dsw = fnet + '\t' + pid + '\t' + stuname + '\t' + quantity
                upd8 = UPDATE_RECORD(inventory, pid, stuname, quantity)
                if upd8 is not None:
                    sfn.setText('Items updated\n' + dsw)
                    WRITE_INVENTORY(inventory, fnet)
                else:
                    sfn.setText('Part Identification does not already exist')
        if c1.x>300 and c1.x<375 and c1.y>295 and c1.y<325:
            #quit and close file
            win.close()
            
                   
main()
