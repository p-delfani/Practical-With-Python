from tkinter import *
import tkinter.messagebox

root = Tk()
#  -------------------------------------- Setting----------------------------------------------
root.geometry("400x200")
root.title("calculator")
root.resizable(width=False, height=False)

color = "pink"
root.configure(bg=color)

#  -------------------------------------- Variable----------------------------------------------
num1 = StringVar()
num2 = StringVar()
res_variable = StringVar()

#  -------------------------------------- Frame----------------------------------------------
top_Fisrt = Frame(root, width=400, height=50, bg=color)
top_Fisrt.pack(side=TOP)

top_Second = Frame(root, width=400, height=50, bg=color)
top_Second.pack(side=TOP)

top_Third = Frame(root, width=400, height=50, bg=color)
top_Third.pack(side=TOP)

top_Fourth = Frame(root, width=400, height=50, bg=color)
top_Fourth.pack(side=TOP)


#  --------------------------------------Function----------------------------------------------

def errorMsg(ms):
    if ms == 'error':
        tkinter.messagebox.showerror('Error', 'something went wrong')
    elif ms == 'division zero error':
        tkinter.messagebox.showerror('Division Error', 'Can Not Divide By 0')


def plus():
    try:
        value = float(num1.get()) + float(num2.get())
        res_variable.set(value)
    except:
        errorMsg('error')


def minus():
    try:
        value = float(num1.get()) - float(num2.get())
        res_variable.set(value)
    except:
        errorMsg('error')


def mul():
    try:
        value = float(num1.get()) * float(num2.get())
        res_variable.set(value)
    except:
        errorMsg('error')


def div():
    if num2.get() == '0':
        errorMsg('division zero error')
    elif num2.get() != '0':
        try:
            value = float(num1.get()) / float(num2.get())
            res_variable.set(value)
        except:
            errorMsg('error')


#  --------------------------------------Button----------------------------------------------

btn_plus = Button(top_Third, text="+", width=10,
                  highlightbackground=color, command=lambda: plus())
btn_plus.pack(side=LEFT, padx=10, pady=10)

btn_minus = Button(top_Third, text="-", width=10,
                   highlightbackground=color, command=lambda: minus())
btn_minus.pack(side=LEFT, padx=10, pady=10)

btn_mul = Button(top_Third, text="*", width=10,
                 highlightbackground=color, command=lambda: mul())
btn_mul.pack(side=LEFT, padx=10, pady=10)

btn_div = Button(top_Third, text="/", width=10,
                 highlightbackground=color, command=lambda: div())
btn_div.pack(side=LEFT, padx=10, pady=10)

#  --------------------------------------Entries&Labels---------------------------------------

label_first_num = Label(top_Fisrt, text='Input Number 1: ', bg=color)
label_first_num.pack(side=LEFT, pady=10, padx=10)

first_num = Entry(top_Fisrt, highlightbackground=color, textvariable=num1)
first_num.pack(side=LEFT)

label_second_num = Label(top_Second, text='Input Number 2: ', bg=color)
label_second_num.pack(side=LEFT, pady=10, padx=10)

second_num = Entry(top_Second, highlightbackground=color, textvariable=num2)
second_num.pack(side=LEFT)

res = Label(top_Fourth, text='Result: ', bg=color)
res.pack(side=LEFT, pady=10, padx=10)

res_num = Entry(top_Fourth, highlightbackground=color, textvariable=res_variable)
res_num.pack(side=LEFT)

root.mainloop()
