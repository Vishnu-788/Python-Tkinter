import tkinter as tk
from tkinter import ttk
import random

window = tk.Tk()
window.title("Number Guess")
window.geometry("400x400")

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

main_frame = ttk.Frame(window)
main_frame.pack(fill="x", expand=True)

main_frame.grid_columnconfigure(0, weight=1)

home_frame = ttk.Frame(main_frame)
home_frame.grid(row=0, column=0)

home_frame.grid_columnconfigure(0, weight=1)

home_label = ttk.Label(home_frame, text="Guess a Number from 1 - 10", font=("Times New Roman", 20))
home_label.grid(row=0, column=0)


def guess_number():
    return random.choice(numbers_list)

def handle_guess():
    guess = guess_number()
    render_asking_frame(guess)

guess_button = ttk.Button(home_frame, text="Guess", command=handle_guess)
guess_button.grid(row=0, column=1)

curr_frame = home_frame

def destroy_curr_frame():
    curr_frame.destroy()

def render_asking_frame(guess):
    global curr_frame
    destroy_curr_frame()
    asking_frame = ttk.Frame(main_frame)
    asking_frame.grid(row=0, column=0)

    ask_label = ttk.Label(asking_frame, text=f"Is it {guess}?", anchor="center" ,font=("Times New Roman", 20))
    ask_label.grid(row=0, column=1, columnspan=2, sticky="ew")

    yes_button = ttk.Button(asking_frame, text="Yes", command=render_success_frame)
    yes_button.grid(row=1, column=1)

    no_button = ttk.Button(asking_frame, text="No", command=handle_guess)
    no_button.grid(row=1, column=2)

    curr_frame=asking_frame

def render_success_frame():
    destroy_curr_frame()
    success_frame = ttk.Frame(main_frame)
    success_frame.grid(row=0, column=0)

    success_label = ttk.Label(success_frame, text="Hooray!!!", font=("Times New ROman", 24))
    success_label.pack(fill="x", expand=True)



window.mainloop()