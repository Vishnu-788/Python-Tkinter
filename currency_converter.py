import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Clock")
window.geometry("600x300")

main_frame = ttk.Frame(window)
main_frame.pack(expand=True, fill="x", anchor="center")

main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_rowconfigure(1, weight=1)

main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(2, weight=1)

# Currency options
DOLLAR = "dollar"
RUPEE = "rupee"
EURO = "euro"

curr_val = [DOLLAR, RUPEE, EURO]

input_currency_label = ttk.Label(main_frame, text="Enter the amount.", font=("Times New Roman", 20))
input_currency_label.grid(row=0, column=0)
intput_currency_entry = ttk.Entry(main_frame, font=("Times New Roman", 20))
intput_currency_entry.grid(row=1, column=0, columnspan=2)

selected_input_currency = tk.StringVar(value=RUPEE)

input_currency_dropdown = ttk.Combobox(
    main_frame,
    state="readonly",
    textvariable=selected_input_currency,
    values=curr_val,
    width=10
)
input_currency_dropdown.grid(row=0, column=1, padx=3)

output_currency_label = ttk.Label(main_frame, text="Money", font=("Times New Roman", 20))
output_currency_label.grid(row=0, column=2, padx=3)
output_currency_entry = ttk.Entry(main_frame, font=("Times New Roman", 20))
output_currency_entry.grid(row=1, column=2, padx=3, columnspan=2)

selected_output_currency = tk.StringVar(value=DOLLAR)

output_currency_dropdown = ttk.Combobox(
    main_frame,
    textvariable=selected_output_currency,
    state="readonly",
    values=curr_val,
    width=10
)
output_currency_dropdown.grid(row=0, column=3, padx=3)

rates = {
    # Dollar ↔ Rupee
    ('DOLLAR', 'RUPEE'): 84.0,
    ('RUPEE', 'DOLLAR'): 0.0119,

    # Dollar ↔ Euro
    ('DOLLAR', 'EURO'): 0.92,
    ('EURO', 'DOLLAR'): 1.09,

    # Rupee ↔ Euro
    ('RUPEE', 'EURO'): 0.011,
    ('EURO', 'RUPEE'): 91.0,
}


def convert(amount, from_cur, to_cur):
    return amount * rates.get((from_cur, to_cur), 1)


def handle_convert_currency():
    output_currency_entry.config(state="normal")

    from_curr = selected_input_currency.get().upper()
    to_curr = selected_output_currency.get().upper()
    from_amount = float(intput_currency_entry.get())

    convt_amount=convert(from_amount, from_curr, to_curr)
    output_currency_entry.delete(0, tk.END)
    output_currency_entry.insert(0, convt_amount)
    output_currency_entry.config(state="readonly")

output_currency_entry.config(state="readonly")

convert_button = ttk.Button(main_frame, text="CONVERT", command=handle_convert_currency)
convert_button.grid(row=2, column=0, columnspan=4, pady=10)

window.mainloop()





