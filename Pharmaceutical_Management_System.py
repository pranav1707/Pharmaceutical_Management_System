import Tkinter
import tkMessageBox
import MySQLdb
from Tkinter import *


def buy():
    flag = 0
    #print(variable.get())
    db=MySQLdb.connect("localhost","root","","sd")   
    cursor = db.cursor()
    sql="select * from medicineDetails"
    cursor.execute(sql)
    data = cursor.fetchall()

    for row in data: 
        if(medicineName.get() == row[0]):                  
            flag = 1
            query = "insert into purchase(medicineName,qty,cost) values(%s,%s,%s)"
            w_price = int(row[1])
            cost = int(quantity.get()) * w_price
            cursor.execute(query,(medicineName.get(),quantity.get(),cost))
            tkMessageBox.showinfo("Message","Successfully purchased medicine")
                
    if(flag == 0):
        tkMessageBox.showinfo("Message","Medicine not found")
            
    db.commit()
    db.close()
    
def addMedicine():
    try:
        db=MySQLdb.connect("localhost","root","","sd")   
        cursor = db.cursor()
        sql="insert into medicineDetails values(%s,%s,%s,%s)"
        cursor.execute(sql,(medicineName.get(),wholesalePrice.get(),retailPrice.get(),totalStrips.get()))
        tkMessageBox.showinfo("Message","Successfully added medicine")
        db.commit()
        db.close()
    except:
        tkMessageBox.showinfo("Error Message","Error")
        db.rollback()
        db.close()
        
#WINDOW 6
def addNewMedicine():
    global window6
    global medicineName
    global wholesalePrice
    global retailPrice
    global totalStrips

    window6 = Toplevel(window2)
    window6.geometry("500x500+425+170")
    window6.configure(bg = "black")

    Label(window6, text = "Medicine name", bg = "black", fg = "gold", font = "Helvetica 15").grid(sticky = W,row=0,column=0)
    medicineName = Entry(window6, width = 30)
    medicineName.grid(row=0,column=1)

    Label(window6, text = "Wholesale price", bg = "black", fg = "gold", font = "Helvetica 15").grid(sticky = W,row=1,column=0)
    wholesalePrice = Entry(window6, width = 30)
    wholesalePrice.grid(row=1,column=1)
    
    Label(window6, text = "Retail price", bg = "black", fg = "gold", font = "Helvetica 15").grid(sticky = W,row=2,column=0)
    retailPrice = Entry(window6, width = 30)
    retailPrice.grid(row=2,column=1)

    Label(window6, text = "Total strips", bg = "black", fg = "gold", font = "Helvetica 15").grid(sticky = W,row=3,column=0)
    totalStrips = Entry(window6, width = 30)
    totalStrips.grid(row=3,column=1)

    Button(window6, text = "Add", bg = "red", fg = "gold", command = addMedicine, font = "Helvetica 12").grid(row=4,column=1)



def registerButton():
    try:
        db=MySQLdb.connect("localhost","root","","sd")   
        cursor = db.cursor()
        sql="insert into wholesaler values(%s,%s,%s,%s)"
        cursor.execute(sql,(name.get(),mobileNo.get(),gstNo.get(),address.get()))
        tkMessageBox.showinfo("Message","Successfully registered")
        db.commit()
        db.close()
    except:
        tkMessageBox.showinfo("Error Message","Error")
        db.rollback()
        db.close()

#WINDOW 5
def registerWholesaler():
    global window5
    global name
    global mobileNo
    global gstNo
    global address

    window5 = Toplevel(window3)
    window5.geometry("500x500+425+170")
    window5.configure(bg = "black")

    Label(window5, text = "Name", bg = "black", fg = "gold", font = "Helvetica 15").grid(sticky = W,row=0,column=0)
    name = Tkinter.Entry(window5, width = 30)
    name.grid(row=0,column=1)
    
    Label(window5, text = "Moblie number", bg = "black", fg = "gold", font = "Helvetica 15").grid(sticky = W,row=1,column=0)
    mobileNo = Tkinter.Entry(window5, width = 30)
    mobileNo.grid(row=1,column=1)
    
    Label(window5, text = "GST number", bg = "black", fg = "gold", font = "Helvetica 15").grid(sticky = W,row=2,column=0)
    gstNo = Tkinter.Entry(window5, width = 30)
    gstNo.grid(row=2,column=1)
    
    Label(window5, text = "Address", bg = "black", fg = "gold", font = "Helvetica 15").grid(sticky = W,row=3,column=0)
    address = Tkinter.Entry(window5, width = 30)
    address.grid(row=3,column=1)
    
    Button(window5, text = "Register", bg = "red", fg = "gold", command = registerButton, font = "Helvetica 12").grid(row=4,column=1)


