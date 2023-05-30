import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from tkinter import font
import util.generic as utl


class Registro:

     def ventanaprincipal(self):
        from Formulario.form_login import Aplicacion
        self.ventana.destroy()
        Aplicacion()
    
     def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Registro')
        self.ventana.geometry('350x350')
        self.ventana.config(bg='#323232')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 350,350)

        btn_registro=tk.Button(self.ventana,text="Registrado", command=self.ventanaprincipal)
        btn_registro.place(x=145, y=135, width=65, height=45)




# def accion():
#     print("¡Se hizo clic en el label!")

# ventana = tk.Tk()

# def on_enter(event):
#     label.config(fg='blue')

# def on_leave(event):
#     label.config(fg='black')

# label = tk.Label(ventana, text="Haz clic aquí", fg='black')
# label.pack()

# label.bind("<Enter>", on_enter)
# label.bind("<Leave>", on_leave)
# label.bind("<Button-1>", lambda event: accion())

# ventana.mainloop()




# def on_enter(event):
#     label.config(font=underline_font)

# def on_leave(event):
#     label.config(font=normal_font)

# ventana = tk.Tk()

# normal_font = font.Font(family="Helvetica", size=12)
# underline_font = font.Font(family="Helvetica", size=12, underline=True)

# label = tk.Label(ventana, text="Haz clic aquí", font=normal_font)
# label.pack()

# label.bind("<Enter>", on_enter)
# label.bind("<Leave>", on_leave)

# ventana.mainloop()






































