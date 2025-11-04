import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Temperature conversion.")
window.geometry("600x200")

main_frame = ttk.Frame(window)
main_frame.pack(fill="x", expand=True)

main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

temp_label = ttk.Label(main_frame, text="Enter your temperature in here.", font=("Times New Roman", 16))
temp_label.grid(row=0, column=0, padx=5)
temp_entry = ttk.Entry(main_frame, font=("Times New Roman", 16))
temp_entry.grid(row=1, column=0, padx=5, sticky="ew")

convert_label = ttk.Label(main_frame, text="Converted to Celsius", font=("Times New Roman", 16))
convert_label.grid(row=0, column=1, padx=5)
convert_entry = ttk.Entry(main_frame, font=("Times New Roman", 16))
convert_entry.grid(row=1, column=1, padx=5, sticky="ew")

def insert_temp(val):
    convert_entry.delete(0, tk.END)
    value = f"{val} C"
    convert_entry.insert(0, value)

def handle_convert():
    f_temp = int(temp_entry.get())
    c_temp = convert_f_to_c(f_temp)
    insert_temp(c_temp)

convert_button = ttk.Button(main_frame, text="CONVERT", command=handle_convert)
convert_button.grid(row=2, column=0, columnspan=2, pady=10)


def convert_f_to_c(temp):
    return (temp - 32) / 1.8

window.mainloop()
