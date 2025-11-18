#Câu 5: Màn hình đăng nhập

import tkinter as tk
from tkinter import messagebox

def login():
    user = nhapten.get()
    pw = matkhau.get()

    # Tài khoản mẫu (bạn có thể thay đổi)
    if user == "admin" and pw == "123":
        messagebox.showinfo("Login", "Đăng nhập thành công!")
    else:
        messagebox.showerror("Login", "Sai Username hoặc Password!")

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Login Form")
root.geometry("350x200")

# Label Username
lbl_user = tk.Label(root, text="Username:", font=("Arial", 12))
lbl_user.place(x=30, y=40)

# Entry Username
nhapten = tk.Entry(root, width=25, font=("Arial", 12))
nhapten.place(x=120, y=40)

# Label Password
lbl_pass = tk.Label(root, text="Password:", font=("Arial", 12))
lbl_pass.place(x=30, y=80)

# Entry Password (ẩn ký tự)
matkhau = tk.Entry(root, width=25, font=("Arial", 12), show="*")
matkhau.place(x=120, y=80)

# Button Login
btn_login = tk.Button(root, text="Login", width=10, command=login, font=("Arial", 12))
btn_login.place(x=80, y=130)

# Button Exit
btn_exit = tk.Button(root, text="Exit", width=10, command=exit_app, font=("Arial", 12))
btn_exit.place(x=190, y=130)

root.mainloop()
