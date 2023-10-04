import tkinter as tk
from menu_bar import create_menu_bar

def create_base_window():
    root = tk.Tk()
    root.title("My Python IDE")
    
    # Create a menu bar using the imported function
    create_menu_bar(root)

    # Create a text widget (for code editing)
    text_widget = tk.Text(root, wrap=tk.WORD)
    text_widget.pack(expand=tk.YES, fill=tk.BOTH)

    # Create a scrollbar for the text widget
    scrollbar = tk.Scrollbar(text_widget)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_widget.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=text_widget.yview)

    return root

if __name__ == "__main__":
    app = create_base_window()
    app.mainloop()
