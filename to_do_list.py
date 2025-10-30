from tkinter import *
from tkinter.simpledialog import askstring

# Creation and configuration of window object.
window = Tk()
window.geometry("600x600")
window.title("My To-do Application.")

# Window grid column configures.
window.grid_columnconfigure(0, weight=1)

# Window grid row configures.
window.grid_rowconfigure(1, weight=1)

# Global variables.
task_count=0

def add_task_ui(text):
    task_frame.grid_rowconfigure(0, weight=1)
    check_button = Checkbutton(task_frame, text=text, anchor="w", font=("Arial", 20))
    check_button.pack(anchor="w", pady=5, fill="x", expand=False)

def handle_add_task(task):
    global task_count
    task_count += 1
    print(f"Task count updated. {task_count}")
    add_task_ui(task)

def take_input():
    task = askstring('Task', "Enter your task.")
    handle_add_task(task)


# Header frame to hold the header objects.
header_frame = Frame(window, width=600)
header_frame.grid(row=0, column=0, sticky="ew", pady=10)
header_frame.grid_columnconfigure(0, weight=1)

header_label = Label(header_frame, text="To-do List", font=("Arial", 24))
header_label.grid(row=0, column=0, padx=10)

# Task menu.
task_frame = Frame(window, width=600, bg="#ffffff")
task_frame.grid(row=1, column=0, sticky="nsew")

# Footer frame.
footer_frame = Frame(window, width=600, bg="#f3f3f3", )
footer_frame.grid(row=2, column=0, sticky="nsew")
# Task Entry.
task_entry = Entry(footer_frame, font=("Arial", 20))
task_entry.pack(ipady=10, fill="x", expand=True)

add_task_button = Button(footer_frame, text="+", width=4, height=1, font=("Arial", 16), command=take_input)
add_task_button.pack(side="right", )


# Start the main loop.
window.mainloop()