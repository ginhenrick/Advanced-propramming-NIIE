from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Hỏi em mụt câu nhóe")
root.geometry("400x300")

Label(
    root,
    text="Em thích anh hơm",
    fg="red",
    bg="white",
    font="Arial 14"
).grid(row=0,column=0)
Điềnvàođiem = Entry(root)
Điềnvàođiem.grid(row=1,column=1)
Entry(root).grid(row=0,column=1)

Label(root,text="Làm người yêu anh nha!", fg="red",bg="white", font="Arial 14").grid(row=1,column=0)
Entry(root).grid(row=0,column=1)

Label(root, text="Em ăn cơm chưa?", fg="red",bg="white", font="Arial 14").grid(row=2, column=0)
Entry(root).grid(row=2,column=1)
def handleshow():
    messagebox.showinfo("Thông báo cho em nè","Em mún từ chối cũng hởm có được hehe")




Button(root,text="Show", command= handleshow).grid(row=4,column=0)
Button(root,text="Quit", command= root.quit).grid(row=4,column=1)

root.mainloop()