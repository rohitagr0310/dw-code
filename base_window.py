import tkinter as tk
from menu_bar import create_menu_bar
from tkinter import scrolledtext

def create_base_window():
    root = tk.Tk()
    root.title("My Python IDE")
    
    # Create a menu bar using the imported function
    create_menu_bar(root)

    # Create a text widget (for code editing)
    text_widget = scrolledtext.ScrolledText(
        root,
        wrap=tk.WORD,
        font=("Consolas", 12),  # Use a monospaced font like Consolas
        insertbackground="Black",  # Color of the cursor
        selectbackground="lightblue"  # Color of selected text
    )
    text_widget.pack(expand=tk.YES, fill=tk.BOTH)

    return root

if __name__ == "__main__":
    app = create_base_window()
    app.mainloop()
