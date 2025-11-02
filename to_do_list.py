from tkinter import *
from tkinter.simpledialog import askstring

# Creation and configuration of window object.
window = Tk()
window.geometry("600x600")
window.title("My To-do Application.")
window.configure(bg="#e6e6ff")

# Window grid column configures.
window.grid_columnconfigure(0, weight=1)

# Window grid row configures.
window.grid_rowconfigure(1, weight=1)

# Global variables.
task_count=0

def handle_on_toggle(check_button, var):
    if var.get() == 1:
        check_button.config(font=("Arial", 20, "overstrike"))
    else:
        check_button.config(font=("Arial", 20))

def handle_delete(task_row):
    task_row.destroy()

def add_task_ui(text):
    task_row = Frame(task_frame, bg="#000000")
    task_row.pack(fill="x", expand=False, pady=5, padx=10)

    var = IntVar()

    check_button = Checkbutton(
        task_row,
        text=text,
        anchor="w",
        font=("Arial", 20),
        variable=var,
        command=lambda: handle_on_toggle(check_button, var),
        bg="#000000",
        fg="white",
        selectcolor="#000000"
    )
    check_button.pack(side="left", fill="x", expand=True, padx=10, pady=5)

    delete_button = Button(task_row, text="Delete", command= lambda: handle_delete(task_row))
    delete_button.pack(side="right", padx=10, pady=5)


def handle_add_task(task):
    global task_count
    task_count += 1
    print(f"Task count updated. {task_count}")
    add_task_ui(task)

def take_input():
    task = task_entry.get()
    if task != "":
        handle_add_task(task)
        task_entry.delete(0, "end")
        return
    print("Error.")



# Header frame to hold the header objects.
header_frame = Frame(window, width=600, bg="#e6e6ff")
header_frame.grid(row=0, column=0, sticky="ew", pady=10)
header_frame.grid_columnconfigure(0, weight=1)

header_label = Label(header_frame, text="To-do List", bg="#e6e6ff", font=("Arial", 24))
header_label.grid(row=0, column=0, padx=10)

# Task menu.
task_frame = Frame(window, width=600, bg="#e6e6ff")
task_frame.grid(row=1, column=0, sticky="nsew")

# Footer frame.
footer_frame = Frame(window, width=600, bg="#e6e6ff")
footer_frame.grid(row=2, column=0, sticky="nsew")

footer_frame.grid_columnconfigure(0, weight=1)
footer_frame.grid_columnconfigure(1, weight=0)
footer_frame.grid_rowconfigure(0, weight=1)

task_entry = Entry(footer_frame, font=("Arial", 20))
task_entry.grid(row=0, column=0, sticky="nsew")

add_task_button = Button(
    footer_frame,
    text="+",
    font=("Arial", 20, "bold"),
    command=take_input
)
add_task_button.grid(row=0, column=1, sticky="nsew")


# Start the main loop.
window.mainloop()