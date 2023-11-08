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
            "admin": {
                "pwd": "admin",
                "type": "admin",
                "ID": "",
                "name":"",
                "lastname": "",
                "middlename": "",
                "mail": "",
            },
            "teacher": {
                "pwd": "teacher",
                "type": "teacher",
                "ID": "",
                "name":"name",
                "lastname": "",
                "middlename": "",
                "mail": "",
            },
            "student": {
                "pwd": "student",
                "type": "student",
                "ID": "1212",
                "name":"Manuel",
                "lastname": "Gomez",
                "middlename": "Tarula",
                "mail": "test@mail.com",
            }
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
            "Usuarios": ttk.Frame(self.tab_control),
            "Alumnos": ttk.Frame(self.tab_control),
            "Maestros": ttk.Frame(self.tab_control),
            "Materias": ttk.Frame(self.tab_control),
            "Grupos": ttk.Frame(self.tab_control),
            "Horarios": ttk.Frame(self.tab_control),
            "Salon": ttk.Frame(self.tab_control),
            "Carrera": ttk.Frame(self.tab_control),
            "Planeacion": ttk.Frame(self.tab_control),
        }

        for tab_name, tab_frame in self.tabs.items():
            self.tab_control.add(tab_frame, text=tab_name, padding=40)
            self.tab_control.tab(tab_frame, state="disabled")

        # Empacar el controlador de pestañas
        self.tab_control.pack(expand=True, fill=tk.BOTH,)

    def login(self):
        username = self.username_entry.get().lower()
        password = self.password_entry.get()

        # Verificar el inicio de sesión y establecer el rol del usuario
        if username in self.users and password == self.users[username]["pwd"]:
            self.current_user_role = self.users[username]["type"]
            self.enable_tabs_for_role(self.users[username]["type"])
            self.status_label.config(text="Inicio de sesión exitoso")
        else:
            self.status_label.config(text="Credenciales incorrectas")
    
    def enable_tabs_for_role(self, role):
        for tab_frame in self.tabs.values():
            self.tab_control.tab(tab_frame, state="disabled")
        
        if role == "teacher":
            self.tab_control.tab(self.tabs["Maestros"], state="normal")
            self.teacher_tab()
        elif role == "student":
            self.tab_control.tab(self.tabs["Alumnos"], state="normal")
            self.student_tab()
        elif role == "admin":
            for tab_frame in self.tabs.values():
                self.tab_control.tab(tab_frame, state="normal")
            self.users_tab()
            self.teacher_tab()
            self.student_tab()
            self.groups_tab()
            self.schedule_tab()
            self.lounge_tab()
            self.career_tab()
            self.plannig_tab()
                
    def users_tab(self):
        # Elementos en la pestaña de usuarios
        users_frame = self.tabs["Usuarios"]

        self.find_user_label = tk.Label(users_frame, text="Ingrese codigo de usuario: ")
        self.find_user_label.grid(column=2, row=1)
        
        self.find_user_entry = tk.Entry(users_frame)
        self.find_user_entry.grid(column=8, row=1, padx=40)
        
        self.find_user_button = ttk.Button(users_frame, text="Buscar", command=self.find_user, bootstyle="success")
        self.find_user_button.grid(column=12, row=1)

        ttk.Separator(users_frame, orient='horizontal').grid(row=2, columnspan=1000, sticky="ew", pady=20)
        
        # Label y cuadro de texto para "ID"
        id_label = tk.Label(users_frame, text="ID:")
        id_label.grid(column=2, row=4, pady=10)
        id_entry = tk.Entry(users_frame)
        id_entry.grid(column=8, row=4, padx=40, pady=10)

        # Label y cuadro de texto para "Nombre de usuario"
        username_label = tk.Label(users_frame, text="Nombre de usuario:")
        username_label.grid(column=2, row=6, pady=10)
        username_entry = tk.Entry(users_frame)
        username_entry.grid(column=8, row=6, padx=40, pady=10)

        # Label y cuadro de texto para "Nombre"
        name_label = tk.Label(users_frame, text="Nombre:")
        name_label.grid(column=2, row=8, pady=10)
        name_entry = tk.Entry(users_frame)
        name_entry.grid(column=8, row=8, padx=40, pady=10)

        # Label y cuadro de texto para "Apellido paterno"
        last_name_label = tk.Label(users_frame, text="Apellido paterno:")
        last_name_label.grid(column=2, row=10, pady=10)
        last_name_entry = tk.Entry(users_frame)
        last_name_entry.grid(column=8, row=10, padx=40, pady=10)

        # Label y cuadro de texto para "Apellido materno"
        mother_name_label = tk.Label(users_frame, text="Apellido materno:")
        mother_name_label.grid(column=2, row=12, pady=10)
        mother_name_entry = tk.Entry(users_frame)
        mother_name_entry.grid(column=8, row=12, padx=40, pady=10)

        # Label y cuadro de texto para "Contraseña"
        password_label = tk.Label(users_frame, text="Contraseña:")
        password_label.grid(column=2, row=13, pady=10)
        password_entry = tk.Entry(users_frame, show="*")
        password_entry.grid(column=8, row=13, padx=40, pady=10)

        # Label y cuadro de texto para "Email"
        email_label = tk.Label(users_frame, text="Email:")
        email_label.grid(column=2, row=14, pady=10)
        email_entry = tk.Entry(users_frame)
        email_entry.grid(column=8, row=14, padx=40, pady=10)

        # Label y cuadro de texto para "Tipo de usuario" (puedes usar una lista desplegable)
        user_type_label = tk.Label(users_frame, text="Tipo de usuario:")
        user_type_label.grid(column=2, row=16, pady=10)
        
        user_types = ["Admin", "Maestro", "Alumno"]  # Opciones para el tipo de usuario
        user_type_var = ttk.StringVar(users_frame)
        user_type_var.set(user_types[0])  # Valor predeterminado
        user_type_dropdown = tk.OptionMenu(users_frame, user_type_var, *user_types)
        user_type_dropdown.grid(column=8, row=16, pady=10)

        # Botón para agregar el usuario
        add_user_button = ttk.Button(users_frame, text="Nuevo", command=self.add_user, bootstyle="success")
        add_user_button.grid(column=2, row=20, columnspan=2, pady=20, padx=10)
    
        # Botón para agregar el usuario
        add_user_button = ttk.Button(users_frame, text="Guardar", command=self.add_user, bootstyle="success")
        add_user_button.grid(column=4, row=20, columnspan=2, pady=20, padx=10)
    
        # Botón para agregar el usuario
        add_user_button = ttk.Button(users_frame, text="Cancelar", command=self.add_user, bootstyle="success")
        add_user_button.grid(column=6, row=20, columnspan=2, pady=20, padx=10)
        
        # Botón para agregar el usuario
        add_user_button = ttk.Button(users_frame, text="Editar", command=self.add_user, bootstyle="success")
        add_user_button.grid(column=8, row=20, columnspan=2, pady=20, padx=10)
        
        # Botón para agregar el usuario
        add_user_button = ttk.Button(users_frame, text="Baja", command=self.add_user, bootstyle="success")
        add_user_button.grid(column=10, row=20, columnspan=2, pady=20, padx=10)
    
    def find_user(self):
        pass

    def add_user(self):
        pass
    
    def student_tab(self):
        # Elementos en la pestaña de alumnos
        students_frame = self.tabs["Alumnos"]
    
    def teacher_tab(self):
        # Elementos en la pestaña de maestros
        teachers_frame = self.tabs["Maestros"]
        teacher_label = tk.Label(teachers_frame, text="Bienvenido, Maestro")
        teacher_label.pack(pady=20)
        teacher_textbox = tk.Entry(teachers_frame)
        teacher_textbox.pack()
    
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