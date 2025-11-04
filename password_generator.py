import tkinter as tk
import random
from tkinter import ttk

window = tk.Tk()
window.geometry("400x400")
window.title("Password generator")

mainframe = ttk.Frame(window)
mainframe.pack(fill="x", expand=True)

mainframe.grid_columnconfigure(0, weight=1)

def handle_generate():
    password = generate_password(10)
    password_label.config(text=password)


password_label = ttk.Label(mainframe, text="Lets create a strong password")
password_label.grid(row=0, column=0)

generate_button = ttk.Button(mainframe, text="GENERATE", command=handle_generate)
generate_button.grid(row=0, column=1)


choices = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"

def generate_password(strength):
    password=""
    for i in range(1, strength):
        password += random.choice(choices)
    return password

window.mainloop()