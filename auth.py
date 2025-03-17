import tkinter as tk
from tkinter import messagebox
import json

def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file)

users = load_users()  # Definir users como una variable global

def register_user(username_var, password_var, login_frame, register_frame):
    username = username_var.get()
    password = password_var.get()
    if username and password:
        users[username] = password
        save_users(users)
        messagebox.showinfo("Registro", "Usuario registrado exitosamente")
        login_frame.pack()
        register_frame.pack_forget()
    else:
        messagebox.showerror("Error", "Ingrese un usuario y contraseña válidos")

def login_user(login_username_var, login_password_var, users,login_frame, root,show_calculator):
    username = login_username_var.get()
    password = login_password_var.get()
    if username in users and users[username] == password:
        messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso")
        login_frame.pack_forget()
        show_calculator(root)
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

def show_register(root, users, login_frame, register_frame, show_login):
    register_frame.pack()
    login_frame.pack_forget()

def show_login(root, show_calculator):
    global users  # Para asegurar que se usa la variable global

    username_var = tk.StringVar()
    password_var = tk.StringVar()
    login_username_var = tk.StringVar()
    login_password_var = tk.StringVar()
    
    login_frame = tk.Frame(root)
    register_frame = tk.Frame(root)
    
    tk.Label(login_frame, text="Inicio de Sesión", font=("Arial", 14)).pack()
    tk.Label(login_frame, text="Usuario:").pack()
    tk.Entry(login_frame, textvariable=login_username_var).pack()
    tk.Label(login_frame, text="Contraseña:").pack()
    tk.Entry(login_frame, textvariable=login_password_var, show="*").pack()
    tk.Button(login_frame, text="Iniciar Sesión", command=lambda: login_user(login_username_var, login_password_var, users, login_frame, root, show_calculator)).pack()
    tk.Button(login_frame, text="Ir a Registro", command=lambda: show_register(root, login_frame, register_frame, show_login)).pack()
    
    tk.Label(register_frame, text="Registro", font=("Arial", 14)).pack()
    tk.Label(register_frame, text="Usuario:").pack()
    tk.Entry(register_frame, textvariable=username_var).pack()
    tk.Label(register_frame, text="Contraseña:").pack()
    tk.Entry(register_frame, textvariable=password_var, show="*").pack()
    tk.Button(register_frame, text="Registrar", command=lambda: register_user(username_var, password_var, login_frame, register_frame)).pack()
    tk.Button(register_frame, text="Ir a Login", command=lambda: show_login(root, show_calculator)).pack()
    
    login_frame.pack()