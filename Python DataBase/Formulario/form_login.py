import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from Formulario.form_master import MasterPanel
from Formulario.form_registro import Registro
from tkinter import font
#from Hayahser import DataBaseInterface




class Aplicacion:

    def verificacion(self):
        usu = self.user.get()
        password = self.password.get()

        if(usu == "" and password == ""):
            self.ventana.destroy()
            #DataBaseInterface()
            MasterPanel()

        # elif(usu == "" and password == "1"):
        #     messagebox.showerror(message="Por favor ingrese su usuario", title="ERROR")

        # elif(usu == "1" and password == ""):
        #     messagebox.showerror(message="Por favor ingrese su contraseña", title="ERROR")

        # else:
        #     messagebox.showerror(message="La contraseña o el usuario son incorrectos", title="ERROR")

    def registro(self):
        self.ventana.destroy()
        Registro()

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('LOGIN')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 800,500)
        

        logo = utl.leer_imagen("Imagenes/database.png", (200,200))


        #Logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='blue')
        frame_logo.pack(side="left", expand=tk.NO, fill=tk.BOTH)

        label = tk.Label(frame_logo, image=logo, bg='blue')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        #Panel1
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        #Panel de texto "LOGIN"
        frame_top = tk.Frame(frame_form, height=50,bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_top, text="-LOGIN DATABASE-", font=('Times', 30, BOLD), fg='#000000', bg='#fcfcfc', pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        #Panel de los Labels en donde se pedira al usuario su user/password
        frame_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        #Panel Usuario
        label_user = tk.Label(frame_fill, text="User", font=('Times', 14), fg='#000000', bg='#fcfcfc', anchor="w")
        label_user.pack(fill=tk.X, padx=20, pady=5)
        self.user = ttk.Entry(frame_fill, font=('Times', 14))
        self.user.pack(fill=tk.X, padx=20, pady=10)

        label_password = tk.Label(frame_fill, text="Password", font=('Times', 14), fg='#000000', bg='#fcfcfc', anchor="w")
        label_password.pack(fill=tk.X, padx=20, pady=5)
        self.password = ttk.Entry(frame_fill, font=('Times', 14))
        self.password.pack(fill=tk.X, padx=20, pady=10)
        self.password.config(show="*")

        #Boton Login
        inicio = tk.Button(frame_fill, text="Log in", font=('Times', 15, BOLD), bg="blue", bd=0, fg="#fff", command=self.verificacion)
        inicio.pack(fill=tk.X, padx=20, pady=20)

        #Label/Boton para ir a Registro

        def on_enter(event):
            registrarse.config(fg='blue', font= underline_font)

        def on_leave(event):
            registrarse.config(fg='black', font=normal_font)

        
        normal_font = font.Font(family="Times", size=12),
        underline_font = font.Font(family="Times", size=12, underline=True)

        registrarse = tk.Label(frame_fill,font=('Times', 12) ,text="Registrarse", bg='white')
        registrarse.place(x=20, y=225)

        registrarse.bind("<Enter>", on_enter)
        registrarse.bind("<Leave>", on_leave)
        registrarse.bind("<Button-1>", lambda event: self.registro())


        #inicio.bind("<Return>", lambda event: self.verificacion())


        self.ventana.mainloop()
    

        














































































































