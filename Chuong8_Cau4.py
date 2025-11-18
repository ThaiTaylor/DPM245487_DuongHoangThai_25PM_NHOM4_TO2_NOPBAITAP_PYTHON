#Câu 4: Máy tính bỏ túi

import tkinter as tk
from tkinter import messagebox

# Hàm xử lý khi nhấn phím
def on_click(value):
    entry.insert(tk.END, value)

# Hàm tính toán
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        messagebox.showerror("Error", "Phép tính không hợp lệ!")

# Hàm xóa toàn bộ
def clear_screen():
    entry.delete(0, tk.END)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Calculator")

# Ô hiển thị
entry = tk.Entry(root, width=25, font=("Arial", 18), bd=3, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Danh sách nút theo layout của hình
buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
    ('0', 4, 1),
    ('+', 5, 0), ('-', 5, 1), ('*', 5, 2), ('/', 5, 3),
    ('=', 4, 2),
]

# Tạo nút theo vị trí
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=8, height=2,
                        command=calculate, font=("Arial", 12))
    else:
        btn = tk.Button(root, text=text, width=8, height=2,
                        command=lambda v=text: on_click(v), font=("Arial", 12))
    btn.grid(row=row, column=col, padx=3, pady=3)

# Nút Clr (xóa)
clr_button = tk.Button(root, text="Clr", width=32, height=2,
                       command=clear_screen, font=("Arial", 12))
clr_button.grid(row=6, column=0, columnspan=4, padx=3, pady=3)

root.mainloop()
