from tkinter import *
import tkinter as tk
import ttkbootstrap as ttk
from Connection import PostgresDBConnection

class ControlEscolar:

    def __init__(self, root):
        self.root = root
        self.root.title("Control Escolar")
        self.root.geometry("750x720")
        self.root.iconbitmap("Escuela.ico")
        self.connection = PostgresDBConnection(
            host="localhost",
            database="ControlEscolar",
            user="postgres",
            password="Loquesea24.,."
        )
        
        # Inicialmente, las pestañas estarán bloqueadas
        self.tabs_enabled = False

        self.users = {
            "admin": "admin",
            "teacher": "teacher",
            "student": "student"
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
        if username in self.users and password == self.users[username]:
            self.current_user_role = username
            self.enable_tabs_for_role(username)
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
            self.usuarios_tab()
            self.maestros_tab()
            self.alumnos_tab()
            self.grupos_tab()
            self.materias_tab()
            self.horarios_tab()
            self.salon_tab()
            self.carrera_tab()
            self.planeacion_tab()
                
    def usuarios_tab(self):
        # Elementos en la pestaña de usuarios
        users_frame = self.tabs["Usuarios"]

        # Label para "Ingrese código de usuario"
        codigo_usuario_label = tk.Label(users_frame, text="Ingrese código de usuario:")
        codigo_usuario_label.grid(column=2, row=1)

        # Cuadro de texto para ingresar el código de usuario
        codigo_usuario_entry = tk.Entry(users_frame)
        codigo_usuario_entry.grid(column=8, row=1, padx=40)

        # Botón de búsqueda
        buscar_button = ttk.Button(users_frame, text="Buscar", command=self.busca, bootstyle="success")
        buscar_button.grid(column=12, row=1)

        # Separador horizontal
        ttk.Separator(users_frame, orient='horizontal').grid(row=2, columnspan=1000, sticky="ew", pady=20)

        # Labels y cuadros de texto para información del usuario
        id_label = tk.Label(users_frame, text="ID:")
        id_label.grid(column=2, row=4, pady=10)
        id_entry = tk.Entry(users_frame)
        id_entry.grid(column=8, row=4, padx=40, pady=10)

        username_label = tk.Label(users_frame, text="Nombre de usuario:")
        username_label.grid(column=2, row=6, pady=10)
        username_entry = tk.Entry(users_frame)
        username_entry.grid(column=8, row=6, padx=40, pady=10)

        nombre_label = tk.Label(users_frame, text="Nombre:")
        nombre_label.grid(column=2, row=8, pady=10)
        nombre_entry = tk.Entry(users_frame)
        nombre_entry.grid(column=8, row=8, padx=40, pady=10)

        apellido_paterno_label = tk.Label(users_frame, text="Apellido paterno:")
        apellido_paterno_label.grid(column=2, row=10, pady=10)
        apellido_paterno_entry = tk.Entry(users_frame)
        apellido_paterno_entry.grid(column=8, row=10, padx=40, pady=10)

        apellido_materno_label = tk.Label(users_frame, text="Apellido materno:")
        apellido_materno_label.grid(column=2, row=12, pady=10)
        apellido_materno_entry = tk.Entry(users_frame)
        apellido_materno_entry.grid(column=8, row=12, padx=40, pady=10)

        password_label = tk.Label(users_frame, text="Contraseña:")
        password_label.grid(column=2, row=13, pady=10)
        password_entry = tk.Entry(users_frame, show="*")
        password_entry.grid(column=8, row=13, padx=40, pady=10)

        email_label = tk.Label(users_frame, text="Email:")
        email_label.grid(column=2, row=14, pady=10)
        email_entry = tk.Entry(users_frame)
        email_entry.grid(column=8, row=14, padx=40, pady=10)

        tipo_usuario_label = tk.Label(users_frame, text="Tipo de usuario:")
        tipo_usuario_label.grid(column=2, row=16, pady=10)
        
        tipos_usuario = ["Admin", "Maestro", "Alumno"]  # Opciones para el tipo de usuario
        
        tipo_usuario_var = ttk.StringVar(users_frame)
        tipo_usuario_var.set(tipos_usuario[0])  # Valor predeterminado
        tipo_usuario_dropdown = tk.OptionMenu(users_frame, tipo_usuario_var, *tipos_usuario)
        tipo_usuario_dropdown.grid(column=8, row=16, pady=10)

        # Botones para realizar acciones
        nuevo_button = ttk.Button(users_frame, text="Nuevo", command=self.busca, bootstyle="success")
        nuevo_button.grid(column=2, row=20, columnspan=2, pady=20, padx=10)

        guardar_button = ttk.Button(users_frame, text="Guardar", command=self.busca, bootstyle="success")
        guardar_button.grid(column=4, row=20, columnspan=2, pady=20, padx=10)

        cancelar_button = ttk.Button(users_frame, text="Cancelar", command=self.busca, bootstyle="success")
        cancelar_button.grid(column=6, row=20, columnspan=2, pady=20, padx=10)

        editar_button = ttk.Button(users_frame, text="Editar", command=self.busca, bootstyle="success")
        editar_button.grid(column=8, row=20, columnspan=2, pady=20, padx=10)

        baja_button = ttk.Button(users_frame, text="Baja", command=self.busca, bootstyle="success")
        baja_button.grid(column=10, row=20, columnspan=2, pady=20, padx=10)

    def alumnos_tab(self):
        # Elementos en la pestaña de alumnos
        students_frame = self.tabs["Alumnos"]

        # Label para "Ingrese código de alumno"
        codigo_alumno_label = tk.Label(students_frame, text="Ingrese código de alumno:")
        codigo_alumno_label.grid(column=2, row=1)

        # Cuadro de texto para ingresar el código del alumno
        codigo_alumno_entry = tk.Entry(students_frame)
        codigo_alumno_entry.grid(column=8, row=1, padx=40)

        # Botón de búsqueda
        buscar_button = ttk.Button(students_frame, text="Buscar", command=self.busca, bootstyle="success")
        buscar_button.grid(column=12, row=1)

        # Separador horizontal
        ttk.Separator(students_frame, orient='horizontal').grid(row=2, columnspan=1000, sticky="ew", pady=20)

        # Labels y cuadros de texto para información del alumno
        id_label = tk.Label(students_frame, text="ID:")
        id_label.grid(column=2, row=4, pady=10)
        id_entry = tk.Entry(students_frame)
        id_entry.grid(column=8, row=4, padx=40, pady=10)

        nombre_label = tk.Label(students_frame, text="Nombre:")
        nombre_label.grid(column=2, row=8, pady=10)
        nombre_entry = tk.Entry(students_frame)
        nombre_entry.grid(column=8, row=8, padx=40, pady=10)

        apellido_paterno_label = tk.Label(students_frame, text="Apellido paterno:")
        apellido_paterno_label.grid(column=2, row=10, pady=10)
        apellido_paterno_entry = tk.Entry(students_frame)
        apellido_paterno_entry.grid(column=8, row=10, padx=40, pady=10)

        apellido_materno_label = tk.Label(students_frame, text="Apellido materno:")
        apellido_materno_label.grid(column=2, row=12, pady=10)
        apellido_materno_entry = tk.Entry(students_frame)
        apellido_materno_entry.grid(column=8, row=12, padx=40, pady=10)

        carrera_label = tk.Label(students_frame, text="Carrera:")
        carrera_label.grid(column=2, row=13, pady=10)
        carreras = ["Ingenieria en Computacion", "Ingenieria en Informatica"]
        carrera_var = ttk.StringVar(students_frame)
        carrera_var.set(carreras[0])  # Valor predeterminado
        carrera_dropdown = tk.OptionMenu(students_frame, carrera_var, *carreras)
        carrera_dropdown.grid(column=8, row=13, pady=10)

        fecha_nacimiento_label = tk.Label(students_frame, text="Fecha de Nacimiento:")
        fecha_nacimiento_label.grid(column=2, row=14, pady=10)
        fecha_nacimiento_entry = tk.Entry(students_frame, show="*")
        fecha_nacimiento_entry.grid(column=8, row=14, padx=40, pady=10)

        email_label = tk.Label(students_frame, text="Email:")
        email_label.grid(column=2, row=15, pady=10)
        email_entry = tk.Entry(students_frame)
        email_entry.grid(column=8, row=15, padx=40, pady=10)

        estado_label = tk.Label(students_frame, text="Estado:")
        estado_label.grid(column=2, row=17, pady=10)
        
        states = [
            "Aguascalientes",
            "Baja California",
            "Baja California Sur",
            "Campeche",
            "Chiapas",
            "Chihuahua",
            "Coahuila",
            "Colima",
            "Durango",
            "Guanajuato",
            "Guerrero",
            "Hidalgo",
            "Jalisco",
            "Estado de México",
            "Ciudad de México",
            "Michoacán",
            "Morelos",
            "Nayarit",
            "Nuevo León",
            "Oaxaca",
            "Puebla",
            "Querétaro",
            "Quintana Roo",
            "San Luis Potosí",
            "Sinaloa",
            "Sonora",
            "Tabasco",
            "Tamaulipas",
            "Tlaxcala",
            "Veracruz",
            "Yucatán",
            "Zacatecas"
        ]
        
        estado_var = ttk.StringVar(students_frame)
        estado_var.set(states[0])  # Valor predeterminado
        estado_dropdown = tk.OptionMenu(students_frame, estado_var, *states)
        estado_dropdown.grid(column=8, row=17, pady=10)

        materias_label = tk.Label(students_frame, text="Materias:")
        materias_label.grid(column=2, row=16, pady=10)
        
        materias = [
            "Física 1",
            "Programación Estructurada",
            "Estructura de Datos",
            "Inteligencia Artificial",
            "Ingeniería de Software 1"
        ]
        
        materias_var = ttk.StringVar(students_frame)
        materias_var.set(materias[0])  # Valor predeterminado
        materias_dropdown = tk.OptionMenu(students_frame, materias_var, *materias)
        materias_dropdown.grid(column=8, row=16, pady=10)

        # Botones para realizar acciones
        nuevo_button = ttk.Button(students_frame, text="Nuevo", command=self.busca, bootstyle="success")
        nuevo_button.grid(column=2, row=23, columnspan=2, pady=20, padx=10)

        guardar_button = ttk.Button(students_frame, text="Guardar", command=self.busca, bootstyle="success")
        guardar_button.grid(column=4, row=23, columnspan=2, pady=20, padx=10)

        cancelar_button = ttk.Button(students_frame, text="Cancelar", command=self.busca, bootstyle="success")
        cancelar_button.grid(column=6, row=23, columnspan=2, pady=20, padx=10)

        editar_button = ttk.Button(students_frame, text="Editar", command=self.busca, bootstyle="success")
        editar_button.grid(column=8, row=23, columnspan=2, pady=20, padx=10)

        baja_button = ttk.Button(students_frame, text="Baja", command=self.busca, bootstyle="success")
        baja_button.grid(column=10, row=23, columnspan=2, pady=20, padx=10)
    
    def maestros_tab(self):
    # Elementos en la pestaña de maestros
        teachers_frame = self.tabs["Maestros"]
        
        # Label para "Ingrese código del maestro"
        codigo_maestro_label = tk.Label(teachers_frame, text="Ingrese código del maestro:")
        codigo_maestro_label.grid(column=2, row=1)

        # Cuadro de texto para ingresar el código del maestro
        codigo_maestro_entry = tk.Entry(teachers_frame)
        codigo_maestro_entry.grid(column=8, row=1, padx=40)

        # Botón de búsqueda
        buscar_button = ttk.Button(teachers_frame, text="Buscar", command=self.busca, bootstyle="success")
        buscar_button.grid(column=12, row=1)

        # Separador horizontal
        ttk.Separator(teachers_frame, orient='horizontal').grid(row=2, columnspan=1000, sticky="ew", pady=20)

        # Labels y cuadros de texto para información del maestro
        id_label = tk.Label(teachers_frame, text="ID:")
        id_label.grid(column=2, row=4, pady=10)
        id_entry = tk.Entry(teachers_frame)
        id_entry.grid(column=8, row=4, padx=40, pady=10)

        nombre_label = tk.Label(teachers_frame, text="Nombre:")
        nombre_label.grid(column=2, row=8, pady=10)
        nombre_entry = tk.Entry(teachers_frame)
        nombre_entry.grid(column=8, row=8, padx=40, pady=10)

        apellido_paterno_label = tk.Label(teachers_frame, text="Apellido paterno:")
        apellido_paterno_label.grid(column=2, row=10, pady=10)
        apellido_paterno_entry = tk.Entry(teachers_frame)
        apellido_paterno_entry.grid(column=8, row=10, padx=40, pady=10)

        apellido_materno_label = tk.Label(teachers_frame, text="Apellido materno:")
        apellido_materno_label.grid(column=2, row=12, pady=10)
        apellido_materno_entry = tk.Entry(teachers_frame)
        apellido_materno_entry.grid(column=8, row=12, padx=40, pady=10)

        carrera_label = tk.Label(teachers_frame, text="Carrera:")
        carrera_label.grid(column=2, row=13, pady=10)
        carreras = ["Ingenieria en Computacion", "Ingenieria en Informatica"]
        carrera_var = ttk.StringVar(teachers_frame)
        carrera_var.set(carreras[0])  # Valor predeterminado
        carrera_dropdown = tk.OptionMenu(teachers_frame, carrera_var, *carreras)
        carrera_dropdown.grid(column=8, row=13, pady=10)
        
        email_label = tk.Label(teachers_frame, text="Email:")
        email_label.grid(column=2, row=14, pady=10)
        email_entry = tk.Entry(teachers_frame)
        email_entry.grid(column=8, row=14, padx=40, pady=10)

        materias_label = tk.Label(teachers_frame, text="Materias:")
        materias_label.grid(column=2, row=16, pady=10)

        materias = ["Fisica 1", "Programacion Estructurada", "Estructura de Datos", "Inteligencia Artificial", "Ingenieria de Software 1"]
        materias_var = tk.StringVar(teachers_frame)
        materias_var.set(materias[0])
        materias_dropdown = tk.OptionMenu(teachers_frame, materias_var, *materias)
        materias_dropdown.grid(column=8, row=16, pady=10)

        grado_label = tk.Label(teachers_frame, text="Grado de estudios:")
        grado_label.grid(column=2, row=17, pady=10)
        grado_entry = tk.Entry(teachers_frame, show="*")
        grado_entry.grid(column=8, row=17, padx=40, pady=10)

        # Botones
        nuevo_button = ttk.Button(teachers_frame, text="Nuevo", command=self.busca, bootstyle="success")
        nuevo_button.grid(column=2, row=22, columnspan=2, pady=20, padx=10)

        guardar_button = ttk.Button(teachers_frame, text="Guardar", command=self.busca, bootstyle="success")
        guardar_button.grid(column=4, row=22, columnspan=2, pady=20, padx=10)

        cancelar_button = ttk.Button(teachers_frame, text="Cancelar", command=self.busca, bootstyle="success")
        cancelar_button.grid(column=6, row=22, columnspan=2, pady=20, padx=10)

        editar_button = ttk.Button(teachers_frame, text="Editar", command=self.busca, bootstyle="success")
        editar_button.grid(column=8, row=22, columnspan=2, pady=20, padx=10)

        baja_button = ttk.Button(teachers_frame, text="Baja", command=self.busca, bootstyle="success")
        baja_button.grid(column=10, row=22, columnspan=2, pady=20, padx=10)
    
    def materias_tab(self):
        # Elementos en la pestaña de materias
        materias_frame = self.tabs["Materias"]
        
        # Label para "Ingrese ID de la materia"
        id_materia_label = tk.Label(materias_frame, text="Ingrese ID de la materia:")
        id_materia_label.grid(column=2, row=1)

        # Cuadro de texto para ingresar el ID de la materia
        id_materia_entry = tk.Entry(materias_frame)
        id_materia_entry.grid(column=8, row=1, padx=40)

        # Botón de búsqueda
        buscar_button = ttk.Button(materias_frame, text="Buscar", command=self.busca, bootstyle="success")
        buscar_button.grid(column=12, row=1)

        # Separador horizontal
        ttk.Separator(materias_frame, orient='horizontal').grid(row=2, columnspan=1000, sticky="ew", pady=20)

        # Labels y cuadros de texto para información de la materia
        asignatura_label = tk.Label(materias_frame, text="Asignatura:")
        asignatura_label.grid(column=2, row=4, pady=10)
        asignatura_entry = tk.Entry(materias_frame)
        asignatura_entry.grid(column=8, row=4, padx=40, pady=10)

        creditos_label = tk.Label(materias_frame, text="Créditos:")
        creditos_label.grid(column=2, row=8, pady=10)
        creditos_entry = tk.Entry(materias_frame)
        creditos_entry.grid(column=8, row=8, padx=40, pady=10)

        semestre_label = tk.Label(materias_frame, text="Semestre:")
        semestre_label.grid(column=2, row=10, pady=10)
        semestre_entry = tk.Entry(materias_frame)
        semestre_entry.grid(column=8, row=10, padx=40, pady=10)

        carrera_label = tk.Label(materias_frame, text="Carrera:")
        carrera_label.grid(column=2, row=12, pady=10)
        carreras = ["Ingenieria en Computacion", "Ingenieria en Informatica"]
        carrera_var = ttk.StringVar(materias_frame)
        carrera_var.set(carreras[0])  # Valor predeterminado
        carrera_dropdown = tk.OptionMenu(materias_frame, carrera_var, *carreras)
        carrera_dropdown.grid(column=8, row=12, pady=10)

        # Botones
        nuevo_button = ttk.Button(materias_frame, text="Nuevo", command=self.busca, bootstyle="success")
        nuevo_button.grid(column=2, row=17, columnspan=2, pady=20, padx=10)

        guardar_button = ttk.Button(materias_frame, text="Guardar", command=self.busca, bootstyle="success")
        guardar_button.grid(column=4, row=17, columnspan=2, pady=20, padx=10)

        cancelar_button = ttk.Button(materias_frame, text="Cancelar", command=self.busca, bootstyle="success")
        cancelar_button.grid(column=6, row=17, columnspan=2, pady=20, padx=10)

        editar_button = ttk.Button(materias_frame, text="Editar", command=self.busca, bootstyle="success")
        editar_button.grid(column=8, row=17, columnspan=2, pady=20, padx=10)

        baja_button = ttk.Button(materias_frame, text="Baja", command=self.busca, bootstyle="success")
        baja_button.grid(column=10, row=17, columnspan=2, pady=20, padx=10)
  
    def grupos_tab(self):
        # Elementos en la pestaña de grupos
        grupus_frame = self.tabs["Grupos"]
    
    def horarios_tab(self):
        # Elementos en la pestaña de Horario
        horario_frame = self.tabs["Horarios"]
        
        # Label para "Ingrese ID de Horario"
        id_horario_label = tk.Label(horario_frame, text="Ingrese ID de Horario:")
        id_horario_label.grid(column=2, row=1)

        # Cuadro de texto para ingresar el ID de horario
        id_horario_entry = tk.Entry(horario_frame)
        id_horario_entry.grid(column=8, row=1, padx=40)

        # Botón de búsqueda
        buscar_button = ttk.Button(horario_frame, text="Buscar", command=self.busca, bootstyle="success")
        buscar_button.grid(column=12, row=1)

        # Separador horizontal
        ttk.Separator(horario_frame, orient='horizontal').grid(row=2, columnspan=1000, sticky="ew", pady=20)

        # Label para "Turno"
        turno_label = tk.Label(horario_frame, text="Turno:")
        turno_label.grid(column=2, row=4, pady=10)
        
        # Cuadro de texto para ingresar el turno
        turno_entry = tk.Entry(horario_frame)
        turno_entry.grid(column=8, row=4, padx=40, pady=10)

        # Label para "Horario"
        horario_label = tk.Label(horario_frame, text="Horario (HH:MM):")
        horario_label.grid(column=2, row=8, pady=10)
        
        # Cuadro de texto para ingresar la hora
        horario_entry = tk.Entry(horario_frame)
        horario_entry.grid(column=8, row=8, padx=40, pady=10)

        # Botones para realizar acciones
        nuevo_button = ttk.Button(horario_frame, text="Nuevo", command=self.busca, bootstyle="success")
        nuevo_button.grid(column=2, row=13, columnspan=2, pady=20, padx=10)

        guardar_button = ttk.Button(horario_frame, text="Guardar", command=self.busca, bootstyle="success")
        guardar_button.grid(column=4, row=13, columnspan=2, pady=20, padx=10)

        cancelar_button = ttk.Button(horario_frame, text="Cancelar", command=self.busca, bootstyle="success")
        cancelar_button.grid(column=6, row=13, columnspan=2, pady=20, padx=10)

        editar_button = ttk.Button(horario_frame, text="Editar", command=self.busca, bootstyle="success")
        editar_button.grid(column=8, row=13, columnspan=2, pady=20, padx=10)

        baja_button = ttk.Button(horario_frame, text="Baja", command=self.busca, bootstyle="success")
        baja_button.grid(column=10, row=13, columnspan=2, pady=20, padx=10)

        
    def salon_tab(self):
        # Elementos en la pestaña de Salones
        salones_frame = self.tabs["Salon"]
        
        # Label para "Ingrese ID de Salón"
        id_salon_label = tk.Label(salones_frame, text="Ingrese ID de Salón:")
        id_salon_label.grid(column=2, row=1)

        # Cuadro de texto para ingresar el ID del salón
        id_salon_entry = tk.Entry(salones_frame)
        id_salon_entry.grid(column=8, row=1, padx=40)

        # Botón de búsqueda
        buscar_button = ttk.Button(salones_frame, text="Buscar", command=self.busca, bootstyle="success")
        buscar_button.grid(column=12, row=1)

        # Separador horizontal
        ttk.Separator(salones_frame, orient='horizontal').grid(row=2, columnspan=1000, sticky="ew", pady=20)

        # Labels y cuadros de texto para información del salón
        nombre_salon_label = tk.Label(salones_frame, text="Nombre de Salón:")
        nombre_salon_label.grid(column=2, row=4, pady=10)
        nombre_salon_entry = tk.Entry(salones_frame)
        nombre_salon_entry.grid(column=8, row=4, padx=40, pady=10)

        edificio_label = tk.Label(salones_frame, text="Edificio:")
        edificio_label.grid(column=2, row=8, pady=10)

        # Opciones para el menú desplegable de edificios de "A" a "Z" en mayúscula
        edificios = [chr(i) for i in range(ord('A'), ord('Z')+1)]

        edificio_var = tk.StringVar(salones_frame)
        edificio_var.set(edificios[0])  # Valor predeterminado
        edificio_dropdown = tk.OptionMenu(salones_frame, edificio_var, *edificios)
        edificio_dropdown.grid(column=8, row=8, pady=10)

        # Botones para realizar acciones
        nuevo_button = ttk.Button(salones_frame, text="Nuevo", command=self.busca, bootstyle="success")
        nuevo_button.grid(column=2, row=13, columnspan=2, pady=20, padx=10)

        guardar_button = ttk.Button(salones_frame, text="Guardar", command=self.busca, bootstyle="success")
        guardar_button.grid(column=4, row=13, columnspan=2, pady=20, padx=10)

        cancelar_button = ttk.Button(salones_frame, text="Cancelar", command=self.busca, bootstyle="success")
        cancelar_button.grid(column=6, row=13, columnspan=2, pady=20, padx=10)

        editar_button = ttk.Button(salones_frame, text="Editar", command=self.busca, bootstyle="success")
        editar_button.grid(column=8, row=13, columnspan=2, pady=20, padx=10)

        baja_button = ttk.Button(salones_frame, text="Baja", command=self.busca, bootstyle="success")
        baja_button.grid(column=10, row=13, columnspan=2, pady=20, padx=10)

    
    def carrera_tab(self):
        # Elementos en la pestaña de Carreras
        carreras_frame = self.tabs["Carrera"]
        
        # Label para "Ingrese ID de Carrera"
        id_carrera_label = tk.Label(carreras_frame, text="Ingrese ID de Carrera:")
        id_carrera_label.grid(column=2, row=1)

        # Cuadro de texto para ingresar el ID de la carrera
        id_carrera_entry = tk.Entry(carreras_frame)
        id_carrera_entry.grid(column=8, row=1, padx=40)

        # Botón de búsqueda
        buscar_button = ttk.Button(carreras_frame, text="Buscar", command=self.busca, bootstyle="success")
        buscar_button.grid(column=12, row=1)

        # Separador horizontal
        ttk.Separator(carreras_frame, orient='horizontal').grid(row=2, columnspan=1000, sticky="ew", pady=20)

        # Labels y cuadros de texto para información de la carrera
        nombre_carrera_label = tk.Label(carreras_frame, text="Nombre de Carrera:")
        nombre_carrera_label.grid(column=2, row=4, pady=10)
        nombre_carrera_entry = tk.Entry(carreras_frame)
        nombre_carrera_entry.grid(column=8, row=4, padx=40, pady=10)

        semestres_label = tk.Label(carreras_frame, text="Número de Semestres:")
        semestres_label.grid(column=2, row=8, pady=10)
        semestres_entry = tk.Entry(carreras_frame)
        semestres_entry.grid(column=8, row=8, padx=40, pady=10)

        materias_label = tk.Label(carreras_frame, text="Materias:")
        materias_label.grid(column=2, row=10, pady=10)
        
        materias = ["Física 1", "Programación Estructurada", "Estructura de Datos", "Inteligencia Artificial", "Ingeniería de Software 1"]
        materias_var = tk.StringVar(carreras_frame)
        materias_var.set(materias[0])  # Valor predeterminado
        materias_dropdown = tk.OptionMenu(carreras_frame, materias_var, *materias)
        materias_dropdown.grid(column=8, row=10, pady=10)

        # Botones para realizar acciones
        nuevo_button = ttk.Button(carreras_frame, text="Nuevo", command=self.busca, bootstyle="success")
        nuevo_button.grid(column=2, row=15, columnspan=2, pady=20, padx=10)

        guardar_button = ttk.Button(carreras_frame, text="Guardar", command=self.busca, bootstyle="success")
        guardar_button.grid(column=4, row=15, columnspan=2, pady=20, padx=10)

        cancelar_button = ttk.Button(carreras_frame, text="Cancelar", command=self.busca, bootstyle="success")
        cancelar_button.grid(column=6, row=15, columnspan=2, pady=20, padx=10)

        editar_button = ttk.Button(carreras_frame, text="Editar", command=self.busca, bootstyle="success")
        editar_button.grid(column=8, row=15, columnspan=2, pady=20, padx=10)

        baja_button = ttk.Button(carreras_frame, text="Baja", command=self.busca, bootstyle="success")
        baja_button.grid(column=10, row=15, columnspan=2, pady=20, padx=10)
        
    def planeacion_tab(self):
        # Elementos en la pestaña de planeacion
        plannig_frame = self.tabs["Planeacion"]

# ===========================================================================
# Metodos usados por la clase
# ===========================================================================

    def busca(self):
        pass