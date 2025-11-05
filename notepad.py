from tkinter import ttk
import tkinter as tk

# Window configs.
window = tk.Tk()
window.title("Note Pad")
window.geometry("600x600")

# Functions to handle button clicks.

def handle_new_file():
    pass

def handle_open():
    pass

def handle_edit():
    pass

def handle_exit():
    pass

menubar = tk.Menu(window)
file = tk.Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu = file)
window.config(menu=menubar)
file.add_command(label = "New File", command=handle_new_file)
file.add_command(label = "Open", command=handle_open)
file.add_command(label = "Edit", command=handle_edit)
file.add_separator()
file.add_command(label = "Exit", command=handle_exit)

# Start the main loop.
window.mainloop()
