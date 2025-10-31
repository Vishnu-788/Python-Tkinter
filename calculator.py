from tkinter import *

# Creation of window object.
window = Tk()
window.title("Calculator")
window.geometry("260x230")
window.resizable(False, False)
window.grid_rowconfigure(0, pad=5)

for i in range(4):
    window.grid_columnconfigure(i, weight=1)

# Widgets and their placements.
# Display
display_label = Entry(window, font=("Arial", 22), state="disabled" , justify="right")
display_label.grid(row=0, column=0, sticky="nsew", padx=10, columnspan=4)

# Application logic.

# Global variables.
expression="0"
operators_tup = ("+", "-", "/", "*")

def build_expression(exp):
    global expression
    if expression != "0":
        if expression[-1] in operators_tup and exp in operators_tup:
            expression = expression[:-1]
    else:
        expression = ""
    expression = expression + str(exp)

def evaluate_expression():
    try:
        return eval(expression)
    except ZeroDivisionError:
        return "ZERO DIVISION"
    except SyntaxError:
        return "SYNTAX ERROR"

def update_entry():
    temp_exp = expression.replace("*", "x")

    display_label.config(state="normal")
    display_label.delete(0, "end")
    display_label.insert(0, temp_exp)
    display_label.config(state="disabled")

def handle_equals():
    global expression
    res=evaluate_expression()
    expression=str(res)
    update_entry()

def handle_button_click(op):
    build_expression(op)
    update_entry()

def handle_clear():
    global expression
    expression="0"
    update_entry()

update_entry()

# Buttons
# First row
button9 = Button(text=9, width=5, command=lambda: handle_button_click(9))
button9.grid(row=1, column=0, padx=10, pady=10)

button8 = Button(text=8, width=5, command=lambda: handle_button_click(8))
button8.grid(row=1, column=1, padx=10, pady=10)


button7 = Button(text=7, width=5, command=lambda: handle_button_click(7))
button7.grid(row=1, column=2, padx=10, pady=10)

button_addition = Button(text="+", width=5, command=lambda: handle_button_click("+"))
button_addition.grid(row=1, column=3, padx=10, pady=10)

# Second row
button6 = Button(text=6, width=5, command=lambda: handle_button_click(6))
button6.grid(row=2, column=0, padx=10, pady=10)

button5 = Button(text=5, width=5, command=lambda: handle_button_click(5))
button5.grid(row=2, column=1, padx=10, pady=10)

button4 = Button(text=4, width=5, command=lambda: handle_button_click(4))
button4.grid(row=2, column=2, padx=10, pady=10)

button_subtraction = Button(text="-", width=5, command=lambda: handle_button_click("-"))
button_subtraction.grid(row=2, column=3, padx=10, pady=10)

# Third row
button3 = Button(text=3, width=5, command=lambda: handle_button_click(3))
button3.grid(row=3, column=0, padx=10, pady=10)

button2 = Button(text=2, width=5, command=lambda: handle_button_click(2))
button2.grid(row=3, column=1, padx=10, pady=10)

button1 = Button(text=1, width=5, command=lambda: handle_button_click(1))
button1.grid(row=3, column=2, padx=10, pady=10)

button_multiplication = Button(text="x", width=5, command=lambda: handle_button_click("*"))
button_multiplication.grid(row=3, column=3, padx=10, pady=10)

# Last row
button_clear = Button(text="clear", width=5, command=lambda: handle_clear())
button_clear.grid(row=4, column=0, padx=10, pady=10)

button0 = Button(text=0, width=5, command=lambda: handle_button_click(0))
button0.grid(row=4, column=1, padx=10, pady=10)

button_division = Button(text="/", width=5, command=lambda: handle_button_click("/"))
button_division.grid(row=4, column=2, padx=10, pady=10)

button_equals = Button(text="=", width=5, command=lambda: handle_equals())
button_equals.grid(row=4, column=3, padx=10, pady=10)

# Start the main loop.
window.mainloop()