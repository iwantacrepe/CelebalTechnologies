import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from itertools import groupby


# ------------ Functions for Concepts ------------
def run_conditionals():
    try:
        num = int(entry_input.get())
        if num > 0:
            result = "Positive Number"
        elif num < 0:
            result = "Negative Number"
        else:
            result = "Zero"
        output_label.config(text=result)
    except:
        output_label.config(text="Please enter a valid number")


def run_arithmetic():
    try:
        x, y = map(int, entry_input.get().split())
        result = f"Add: {x+y}, Sub: {x-y}, Mul: {x*y}, Div: {x/y:.2f}"
        output_label.config(text=result)
    except:
        output_label.config(text="Enter 2 numbers separated by space")


def run_compress_string():
    s = entry_input.get()
    result = ' '.join(f"({len(list(g))}, '{k}')" for k, g in groupby(s))
    output_label.config(text=result)


def run_write_function():
    try:
        n = int(entry_input.get())
        def factorial(x):
            return 1 if x == 0 else x * factorial(x-1)
        output_label.config(text=f"{n}! = {factorial(n)}")
    except:
        output_label.config(text="Enter a valid integer")


# ------------ Main App Window ------------
app = tk.Tk()
app.title("Python Learning App")
app.geometry("500x400")
app.resizable(False, False)

style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 10))
style.configure("TLabel", font=("Segoe UI", 11))

# ------------ UI Elements ------------
title_label = ttk.Label(app, text="Python Concepts Explorer", font=("Segoe UI", 14, "bold"))
title_label.pack(pady=10)

entry_input = ttk.Entry(app, width=40)
entry_input.pack(pady=10)

button_frame = ttk.Frame(app)
button_frame.pack(pady=10)

ttk.Button(button_frame, text="Conditionals", command=run_conditionals).grid(row=0, column=0, padx=5, pady=5)
ttk.Button(button_frame, text="Arithmetic", command=run_arithmetic).grid(row=0, column=1, padx=5, pady=5)
ttk.Button(button_frame, text="Compress String", command=run_compress_string).grid(row=1, column=0, padx=5, pady=5)
ttk.Button(button_frame, text="Factorial", command=run_write_function).grid(row=1, column=1, padx=5, pady=5)

output_label = ttk.Label(app, text="Output will appear here", wraplength=450)
output_label.pack(pady=20)

# ------------ Run the App ------------
app.mainloop()
