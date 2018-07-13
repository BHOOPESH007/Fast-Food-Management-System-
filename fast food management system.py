from tkinter import*
from tkinter import messagebox
import random
import time;
import datetime;



root = Tk()
root.geometry("1350x750+0+0")
root.title("Fast food System")
root.configure(background='black')

Tops = Frame(root,width=1350, height=80, bd=14, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(root,width=900, height=650, bd=8, relief="raise")
f1.pack(side=LEFT)
f2 = Frame(root,width=440, height=650, bd=8, relief="raise")
f2.pack(side=RIGHT)

f1a=Frame(f1,width=900, height=330, bd=8, relief="raise")
f1a.pack(side=TOP)
f2a=Frame(f1,width=900, height=320, bd=6, relief="raise")
f2a.pack(side=BOTTOM)

ft2=Frame(f2,width=440, height=450, bd=12, relief="raise")
ft2.pack(side=TOP)
fb2=Frame(f2,width=440, height=50, bd=16, relief="raise")
fb2.pack(side=BOTTOM)

f1aa=Frame(f1a,width=400, height=330, bd=16, relief="raise")
f1aa.pack(side=LEFT)
f1ab=Frame(f1a,width=400, height=330, bd=16, relief="raise")
f1ab.pack(side=RIGHT)

f2aa=Frame(f2a,width=450, height=330, bd=14, relief="raise")
f2aa.pack(side=LEFT)
f2ab=Frame(f2a,width=450, height=330, bd=14, relief="raise")
f2ab.pack(side=RIGHT)

Tops.configure(background='black')
f1.configure(background='black')
f2.configure(background='black')
#=====price
PricePlain_Burger = 65
PriceVeggie_Burger= 115
PriceIced_Plain_Burger=115
PriceDouble_Burger=155
PriceCombo_Burger=135
PriceChicken_Burger=125
PriceCheese_Burger=125
PriceHot_Dog_Combo=125

PriceTriple_Burger=130
PriceBacon_Burger=135
PriceFire_Burger=145
PriceHawaiian_Burger=125
PriceButcher_Bacon_Burger=140
PriceButcher_Mushroom_Burger=155
PriceThe_MasterPiece_Burger=115
PriceSouthern_BBQ_Burger=120

#============CostofItem
def CostofItem():
    Item1 = float(E_Plain_Burger.get())
    Item2 = float(E_Veggie_Burger.get())
    Item3 =float(E_Iced_Plain_Burger.get())
    Item4 =float(E_Double_Burger.get())
    Item5 =float(E_Combo_Burger.get())
    Item6 = float(E_Chicken_Burger.get())
    Item7 =float(E_Cheese_Burger.get())
    Item8 = float(E_Hot_Dog_Combo.get())
    Item9 =float(E_Triple_Burger.get())
    Item10 = float(E_Bacon_Burger.get())
    Item11 =float(E_Fire_Burger.get())
    Item12 = float(E_Hawaiian_Burger.get())
    Item13 =float(E_Butcher_Bacon_Burger.get())
    Item14 = float(E_Butcher_Mushroom_Burger.get())
    Item15 =float(E_The_MasterPiece_Burger.get())
    Item16 =float(E_Southern_BBQ_Burger.get())

    ItemDiscount=float(E_Discount.get())

    
    
    #==========TotalCost
    Total = ((Item1 * PricePlain_Burger) + (Item2 * PriceVeggie_Burger)
             + (Item3 * PriceIced_Plain_Burger) + (Item4 * PriceDouble_Burger)
             + (Item5 * PriceCombo_Burger) + (Item6 * PriceChicken_Burger)
             + (Item7 * PriceCheese_Burger) + (Item8 * PriceHot_Dog_Combo)
             + (Item9 * PriceTriple_Burger) + (Item10 * PriceBacon_Burger)
             + (Item11 * PriceFire_Burger) + (Item12 * PriceHawaiian_Burger)
             + (Item13 * PriceButcher_Bacon_Burger) + (Item14 * PriceButcher_Mushroom_Burger)
             + (Item15 * PriceThe_MasterPiece_Burger) + (Item16 * PriceSouthern_BBQ_Burger))
    Grand_Total = str(float(Total * float(1 - (ItemDiscount/100))))
    
    E_Total.set(str(Total))
    E_Grand_Total.set(Grand_Total)
             

#====================================== functions
def Sub():
    Return = str(float(E_Pay.get()) - float(E_Grand_Total.get()))
    E_Return.set(Return)


def Apply():
    E_Grand_Total.set(str(float(E_Total.get()) * (1 - (float(E_Discount.get())/100))))
    
def qExit():
    qExit = messagebox.askyesno("Quit System", "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return

def Reset():

    SetVal() ## set 0
    var = [var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16]
    for i in range(16):
        var[i].set("0")

    var20.set("0")

    arr = [txtPlain_Burger,txtVeggie_Burger,txtIced_Plain_Burger,txtDouble_Burger,txtCombo_Burger,txtChicken_Burger,
           txtCheese_Burger,txtHot_Dog_Combo,txtTriple_Burger,txtBacon_Burger,txtFire_Burger,
           txtHawaiian_Burger,txtButcher_Bacon_Burger,txtButcher_Mushroom_Burger,txtThe_MasterPiece_Burger,txtSouthern_BBQ_Burger]
    for i in range(16):
        arr[i].configure(state=DISABLED)
    

    txtDiscount.configure(state=DISABLED)
#====Recieps===

def Receipt():
    txtReceipt.delete("1.0",END)
    x=random.randint(10908,500876)
    randomRef = str(x)
    Receipt_Ref.set("BILL"+randomRef)

    txtReceipt.insert(END,'Receipt Ref: '+ Receipt_Ref.get() + '\t\t'+ DateofOrder.get()+' '+ TimeofOrder.get()+"\n")
    
    txtReceipt.insert(END,'Item\t\t\t'+'Qty\t\t'+"Cost of itmes\n")
    txtReceipt.insert(END,"----------------------------------------------------------------\n")
    if E_Plain_Burger.get()!='0':
        txtReceipt.insert(END,'Plain_Burger:\t\t\t'+E_Plain_Burger.get()+'\t'+ str(int(E_Plain_Burger.get())* PricePlain_Burger) +"\n")
    if E_Veggie_Burger.get()!='0':
        txtReceipt.insert(END,'Veggie_Burger: \t\t\t'+E_Veggie_Burger.get()+'\t'+ str(int(E_Veggie_Burger.get())* PriceVeggie_Burger) +"\n")
    if E_Iced_Plain_Burger.get()!='0':
        txtReceipt.insert(END,'Iced_Plain_Burger:\t\t '+E_Iced_Plain_Burger.get()+'\t'+ str(int(E_Iced_Plain_Burger.get())* PriceIced_Plain_Burger) +"\n")
    if E_Double_Burger.get()!='0':
        txtReceipt.insert(END,'Double_Burger: \t\t\t'+E_Double_Burger.get()+'\t'+ str(int(E_Double_Burger.get())* PriceDouble_Burger) +"\n")
    if E_Combo_Burger.get()!='0':
        txtReceipt.insert(END,'Combo_Burger: \t\t\t'+E_Combo_Burger.get()+'\t'+ str(int(E_Combo_Burger.get())* PriceCombo_Burger) +"\n")
    if E_Chicken_Burger.get()!='0':
        txtReceipt.insert(END,'Chicken_Burger: \t\t\t'+E_Chicken_Burger.get()+'\t'+ str(int(E_Chicken_Burger.get())* PriceChicken_Burger) +"\n")
    if E_Cheese_Burger.get()!='0':
        txtReceipt.insert(END,'Cheese_Burger: \t\t\t'+E_Cheese_Burger.get()+'\t'+ str(int(E_Cheese_Burger.get())* PriceCheese_Burger) +"\n")
    if E_Hot_Dog_Combo.get()!='0':
        txtReceipt.insert(END,'Hot_Dog_Combo:\t\t\t '+E_Hot_Dog_Combo.get()+'\t'+ str(int(E_Hot_Dog_Combo.get())* PriceHot_Dog_Combo) +"\n")
    if E_Triple_Burger.get()!='0':
        txtReceipt.insert(END,'Triple_Burger: \t\t'+E_Triple_Burger.get()+'\t'+ str(int(E_Triple_Burger.get())* PriceTriple_Burger) +"\n")
    if E_Bacon_Burger.get()!='0':
        txtReceipt.insert(END,'Bacon_Burger: \t\t'+E_Bacon_Burger.get()+'\t'+ str(int(E_Bacon_Burger.get())* PriceBacon_Burger) +"\n")
    if E_Fire_Burger.get()!='0':
        txtReceipt.insert(END,'Fire_Burger: \t\t'+E_Fire_Burger.get()+'\t'+ str(int(E_Fire_Burger.get())* PriceFire_Burger) +"\n")
    if E_Hawaiian_Burger.get()!='0':
        txtReceipt.insert(END,'Hawaiian_Burger: \t\t'+E_Hawaiian_Burger.get()+'\t\t\t\t'+ str(int(E_Hawaiian_Burger.get())* PriceHawaiian_Burger) +"\n")
    if E_Butcher_Bacon_Burger.get()!='0':
        txtReceipt.insert(END,'Butcher_Bacon_Burger: \t\t'+E_Butcher_Bacon_Burger.get()+'\t\t\t\t'+ str(int(E_Butcher_Bacon_Burger.get())* PriceButcher_Bacon_Burger) +"\n")
    if E_Butcher_Mushroom_Burger.get()!='0':
        txtReceipt.insert(END,'Butcher_Mushroom_Burger: \t\t'+E_Butcher_Mushroom_Burger.get()+'\t\t'+ str(int(E_Butcher_Mushroom_Burger.get())* PriceButcher_Mushroom_Burger) +"\n")
    if E_The_MasterPiece_Burger.get()!='0':
        txtReceipt.insert(END,'The_MasterPiece_Burger: \t\t'+E_The_MasterPiece_Burger.get()+"\t\t\t"+ str(int(E_The_MasterPiece_Burger.get())* PriceThe_MasterPiece_Burger) +"\n")
    if E_Southern_BBQ_Burger.get()!='0':
        txtReceipt.insert(END,'Southern_BBQ_Burger: \t\t'+E_Southern_BBQ_Burger.get()+"\t\t\t"+ str(int(E_Southern_BBQ_Burger.get())* PriceSouthern_BBQ_Burger) +"\n")   
    txtReceipt.insert(END,"----------------------------------------------------------------\n")
    txtReceipt.insert(END,'Sub_Total: \t\t\t\t\t'+E_Total.get()+"\n")
    txtReceipt.insert(END,'Discount: \t\t\t\t\t-'+str(float(E_Discount.get())/100*float(E_Total.get()))+"\n")
    txtReceipt.insert(END,'Grand_Total: \t\t\t\t\t'+E_Grand_Total.get()+"\n")

#=======Heading
        
lblInfo=Label(Tops, font =('arrial',70 , 'bold'), text="    Burgers for you System    ",
              bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
#========

def chkbutton_value():
    if var1.get() == 1 :
        txtPlain_Burger.configure(state= NORMAL)
    elif var1.get() == 0:
        txtPlain_Burger.configure(state= DISABLED)
        E_Plain_Burger.set("0")
        
    if var2.get() == 1 :
        txtVeggie_Burger.configure(state=NORMAL)
    elif var2.get() == 0:
        txtVeggie_Burger.configure(state=DISABLED)
        E_Veggie_Burger.set("0")

    if var3.get() == 1 :
        txtIced_Plain_Burger.configure(state= NORMAL)
    elif var3.get() == 0:
        txtIced_Plain_Burger.configure(state= DISABLED)
        E_Iced_Plain_Burger.set("0")
        
    if var4.get() == 1 :
        txtDouble_Burger.configure(state=NORMAL)
    elif var4.get() == 0:
        txtDouble_Burger.configure(state=DISABLED)
        E_Double_Burger.set("0")

    if var5.get() == 1 :
        txtCombo_Burger.configure(state= NORMAL)
    elif var5.get() == 0:
        txtCombo_Burger.configure(state= DISABLED)
        E_Combo_Burger.set("0")
        
    if var6.get() == 1 :
        txtChicken_Burger.configure(state=NORMAL)
    elif var6.get() == 0:
        txtChicken_Burger.configure(state=DISABLED)
        E_Chicken_Burger.set("0")

    if var7.get() == 1 :
        txtCheese_Burger.configure(state= NORMAL)
    elif var7.get() == 0:
        txtCheese_Burger.configure(state= DISABLED)
        E_Cheese_Burger.set("0")
        
    if var8.get() == 1 :
        txtHot_Dog_Combo.configure(state=NORMAL)
    elif var8.get() == 0:
        txtHot_Dog_Combo.configure(state=DISABLED)
        E_Hot_Dog_Combo.set("0")

    if var9.get() == 1 :
        txtTriple_Burger.configure(state= NORMAL)
    elif var9.get() == 0:
        txtTriple_Burger.configure(state= DISABLED)
        E_Triple_Burger.set("0")
        
    if var10.get() == 1 :
        txtBacon_Burger.configure(state=NORMAL)
    elif var10.get() == 0:
        txtBacon_Burger.configure(state=DISABLED)
        E_Bacon_Burger.set("0")

    if var11.get() == 1 :
        txtFire_Burger.configure(state= NORMAL)
    elif var11.get() == 0:
        txtFire_Burger.configure(state= DISABLED)
        E_Fire_Burger.set("0")
        
    if var12.get() == 1 :
        txtHawaiian_Burger.configure(state=NORMAL)
    elif var12.get() == 0:
        txtHawaiian_Burger.configure(state=DISABLED)
        E_Hawaiian_Burger.set("0")

    if var13.get() == 1 :
        txtButcher_Bacon_Burger.configure(state= NORMAL)
    elif var13.get() == 0:
        txtButcher_Bacon_Burger.configure(state= DISABLED)
        E_Butcher_Bacon_Burger.set("0")
        
    if var14.get() == 1 :
        txtButcher_Mushroom_Burger.configure(state=NORMAL)
    elif var14.get() == 0:
        txtButcher_Mushroom_Burger.configure(state=DISABLED)
        E_Butcher_Mushroom_Burger.set("0")

    if var15.get() == 1 :
        txtThe_MasterPiece_Burger.configure(state= NORMAL)
    elif var15.get() == 0:
        txtThe_MasterPiece_Burger.configure(state= DISABLED)
        E_The_MasterPiece_Burger.set("0")
        
    if var16.get() == 1 :
        txtSouthern_BBQ_Burger.configure(state=NORMAL)
    elif var16.get() == 0:
        txtSouthern_BBQ_Burger.configure(state=DISABLED)
        E_Southern_BBQ_Burger.set("0")

    if var20.get() == 1 : #
        txtDiscount.configure(state=NORMAL)
    elif var20.get() == 0:
        txtDiscount.configure(state=DISABLED)
        E_Discount.set("0")
        

#======= variable
           
var0 = IntVar()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

var20 = IntVar()#
DateofOrder=StringVar()
TimeofOrder=StringVar()
Receipt_Ref=StringVar()


E_Plain_Burger=StringVar()
E_Veggie_Burger=StringVar()
E_Iced_Plain_Burger=StringVar()
E_Double_Burger=StringVar()
E_Combo_Burger=StringVar()
E_Chicken_Burger=StringVar()
E_Cheese_Burger=StringVar()
E_Hot_Dog_Combo=StringVar()

E_Triple_Burger=StringVar()
E_Bacon_Burger=StringVar()
E_Fire_Burger=StringVar()
E_Hawaiian_Burger=StringVar()
E_Butcher_Bacon_Burger=StringVar()
E_Butcher_Mushroom_Burger=StringVar()
E_The_MasterPiece_Burger=StringVar()
E_Southern_BBQ_Burger=StringVar()
E_Total= StringVar()
E_Discount=StringVar()#
E_Grand_Total = StringVar()
E_Return =StringVar()
E_Pay = StringVar()

def SetVal():
    arr = [E_Plain_Burger,E_Veggie_Burger,E_Iced_Plain_Burger,E_Double_Burger,E_Combo_Burger,E_Chicken_Burger,
               E_Cheese_Burger,E_Hot_Dog_Combo,E_Triple_Burger,E_Bacon_Burger,E_Fire_Burger,
               E_Hawaiian_Burger,E_Butcher_Bacon_Burger,E_Butcher_Mushroom_Burger,E_The_MasterPiece_Burger,
           E_Southern_BBQ_Burger,E_Discount,E_Total,E_Grand_Total,E_Return,E_Pay]
    for i in range(21):
        
        arr[i].set("0")

SetVal()

##E_Plain_Burger.set("0")
##E_Veggie_Burger.set("0")
##E_Iced_Plain_Burger.set("0")
##E_Double_Burger.set("0")
##E_Combo_Burger.set("0")
##E_Chicken_Burger.set("0")
##E_Cheese_Burger.set("0")
##E_Hot_Dog_Combo.set("0")
##E_Triple_Burger.set("0")
##E_Bacon_Burger.set("0")
##E_Fire_Burger.set("0")
##E_Hawaiian_Burger.set("0")
##E_Butcher_Bacon_Burger.set("0")
##E_Butcher_Mushroom_Burger.set("0")
##E_The_MasterPiece_Burger.set("0")
##E_Southern_BBQ_Burger.set("0")

##E_Discount.set("0")#
##E_Total.set("0")
##E_Grand_Total.set("0")
##E_Return.set("0")
##E_Pay.set("0")

DateofOrder.set(time.strftime("%d/%m/%y"))
TimeofOrder.set(time.strftime("%H:%M:%S"))

#----------------------------------drink--------------------------
Plain_Burger = Checkbutton(f1aa, text="Plain_Burger ", variable = var1, onvalue = 1, offvalue =0,
                    font=('arial', 18, 'bold'),command=chkbutton_value).grid(row = 0,sticky=W)

Veggie_Burger = Checkbutton(f1aa, text="Veggie_Burger ", variable = var2, onvalue = 1, offvalue =0,
                    font=('arial', 18, 'bold'),command=chkbutton_value).grid(row = 1,sticky=W)

Iced_Plain_Burger = Checkbutton(f1aa, text="Iced_Plain_Burger   ", variable = var3, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 2,sticky=W)

Double_Burger = Checkbutton(f1aa, text="Double_Burger ", variable = var4, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 3,sticky=W)

Combo_Burger = Checkbutton(f1aa, text="Combo_Burger ", variable = var5, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 4,sticky=W)

Chicken_Burger = Checkbutton(f1aa, text="Chicken_Burger ", variable = var6, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 5,sticky=W)

Cheese_Burger = Checkbutton(f1aa, text="Cheese_Burger ", variable = var7, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 6,sticky=W)

Hot_Dog_Combo = Checkbutton(f1aa, text="Hot_Dog_Combo ", variable = var8, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 7,sticky=W)

#=======================Cake==========================
Triple_Burger = Checkbutton(f1ab, text="Triple_Burger ", variable = var9, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 0,sticky=W)

Bacon_Burger = Checkbutton(f1ab, text="Bacon_Burger ", variable = var10, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 1,sticky=W)

Fire_Burger = Checkbutton(f1ab, text="Fire_Burger ", variable = var11, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 2,sticky=W)

Hawaiian_Burger = Checkbutton(f1ab, text="Hawaiian_Burger ", variable = var12, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 3,sticky=W)

Butcher_Bacon_Burger = Checkbutton(f1ab, text="Butcher_Bacon_Burger ", variable = var13, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 4,sticky=W)

Butcher_Mushroom_Burger = Checkbutton(f1ab, text="Butcher_Mushroom_Burger ", variable = var14, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 5,sticky=W)

The_MasterPiece_Burger = Checkbutton(f1ab, text="The_MasterPiece_Burger ", variable = var15, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 6,sticky=W)

Southern_BBQ_Burger = Checkbutton(f1ab, text="Southern_BBQ_Burger ", variable = var16, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 7,sticky=W)


#---------------------------Widget-----------
txtPlain_Burger = Entry(f1aa,font=('arial',16,'bold'), textvariable=E_Plain_Burger,
                 bd=8, width=6, justify='left', state= DISABLED)
txtPlain_Burger.grid(row =0, column=1)
txtVeggie_Burger = Entry(f1aa,font=('arial',16,'bold'), textvariable=E_Veggie_Burger,
                    bd=8, width=6, justify='left', state=DISABLED)
txtVeggie_Burger.grid(row =1, column=1)
txtIced_Plain_Burger = Entry(f1aa,font=('arial',16,'bold'), textvariable=E_Iced_Plain_Burger,
                      bd=8, width=6, justify='left', state=DISABLED)
txtIced_Plain_Burger.grid(row =2, column=1)
txtDouble_Burger = Entry(f1aa,font=('arial',16,'bold'),textvariable=E_Double_Burger,
                 bd=8, width=6, justify='left', state=DISABLED)
txtDouble_Burger.grid(row =3, column=1)
txtCombo_Burger = Entry(f1aa,font=('arial',16,'bold'),textvariable=E_Combo_Burger,
                 bd=8, width=6, justify='left', state=DISABLED)
txtCombo_Burger.grid(row =4, column=1)
txtChicken_Burger = Entry(f1aa,font=('arial',16,'bold'),textvariable=E_Chicken_Burger,
                 bd=8, width=6, justify='left', state=DISABLED)
txtChicken_Burger.grid(row =5, column=1)
txtCheese_Burger = Entry(f1aa,font=('arial',16,'bold'),textvariable=E_Cheese_Burger,
                 bd=8, width=6, justify='left', state=DISABLED)
txtCheese_Burger.grid(row =6, column=1)
txtHot_Dog_Combo = Entry(f1aa,font=('arial',16,'bold'), textvariable=E_Hot_Dog_Combo,
                 bd=8, width=6, justify='left', state=DISABLED)
txtHot_Dog_Combo.grid(row =7, column=1)

#--------------------
txtTriple_Burger = Entry(f1ab,font=('arial',16,'bold'),textvariable=E_Triple_Burger,
                       bd=8, width=6, justify='left', state=DISABLED)
txtTriple_Burger.grid(row =0, column=1)
txtBacon_Burger = Entry(f1ab,font=('arial',16,'bold'), textvariable=E_Bacon_Burger,
                           bd=8, width=6, justify='left', state=DISABLED)
txtBacon_Burger.grid(row =1, column=1)
txtFire_Burger = Entry(f1ab,font=('arial',16,'bold'),textvariable=E_Fire_Burger,
                             bd=8, width=6, justify='left', state=DISABLED)
txtFire_Burger.grid(row =2, column=1)
txtHawaiian_Burger = Entry(f1ab,font=('arial',16,'bold'), textvariable=E_Hawaiian_Burger,
                             bd=8, width=6, justify='left', state=DISABLED)
txtHawaiian_Burger.grid(row =3, column=1)
txtButcher_Bacon_Burger = Entry(f1ab,font=('arial',16,'bold'), textvariable=E_Butcher_Bacon_Burger,
                                bd=8, width=6, justify='left', state=DISABLED)
txtButcher_Bacon_Burger.grid(row =4, column=1)
txtButcher_Mushroom_Burger = Entry(f1ab,font=('arial',16,'bold'), textvariable=E_Butcher_Mushroom_Burger,
                                  bd=8, width=6, justify='left', state=DISABLED)
txtButcher_Mushroom_Burger.grid(row =5, column=1)
txtThe_MasterPiece_Burger = Entry(f1ab,font=('arial',16,'bold'), textvariable=E_The_MasterPiece_Burger,
                                       bd=8, width=6, justify='left', state=DISABLED)
txtThe_MasterPiece_Burger.grid(row =6, column=1)
txtSouthern_BBQ_Burger = Entry(f1ab,font=('arial',16,'bold'), textvariable=E_Southern_BBQ_Burger,
                                     bd=8, width=6, justify='left', state=DISABLED)
txtSouthern_BBQ_Burger.grid(row =7, column=1)

                                                                              
#=================
Total = Label(f2aa,font=('arial',16,'bold'), text="Total \t",bd =8)
Total.grid(row=2, column=0, sticky=W)
txtTotal=Entry(f2aa,font=('arial',16,'bold'), textvariable=E_Total, bd=8, width=10, justify='left',state = DISABLED)
txtTotal.grid(row=2,column=1, sticky=W)
Grand_Total = Label(f2aa,font=('arial',16,'bold'), text="Grand Total \t",bd =8)
Grand_Total.grid(row=3, column=0, sticky=W)
txtGrand_Total=Entry(f2aa,font=('arial',16,'bold'), textvariable=E_Grand_Total,
                     bd=8,width=10, justify='left', state=DISABLED)
txtGrand_Total.grid(row=3,column=1, sticky=W)
lblCostofDrink = Label(f2aa,font=('arial',16,'bold'), text="Coupon Code",bd =8)
lblCostofDrink.grid(row=4, column=0, sticky=W)
txtCostofDrink=Entry(f2aa,font=('arial',16,'bold'),bd=8,width=10, justify='left')
txtCostofDrink.grid(row=4,column=1, sticky=W)
#===========================
#============================ discount & Coupon

Discount = Checkbutton(f2ab, text="Discount \t", variable = var20, onvalue = 1, offvalue =0,
                    font=('arial', 16, 'bold'),command=chkbutton_value).grid(row = 2,sticky=W)
txtDiscount=Entry(f2ab,font=('arial',16,'bold'), textvariable=E_Discount,
                  bd=8, width=10, justify='left', state=DISABLED)
txtDiscount.grid(row=2,column=1, sticky=W)
#subbtn
btnAppy = Button(f2ab, padx=16 , pady=1, bd=4, fg="black", font=('arial',16,'bold'),
                  width=5, text="Apply", command=Apply).grid(row=2,column=2, sticky=W)
#===
Pay = Label(f2ab,font=('arial',16,'bold'), text="Cash Pay",bd =4)
Pay.grid(row=3, column=0, sticky=W)
txtPay=Entry(f2ab,font=('arial',16,'bold'), textvariable=E_Pay, bd=4, width=10, justify='left')
txtPay.grid(row=3,column=1, sticky=W)
#subbtn
btnSub = Button(f2ab, padx=16 , pady=1, bd=4, fg="black", font=('arial',16,'bold'),
                  width=5, text="=", command=Sub).grid(row=3,column=2, sticky=W)
#===
Return = Label(f2ab,font=('arial',16,'bold'), text="Return \t",bd =4)
Return.grid(row=4, column=0, sticky=W)
txtReturn=Entry(f2ab,font=('arial',16,'bold'), textvariable=E_Return,
                bd=4, width=10, justify='left')
txtReturn.grid(row=4,column=1, sticky=W)

#===================
lblReceipt = Label(ft2,font=('arial', 12, 'bold'), text='Reciept', bd=2, anchor='w')
lblReceipt.grid(row=0, column=0 , sticky=W)
txtReceipt = Text(ft2, width=59, height=22, bg="white", bd=8,
                  font=('arial', 11, 'bold'))
txtReceipt.grid(row=1, column=0)

#======================== button===============
btnTotal = Button(fb2, padx=16 , pady=1, bd=4, fg="black", font=('arial',16,'bold'),
                  width=5, text="Total ", command= CostofItem).grid(row=0,column=0)
btnReceipt = Button(fb2, padx=16 , pady=1, bd=4, fg="black", font=('arial',16,'bold'),
                  width=5, text="Receipt ", command=Receipt).grid(row=0,column=1)
btnReset = Button(fb2, padx=16 , pady=1, bd=4, fg="black", font=('arial',16,'bold'),
                  width=5, text="Reset ", command=Reset).grid(row=0,column=2)
btnExit = Button(fb2, padx=16 , pady=1, bd=4, fg="black", font=('arial',16,'bold'),
                  width=5, text="Exit ",bg="red", command= qExit).grid(row=0,column=3)

root.mainloop()