#WINDOW 4
def purchaseFromDealer():
    global window4
    global dealerName
    global medicineName
    global quantity
    global choices
    global variable

    choices = []
    window4 = Toplevel(window3)
    window4.geometry("500x500+425+170")
    window4.configure(bg = "black")
    variable = StringVar()
    
    try:
        db=MySQLdb.connect("localhost","root","","sd")   
        cursor = db.cursor()
        sql = "select * from wholesaler"
        cursor.execute(sql)
        data = cursor.fetchall()
        
        for row in data:
             choices.append(row[0])
             
        db.commit()
        db.close()

    except:
        tkMessageBox.showinfo("Error Message","Error")
        db.rollback()
        db.close()

    Label(window4, text = "Wholesaler name", bg = "black", fg = "gold", font = "Helvetica 15").grid(sticky = W,row=0,column=0)
    dealerName = OptionMenu(window4, variable, *choices )
    dealerName.grid(row=0,column=1)
    dealerName.config(width = 24)

    

    Label(window4, text = "Medicine name", bg = "black", fg = "gold", font = "Helvetica 15").grid(sticky = W,row=1,column=0)
    medicineName = Entry(window4, width = 30)
    medicineName.grid(row=1,column=1)

    Label(window4, text = "Quantity", bg = "black", fg = "gold", font = "Helvetica 15").grid(sticky = W,row=2,column=0)
    quantity = Entry(window4, width = 30)
    quantity.grid(row=2,column=1)

    Button(window4, text = "Buy", bg = "red", fg = "gold", command = buy, font = "Helvetica 12").grid(row=3,column=1)
    
    


#WINDOW 3
def purchase():
    global window3
    global registerWholesaler
    global purchaseFromDealer
    global purchasingHistory

    
    window3 = Toplevel(window2)
    window3.geometry("500x500+425+170")
    window3.configure(bg = "black")
    
    registerWholesaler = Button(window3, text = "Register wholesaler  ", bg = "red", fg = "gold",  command = registerWholesaler, font = "Helvetica 15")
    registerWholesaler.place(x=40,y=20)
    
    purchaseFromDealer = Button(window3, text = "Purchase from dealer", bg = "red", fg = "gold",  command = purchaseFromDealer, font = "Helvetica 15")
    purchaseFromDealer.place(x=40,y=70)
    
    purchasingHistory = Button(window3, text = "Purchasing history     ", bg = "red", fg = "gold",  command = login, font = "Helvetica 15")
    purchasingHistory.place(x=40,y=120)

#WINDOW 2
def login():
    global window2
    global search
    global purchase
    global sell
    global customer
    global medicine
    if(username.get()=="admin" and password.get()=="admin123"):
        username.delete(0,END)
        password.delete(0,END)
        window2=Toplevel(window1)
        window2.geometry("500x500+425+170")
        window2.configure(bg = "black")

        Label(window2, text = "PHARMACY MANAGEMENT SYSTEM", bg = "black", fg = "gold", font = "Helvetica 17 bold").pack()

        Button(window2, text = "Add new medicine ", bg = "red", fg = "gold", command = addNewMedicine, font = "Helvetica 15").place(x=40,y=70)                                                                                                                                                
        Button(window2, text = "Purchase medicine", bg = "red", fg = "gold",  command = purchase, font = "Helvetica 15").place(x=40,y=120)
        Button(window2, text = "Search medicine   ", bg = "red", fg = "gold", command = login, font = "Helvetica 15").place(x=40,y=170)
        Button(window2, text = "Sell medicine        ", bg = "red", fg = "gold", command = login, font = "Helvetica 15").place(x=40,y=220)

    else:
        username.delete(0,END)
        password.delete(0,END)
        tkMessageBox.showinfo("error","Invalid username or password")



#WINDOW1
def main():
    global window1
    global username
    global password

    window1 = Tkinter.Tk()
    window1.geometry("500x500+425+170")
    window1.configure(bg = "black")

    Label(window1, text = "Username", fg = "gold", bg = "black", height = 2, width = 20, anchor = CENTER, font = "Helvetica 14").pack()
    username = Entry(window1,width = 30)
    username.pack()

    Label(window1, text = "Password", fg = "gold", bg = "black", height = 2, width = 20, anchor = CENTER, font = "Helvetica 14").pack()
    password = Entry(window1, width = 30, show = "*")
    password.pack()

    Label(window1, bg = "black").pack()
    
    Button(window1, text = "Login", bg = "red", fg = "gold", command = login, font = "Helvetica 11").pack()
    window1.mainloop()

main()
