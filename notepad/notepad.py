from tkinter import ttk, Toplevel
import tkinter as tk

# Window configs.
window = tk.Tk()
window.title("Note Pad")
window.geometry("600x600")

# File handling modes
READ = "r"
WRITE = "w"
APPEND = "a"
READ_AND_WRITE = "r+"

# Menu bar configuration.
def get_file_path(filename):
    return fr"E:\QIS Academy\workspace\Assessment\tkinter assessment\notepad\files\{filename}"

def create_window():
    new_window = Toplevel(window)  # Create a new window
    new_window.title("New Window")
    new_window.geometry("250x150")
    return new_window

def handle_cancel(new_window):
    new_window.destroy()

def open_save_window():
    new_window = create_window()
    label = tk.Label(new_window, text="Enter the filename: ")
    label.pack(pady=10, padx=10, anchor="w")

    entry = tk.Entry(new_window)
    entry.pack(pady=5, padx=10, fill="x")

    buttons_frame = ttk.Frame(new_window)
    buttons_frame.pack(fill="x", padx=10, pady=5)

    buttons_frame.grid_columnconfigure(0, weight=1)
    buttons_frame.grid_columnconfigure(1, weight=1)

    save_button = ttk.Button(buttons_frame, text="Save", command=lambda: handle_save(entry, new_window))
    save_button.grid(row=0, column=0, sticky="w")

    cancel_button = ttk.Button(buttons_frame, text="cancel",command=lambda: handle_cancel(new_window))
    cancel_button.grid(row=0, column=1, sticky="e")

def handle_open():
    new_window = create_window()

    label = tk.Label(new_window, text="Enter the filename: ")
    label.pack(pady=10, padx=10, anchor="w")

    entry = tk.Entry(new_window)
    entry.pack(pady=5, padx=10, fill="x")

    buttons_frame = ttk.Frame(new_window)
    buttons_frame.pack(fill="x", padx=10, pady=5)

    buttons_frame.grid_columnconfigure(0, weight=1)
    buttons_frame.grid_columnconfigure(1, weight=1)

    open_button = ttk.Button(buttons_frame, text="open", command=lambda: open_file(entry, new_window))
    open_button.grid(row=0, column=0, sticky="w")

def open_file(entry, new_window):
    file_name = entry.get()
    new_window.destroy()
    contents=""
    with open(get_file_path(file_name), READ) as f1:
        contents = f1.read()
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", contents)


def handle_save(entry, new_window):
    file_name = entry.get()
    save_file(get_file_path(file_name), WRITE)
    new_window.destroy()


def handle_edit():
    pass

def handle_exit():
    global window
    window.destroy()

def get_content():
    return text_area.get("1.0", tk.END)

def save_file(filepath, mode):
    with open(filepath, mode) as f1:
        contents = get_content()
        f1.write(contents)

# Menu bar
menubar = tk.Menu(window)
file = tk.Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu = file)
window.config(menu=menubar)

file.add_command(label = "New File", command=open_save_window)
file.add_command(label = "Open", command=handle_open)
file.add_command(label = "Edit", command=handle_edit)
file.add_command(label = "Save", command=open_save_window)
file.add_separator()
file.add_command(label = "Exit", command=handle_exit)

edit = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit)

view = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=view)

insert = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Insert", menu=insert)

# Text Area.
main_frame = ttk.Frame(window)
main_frame.pack(fill="both", expand=True)

text_area = tk.Text(main_frame)
text_area.pack(fill="both", expand=True)


# Start the main loop.
window.mainloop()
