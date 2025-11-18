#Câu 9: Phần mềm tính BMI

import tkinter as tk
from tkinter import ttk, messagebox

def tinh_bmi():
    try:
        can_nang = float(entry_weight.get())
        chieu_cao = float(entry_height.get())

        if chieu_cao <= 0 or can_nang <= 0:
            raise ValueError

        bmi = can_nang / (chieu_cao ** 2)
        ket_qua.set(f"{bmi:.2f}")

        # Phân loại BMI
        if bmi < 18.5:
            phan_loai.set("Gầy")
        elif 18.5 <= bmi < 24.9:
            phan_loai.set("Bình thường")
        elif 25 <= bmi < 29.9:
            phan_loai.set("Thừa cân")
        else:
            phan_loai.set("Béo phì")

    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng số!")

# Tạo cửa sổ
root = tk.Tk()
root.title("Tính BMI")
root.geometry("350x300")

# Tiêu đề
ttk.Label(root, text="TÍNH BMI", font=("Arial", 16, "bold")).pack(pady=10)

# Nhập cân nặng
frame1 = ttk.Frame(root)
frame1.pack(pady=5)
ttk.Label(frame1, text="Cân nặng (kg): ", font=("Arial", 12)).grid(row=0, column=0)
entry_weight = ttk.Entry(frame1, width=15)
entry_weight.grid(row=0, column=1)

# Nhập chiều cao
frame2 = ttk.Frame(root)
frame2.pack(pady=5)
ttk.Label(frame2, text="Chiều cao (m): ", font=("Arial", 12)).grid(row=0, column=0)
entry_height = ttk.Entry(frame2, width=15)
entry_height.grid(row=0, column=1)

# Nút tính
ttk.Button(root, text="Tính BMI", command=tinh_bmi).pack(pady=10)

# Kết quả BMI
ket_qua = tk.StringVar()
phan_loai = tk.StringVar()

ttk.Label(root, text="BMI:", font=("Arial", 12)).pack()
ttk.Label(root, textvariable=ket_qua, font=("Arial", 14), foreground="blue").pack()

ttk.Label(root, text="Phân loại:", font=("Arial", 12)).pack(pady=(10,0))
ttk.Label(root, textvariable=phan_loai, font=("Arial", 14), foreground="green").pack()

root.mainloop()
