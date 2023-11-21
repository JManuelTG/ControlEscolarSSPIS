from tkinter import *
import tkinter as tk
import ttkbootstrap as ttk
from Connection import PostgresDBConnection
import csv

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
        self.codigo_usuario_entry = tk.Entry(users_frame)
        self.codigo_usuario_entry.grid(column=8, row=1, padx=40)
        
        # Botón de búsqueda
        buscar_button = ttk.Button(users_frame, text="Buscar", command=self.buscar_usuario, bootstyle="success")
        buscar_button.grid(column=12, row=1)

        # Separador horizontal
        ttk.Separator(users_frame, orient='horizontal').grid(row=2, columnspan=1000, sticky="ew", pady=20)

        # Labels y cuadros de texto para información del usuario
        self.usuario_id_label = tk.Label(users_frame, text="ID:")
        self.usuario_id_label.grid(column=2, row=4, pady=10)
        self.usuario_id_entry = tk.Entry(users_frame)
        self.usuario_id_entry.grid(column=8, row=4, padx=40, pady=10)

        self.username_label = tk.Label(users_frame, text="Nombre de usuario:")
        self.username_label.grid(column=2, row=6, pady=10)
        self.username_entry = tk.Entry(users_frame)
        self.username_entry.grid(column=8, row=6, padx=40, pady=10)

        self.usuario_nombre_label = tk.Label(users_frame, text="Nombre:")
        self.usuario_nombre_label.grid(column=2, row=8, pady=10)
        self.usuario_nombre_entry = tk.Entry(users_frame)
        self.usuario_nombre_entry.grid(column=8, row=8, padx=40, pady=10)

        self.usuario_apellido_paterno_label = tk.Label(users_frame, text="Apellido paterno:")
        self.usuario_apellido_paterno_label.grid(column=2, row=10, pady=10)
        self.usuario_apellido_paterno_entry = tk.Entry(users_frame)
        self.usuario_apellido_paterno_entry.grid(column=8, row=10, padx=40, pady=10)

        self.usuario_apellido_materno_label = tk.Label(users_frame, text="Apellido materno:")
        self.usuario_apellido_materno_label.grid(column=2, row=12, pady=10)
        self.usuario_apellido_materno_entry = tk.Entry(users_frame)
        self.usuario_apellido_materno_entry.grid(column=8, row=12, padx=40, pady=10)

        self.usuario_password_label = tk.Label(users_frame, text="Contraseña:")
        self.usuario_password_label.grid(column=2, row=13, pady=10)
        self.usuario_password_entry = tk.Entry(users_frame, show="*")
        self.usuario_password_entry.grid(column=8, row=13, padx=40, pady=10)

        self.usuario_email_label = tk.Label(users_frame, text="Email:")
        self.usuario_email_label.grid(column=2, row=14, pady=10)
        self.usuario_email_entry = tk.Entry(users_frame)
        self.usuario_email_entry.grid(column=8, row=14, padx=40, pady=10)

        self.tipo_usuario_label = tk.Label(users_frame, text="Tipo de usuario:")
        self.tipo_usuario_label.grid(column=2, row=16, pady=10)
        
        self.tipos_usuario = ["Admin", "Maestro", "Alumno"]  # Opciones para el tipo de usuario
        
        self.tipo_usuario_var = ttk.StringVar(users_frame)
        self.tipo_usuario_var.set(self.tipos_usuario[0])  # Valor predeterminado
        self.tipo_usuario_dropdown = tk.OptionMenu(users_frame, self.tipo_usuario_var, *self.tipos_usuario)
        self.tipo_usuario_dropdown.grid(column=8, row=16, pady=10)

        guardar_button = ttk.Button(users_frame, text="Guardar", command=self.guardar_usuario, bootstyle="success")
        guardar_button.grid(column=2, row=20, columnspan=2, pady=20, padx=10)

        cancelar_button = ttk.Button(users_frame, text="Cancelar", command=self.cancelar_usuario, bootstyle="success")
        cancelar_button.grid(column=6, row=20, columnspan=2, pady=20, padx=10)

        editar_button = ttk.Button(users_frame, text="Editar", command=self.editar_button, bootstyle="success")
        editar_button.grid(column=8, row=20, columnspan=2, pady=20, padx=10)

        baja_button = ttk.Button(users_frame, text="Baja", command=self.borrar_usuario, bootstyle="success")
        baja_button.grid(column=10, row=20, columnspan=2, pady=20, padx=10)

    def buscar_usuario(self):
        try:
            with open('data/usuarios.csv', mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] == self.codigo_usuario_entry.get():
                        # Encontrado: Actualizar los campos de entrada con los datos encontrados
                        self.usuario_id_entry.delete(0, tk.END)
                        self.usuario_id_entry.insert(0, row[0])

                        self.username_entry.delete(0, tk.END)
                        self.username_entry.insert(0, row[1])

                        self.usuario_nombre_entry.delete(0, tk.END)
                        self.usuario_nombre_entry.insert(0, row[2])

                        self.usuario_apellido_paterno_entry.delete(0, tk.END)
                        self.usuario_apellido_paterno_entry.insert(0, row[3])
                        
                        self.usuario_apellido_materno_entry.delete(0, tk.END)
                        self.usuario_apellido_materno_entry.insert(0, row[4])

                        self.usuario_password_entry.delete(0, tk.END)
                        self.usuario_password_entry.insert(0, row[5])

                        self.usuario_email_entry.delete(0, tk.END)
                        self.usuario_email_entry.insert(0, row[6])

                        self.tipo_usuario_var.set(row[7])

                        self.status_label.config(text="Usuario encontrado", fg="green")
                        return
            # Usuario no encontrado
            self.status_label.config(text="Usuario no encontrado", fg="red")

        except Exception as e:
            # Manejar errores
            self.status_label.config(text=f"Error al buscar usuario: {str(e)}", fg="red")
    
    def guardar_usuario(self):
        # Obtener los valores de los campos de entrada
        usuario_id = self.usuario_id_entry.get()
        username = self.username_entry.get()
        usuario_nombre = self.usuario_nombre_entry.get()
        usuario_apellido_paterno = self.usuario_apellido_paterno_entry.get()
        usuario_apellido_materno = self.usuario_apellido_materno_entry.get()
        usuario_password = self.usuario_password_entry.get()
        usuario_email = self.usuario_email_entry.get()
        tipo_usuario = self.tipo_usuario_var.get()

        try:
            # Abrir el archivo CSV en modo de escritura
            with open('data/usuarios.csv', mode='a', newline='') as file:
                writer = csv.writer(file)

                # Escribir una nueva fila con los datos del usuario
                writer.writerow([usuario_id, username, usuario_nombre, usuario_apellido_paterno,
                                usuario_apellido_materno, usuario_password, usuario_email, tipo_usuario])

            # Mensaje de éxito
            self.status_label.config(text="Datos guardados exitosamente", fg="green")

        except Exception as e:
            # Mostrar mensaje de error en caso de fallo
            self.status_label.config(text=f"Error al guardar datos: {str(e)}", fg="red")
        self.cancelar_usuario()

    def borrar_usuario(self):
        try:
            with open('data/usuarios.csv', mode='r') as file:
                registros = list(csv.reader(file))

            with open('data/usuarios.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                for row in registros:
                    if row and row[0] == self.codigo_usuario_entry.get():
                        # Saltar la fila correspondiente para borrar
                        continue
                    writer.writerow(row)

            # Mensaje de éxito
            self.status_label.config(text="Usuario borrado exitosamente", fg="green")

        except Exception as e:
            # Manejar errores
            self.status_label.config(text=f"Error al borrar usuario: {str(e)}", fg="red")
        self.cancelar_usuario()

    def cancelar_usuario(self):
        # Limpiar todos los campos de entrada
        self.codigo_usuario_entry.delete(0, tk.END)
        self.usuario_id_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.usuario_nombre_entry.delete(0, tk.END)
        self.usuario_apellido_paterno_entry.delete(0, tk.END)
        self.usuario_apellido_materno_entry.delete(0, tk.END)
        self.usuario_password_entry.delete(0, tk.END)
        self.usuario_email_entry.delete(0, tk.END)
        self.tipo_usuario_var.set(self.tipos_usuario[0])  # Restablecer el valor predeterminado en el menú desplegable
        self.status_label.config(text="Campos limpiados", fg="black")

    def editar_button(self):
        try:
            with open('data/usuarios.csv', mode='r') as file:
                registros = list(csv.reader(file))

            encontrado = False
            for i, row in enumerate(registros):
                if row and row[0] == self.codigo_usuario_entry.get():
                    # Encontrado: Actualizar los campos en el registro
                    registros[i] = [
                        self.usuario_id_entry.get(),
                        self.username_entry.get(),
                        self.usuario_nombre_entry.get(),
                        self.usuario_apellido_paterno_entry.get(),
                        self.usuario_apellido_materno_entry.get(),
                        self.usuario_password_entry.get(),
                        self.usuario_email_entry.get(),
                        self.tipo_usuario_var.get()
                    ]
                    encontrado = True
                    break

            if encontrado:
                # Escribir todos los registros de vuelta al archivo
                with open('data/usuarios.csv', mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(registros)

                self.status_label.config(text="Usuario editado exitosamente", fg="green")
            else:
                # Usuario no encontrado
                self.status_label.config(text="Usuario no encontrado para editar", fg="red")

        except Exception as e:
            # Manejar errores
            self.status_label.config(text=f"Error al editar usuario: {str(e)}", fg="red")

    def alumnos_tab(self):
        # Elementos en la pestaña de alumnos
        students_frame = self.tabs["Alumnos"]

        # Label para "Ingrese código de alumno"
        self.codigo_alumno_label = tk.Label(students_frame, text="Ingrese código de alumno:")
        self.codigo_alumno_label.grid(column=2, row=1)

        # Cuadro de texto para ingresar el código del alumno
        self.codigo_alumno_entry = tk.Entry(students_frame)
        self.codigo_alumno_entry.grid(column=8, row=1, padx=40)

        # Botón de búsqueda
        buscar_button = ttk.Button(students_frame, text="Buscar", command=self.buscar_alumno, bootstyle="success")
        buscar_button.grid(column=12, row=1)

        # Separador horizontal
        ttk.Separator(students_frame, orient='horizontal').grid(row=2, columnspan=1000, sticky="ew", pady=20)

        # Labels y cuadros de texto para información del alumno
        self.id_alumno_label = tk.Label(students_frame, text="ID:")
        self.id_alumno_label.grid(column=2, row=4, pady=10)
        self.id_alumno_entry = tk.Entry(students_frame)
        self.id_alumno_entry.grid(column=8, row=4, padx=40, pady=10)

        self.nombre_alumno_label = tk.Label(students_frame, text="Nombre:")
        self.nombre_alumno_label.grid(column=2, row=8, pady=10)
        self.nombre_alumno_entry = tk.Entry(students_frame)
        self.nombre_alumno_entry.grid(column=8, row=8, padx=40, pady=10)

        self.alumno_apellido_paterno_label = tk.Label(students_frame, text="Apellido paterno:")
        self.alumno_apellido_paterno_label.grid(column=2, row=10, pady=10)
        self.alumno_apellido_paterno_entry = tk.Entry(students_frame)
        self.alumno_apellido_paterno_entry.grid(column=8, row=10, padx=40, pady=10)

        self.alumno_apellido_materno_label = tk.Label(students_frame, text="Apellido materno:")
        self.alumno_apellido_materno_label.grid(column=2, row=12, pady=10)
        self.alumno_apellido_materno_entry = tk.Entry(students_frame)
        self.alumno_apellido_materno_entry.grid(column=8, row=12, padx=40, pady=10)

        self.alumno_carrera_label = tk.Label(students_frame, text="Carrera:")
        self.alumno_carrera_label.grid(column=2, row=13, pady=10)
        self.alumno_carreras = ["Ingenieria en Computacion", "Ingenieria en Informatica"]
        self.alumno_carrera_var = ttk.StringVar(students_frame)
        self.alumno_carrera_var.set(self.alumno_carreras[0])  # Valor predeterminado
        self.alumno_carrera_dropdown = tk.OptionMenu(students_frame, self.alumno_carrera_var, *self.alumno_carreras)
        self.alumno_carrera_dropdown.grid(column=8, row=13, pady=10)

        self.fecha_nacimiento_alumno_label = tk.Label(students_frame, text="Fecha de Nacimiento:")
        self.fecha_nacimiento_alumno_label.grid(column=2, row=14, pady=10)
        self.fecha_nacimiento_alumno_entry = tk.Entry(students_frame, show="*")
        self.fecha_nacimiento_alumno_entry.grid(column=8, row=14, padx=40, pady=10)

        self.email_alumno_label = tk.Label(students_frame, text="Email:")
        self.email_alumno_label.grid(column=2, row=15, pady=10)
        self.email_alumno_entry = tk.Entry(students_frame)
        self.email_alumno_entry.grid(column=8, row=15, padx=40, pady=10)

        self.alumno_estado_label = tk.Label(students_frame, text="Estado:")
        self.alumno_estado_label.grid(column=2, row=17, pady=10)
        
        self.alumno_states = [
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
        
        self.alumnoestado_var = ttk.StringVar(students_frame)
        self.alumnoestado_var.set(self.alumno_states[0])  # Valor predeterminado
        self.alumnoestado_dropdown = tk.OptionMenu(students_frame, self.alumnoestado_var, *self.alumno_states)
        self.alumnoestado_dropdown.grid(column=8, row=17, pady=10)

        self.alumno_materias_label = tk.Label(students_frame, text="Materias:")
        self.alumno_materias_label.grid(column=2, row=16, pady=10)
        
        self.alumno_materias = [
            "Física 1",
            "Programación Estructurada",
            "Estructura de Datos",
            "Inteligencia Artificial",
            "Ingeniería de Software 1"
        ]
        
        self.alumnos_materias_var = ttk.StringVar(students_frame)
        self.alumnos_materias_var.set( self.alumno_materias[0])  # Valor predeterminado
        self.alumnos_materias_dropdown = tk.OptionMenu(students_frame, self.alumnos_materias_var, * self.alumno_materias)
        self.alumnos_materias_dropdown.grid(column=8, row=16, pady=10)

        guardar_button = ttk.Button(students_frame, text="Guardar", command=self.guardar_alumno, bootstyle="success")
        guardar_button.grid(column=2, row=23, columnspan=2, pady=20, padx=10)

        cancelar_button = ttk.Button(students_frame, text="Cancelar", command=self.cancelar_alumno, bootstyle="success")
        cancelar_button.grid(column=6, row=23, columnspan=2, pady=20, padx=10)

        editar_button = ttk.Button(students_frame, text="Editar", command=self.editar_alumno, bootstyle="success")
        editar_button.grid(column=8, row=23, columnspan=2, pady=20, padx=10)

        baja_button = ttk.Button(students_frame, text="Baja", command=self.borrar_alumno, bootstyle="success")
        baja_button.grid(column=10, row=23, columnspan=2, pady=20, padx=10)

    def buscar_alumno(self):
        try:
            with open('data/alumnos.csv', mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] == self.codigo_alumno_entry.get():
                        # Encontrado: Actualizar los campos de entrada con los datos encontrados
                        self.id_alumno_entry.delete(0, tk.END)
                        self.id_alumno_entry.insert(0, row[0])

                        self.nombre_alumno_entry.delete(0, tk.END)
                        self.nombre_alumno_entry.insert(0, row[1])

                        self.alumno_apellido_paterno_entry.delete(0, tk.END)
                        self.alumno_apellido_paterno_entry.insert(0, row[2])

                        self.alumno_apellido_materno_entry.delete(0, tk.END)
                        self.alumno_apellido_materno_entry.insert(0, row[3])

                        self.alumno_carrera_var.set(row[4])

                        self.fecha_nacimiento_alumno_entry.delete(0, tk.END)
                        self.fecha_nacimiento_alumno_entry.insert(0, row[5])

                        self.email_alumno_entry.delete(0, tk.END)
                        self.email_alumno_entry.insert(0, row[6])

                        self.alumnoestado_var.set(row[7])

                        self.alumnos_materias_var.set(row[8])

                        self.status_label.config(text="Alumno encontrado", fg="green")
                        return
            # Alumno no encontrado
            self.status_label.config(text="Alumno no encontrado", fg="red")

        except Exception as e:
            # Manejar errores
            self.status_label.config(text=f"Error al buscar alumno: {str(e)}", fg="red")

    def guardar_alumno(self):
        # Obtener los valores de los campos de entrada
        alumno_id = self.id_alumno_entry.get()
        alumno_nombre = self.nombre_alumno_entry.get()
        apellido_paterno = self.alumno_apellido_paterno_entry.get()
        apellido_materno = self.alumno_apellido_materno_entry.get()
        carrera = self.alumno_carrera_var.get()
        fecha_nacimiento = self.fecha_nacimiento_alumno_entry.get()
        email = self.email_alumno_entry.get()
        estado = self.alumnoestado_var.get()
        materias = self.alumnos_materias_var.get()

        try:
            # Abrir el archivo CSV en modo de escritura
            with open('data/alumnos.csv', mode='a', newline='') as file:
                writer = csv.writer(file)

                # Escribir una nueva fila con los datos del alumno
                writer.writerow([alumno_id, alumno_nombre, apellido_paterno, apellido_materno,
                                carrera, fecha_nacimiento, email, estado, materias])

            # Mensaje de éxito
            self.status_label.config(text="Datos guardados exitosamente", fg="green")

        except Exception as e:
            # Mostrar mensaje de error en caso de fallo
            self.status_label.config(text=f"Error al guardar datos: {str(e)}", fg="red")
        self.cancelar_alumno()

    def borrar_alumno(self):
        try:
            with open('data/alumnos.csv', mode='r') as file:
                registros = list(csv.reader(file))

            with open('data/alumnos.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                for row in registros:
                    if row and row[0] == self.codigo_alumno_entry.get():
                        # Saltar la fila correspondiente para borrar
                        continue
                    writer.writerow(row)

            # Mensaje de éxito
            self.status_label.config(text="Alumno borrado exitosamente", fg="green")

        except Exception as e:
            # Manejar errores
            self.status_label.config(text=f"Error al borrar alumno: {str(e)}", fg="red")
        self.cancelar_alumno()

    def cancelar_alumno(self):
        # Limpiar todos los campos de entrada
        self.codigo_alumno_entry.delete(0, tk.END)
        self.id_alumno_entry.delete(0, tk.END)
        self.nombre_alumno_entry.delete(0, tk.END)
        self.alumno_apellido_paterno_entry.delete(0, tk.END)
        self.alumno_apellido_materno_entry.delete(0, tk.END)
        self.alumno_carrera_var.set(self.alumno_carreras[0])  # Restablecer el valor predeterminado en el menú desplegable
        self.fecha_nacimiento_alumno_entry.delete(0, tk.END)
        self.email_alumno_entry.delete(0, tk.END)
        self.alumnoestado_var.set(self.alumno_states[0])  # Restablecer el valor predeterminado en el menú desplegable
        self.alumnos_materias_var.set( self.alumno_materias[0])  # Restablecer el valor predeterminado en el menú desplegable
        self.status_label.config(text="Campos limpiados", fg="black")

    def editar_alumno(self):
        try:
            with open('data/alumnos.csv', mode='r') as file:
                registros = list(csv.reader(file))

            encontrado = False
            for i, row in enumerate(registros):
                if row and row[0] == self.codigo_alumno_entry.get():
                    # Encontrado: Actualizar los campos en el registro
                    registros[i] = [
                        self.id_alumno_entry.get(),
                        self.nombre_alumno_entry.get(),
                        self.alumno_apellido_paterno_entry.get(),
                        self.alumno_apellido_materno_entry.get(),
                        self.alumno_carrera_var.get(),
                        self.fecha_nacimiento_alumno_entry.get(),
                        self.email_alumno_entry.get(),
                        self.alumnoestado_var.get(),
                        self.alumnos_materias_var.get()
                    ]
                    encontrado = True
                    break

            if encontrado:
                # Escribir todos los registros de vuelta al archivo
                with open('data/alumnos.csv', mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(registros)

                self.status_label.config(text="Alumno editado exitosamente", fg="green")
            else:
                # Alumno no encontrado
                self.status_label.config(text="Alumno no encontrado para editar", fg="red")

        except Exception as e:
            # Manejar errores
            self.status_label.config(text=f"Error al editar alumno: {str(e)}", fg="red")
    
    def maestros_tab(self):
    # Elementos en la pestaña de maestros
        teachers_frame = self.tabs["Maestros"]
        
        # Label para "Ingrese código del maestro"
        self.codigo_maestro_label = tk.Label(teachers_frame, text="Ingrese código del maestro:")
        self.codigo_maestro_label.grid(column=2, row=1)

        # Cuadro de texto para ingresar el código del maestro
        self.codigo_maestro_entry = tk.Entry(teachers_frame)
        self.codigo_maestro_entry.grid(column=8, row=1, padx=40)

        # Botón de búsqueda
        buscar_button = ttk.Button(teachers_frame, text="Buscar", command=self.buscar_maestro, bootstyle="success")
        buscar_button.grid(column=12, row=1)

        # Separador horizontal
        ttk.Separator(teachers_frame, orient='horizontal').grid(row=2, columnspan=1000, sticky="ew", pady=20)

        # Labels y cuadros de texto para información del maestro
        self.maestro_id_label = tk.Label(teachers_frame, text="ID:")
        self.maestro_id_label.grid(column=2, row=4, pady=10)
        self.maestro_id_entry = tk.Entry(teachers_frame)
        self.maestro_id_entry.grid(column=8, row=4, padx=40, pady=10)

        self.maestro_nombre_label = tk.Label(teachers_frame, text="Nombre:")
        self.maestro_nombre_label.grid(column=2, row=8, pady=10)
        self.maestro_nombre_entry = tk.Entry(teachers_frame)
        self.maestro_nombre_entry.grid(column=8, row=8, padx=40, pady=10)

        self.maestro_apellido_paterno_label = tk.Label(teachers_frame, text="Apellido paterno:")
        self.maestro_apellido_paterno_label.grid(column=2, row=10, pady=10)
        self.maestro_apellido_paterno_entry = tk.Entry(teachers_frame)
        self.maestro_apellido_paterno_entry.grid(column=8, row=10, padx=40, pady=10)

        self.maestro_apellido_materno_label = tk.Label(teachers_frame, text="Apellido materno:")
        self.maestro_apellido_materno_label.grid(column=2, row=12, pady=10)
        self.maestro_apellido_materno_entry = tk.Entry(teachers_frame)
        self.maestro_apellido_materno_entry.grid(column=8, row=12, padx=40, pady=10)

        self.maestro_carrera_label = tk.Label(teachers_frame, text="Carrera:")
        self.maestro_carrera_label.grid(column=2, row=13, pady=10)
        self.maestro_carreras = ["Ingenieria en Computacion", "Ingenieria en Informatica"]
        self.maestro_carrera_var = ttk.StringVar(teachers_frame)
        self.maestro_carrera_var.set(self.maestro_carreras[0])  # Valor predeterminado
        self.maestro_carrera_dropdown = tk.OptionMenu(teachers_frame, self.maestro_carrera_var, *self.maestro_carreras)
        self.maestro_carrera_dropdown.grid(column=8, row=13, pady=10)
        
        self.maestro_email_label = tk.Label(teachers_frame, text="Email:")
        self.maestro_email_label.grid(column=2, row=14, pady=10)
        self.maestro_email_entry = tk.Entry(teachers_frame)
        self.maestro_email_entry.grid(column=8, row=14, padx=40, pady=10)

        self.maestro_materias_label = tk.Label(teachers_frame, text="Materias:")
        self.maestro_materias_label.grid(column=2, row=16, pady=10)

        self.maestro_materias = ["Fisica 1", "Programacion Estructurada", "Estructura de Datos", "Inteligencia Artificial", "Ingenieria de Software 1"]
        self.maestro_materias_var = tk.StringVar(teachers_frame)
        self.maestro_materias_var.set( self.maestro_materias[0])
        self.maestro_materias_dropdown = tk.OptionMenu(teachers_frame, self.maestro_materias_var, * self.maestro_materias)
        self.maestro_materias_dropdown.grid(column=8, row=16, pady=10)

        self.maestro_grado_label = tk.Label(teachers_frame, text="Grado de estudios:")
        self.maestro_grado_label.grid(column=2, row=17, pady=10)
        self.maestro_grado_entry = tk.Entry(teachers_frame, show="*")
        self.maestro_grado_entry.grid(column=8, row=17, padx=40, pady=10)

        # Botones
        guardar_button = ttk.Button(teachers_frame, text="Guardar", command=self.guardar_maestro, bootstyle="success")
        guardar_button.grid(column=2, row=22, columnspan=2, pady=20, padx=10)

        cancelar_button = ttk.Button(teachers_frame, text="Cancelar", command=self.cancelar_maestro, bootstyle="success")
        cancelar_button.grid(column=6, row=22, columnspan=2, pady=20, padx=10)

        editar_button = ttk.Button(teachers_frame, text="Editar", command=self.editar_maestro, bootstyle="success")
        editar_button.grid(column=8, row=22, columnspan=2, pady=20, padx=10)

        baja_button = ttk.Button(teachers_frame, text="Baja", command=self.borrar_maestro, bootstyle="success")
        baja_button.grid(column=10, row=22, columnspan=2, pady=20, padx=10)

    def buscar_maestro(self):
        try:
            with open('data/maestros.csv', mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] == self.codigo_maestro_entry.get():
                        # Encontrado: Actualizar los campos de entrada con los datos encontrados
                        self.maestro_id_entry.delete(0, tk.END)
                        self.maestro_id_entry.insert(0, row[0])

                        self.maestro_nombre_entry.delete(0, tk.END)
                        self.maestro_nombre_entry.insert(0, row[1])

                        self.maestro_apellido_paterno_entry.delete(0, tk.END)
                        self.maestro_apellido_paterno_entry.insert(0, row[2])

                        self.maestro_apellido_materno_entry.delete(0, tk.END)
                        self.maestro_apellido_materno_entry.insert(0, row[3])

                        self.maestro_carrera_var.set(row[4])

                        self.maestro_email_entry.delete(0, tk.END)
                        self.maestro_email_entry.insert(0, row[5])

                        self.maestro_materias_var.set(row[6])

                        self.maestro_grado_entry.delete(0, tk.END)
                        self.maestro_grado_entry.insert(0, row[7])

                        self.status_label.config(text="Maestro encontrado", fg="green")
                        return
            # Maestro no encontrado
            self.status_label.config(text="Maestro no encontrado", fg="red")

        except Exception as e:
            # Manejar errores
            self.status_label.config(text=f"Error al buscar maestro: {str(e)}", fg="red")

    def guardar_maestro(self):
        # Obtener los valores de los campos de entrada
        maestro_id = self.maestro_id_entry.get()
        maestro_nombre = self.maestro_nombre_entry.get()
        apellido_paterno = self.maestro_apellido_paterno_entry.get()
        apellido_materno = self.maestro_apellido_materno_entry.get()
        carrera = self.maestro_carrera_var.get()
        email = self.maestro_email_entry.get()
        materias = self.maestro_materias_var.get()
        grado_estudios = self.maestro_grado_entry.get()

        try:
            # Abrir el archivo CSV en modo de escritura
            with open('data/maestros.csv', mode='a', newline='') as file:
                writer = csv.writer(file)

                # Escribir una nueva fila con los datos del maestro
                writer.writerow([maestro_id, maestro_nombre, apellido_paterno, apellido_materno,
                                carrera, email, materias, grado_estudios])

            # Mensaje de éxito
            self.status_label.config(text="Datos del maestro guardados exitosamente", fg="green")

        except Exception as e:
            # Mostrar mensaje de error en caso de fallo
            self.status_label.config(text=f"Error al guardar datos del maestro: {str(e)}", fg="red")
        self.cancelar_maestro()

    def borrar_maestro(self):
        try:
            with open('data/maestros.csv', mode='r') as file:
                registros = list(csv.reader(file))

            with open('data/maestros.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                for row in registros:
                    if row and row[0] == self.codigo_maestro_entry.get():
                        # Saltar la fila correspondiente para borrar
                        continue
                    writer.writerow(row)

            # Mensaje de éxito
            self.status_label.config(text="Maestro borrado exitosamente", fg="green")

        except Exception as e:
            # Manejar errores
            self.status_label.config(text=f"Error al borrar maestro: {str(e)}", fg="red")
        self.cancelar_maestro()

    def cancelar_maestro(self):
        # Limpiar todos los campos de entrada
        self.codigo_maestro_entry.delete(0, tk.END)
        self.maestro_id_entry.delete(0, tk.END)
        self.maestro_nombre_entry.delete(0, tk.END)
        self.maestro_apellido_paterno_entry.delete(0, tk.END)
        self.maestro_apellido_materno_entry.delete(0, tk.END)
        self.maestro_carrera_var.set(self.maestro_carreras[0])  # Restablecer el valor predeterminado en el menú desplegable
        self.maestro_email_entry.delete(0, tk.END)
        self.maestro_materias_var.set(self.maestro_materias[0])  # Restablecer el valor predeterminado en el menú desplegable
        self.maestro_grado_entry.delete(0, tk.END)
        self.status_label.config(text="Campos limpiados", fg="black")

    def editar_maestro(self):
        try:
            with open('data/maestros.csv', mode='r') as file:
                registros = list(csv.reader(file))

            encontrado = False
            for i, row in enumerate(registros):
                if row and row[0] == self.codigo_maestro_entry.get():
                    # Encontrado: Actualizar los campos en el registro
                    registros[i] = [
                        self.maestro_id_entry.get(),
                        self.maestro_nombre_entry.get(),
                        self.maestro_apellido_paterno_entry.get(),
                        self.maestro_apellido_materno_entry.get(),
                        self.maestro_carrera_var.get(),
                        self.maestro_email_entry.get(),
                        self.maestro_materias_var.get(),
                        self.maestro_grado_entry.get()
                    ]
                    encontrado = True
                    break

            if encontrado:
                # Escribir todos los registros de vuelta al archivo
                with open('data/maestros.csv', mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(registros)

                self.status_label.config(text="Maestro editado exitosamente", fg="green")
            else:
                # Maestro no encontrado
                self.status_label.config(text="Maestro no encontrado para editar", fg="red")

        except Exception as e:
            # Manejar errores
            self.status_label.config(text=f"Error al editar maestro: {str(e)}", fg="red")

    def materias_tab(self):
        # Elementos en la pestaña de materias
        materias_frame = self.tabs["Materias"]
        
        # Label para "Ingrese ID de la materia"
        id_materia_label = tk.Label(materias_frame, text="Ingrese ID de la materia:")
        id_materia_label.grid(column=2, row=1)

        # Cuadro de texto para ingresar el ID de la materia
        self.id_materia_entry = tk.Entry(materias_frame)
        self.id_materia_entry.grid(column=8, row=1, padx=40)

        # Botón de búsqueda
        buscar_button = ttk.Button(materias_frame, text="Buscar", command=self.buscar_materia, bootstyle="success")
        buscar_button.grid(column=12, row=1)

        # Separador horizontal
        ttk.Separator(materias_frame, orient='horizontal').grid(row=2, columnspan=1000, sticky="ew", pady=20)

        # Labels y cuadros de texto para información de la materia
        self.materias_asignatura_label = tk.Label(materias_frame, text="Asignatura:")
        self.materias_asignatura_label.grid(column=2, row=4, pady=10)
        self.materias_asignatura_entry = tk.Entry(materias_frame)
        self.materias_asignatura_entry.grid(column=8, row=4, padx=40, pady=10)

        self.materias_creditos_label = tk.Label(materias_frame, text="Créditos:")
        self.materias_creditos_label.grid(column=2, row=8, pady=10)
        self.materias_creditos_entry = tk.Entry(materias_frame)
        self.materias_creditos_entry.grid(column=8, row=8, padx=40, pady=10)

        self.materias_semestre_label = tk.Label(materias_frame, text="Semestre:")
        self.materias_semestre_label.grid(column=2, row=10, pady=10)
        self.materias_semestre_entry = tk.Entry(materias_frame)
        self.materias_semestre_entry.grid(column=8, row=10, padx=40, pady=10)

        self.materias_carrera_label = tk.Label(materias_frame, text="Carrera:")
        self.materias_carrera_label.grid(column=2, row=12, pady=10)
        self.materias_carreras = ["Ingenieria en Computacion", "Ingenieria en Informatica"]
        self.materias_carrera_var = ttk.StringVar(materias_frame)
        self.materias_carrera_var.set(self.materias_carreras[0])  # Valor predeterminado
        self.materias_carrera_dropdown = tk.OptionMenu(materias_frame, self.materias_carrera_var, *self.materias_carreras)
        self.materias_carrera_dropdown.grid(column=8, row=12, pady=10)

        # Botones
        guardar_button = ttk.Button(materias_frame, text="Guardar", command=self.guardar_materia, bootstyle="success")
        guardar_button.grid(column=2, row=17, columnspan=2, pady=20, padx=10)

        cancelar_button = ttk.Button(materias_frame, text="Cancelar", command=self.cancelar_materia, bootstyle="success")
        cancelar_button.grid(column=6, row=17, columnspan=2, pady=20, padx=10)

        editar_button = ttk.Button(materias_frame, text="Editar", command=self.editar_materia, bootstyle="success")
        editar_button.grid(column=8, row=17, columnspan=2, pady=20, padx=10)

        baja_button = ttk.Button(materias_frame, text="Baja", command=self.borrar_materia, bootstyle="success")
        baja_button.grid(column=10, row=17, columnspan=2, pady=20, padx=10)
  
    def buscar_materia(self):
        try:
            with open('data/materias.csv', mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] == self.id_materia_entry.get():
                        # Encontrado: Actualizar los campos de entrada con los datos encontrados
                        self.materias_asignatura_entry.delete(0, tk.END)
                        self.materias_asignatura_entry.insert(0, row[1])

                        self.materias_creditos_entry.delete(0, tk.END)
                        self.materias_creditos_entry.insert(0, row[2])

                        self.materias_semestre_entry.delete(0, tk.END)
                        self.materias_semestre_entry.insert(0, row[3])

                        self.materias_carrera_var.set(row[4])

                        self.status_label.config(text="Materia encontrada", fg="green")
                        return
            # Materia no encontrada
            self.status_label.config(text="Materia no encontrada", fg="red")

        except Exception as e:
            # Manejar errores
            self.status_label.config(text=f"Error al buscar materia: {str(e)}", fg="red")

    def guardar_materia(self):
        # Obtener los valores de los campos de entrada
        id = self.id_materia_entry.get()
        asignatura = self.materias_asignatura_entry.get()
        creditos = self.materias_creditos_entry.get()
        semestre = self.materias_semestre_entry.get()
        carrera = self.materias_carrera_var.get()

        try:
            # Abrir el archivo CSV en modo de escritura
            with open('data/materias.csv', mode='a', newline='') as file:
                writer = csv.writer(file)

                # Escribir una nueva fila con los datos de la materia
                writer.writerow([id, asignatura, creditos, semestre, carrera])

            # Mensaje de éxito
            self.status_label.config(text="Datos de la materia guardados exitosamente", fg="green")

        except Exception as e:
            # Mostrar mensaje de error en caso de fallo
            self.status_label.config(text=f"Error al guardar datos de la materia: {str(e)}", fg="red")
        self.cancelar_materia()

    def borrar_materia(self):
        try:
            with open('data/materias.csv', mode='r') as file:
                registros = list(csv.reader(file))

            with open('data/materias.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                for row in registros:
                    if row and row[0] == self.id_materia_entry.get():
                        # Saltar la fila correspondiente para borrar
                        continue
                    writer.writerow(row)

            # Mensaje de éxito
            self.status_label.config(text="Materia borrada exitosamente", fg="green")

        except Exception as e:
            # Manejar errores
            self.status_label.config(text=f"Error al borrar materia: {str(e)}", fg="red")
        self.cancelar_materia()

    def cancelar_materia(self):
        # Limpiar todos los campos de entrada
        self.id_materia_entry.delete(0, tk.END)
        self.materias_asignatura_entry.delete(0, tk.END)
        self.materias_creditos_entry.delete(0, tk.END)
        self.materias_semestre_entry.delete(0, tk.END)
        self.materias_carrera_var.set(self.materias_carreras[0])  # Restablecer el valor predeterminado en el menú desplegable
        self.status_label.config(text="Campos limpiados", fg="black")

    def editar_materia(self):
        try:
            with open('data/materias.csv', mode='r') as file:
                registros = list(csv.reader(file))

            encontrado = False
            for i, row in enumerate(registros):
                if row and row[0] == self.id_materia_entry.get():
                    # Encontrado: Actualizar los campos en el registro
                    registros[i] = [
                        self.id_materia_entry.get(),
                        self.materias_asignatura_entry.get(),
                        self.materias_creditos_entry.get(),
                        self.materias_semestre_entry.get(),
                        self.materias_carrera_var.get()
                    ]
                    encontrado = True
                    break

            if encontrado:
                # Escribir todos los registros de vuelta al archivo
                with open('data/materias.csv', mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(registros)

                self.status_label.config(text="Materia editada exitosamente", fg="green")
            else:
                # Materia no encontrada
                self.status_label.config(text="Materia no encontrada para editar", fg="red")

        except Exception as e:
            # Manejar errores
            self.status_label.config(text=f"Error al editar materia: {str(e)}", fg="red")

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