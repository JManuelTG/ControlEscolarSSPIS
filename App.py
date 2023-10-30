from tkinter import *
import tkinter as tk
import ttkbootstrap as ttk

class ControlEscolar:
    def __init__(self, root):
        self.root = root
        self.root.title("Control Escolar")
        self.root.geometry("1080x720")
        self.root.iconbitmap("Escuela.ico")
        
        # Inicialmente, las pestañas estarán bloqueadas
        self.tabs_enabled = False
        self.users = {
            "admin" : "admin",
            "teacher" : "teacher",
            "student" : "student"
        }

        self.create_widgets()

    def create_widgets(self):
        
        # Crear un controlador de pestañas
        self.tab_control = ttk.Notebook(self.root, bootstyle="secondary")
        
        # Pestaña de Login
        self.login_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.login_tab, text='Login')
        
        # Elementos en la pestaña de Login
        self.username_label = tk.Label(self.login_tab, text="Usuario:")
        self.username_label.pack(pady=10)
        self.username_entry = tk.Entry(self.login_tab)
        self.username_entry.pack()
        
        self.password_label = tk.Label(self.login_tab, text="Contraseña:")
        self.password_label.pack(pady=10)
        self.password_entry = tk.Entry(self.login_tab, show="*")
        self.password_entry.pack()
        
        self.login_button = ttk.Button(self.login_tab, text="Iniciar Sesión", command=self.login, bootstyle="success")
        self.login_button.pack(pady=20)
        
        self.status_label = tk.Label(self.login_tab, text="", fg="red")
        self.status_label.pack()
        
        # Pestañas adicionales (inicialmente deshabilitadas)
        self.tabs = {
            " Usuarios ": ttk.Frame(self.tab_control),
            " Alumnos  ": ttk.Frame(self.tab_control),
            " Maestros ": ttk.Frame(self.tab_control),
            " Materias ": ttk.Frame(self.tab_control),
            "  Grupos  ": ttk.Frame(self.tab_control),
            " Horarios ": ttk.Frame(self.tab_control),
            "  Salon   ": ttk.Frame(self.tab_control),
            " Carrera  ": ttk.Frame(self.tab_control),
            "Planeacion": ttk.Frame(self.tab_control),
        }
        
        for tab_name, tab_frame in self.tabs.items():
            self.tab_control.add(tab_frame, text=tab_name, padding=40)
            self.tab_control.tab(tab_frame, state="disabled")
        
        # Empacar el controlador de pestañas
        self.tab_control.pack(expand=True, fill=tk.BOTH,)  # Ajustar al tamaño de la ventana

    def login(self):
        username = self.username_entry.get().lower()
        password = self.password_entry.get()
        
        # Verificar el inicio de sesión y establecer el rol del usuario
        if username in self.users and password == self.users[username]:
            self.current_user_role = username
            self.enable_tabs_for_role(username)
            self.status_label.config(text="Inicio de sesión exitoso")
        else:
            self.status_label.config(text="Credenciales incorrectas")

    def enable_tabs_for_role(self, role):
        tabs_to_disable = []

        if role == "teacher":
            tabs_to_disable = ["Alumnos", "Usuarios" ,"Materias", "Grupos", "Horarios", "Salon", "Carrera", "Planeacion"]
        elif role == "student":
            tabs_to_disable = ["Usuarios", "Maestros", "Materias", "Grupos", "Horarios", "Salon", "Carrera", "Planeacion"]
        for tab_name, tab_frame in self.tabs.items():
            state = "normal" if tab_name not in tabs_to_disable else "disabled"
            self.tab_control.tab(tab_frame, state=state)
    
    def users_tab(self):
        # Elementos en la pestaña de usuarios
        users_frame = self.tabs["Usuarios"]
    
    def student_tab(self):
        # Elementos en la pestaña de alumnos
        students_frame = self.tabs["Alumnos"]
    
    def tacher_tab(self):
        # Elementos en la pestaña de maestros
        teachers_frame = self.tabs["Maestros"]
    
    def groups_tab(self):
        # Elementos en la pestaña de grupos
        grupus_frame = self.tabs["Grupos"]
    
    def schedule_tab(self):
        # Elementos en la pestaña de horarios
        schedule_frame = self.tabs["Horarios"]
    
    def lounge_tab(self):
        # Elementos en la pestaña de salon
        lounge_frame = self.tabs["Salon"]
    
    def career_tab(self):
        # Elementos en la pestaña de Carrera
        career_frame = self.tabs["Carrera"]
    
    def plannig_tab(self):
        # Elementos en la pestaña de planeacion
        plannig_frame = self.tabs["Planeacion"]

