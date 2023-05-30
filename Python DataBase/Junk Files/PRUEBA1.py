import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.minsize(300, 300)
root.geometry("1000x700")

s = ttk.Style()
# Alineadas a la izquierda.
s.configure('TNotebook', tabposition='w')

box = ttk.Notebook(root, width=1000, height=650)

tab1 = tk.Frame(root)
tab2 = tk.Frame(root)
tab3 = tk.Frame(root)

box.add(tab1, text="tab1")
box.add(tab2, text="tab2")
box.add(tab3, text="tab3")

box.pack(side=tk.TOP)

root.mainloop()