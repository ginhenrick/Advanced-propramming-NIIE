
#import tkinter as tk
from tkinter import *
# from tkinter import ttk

main=Tk()
main.title("21BITV03")

lbltieude=Label(main,text="Hello ")
lbltieude.pack()

btnsay=Button(main,text="truất chưa")
btnsay.pack()

img= PhotoImage(file="nmt.png")
Label(main,image=img).pack()

main.mainloop()
