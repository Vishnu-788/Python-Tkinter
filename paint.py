import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x600")
window.title("Paint")

menubar = tk.Menu(window)
window.config(menu=menubar)

def use_eraser(w=2):
    set_pen_color("white")
    set_pen_width(w)
    change_cursor("dotbox")

def change_cursor(cursor="arrow"):
    draw_canvas.config(cursor=cursor)

def set_pen_width(w):
    change_cursor()
    draw_canvas.pen_width = w

def set_pen_color(c):
    draw_canvas.pen_color = c

def start_draw(event):
    draw_canvas.last_x, draw_canvas.last_y = event.x, event.y

def draw(event):
    x = event.x
    y = event.y
    draw_canvas.create_line(draw_canvas.last_x, draw_canvas.last_y, x, y,
                            fill=draw_canvas.pen_color,
                            width=draw_canvas.pen_width,
                            capstyle="round"
                            )
    draw_canvas.last_x, draw_canvas.last_y = x, y


pen = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Pen", menu=pen)
pen.add_command(label = "Width 2", command=lambda: set_pen_width(2))
pen.add_command(label = "Width 4", command=lambda: set_pen_width(4))
pen.add_command(label = "Width 6", command=lambda: set_pen_width(6))

color = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Color", menu=color)
color.add_command(label="blue", command=lambda: set_pen_color("blue"))
color.add_command(label="red", command=lambda: set_pen_color("red"))
color.add_command(label="violet", command=lambda: set_pen_color("violet"))

eraser = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Eraser", menu=eraser)
eraser.add_command(label="2", command=lambda: use_eraser())
eraser.add_command(label="4", command=lambda: use_eraser(4))
eraser.add_command(label="8", command=lambda: use_eraser(8))


draw_canvas = tk.Canvas(window, bg="white")

draw_canvas.pen_width=2
draw_canvas.pen_color="black"

draw_canvas.pack(fill="both", expand=True)

draw_canvas.bind("<Button-1>", start_draw)
draw_canvas.bind("<B1-Motion>", draw)

window.mainloop()