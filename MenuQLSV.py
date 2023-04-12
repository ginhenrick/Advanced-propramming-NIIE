from binascii import b2a_base64
from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("400x300")

def mo_mang_hinh_login(main):
    login=Toplevel (main)
    Label(login, text="username").grid(row=0,column=0)
    Label(login, text="Password").grid(row=1, column=0)
    login.mainloop()
def dxShow(main):
    messagebox.showinfo("Đăng xuất sever Trái đất",
            f" Get Go")
mainmenu=Menu(root)
menuht=Menu(mainmenu,tearoff=0)
menuht.add_command(label="đăng nhập",command=lambda :mo_mang_hinh_login(root))
menuht.add_command(label="đăng xuất",command=lambda :dxShow(root))
menuht.add_separator()
menuht.add_command(label="thoat",command=root.quit)
mainmenu.add_cascade(label="He thong",menu= menuht)

menuql=Menu(mainmenu, tearoff=0)
menuql.add_command(label="Lop")
menuql.add_command(label="sinh vien")
menuql.add_command(label="diem")
menuql.add_separator()
mainmenu.add_cascade(label="Quan ly",menu= menuql)
root.config(menu=mainmenu)
root.mainloop()