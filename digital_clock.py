import tkinter as tk
from time import strftime
from tkinter import ttk

window = tk.Tk()
window.title("Clock")
window.geometry("400x400")

clock_frame = ttk.Frame(window)
clock_frame.pack(expand=True, fill="x", anchor="center")

clock_label = ttk.Label(clock_frame, font=("Times New Roman", 40))
clock_label.pack()

def update_time():
    curr_time = strftime("%H:%M:%S")
    clock_label.config(text=curr_time)
    window.after(1000, update_time)

update_time()
clock_frame.mainloop()
        
    