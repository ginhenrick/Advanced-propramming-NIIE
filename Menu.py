from tkinter import *
from tkinter import messagebox
import tkinter as tk

root = Tk("System")
menu_bar = Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=5)
file_menu.add_command(label="Quit", command=root.destroy)
menu_bar.add_cascade(label="Goodbye", menu=file_menu)
root.config(menu=menu_bar)
root.title("System")
root.geometry("400x300")
Label(root,text="Log in").grid(row=1,column=0)
Entry(root).grid(row=1,column=1)
dn=Entry(root)
Label(root,text="Class").grid(row=1,column=3)
Entry(root).grid(row=1,column=4)
lop=Entry(root)
Label(root,text="Student").grid(row=2,column=3)
Entry(root).grid(row=2,column=4)
sv=Entry(root)

def htShow():
    messagebox.showinfo("System",
            f"Log in \n Log out")
def qlShow():
    messagebox.showinfo("Management",
            f"Class \n Student")
def dxShow():
    messagebox.showinfo("Log out complete",
            f" Thank you")
Button(root,text="System",command=htShow).grid(row=0,column=0)
Button(root,text="System",command=qlShow).grid(row=0,column=3)
dx=Button(root,text="Log out",command=dxShow).grid(row=2,column=0)
root.mainloop()