# calculator.py
import tkinter as tk
from tkinter import messagebox

def on_click(button_text, entry_var):
    if button_text == "C":
        entry_var.set("")
    elif button_text == "=":
        try:
            result = eval(entry_var.get())
            entry_var.set(result)
        except Exception:
            messagebox.showerror("Error", "Entrada inválida")
            entry_var.set("")
    else:
        entry_var.set(entry_var.get() + button_text)

def show_calculator(root):
    calculator_frame = tk.Frame(root)
    entry_var = tk.StringVar()
    entry = tk.Entry(calculator_frame, textvariable=entry_var, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify='right')
    entry.pack(fill="both")
    
    buttons = [
        ('7', '8', '9', '/'),
        ('4', '5', '6', '*'),
        ('1', '2', '3', '-'),
        ('C', '0', '=', '+')
    ]
    
    frame = tk.Frame(calculator_frame)
    frame.pack()
    
    for row in buttons:
        row_frame = tk.Frame(frame)
        row_frame.pack(fill="both", expand=True)
        for button_text in row:
            button = tk.Button(row_frame, text=button_text, font=("Arial", 18), 
                               command=lambda bt=button_text: on_click(bt, entry_var))
            button.pack(side="left", fill="both", expand=True)
    
    calculator_frame.pack()
