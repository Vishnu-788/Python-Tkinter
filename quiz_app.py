from tkinter import *
from tkinter import ttk

"""
Main window object creation and its configurations.
GM -> Pack.
"""

window = Tk()
window.geometry("600x400")
window.title("Quiz Application.")

FONT = "Times New Roman"
TEXT_BG = "#000000"

style = ttk.Style()
style.configure("Custom.TRadiobutton", font=(FONT, 16))
style.configure("Custom.TButton", background="#3333ff", font=(FONT, 16))

# Global variables
curr_que=1
score=0
selected_option = StringVar(value="")
questions_options_dictionary = {
    1: {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Paris", "Madrid", "Rome"],
        "answer": "Paris"
    },
    2: {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Venus", "Mars", "Jupiter"],
        "answer": "Mars"
    },
    3: {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["William Wordsworth", "William Shakespeare", "Charles Dickens", "Jane Austen"],
        "answer": "William Shakespeare"
    },
    4: {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Helium"],
        "answer": "Carbon Dioxide"
    },
    5: {
        "question": "What is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "answer": "2"
    },
    6: {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Gold", "Oxygen", "Osmium", "Oxide"],
        "answer": "Oxygen"
    },
    7: {
        "question": "What is the square root of 81?",
        "options": ["7", "8", "9", "10"],
        "answer": "9"
    },
    8: {
        "question": "In which year did World War II end?",
        "options": ["1942", "1945", "1948", "1950"],
        "answer": "1945"
    },
    9: {
        "question": "Which ocean is the largest in the world?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"],
        "answer": "Pacific Ocean"
    },
    10: {
        "question": "Which instrument measures atmospheric pressure?",
        "options": ["Thermometer", "Barometer", "Hygrometer", "Altimeter"],
        "answer": "Barometer"
    },
    11: {
        "question": "Who discovered gravity when an apple fell from a tree?",
        "options": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Nikola Tesla"],
        "answer": "Isaac Newton"
    },
    12: {
        "question": "Which continent is known as the 'Dark Continent'?",
        "options": ["Asia", "Europe", "Africa", "Australia"],
        "answer": "Africa"
    },
    13: {
        "question": "How many sides does a hexagon have?",
        "options": ["5", "6", "7", "8"],
        "answer": "6"
    },
    14: {
        "question": "Which organ in the human body pumps blood?",
        "options": ["Brain", "Heart", "Lungs", "Liver"],
        "answer": "Heart"
    },
    15: {
        "question": "Which language has the most native speakers worldwide?",
        "options": ["English", "Spanish", "Mandarin Chinese", "Hindi"],
        "answer": "Mandarin Chinese"
    },
    16: {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["Iron", "Gold", "Diamond", "Platinum"],
        "answer": "Diamond"
    },
    17: {
        "question": "Which is the fastest land animal?",
        "options": ["Lion", "Cheetah", "Horse", "Leopard"],
        "answer": "Cheetah"
    },
    18: {
        "question": "Which country gifted the Statue of Liberty to the USA?",
        "options": ["France", "England", "Spain", "Germany"],
        "answer": "France"
    },
    19: {
        "question": "Which programming language is known as the 'language of the web'?",
        "options": ["Python", "Java", "C++", "JavaScript"],
        "answer": "JavaScript"
    },
    20: {
        "question": "How many bones are in the adult human body?",
        "options": ["206", "201", "209", "212"],
        "answer": "206"
    }
}


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

score_label = ttk.Label(header_frame, text=f"Score: {score}", font=(FONT, 14))
score_label.grid(row=0, column=1)



"""
MCQ Frame.
GM -> Pack
"""


# Variable to hold the current question number
home_frame = ttk.Frame(window)
home_frame.pack(fill="x", padx=10, pady=10, expand=True)
curr_frame = home_frame
def destroy_curr_frame():
    global curr_frame
    curr_frame.destroy()


def handle_start():
    destroy_curr_frame()
    render_questions_frame()


home_welcome_label = ttk.Label(home_frame, text="Welcome to my Quiz application lets start the Exam.", font=(FONT, 20))
home_sub_label = ttk.Label(home_frame, text="Press START to continue...", font=(FONT, 14))
start_button = ttk.Button(home_frame, text="START", command=handle_start)

home_welcome_label.pack(anchor="center", pady=40)
home_sub_label.pack(anchor="center", pady=5)
start_button.pack(anchor="center", pady=10)


def render_questions_frame():
    global curr_que, selected_option, curr_frame
    destroy_curr_frame()
    mcq_frame = ttk.Frame(window)
    mcq_frame.pack(fill="x", padx=10, pady=10, expand=True)

    question_dict = questions_options_dictionary[curr_que]
    question = question_dict["question"]
    options = question_dict["options"]


    questions_frame = ttk.Frame(mcq_frame, height=80)
    questions_frame.pack_propagate(False)
    questions_frame.pack(fill="x")

    question_label = ttk.Label(questions_frame, anchor="w", text=question, font=(FONT, 18))
    question_label.pack(fill="x")

    answers_frame = ttk.Frame(mcq_frame)
    answers_frame.pack(fill="x", expand=True)



    option_1 = ttk.Radiobutton(answers_frame, text=options[0], value=options[0], variable=selected_option, style="Custom.TRadiobutton")
    option_2 = ttk.Radiobutton(answers_frame, text=options[1], value=options[1], variable=selected_option, style="Custom.TRadiobutton")
    option_3 = ttk.Radiobutton(answers_frame, text=options[2], value=options[2], variable=selected_option, style="Custom.TRadiobutton")
    option_4 = ttk.Radiobutton(answers_frame, text=options[3], value=options[3], variable=selected_option, style="Custom.TRadiobutton")

    option_1.pack(fill="x")
    option_2.pack(fill="x")
    option_3.pack(fill="x")
    option_4.pack(fill="x")

    curr_frame = mcq_frame

"""
Footer Frame.
GM -> Grid.
"""

footer_frame = ttk.Frame(window)
footer_frame.pack(side="bottom")

def render_final_page():

    destroy_curr_frame()
    score_frame = ttk.Frame(window)
    score_frame.pack(fill="x", expand=True)

    final_label = ttk.Label(score_frame, text=f"Score: {score}", font=(FONT, 24))
    final_label.pack(anchor="center", fill="x")
    final_label_2 = ttk.Label(score_frame, text="Thank you for using this app.", font=(FONT, 20))
    final_label_2.pack(anchor="center", fill="x")

def handle_next_button():
    global curr_que, selected_option, score

    answer = selected_option.get()

    if curr_que in questions_options_dictionary:
        if answer == questions_options_dictionary[curr_que]["answer"]:
            score += 1
            score_label.config(text=f"Score: {score}")

    curr_que += 1
    selected_option = StringVar(value="")

    if curr_que in questions_options_dictionary:
        render_questions_frame()
    else:
        render_final_page()


next_button = ttk.Button(footer_frame, text="NEXT", style="Custom.TButton", command=handle_next_button)
next_button.pack(side="right")


# Start the main loop
window.mainloop()