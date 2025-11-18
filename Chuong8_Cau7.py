#Câu 7: Thiết kế màn hình chuyển năm Dương Lịch thành Âm Lịch

import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Chuyển Năm Dương Lịch → Âm Lịch")
root.geometry("350x220")

# Bảng Can – Chi
CAN = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
CHI = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]

def convert_year():
    try:
        year = int(entry_year.get())
        can = CAN[year % 10]
        chi = CHI[year % 12]
        result.set(f"{can} {chi}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên!")

# Label nhập
ttk.Label(root, text="Nhập năm Dương lịch:", font=("Arial", 12)).pack(pady=10)

# Ô nhập
entry_year = ttk.Entry(root, width=25)
entry_year.pack()

# Nút chuyển
ttk.Button(root, text="Chuyển đổi", command=convert_year).pack(pady=15)

# Kết quả
result = tk.StringVar()
lbl_result = ttk.Label(root, textvariable=result, font=("Arial", 16, "bold"), foreground="blue")
lbl_result.pack()

root.mainloop()
