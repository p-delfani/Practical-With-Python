from tkinter import messagebox
from tkinter import *
import webbrowser
import pyperclip3
import random
import os

# add contact   درست
# delete contact   درست
# exit   درست
# save list درست
# open list  درست
# ------------------------------------ setting -----------------------------

root = Tk()
root.title("contact book")
root.geometry("650x300")
background = "#121212"
root.config(bg=background)

# ------------------------------------ functions -----------------------------

def opendirc():
    webbrowser.open("F:\pythonProject2")

def Exit():
    chioce = messagebox.askquestion("Exit Aplication",'Are You Sure You Want To Close The Program ? ')
    if chioce == "yes":
        root.destroy()

    else:
        return


def add_contact():
    contact_string = name_Entry.get() + ": " + phone_Entry.get()
    listbox.insert(END, contact_string)


    name_Entry.delete(0,END)
    phone_Entry.delete(0,END)

def delete_contact():
    listbox.delete(ANCHOR)

def save_list():
     """"  save the list to a simple txt file """

     with open ("F:\pythonProject2\saved.txt","w") as f:
         list_tuple = listbox.get(0,END)
         for item in list_tuple:
             if item.endswith("\n"):
                 f.write(item)
             else :
                 f.write(item+"\n")

def open_list():
    with open("F:\pythonProject2\saved.txt", "r") as f:
        for line in  f :
            listbox.insert(END,line)

def copy_phone():
    selected_contact = listbox.get(ANCHOR)
    number = selected_contact.split(": ")
    pyperclip3.copy(number[1])

# ------------------------------------ Button And  Entry -----------------------------
# contact name lable and Entry

name_lable= Label(root,text = "  Contact name",bg=background,fg = "white",font=("Calibri" ,12),anchor = "w",justify = LEFT )
name_lable.place(relx = 0.1 , rely = 0.1,anchor = "c")

name_Entry= Entry(root,bg="white",fg=background,width = 30,borderwidth=2)
name_Entry.place(relx=0.4,rely=0.1,anchor="c")

# contact number lable and Entry

phone_lable= Label(root,text="      Contact number ",bg=background,fg="white",font= ("Calibri" ,12),anchor = "w",justify = LEFT )
phone_lable.place(relx = 0.1 , rely = 0.2,anchor = "c")

phone_Entry= Entry(root,bg="white",fg=background,width=30,borderwidth=2)
phone_Entry.place(relx=0.4,rely=0.2,anchor="c")

# add contact button
add_buuton = Button(root,text ="Add Contact",bg="#121212",fg="white",borderwidth=3,padx=125 ,command=add_contact)
add_buuton.place(relx =0.29 , rely = 0.35,anchor = "c")

# save list button

save_button = Button(root,text="save list",bg=background,fg="white",borderwidth=3,padx=135,command=save_list)
save_button.place(relx=0.29,rely=0.5,anchor="c")

# copy phone number
copy_button = Button(root,text="Copy Phone Number",bg=background,fg="white",borderwidth=3,padx=10,command=copy_phone)
copy_button.place(relx=0.15,rely=0.65,anchor="c")

# delete contact button
delete_phone = Button(root,text="Delete Phone",bg=background,fg="white",borderwidth=3,padx=25 , command=delete_contact)
delete_phone.place(relx=0.14,rely=0.77,anchor="c")

# open_saved button
open_saved = Button(root,text="Open Saved File",bg=background,fg="white",borderwidth=3,padx=30,command = opendirc)
open_saved.place(relx=0.42,rely=0.65,anchor="c")

# Exit button
exit_button = Button(root,text="Exit App ",bg=background,fg="white",borderwidth=3,padx = 50,command=Exit)
exit_button.place(relx=0.42,rely=0.77,anchor="c")

# ------------------------------------ list Box -----------------------------
# listBox for contact
listbox = Listbox(root,width=40,height=15)
listbox.place(relx=0.75,rely=0.47,anchor="c")

open_list()
root.mainloop()











