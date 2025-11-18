#Câu 6: Màn hình cấu hình Style cho Button

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Demo Button Styles")
root.geometry("400x400")

styles = ttk.Style()

# Lấy danh sách tất cả style hiện có
all_styles = styles.theme_names()

lbl = ttk.Label(root, text="Danh sách style cho Button:", font=("Arial", 14))
lbl.pack(pady=10)

# Chuyển theme để xem nhiều style khác nhau
for theme in all_styles:
    styles.theme_use(theme)

    frame = ttk.Frame(root)
    frame.pack(pady=5)

    ttk.Label(frame, text=f"Theme: {theme}", font=("Arial", 10, "bold")).pack()

    ttk.Button(frame, text=f"Button Style ({theme})").pack(pady=3)

root.mainloop()
