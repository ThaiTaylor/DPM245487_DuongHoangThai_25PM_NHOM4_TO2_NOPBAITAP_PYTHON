#Menu
from tkinter import*

root = Tk()

window_cao = 400
window_rong = 600

screen_cao = root.winfo_screenheight()
screen_rong = root.winfo_screenwidth()

center_x = int(screen_cao//2 - window_cao//2)
center_y = int(screen_rong//2 - window_rong//2)

root.geometry(f'{window_rong}x{window_cao}+{center_y}+{center_x}')

menubar = Menu(root)
file_menu = Menu(menubar, tearoff=1)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Edit", command=lambda: None)

menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)
root.title("Lập trình Tkinter")

root.mainloop()