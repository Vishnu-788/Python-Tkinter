from tkinter import *

window = Tk()
window.title("My Quiz")
window.geometry("600x600")

# Header frame
header_frame = Frame(window, bg="#000000")
header_frame.pack()

title_label = Label(text="Quiz Application.", font=("Arial", 24))

# Start the main loop
window.mainloop()