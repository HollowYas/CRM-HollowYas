from tkinter import Tk, Canvas, Label, Frame, Entry, Button, Listbox, END 
from tkinter import W, E, N, S, ttk 
from tkinter import *
import tkinter as tk
import psycopg2

root = Tk()
root.title ("Python Postgre Prueba")

canvas = Canvas(root, height=1000, width=1000)
canvas.pack()

frame = Frame()
frame.place(relx=0.1 , rely= 0.1, relheight= 4.0, relwidth= 9.0)

def Buscar1(codigo):
    
    conex = psycopg2.connect(
    database = "PyDataBase1", 
    user = "postgres", 
    password = "Hayahser15")
    
    cursor = conex.cursor()

    query = '''select * from prueba.articulos where codigo=%s'''
    cursor.execute(query, (codigo))
    row = cursor.fetchone()

    print(row)

    MostrarBusqueda1(row)

    conex.commit()
    conex.close()

def MostrarBusqueda1(row):
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
    print("Datos eliminados")

    conex.commit()
    conex.close()











root.mainloop()
























































































































