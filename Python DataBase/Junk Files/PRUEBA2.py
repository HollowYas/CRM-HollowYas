import tkinter as tk

def mostrar_contenido(pestaña):
    # Borra el contenido existente en el marco de contenido
    for widget in marco_contenido.winfo_children():
        widget.destroy()

    # Muestra el contenido correspondiente a la pestaña seleccionada
    if pestaña == 1:
        contenido_etiqueta = tk.Label(marco_contenido, text='Contenido de la Pestaña 1', padx=10, pady=10)
        contenido_etiqueta.pack()
    elif pestaña == 2:
        contenido_etiqueta = tk.Label(marco_contenido, text='Contenido de la Pestaña 2', padx=10, pady=10)
        contenido_etiqueta.pack()
    elif pestaña == 3:
        contenido_etiqueta = tk.Label(marco_contenido, text='Contenido de la Pestaña 3', padx=10, pady=10)
        contenido_etiqueta.pack()

# Crear la ventana principal
ventana = tk.Tk()

# Crear el marco principal
marco_principal = tk.Frame(ventana)
marco_principal.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Crear el marco de la pestaña lateral
marco_pestaña_lateral = tk.Frame(marco_principal, width=200, bg='gray')
marco_pestaña_lateral.pack(side=tk.LEFT, fill=tk.Y)

# Crear botones como pestañas
boton_pestaña1 = tk.Button(marco_pestaña_lateral, text='Pestaña 1', bg='gray', padx=10, pady=10, command=lambda: mostrar_contenido(1))
boton_pestaña1.pack()

boton_pestaña2 = tk.Button(marco_pestaña_lateral, text='Pestaña 2', bg='gray', padx=10, pady=10, command=lambda: mostrar_contenido(2))
boton_pestaña2.pack()

boton_pestaña3 = tk.Button(marco_pestaña_lateral, text='Pestaña 3', bg='gray', padx=10, pady=10, command=lambda: mostrar_contenido(3))
boton_pestaña3.pack()

# Crear el marco del contenido principal
marco_contenido = tk.Frame(marco_principal, bg='white')
marco_contenido.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Mostrar contenido inicial
mostrar_contenido(1)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
