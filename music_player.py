import tkinter as tk
from tkinter import ttk, filedialog
import pygame

window = tk.Tk()
window.geometry("600x300")
window.title('Music Player')

pygame.mixer.init()

def handle_play():
    pygame.mixer.music.play()

def handle_pause():
    pygame.mixer.music.pause()

def handle_resume():
    pygame.mixer.music.unpause()

scale_bar_frame = ttk.Frame(window)
scale_bar_frame.pack(fill="x", expand=True, padx=20)

def ask_filename():
    file_path = filedialog.askopenfilename(
        title="Select music files",
        filetypes=[("Audio Files", "*.mp3 .wav .ogg")]
    )
    return file_path

def load_music():
    file_path = ask_filename()
    if file_path:
        current_track.set(file_path.split("/")[-1])
        pygame.mixer.music.load(file_path)

current_track = tk.StringVar(value="No track selected.")

current_track_label = ttk.Label(scale_bar_frame, textvariable=current_track)
current_track_label.pack(fill="x", pady=10)


progress_value = tk.DoubleVar()
scale = ttk.Scale(
    scale_bar_frame,
    orient="horizontal",
    from_=0,
    to=100,
    variable=progress_value
)
scale.pack(fill="x")

music_controls_frame = ttk.Frame(window)
music_controls_frame.pack(fill='x', side="bottom", pady=20)

music_controls_frame.grid_columnconfigure(0, weight=1)
music_controls_frame.grid_columnconfigure(1, weight=1)
music_controls_frame.grid_columnconfigure(2, weight=1)

pause_button = ttk.Button(music_controls_frame, text="Pause", command=handle_pause)
pause_button.grid(row=0, column=0, padx=10)

play_button = ttk.Button(music_controls_frame, text="Play", command=handle_play)
play_button.grid(row=0, column=1, padx=10)

resume_button = ttk.Button(music_controls_frame, text="Resume", command=handle_resume)
resume_button.grid(row=0, column=2, padx=10)

load_music()


window.mainloop()