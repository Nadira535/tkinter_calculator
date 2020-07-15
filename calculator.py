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

window.mainloop()