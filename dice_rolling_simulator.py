import random
import tkinter as tk

window = tk.Tk()
window.geometry("600x600")
window.title("Dice Rolling Simulator")

canvas = tk.Canvas(window)
canvas.pack(fill="both", expand=True)

coords_list = [
     [235, 170, 275, 210],
     [325, 170 ,365, 210],

     [235, 230 ,275, 270],
     [325, 230, 365, 270],

     [235, 290, 275, 330],
     [325, 290, 365, 330]
]

def draw_circles(limit):
    canvas.create_rectangle(200, 150, 400, 350, width=5)

    for coord in range(0, limit):
        x1 = coords_list[coord][0]
        y1 = coords_list[coord][1]
        x2 = coords_list[coord][2]
        y2 = coords_list[coord][3]
        canvas.create_oval(x1, y1, x2, y2, fill="black")

def roll_dice():
    canvas.delete("all")
    numbers = [1, 2, 3, 4, 5, 6]
    roll = random.choice(numbers)
    draw_circles(roll)

def start_rolling(i=1):
    if i<5:
        roll_dice()
        window.after(700, lambda: start_rolling(i+1))

roll_button = tk.Button(window, text="Roll", command=start_rolling, font=("Arial", 20))
roll_button.pack(fill="x", anchor="center", ipady=10)

window.mainloop()