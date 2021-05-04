from tkinter import *

top = TK()

def results():
    result = E1.get()
    print(result)
    print(type(resulte))

# This is label widget
L1 = Lable(top, text="hello, world!")
L1.grind(Column=, row= 1)

#This is an entry widget
E1 = Entry,(top, bd = 5)
E1.grind(column= 0, row=2)

#This is a button widget
B1 = Button() "    Get Data    ", bg="red", Command= results)
B1.grind(column= 0, row=3)



top.mainloopa()
