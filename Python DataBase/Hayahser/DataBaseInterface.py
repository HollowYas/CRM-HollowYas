from tkinter import Tk, Canvas, Label, Frame, Entry, Button, Listbox, END 
from tkinter import W, E, N, S, ttk 
from tkinter import *
import tkinter as tk
import psycopg2
#from Menu import menu


root = Tk()
root.title ("Python Postgre Prueba")

#####################################################
#Creacion de la conexion a la base de datos

#Creacion de las funciones para guardar, buscar y mostrar los datos
def GuardarDatos(codigo, nombre, precio, tipo):

    conex = psycopg2.connect(
        database = "PyDataBase1", 
        user = "postgres", 
        password = "Hayahser15")
    
    cursor = conex.cursor()

    query = '''INSERT INTO prueba.articulos(codigo, nombre, precio, tipo) VALUES (%s, %s, %s, %s)'''
    cursor.execute(query, (codigo, nombre, precio, tipo))
    print("Datos Almacenados")
    conex.commit()
    conex.close()

    MostrarDatos()

   

    # print("El codigo es: ", codigo)
    # print("El nombre del producto es: ", nombre)
    # print("El precio del producto es: ", precio)
    # print("El tipo de producto es: ", tipo)
    
def MostrarDatos():
    conex = psycopg2.connect(
        database = "PyDataBase1", 
        user = "postgres", 
        password = "Hayahser15")
    
    cursor = conex.cursor()

    query = '''select * from prueba.articulos'''
    cursor.execute(query)
    row = cursor.fetchall()

    # # Creamos una tabla usando Treeview
    # tree = ttk.Treeview(frame, columns=("1","2","3","4"))
    # tree.column
    # tree.grid(row=10, columnspan=4, sticky=W+E)

    # # # Definimos el encabezado de la tabla
    # tree.heading(1, text="ID")
    # tree.heading(2, text="Nombre")
    # tree.heading(3, text="Descripción")
    # tree.heading(4, text="Precio")

    listbox = Listbox(frame, width=30, height=5)
    listbox.place(x=0.05, y=250)

    for x in row:
        # tree.insert("", END, values=(row[0], row[1], row[2], row[3]))
        listbox.insert(END, x)


    conex.commit()
    conex.close()

def Buscar(codigo):

    conex = psycopg2.connect(
    database = "PyDataBase1", 
    user = "postgres", 
    password = "Hayahser15")
    
    cursor = conex.cursor()

    query = '''select * from prueba.articulos where codigo=%s'''
    cursor.execute(query, (codigo))
    row = cursor.fetchone()

    print(row)

    MostrarBusqueda(row)

    conex.commit()
    conex.close()



    #print(codigo)   

def MostrarBusqueda(row):
    listobow = Listbox(frame, width=20, height=1)
    listobow.grid(row=9, columnspan=4, sticky=W+E)
    listobow.insert(END, row)

def BorrarDatos(codigo):
    
    conex = psycopg2.connect(
        database = "PyDataBase1", 
        user = "postgres", 
        password = "Hayahser15")
    
    cursor = conex.cursor()

    query = '''delete from prueba.articulos where codigo = %s'''
    cursor.execute(query, (codigo))
    #row = cursor.fetchall()

    print("Datos eliminados")

    #listbox = Listbox(frame, width=30, height=5)
    #listbox.place(x=0.05, y=250)

    #for x in row:
        # tree.insert("", END, values=(row[0], row[1], row[2], row[3]))
        #listbox.insert(END, x)

    conex.commit()
    conex.close()




#####################################################
#Canvas
canvas = Canvas(root, height=1000, width=1000)
canvas.pack()

frame = Frame()
frame.place(relx=0.1 , rely= 0.1, relheight= 4.0, relwidth= 9.0)

label = Label(frame, text="BASE DE DATOS ARTICULO")
label.place(x=100, y=100)

label = Label(frame, text="" )
label.grid(row=1, column=0, sticky="W")


#####################################################
#Ingresar el codigo
label = Label(frame, text= "Ingrese el codigo")
label.grid(row=2, column=0, sticky="w")

#Entry para poder ingresar un dato en codigo
entry_codigo = Entry(frame)
entry_codigo.grid(row=2, column=1, sticky="w")

#####################################################
#Ingresar el nombre
label = Label(frame, text= "Ingrese el producto")
label.grid(row=3, column=0, sticky="w")

entry_nombre = Entry(frame)
entry_nombre.grid(row=3, column=1, sticky="w")

#####################################################
#Ingresar el tipo de articulo(fruta, verdura, etc...)

label = Label(frame, text= "Ingrese el tipo")
label.grid(row=4, column=0, sticky="w")
#----------------------------------------------------------------------------------------------
# # Variable de control para la opción seleccionada
# opcselec = tk.StringVar(root)
# opcselec.set("")

# # Menu de opciones
# opciones = ["Frutas", "Verduras", "Tuberculos", "Hortalizas"]

# # Funcion para manejar la seleccion de una opcion
# def opcion_seleccionada_cambio(*args):
#     print("Opcion Seleccionada:", opcselec.get())

# # Crear el Option enu
# opc_menu = tk.OptionMenu(root, opcselec, *opciones, command=opcion_seleccionada_cambio)
# opc_menu.pack(side="top")
#----------------------------------------------------------------------------------------------
entry_tipo = Entry(frame)
entry_tipo.grid(row=4, column=1, sticky="w")

#####################################################
#Ingresar el precio del articulo
label = Label(frame, text= "Ingrese el precio")
label.grid(row=5, column=0, sticky="w")

entry_precio = Entry(frame)
entry_precio.grid(row=5, column=1, sticky="w")


#####################################################
#Creacion del boton Agregar
boton = Button(frame, text="AGREGAR" ,command=lambda:GuardarDatos(entry_codigo.get(), entry_nombre.get(), entry_precio.get(), entry_tipo.get()))
boton.grid(row=6,column=1, sticky=W+E)

#++++++++++++++++++++++++++++++++++++++++++++++++++++
#Creacion del boton Buscar
label = Label(frame, text="")
label.grid(row=7, column=0)

label = Label(frame, text="Buscar por Codigo")
label.grid(row = 8, column = 0)

entry_buscar = Entry(frame)
entry_buscar.grid(row=8, column=1, sticky="W")

boton = Button(frame, text="BUSCAR", command=lambda:Buscar(entry_buscar.get()))
boton.grid(row=8,column=2, sticky=W)


label = Label(frame, text="Borrar por Codigo")
label.place(x=1, y=223)

entry_borrar = Entry(frame)
entry_borrar.place(x=108, y=223)

boton = Button(frame, text="BORRAR", command=lambda:BorrarDatos(entry_borrar.get()))
boton.place(x=255, y=223)




MostrarDatos()
root.mainloop()


































































































































































































