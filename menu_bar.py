import tkinter as tk
from tkinter import Menu

def on_exit(root):
    root.destroy()

def create_menu_bar(root):
    menubar = Menu(root)
    root.config(menu=menubar)

    file_menu = Menu(menubar)
    menubar.add_cascade(label="File", menu=file_menu)

    file_menu.add_command(label="New")
    file_menu.add_command(label="Open")
    file_menu.add_separator()
    file_menu.add_command(label="Save")
    file_menu.add_command(label="Save As")
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=lambda: on_exit(root))

    edit_menu = Menu(menubar)
    menubar.add_cascade(label="Edit", menu=edit_menu)

    edit_menu.add_command(label="Cut")
    edit_menu.add_command(label="Copy")
    edit_menu.add_command(label="Paste")

if __name__ == "__main__":
    root = tk.Tk()
    create_menu_bar(root)
    root.mainloop()
 