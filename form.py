from tkinter import *

# Creation of window object.
window = Tk()
window.title("Forms")
window.geometry("500x600")
window.resizable(False, False)

# Configuration for grid.
head_frame = Frame(window)
head_frame.grid(row=0, column=0, columnspan=2, sticky='ew')

head_frame.grid_columnconfigure(0, weight=1)
head_frame.grid_columnconfigure(1, weight=1)
head_frame.grid_columnconfigure(2, weight=1)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=3)

for i in range(7):
    window.grid_rowconfigure(i, pad=10)

# Widgets and placements.
# Heading
head = Label(head_frame, text="Form", font=("Helvetica", 20))
head.grid(row=0, column=1)

# Form fields.
name_label = Label(window, text="Name", font="Helvetica")
name_entry = Entry(window)
name_label.grid(row=2, column=0, sticky="w")
name_entry.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)

email_label = Label(window, text="Email", font="Helvetica")
email_entry = Entry(window)
email_label.grid(row=3, column=0, sticky="w")
email_entry.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)

phn_no_label = Label(window, text="Phone No", font="Helvetica")
phn_no_entry = Entry(window)
phn_no_label.grid(row=4, column=0, sticky="w")
phn_no_entry.grid(row=4, column=1, sticky="nsew", padx=10, pady=5)

pwd_label = Label(window, text="Password", font="Helvetica")
pwd_entry = Entry(window)
pwd_label.grid(row=5, column=0, sticky="w")
pwd_entry.grid(row=5, column=1, sticky="nsew", padx=10, pady=5)

confirm_pwd_label = Label(window, text="Confirm Password", font="Helvetica")
confirm_pwd_entry = Entry(window)
confirm_pwd_label.grid(row=6, column=0, sticky="w")
confirm_pwd_entry.grid(row=6, column=1, sticky="nsew", padx=10, pady=5)

# Handle the submission.
def handle_submit():
    name = name_entry.get()
    email = email_entry.get()
    phn_no = phn_no_entry.get()
    pwd = pwd_entry.get()
    confirm_pwd = confirm_pwd_entry.get()

    if not "@gmail.com" in email:
        print("Please enter a valid email.")
        return
    if len(str(phn_no)) != 10:
        print("Please enter 10 digit mobile number.")
        return
    if pwd != confirm_pwd:
        print("Password mismatch.")
        return
    print(f"{name} Successfully registered.")


submit_button = Button(text="Submit",  padx=30, pady=10, command=handle_submit)
submit_button.grid(row=7, column=0, columnspan=2)

# Start the main loop.
window.mainloop()
