from tkinter import *
root = Tk()
root.title("DIEM")
root.geometry("400x300")
Label(root,text="First name").grid(grow=0,column=0)
Entry(root).grid(grow=0,column=1)

Label(root,text="Last name").grid(grow=1,column=0)
Entry(root).grid(grow=0,column=1)

Button(root,text="Show").grid(grow=2,column=1)
Button(root,text="Quit").grid(grow=2,column=0)

root.mainloop()