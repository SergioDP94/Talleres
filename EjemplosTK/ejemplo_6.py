from tkinter import *

ventana = Tk()

etiqueta = Label(ventana, text="primero", bg="red", fg="black")
etiqueta.grid(column = 0, row = 0, padx = 5, pady = 20)

etiqueta = Label(ventana, text="SEGUNDO", bg="green", fg="white")
etiqueta.grid(column = 0, row = 1, padx = 5, pady = 20)

etiqueta = Label(ventana, text="tercero", bg="blue", fg="orange")
etiqueta.grid(column = 1, row = 0, padx = 5, pady = 20, rowspan = 2, sticky = "nsew")

ventana.mainloop()
