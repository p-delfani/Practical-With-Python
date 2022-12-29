from tkinter import *
from tkinter.ttk import *

from time import strftime

root =tk()
root.title("clock")

def time():
   string = strftime("%H:%M:%S:%P")
   label.config(text=string)
   label.after(1000,time)

label = label(root,front=("ds-digital",80),background="black",foreground="cyan")
label.pack(anchor='center')
time()

mianloop()