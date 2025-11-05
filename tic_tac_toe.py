import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Tic Tac Toe")
window.geometry("400x450")
window.resizable(False, False)

current_player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]

def check_winner():
    # Check rows, columns, diagonals
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False

def is_draw():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True

def on_click(r, c):
    global current_player
    if buttons[r][c]["text"] == "":
        buttons[r][c]["text"] = current_player
        buttons[r][c]["state"] = "disabled"

        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_board()
            return

        if is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
            return

        current_player = "O" if current_player == "X" else "X"

def reset_board():
    global current_player
    current_player = "X"
    for r in range(3):
        for c in range(3):
            buttons[r][c]["text"] = ""
            buttons[r][c]["state"] = "normal"

def make_board():
    frame = tk.Frame(window)
    frame.pack(pady=30)

    for r in range(3):
        for c in range(3):
            btn = tk.Button(
                frame,
                text="",
                font=("Times New Roman", 32, "bold"),
                width=3,
                height=1,
                command=lambda r=r, c=c: on_click(r, c)
            )
            btn.grid(row=r, column=c, padx=5, pady=5)
            buttons[r][c] = btn

    reset_btn = tk.Button(window, text="Reset Game", font=("Times New Roman", 14), command=reset_board)
    reset_btn.pack(pady=10)

make_board()
window.mainloop()
