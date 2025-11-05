import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Stopwatch")
window.geometry("400x400")

# Variables
h, m, s = 0, 0, 0
running = False


clock_frame = ttk.Frame(window)
clock_frame.pack(expand=True, fill="both", anchor="center", pady=50)

clock_label = ttk.Label(clock_frame, font=("Times New Roman", 40), text="00:00:00")
clock_label.pack(pady=20)


def format_time(h, m, s):
    return f"{h:02d}:{m:02d}:{s:02d}"

def update_time():
    global h, m, s, running

    if running:
        s += 1
        if s == 60:
            s = 0
            m += 1
        if m == 60:
            m = 0
            h += 1

        clock_label.config(text=format_time(h, m, s))
        window.after(1000, update_time)

def start():
    global running
    if not running:
        running = True
        update_time()

def stop():
    global running
    running = False

def reset():
    global h, m, s, running
    running = False
    h, m, s = 0, 0, 0
    clock_label.config(text="00:00:00")

btn_frame = ttk.Frame(window)
btn_frame.pack(pady=20)

start_btn = ttk.Button(btn_frame, text="Start", command=start)
start_btn.grid(row=0, column=0, padx=10)

stop_btn = ttk.Button(btn_frame, text="Stop", command=stop)
stop_btn.grid(row=0, column=1, padx=10)

reset_btn = ttk.Button(btn_frame, text="Reset", command=reset)
reset_btn.grid(row=0, column=2, padx=10)

window.mainloop()
