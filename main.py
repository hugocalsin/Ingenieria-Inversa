# main.py
import tkinter as tk
from auth import show_login
from calculator import show_calculator

# Crear la ventana
root = tk.Tk()
root.title("Calculadora con Registro")
root.geometry("300x400")

# Mostrar la pantalla de login por defecto
show_login(root, show_calculator)

#Se lanza 
root.mainloop()
