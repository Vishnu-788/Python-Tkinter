from tkinter import *
from tkinter import ttk

"""
Main window object creation and its configurations.
GM -> Pack.
"""

window = Tk()
window.geometry("600x600")
window.title("Quiz Application.")

FONT = "Times New Roman"
TEXT_BG = "#000000"
style = ttk.Style()
style.configure("Custom.TCheckbutton", font=(FONT, 16))

"""
Frame for the header.
GM -> Grid.
"""
header_frame = ttk.Frame(window)
header_frame.pack(fill="x", padx=10, pady=10)

header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=0)
header_frame.grid_rowconfigure(0, weight=1)

header_label = ttk.Label(header_frame, text="MY QUIZ APPLICATION", font=(FONT, 20))
header_label.grid(row=0, column=0, sticky="w")

score_label = ttk.Label(header_frame, text="Score: 0", font=(FONT, 14))
score_label.grid(row=0, column=1)


"""
MCQ Frame.
GM -> Pack
"""

questions_options_dictionary = {
    "que 1" : {
        "What is the capital of Canada?" : ["Toronto", "b", "c", "d"]
    },
    "que 2" : {
        "What is it?" : ["a", "b", "c", "d"]
    }
}

mcq_frame = ttk.Frame(window)
mcq_frame.pack(fill="x", padx=10, pady=10)

def render_questions_frame():

    questions_frame = ttk.Frame(mcq_frame, height=80)
    questions_frame.pack_propagate(False)
    questions_frame.pack(fill="x")

    question_label = ttk.Label(questions_frame, anchor="w", text="Place holder here.", font=(FONT, 18))
    question_label.pack(fill="x")

    answers_frame = ttk.Frame(mcq_frame)
    answers_frame.pack(fill="x", expand=True)

    option_1 = ttk.Checkbutton(answers_frame, text="Option 1", style="Custom.TCheckbutton")
    option_2 = ttk.Checkbutton(answers_frame, text="Option 2", style="Custom.TCheckbutton")
    option_3 = ttk.Checkbutton(answers_frame, text="Option 3", style="Custom.TCheckbutton")
    option_4 = ttk.Checkbutton(answers_frame, text="Option 4", style="Custom.TCheckbutton")

    option_1.pack(fill="x")
    option_2.pack(fill="x")
    option_3.pack(fill="x")
    option_4.pack(fill="x")

render_questions_frame()




# Start the main loop
window.mainloop()