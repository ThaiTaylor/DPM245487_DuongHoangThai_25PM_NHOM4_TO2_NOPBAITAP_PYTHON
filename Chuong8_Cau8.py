#Câu 8: Thiết kế màn hình chuyển độ F thành độ C
import tkinter as tk
from tkinter import ttk, messagebox

# Hàm chuyển độ F sang độ C
def convert_F_to_C():
    try:
        f = float(entry_F.get())
        c = (f - 32) * 5/9
        result.set(f"{c:.2f} °C")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập giá trị số!")

# Tạo cửa sổ
root = tk.Tk()
root.title("Chuyển độ F sang độ C")
root.geometry("350x220")

# Tiêu đề
ttk.Label(root, text="Chuyển đổi độ F → độ C", font=("Arial", 14, "bold")).pack(pady=10)

# Nhập độ F
ttk.Label(root, text="Nhập độ F:", font=("Arial", 12)).pack()
entry_F = ttk.Entry(root, width=25)
entry_F.pack(pady=5)

# Nút chuyển đổi
ttk.Button(root, text="Chuyển đổi", command=convert_F_to_C).pack(pady=10)

# Kết quả
result = tk.StringVar()
ttk.Label(root, textvariable=result, font=("Arial", 16), foreground="blue").pack(pady=10)

# Chạy app
root.mainloop()

