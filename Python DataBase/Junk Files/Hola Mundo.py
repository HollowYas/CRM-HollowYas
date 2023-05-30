import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
        

class Ventana:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1920x1440+0+0")
        
        foto = PhotoImage(file="Imagenes/Midnight Embers.png")
        foto1 = foto.subsample(2)
        #self.resizedimage = foto.resize((foto.width//5, foto.height//5)) 

        self.lbl_imagen1 = ttk.Label(self.root, image = foto1)
        self.lbl_imagen1.pack()
      
        self.btn1 = tk.Button(self.root, text = "Abrir ventana",command = self.openw)
        self.btn1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        #self.btn1.pack()

        self.root.mainloop()
        
    def openw(self):
        self.root.destroy()       
        ventana_secundaria = Figura()
        #self.root.geometry("1440x720")
                          
       #self.btn1.pack()
        
        #===========================================================================
class Figura:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("1368x720+0+0")

        foto2 = PhotoImage(file = "Imagenes/fotoooo.png")
        foto3 = foto2.subsample(2)
        
        self.lbl_imagen2 = ttk.Label(self.ventana, image = foto3)
        self.lbl_imagen2.pack()

        # etiqueta = tk.Label(self.ventana, text="¡Hola, mundo!")
        # etiqueta.pack()
     
        self.ventana.mainloop()   
        

        
if __name__=='__main__':
    app = Ventana()













































































