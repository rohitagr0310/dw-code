import tkinter as tk
from tkinter import scrolledtext

class CodeEditor(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("My Python IDE")
        
        # Create a text widget (for code editing)
        self.text_widget = scrolledtext.ScrolledText(
            self,
            wrap=tk.WORD,
            font=("Consolas", 12),  # Use a monospaced font like Consolas
            insertbackground="Black",  # Color of the cursor
            selectbackground="lightblue"  # Color of selected text
        )
        self.text_widget.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH)

        # Create a frame for line numbers
        self.line_number_frame = tk.Frame(self)
        self.line_number_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Create a line numbers text widget
        self.line_number_text = tk.Text(
            self.line_number_frame,
            width=4,  # Adjust the width as needed
            padx=2,
            borderwidth=0,
            takefocus=0,
            font=("Consolas", 12),  # Use the same font as the code text widget
            state=tk.DISABLED,  # Make it read-only
        )
        self.line_number_text.pack(side=tk.LEFT, fill=tk.Y)

        # Bind the text widget to update line numbers when a key is pressed
        self.text_widget.bind("<Key>", self.update_line_numbers)

        # Initial update of line numbers
        self.update_line_numbers()

    def update_line_numbers(self, *args):
        lines = self.text_widget.get("1.0", "end").splitlines()
        line_count = len(lines)
        line_numbers = "\n".join(str(i) for i in range(1, line_count + 1))
        self.line_number_text.config(state=tk.NORMAL)
        self.line_number_text.delete("1.0", tk.END)
        self.line_number_text.insert("1.0", line_numbers)
        self.line_number_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeEditor(master=root)
    app.mainloop()
