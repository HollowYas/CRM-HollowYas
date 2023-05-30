import tkinter as tk

# Crear la ventana
root = tk.Tk()

# Crear los widgets
codigo_label = tk.Label(root, text="Código:")
codigo_entry = tk.Entry(root)
producto_label = tk.Label(root, text="Producto:")
producto_entry = tk.Entry(root)
precio_label = tk.Label(root, text="Precio:")
precio_entry = tk.Entry(root)
agregar_button = tk.Button(root, text="Agregar")
lb = tk.Listbox(root, height=5)
lb.configure(columns=("codigo", "producto", "precio"))
lb.column("#0", width=0, stretch=False)
lb.column("codigo", width=50, anchor="w")
lb.column("producto", width=100, anchor="w")
lb.column("precio", width=50, anchor="e")

# Función para agregar un producto al Listbox
def agregar_producto():
    codigo = codigo_entry.get()
    producto = producto_entry.get()
    precio = precio_entry.get()
    lb.insert("", "end", values=(codigo, producto, precio))

    # Limpiar los campos
    codigo_entry.delete(0, tk.END)
    producto_entry.delete(0, tk.END)
    precio_entry.delete(0, tk.END)

# Agregar los widgets a la ventana
codigo_label.grid(row=0, column=0, sticky="e")
codigo_entry.grid(row=0, column=1)
producto_label.grid(row=1, column=0, sticky="e")
producto_entry.grid(row=1, column=1)
precio_label.grid(row=2, column=0, sticky="e")
precio_entry.grid(row=2, column=1)
agregar_button.grid(row=3, column=1, sticky="e")
lb.grid(row=4, column=0, columnspan=2)

# Asociar la función agregar_producto al botón
agregar_button.config(command=agregar_producto)

# Mostrar la ventana
root.mainloop()
