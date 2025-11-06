import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x600")
window.title("Dice Rolling Simulator")

canvas = tk.Canvas(window)
canvas.pack(fill="both", expand=True)

rectangle = canvas.create_rectangle(200, 150, 400, 350, width=5)


# First row circles.
row1_circle1 = canvas.create_oval(235, 170, 275, 210, fill="black")
row1_circle2 = canvas.create_oval(325, 170 ,365, 210, fill="black")

# Second row circles.
row2_circle1 = canvas.create_oval(235, 230 ,275, 270, fill="black")
row2_circle2 = canvas.create_oval(325, 230, 365, 270, fill="black")

# Third row circles.
row3_circle1 = canvas.create_oval(235, 290, 275, 330, fill="black")
row3_circle2 = canvas.create_oval(325 , 290, 365, 330, fill="black")

window.mainloop()