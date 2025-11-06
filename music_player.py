import tkinter as tk
from tkinter import ttk
from tkinter.constants import HORIZONTAL

window = tk.Tk()
window.geometry("600x300")
window.title('Music Player')

def handle_play_pause():
    pass

def handle_prev():
    pass

def handle_next():
    pass

progress_bar_frame = ttk.Frame(window)
progress_bar_frame.pack(fill="x", expand=True, padx=20)

progress_bar = ttk.Progressbar(progress_bar_frame, orient="horizontal", length=100, mode="determinate")
progress_bar.pack(fill="x")

music_controls_frame = ttk.Frame(window)
music_controls_frame.pack(fill='x', side="bottom", pady=20)

music_controls_frame.grid_columnconfigure(0, weight=1)
music_controls_frame.grid_columnconfigure(1, weight=1)
music_controls_frame.grid_columnconfigure(2, weight=1)

prev_button = ttk.Button(music_controls_frame, text="Previous")
prev_button.grid(row=0, column=0, padx=10)

play_button = ttk.Button(music_controls_frame, text="Play")
play_button.grid(row=0, column=1, padx=10)

next_button = ttk.Button(music_controls_frame, text="Next")
next_button.grid(row=0, column=2, padx=10)

window.mainloop()