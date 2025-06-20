from tkinter import *

window = Tk()
window.title("Python Calculator")
window.geometry('315x400')

# ENTRY BOX
e = Entry(window, width=51, borderwidth=4)
e.place(x=0,y=0)

# CLICK RESPONSE
def click(num):
    res = e.get()
    e.delete(0,END)
    e.insert(0, str(res) + str(num))

# AIRTHMATIC OPERATIONS

def add():
    n1 = e.get()
    global math 
    math = "addition"
    global i
    i = int(n1)
    e.delete(0, END)

def sub():
    n1 = e.get()
    global math
    math = "subsctraction"
    global i
    i = int(n1)
    e.delete(0, END)

def mul():
    n1 = e.get()
    global math 
    math = "multiplication"
    global i
    i = int(n1)
    e.delete(0, END)

def div():
    n1 = e.get()
    global math 
    math = "division"
    global i
    i = int(n1)
    e.delete(0, END)

def equal():
    n2 = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, i + int(n2))
    elif math == "substraction":
        e.insert(0,i - int(n2))
    elif math == "multiplication":
        e.insert(0,i * int(n2))
    elif math == "division":
        e.insert(0,i / int(n2))

def clear():
    e.delete(0, END)

# NUMBER BUTTONS
btn = Button(window, text="1", width=12, command = lambda:click(1))
btn.place(x=10,y=60)
btn = Button(window, text="2", width=12, command = lambda:click(2))
btn.place(x=110,y=60)
btn = Button(window, text="3", width=12, command = lambda:click(3))
btn.place(x=210,y=60)

btn = Button(window, text="4", width=12, command = lambda:click(4))
btn.place(x=10,y=120)
btn = Button(window, text="5", width=12, command = lambda:click(5))
btn.place(x=110,y=120)
btn = Button(window, text="6", width=12, command = lambda:click(6))
btn.place(x=210,y=120)

btn = Button(window, text="7", width=12, command = lambda:click(7))
btn.place(x=10,y=180)
btn = Button(window, text="8", width=12, command = lambda:click(8))
btn.place(x=110,y=180)
btn = Button(window, text="9", width=12, command = lambda:click(9))
btn.place(x=210,y=180)

btn = Button(window, text="0", width=12, command = lambda:click(0))
btn.place(x=10,y=240)
btn = Button(window, text="+", width=12, command = add)
btn.place(x=110,y=240)
btn = Button(window, text="-", width=12, command = sub)
btn.place(x=210,y=240)

btn = Button(window, text="*", width=12, command = mul)
btn.place(x=10,y=300)
btn = Button(window, text="/", width=12, command = div)
btn.place(x=110,y=300)
btn = Button(window, text="=", width=12, command = equal)
btn.place(x=210,y=300)

btn = Button(window, text="clear", width=40, command=clear)
btn.place(x=10,y=360)




mainloop()