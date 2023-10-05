import tkinter as tk
from code_editor import CodeEditor
from menu_bar import create_menu_bar

def create_base_window():
    root = tk.Tk()
    root.title("My Python IDE")
    
    # Create the custom code editor component
    code_editor = CodeEditor(root)
    code_editor.pack(expand=tk.YES, fill=tk.BOTH)

    create_menu_bar(root)
    
    return root

if __name__ == "__main__":
    app = create_base_window()
    app.mainloop()
