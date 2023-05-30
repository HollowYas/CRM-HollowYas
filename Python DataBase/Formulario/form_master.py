import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl



class MasterPanel:
   
    def home(self):
        from Formulario.form_login import Aplicacion
        self.ventana.destroy()
        Aplicacion()

    
        
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('ADMIN')
        self.ventana.geometry('1100x600')
        self.ventana.config(bg='#bcbcbc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 1100,600)

        def base_page():
            base_frame = tk.Frame(marco_principal, bg='#323232', highlightbackground='green', highlightthickness=1)
            base_frame.pack(side=tk.LEFT)
            base_frame.pack_propagate(False)
            base_frame.configure(height=600, width=960)
            lb = tk.Label(base_frame, text="HOLA YAS\n\nPagina: Base de Datos", font=('Arial', 30))
            lb.pack()
            # base_frame.pack(pady=20)

        def usuarios_page():
            usuarios_frame = tk.Frame(marco_principal, bg='#323232', highlightbackground='green', highlightthickness=1)
            usuarios_frame.pack(side=tk.LEFT)
            usuarios_frame.pack_propagate(False)
            usuarios_frame.configure(height=600, width=960)
            lb = tk.Label(usuarios_frame, text="HOLA YAS\n\nPagina: Usuarios", font=('Arial', 30))
            lb.pack()
            # usuarios_frame.pack(pady=20)

        def prestamo_page():
            prestamo_frame = tk.Frame(marco_principal, bg='#323232', highlightbackground='green', highlightthickness=1)
            prestamo_frame.pack(side=tk.LEFT)
            prestamo_frame.pack_propagate(False)
            prestamo_frame.configure(height=600, width=960)
            lb = tk.Label(prestamo_frame, text="HOLA YAS\n\nPagina: Prestamo", font=('Arial', 30))
            lb.pack()
            # prestamo_frame.pack(pady=20)

        def eprestamo_page():
            eprestamo_frame = tk.Frame(marco_principal, bg='#323232', highlightbackground='green', highlightthickness=1)
            eprestamo_frame.pack(side=tk.LEFT)
            eprestamo_frame.pack_propagate(False)
            eprestamo_frame.configure(height=600, width=960)
            lb = tk.Label(eprestamo_frame, text="HOLA YAS\n\nPagina: Estado de Prestamo", font=('Arial', 30))
            lb.pack()
            # eprestamo_frame.pack(pady=20)

        def alibros_page():
            alibros_frame = tk.Frame(marco_principal, bg='#323232', highlightbackground='green', highlightthickness=1)
            alibros_frame.pack(side=tk.LEFT)
            alibros_frame.pack_propagate(False)
            alibros_frame.configure(height=600, width=960)
            lb = tk.Label(alibros_frame, text="HOLA YAS\n\nPagina: Agregar Libros", font=('Arial', 30))
            lb.pack()
            # alibros_frame.pack(pady=20)

        def libros_page():
            libro_frame = tk.Frame(marco_principal, bg='#323232', highlightbackground='green', highlightthickness=1)
            libro_frame.pack(side=tk.LEFT)
            libro_frame.pack_propagate(False)
            libro_frame.configure(height=600, width=960)
            lb = tk.Label(libro_frame, text="HOLA YAS\n\nPagina: Ver Libros", font=('Arial', 30))
            lb.pack()
            # libro_frame.pack(pady=20)

        def ocultar():
            BaseDatos.config(bg='#000000')
            Usuarios.config(bg='#000000')
            Prestamo.config(bg='#000000')
            EPrestamo.config(bg='#000000')
            ALibros.config(bg='#000000')
            VerLibros.config(bg='#000000')

        def borrar_pages():
            for frame in marco_principal.winfo_children():
                frame.destroy()

        def indicador(label, page):
            ocultar()
            label.config(bg='white')
            borrar_pages()
            page()

        logo = utl.leer_imagen("Imagenes/database.png", (60,60))

            
        ###### <Frame Izquierdo/Botones> ######
        frame_izquierdo = tk.Frame(self.ventana, bg='#000000')
        frame_izquierdo.pack(side=tk.LEFT)
        frame_izquierdo.pack_propagate(False)
        frame_izquierdo.configure(width=140, height=600)

        ###### <Botones> ######
        boton_BaseDatos = tk.Button(frame_izquierdo, text="Base de Datos",padx=23, pady=10, font=('Arial', 10, BOLD) ,fg='white', bg='#000000', bd=0, command=lambda: indicador(BaseDatos, base_page))
        boton_BaseDatos.place(x=9, y=95, width=124)
        BaseDatos = tk.Label(frame_izquierdo, text='', bg='#000000')
        BaseDatos.place(x=3, y=95, width=5, height=42)
        
        boton_usuarios = tk.Button(frame_izquierdo, text="Usuarios", padx=29, pady=10, font=('Arial', 10, BOLD) ,fg='white', bg='#000000', bd=0, command=lambda: indicador(Usuarios, usuarios_page))
        boton_usuarios.place(x=9, y=160, width=124)
        Usuarios = tk.Label(frame_izquierdo, text='', bg='#000000')
        Usuarios.place(x=3, y=160, width=5, height=42)

        boton_prestamo = tk.Button(frame_izquierdo, text="Prestamo", padx=13, pady=10, font=('Arial', 10, BOLD) ,fg='white', bg='#000000', bd=0, command=lambda: indicador(Prestamo, prestamo_page))
        boton_prestamo.place(x=9, y=230, width=124)
        Prestamo = tk.Label(frame_izquierdo, text='', bg='#000000')
        Prestamo.place(x=3, y=230, width=5, height=42)

        boton_estadoprestamo = tk.Button(frame_izquierdo, text="Estado Prestamo", padx=10, pady=10, font=('Arial', 10, BOLD) ,fg='white', bg='#000000', bd=0, command=lambda: indicador(EPrestamo, eprestamo_page))
        boton_estadoprestamo.place(x=9, y=300, width=124)
        EPrestamo = tk.Label(frame_izquierdo, text='', bg='#000000')
        EPrestamo.place(x=3, y=300, width=5, height=42)

        boton_agregarlibros = tk.Button(frame_izquierdo, text="Agregar Libros", padx=10, pady=10, font=('Arial', 10, BOLD) ,fg='white', bg='#000000', bd=0, command=lambda: indicador(ALibros, alibros_page))
        boton_agregarlibros.place(x=9, y=380, width=124)
        ALibros = tk.Label(frame_izquierdo, text='', bg='#000000')
        ALibros.place(x=3, y=380, width=5, height=42)

        boton_verlibros = tk.Button(frame_izquierdo, text="Libros", padx=10, pady=10, font=('Arial', 10, BOLD) ,fg='white', bg='#000000', bd=0, command=lambda: indicador(VerLibros, libros_page))
        boton_verlibros.place(x=9, y=460, width=124)
        VerLibros = tk.Label(frame_izquierdo, text='', bg='#000000')
        VerLibros.place(x=3, y=460, width=5, height=42)

        boton_regresar = tk.Button(frame_izquierdo, text="Salir", padx=10, pady=10, font=('Arial', 10, BOLD) ,fg='white', bg='#000000', bd=0, command=self.home)
        boton_regresar.place(x=9, y=530, width=124)
        
        ###### <Frame de Opciones> ######
        marco_principal = tk.Frame(self.ventana, bg='#323232', highlightbackground='green', highlightthickness=2)
        marco_principal.pack(side=tk.LEFT)
        marco_principal.pack_propagate(False)
        marco_principal.configure(height=600, width=960)

        # titulo = tk.Label(marco_principal, text="PROGRAMA DE BASE DE DATOS REALIZADO POR HOLLOWYAS", font=('Times', 20, BOLD), fg='#fcfcfc', bg='#bcbcbc')
        # titulo.place(x=100, y=200)


        ###### <Logo> ######
        labellogo = tk.Label(frame_izquierdo, image=logo, bg='#000000')
        labellogo.place(x=40, y=20)
                           
        self.ventana.mainloop()































































































