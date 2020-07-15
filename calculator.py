from tkinter import*

window=Tk()

window.geometry("354x460")
window.title("CALCULATOR")
melabel = Label(window,text="CALCULATOR",bg='Blue',font=("Times",30,'bold'))
melabel.pack(side=TOP)
window.config(background='Dark Gray')

textin=StringVar()
operator=""


def clickbut(number):  # lambda:clickbut(1)
    global operator
    operator = operator + str(number)
    textin.set(operator)


def equlbut():
    global operator
    add = str(eval(operator))
    textin.set(add)
    operator = ''


def equlbut():
    global operator
    sub = str(eval(operator))
    textin.set(sub)
    operator = ''

def equlbut():
    global operator
    mul = str(eval(operator))
    textin.set(mul)
    operator = ''

def equlbut():
    global operator
    div = str(eval(operator))
    textin.set(div)
    operator = ''

def clrbut():
    textin.set('')

metext = Entry(window, font=("Courier New", 12, 'bold'), textvar=textin, width=25, bd=5, bg='powder blue')
metext.pack()

but1 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(1), text="1",
                   font=("Courier New", 16, 'bold'))
but1.place(x=10, y=100)

but2 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(2), text="2",
                   font=("Courier New", 16, 'bold'))
but2.place(x=10, y=170)

but3 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(3), text="3",
                   font=("Courier New", 16, 'bold'))
but3.place(x=10, y=240)

but4 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(4), text="4",
                   font=("Courier New", 16, 'bold'))
but4.place(x=75, y=100)

but5 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(5), text="5",
                   font=("Courier New", 16, 'bold'))
but5.place(x=75, y=170)

but6 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(6), text="6",
                   font=("Courier New", 16, 'bold'))
but6.place(x=75, y=240)

but7 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(7), text="7",
                   font=("Courier New", 16, 'bold'))
but7.place(x=140, y=100)

but8 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(8), text="8",
                   font=("Courier New", 16, 'bold'))
but8.place(x=140, y=170)

but9 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(9), text="9",
                   font=("Courier New", 16, 'bold'))
but9.place(x=140, y=240)

but0 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(0), text="0",
                   font=("Courier New", 16, 'bold'))
but0.place(x=10, y=310)

window.mainloop()