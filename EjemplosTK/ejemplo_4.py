from tkinter import *

ventana = Tk()

etiqueta = Label(ventana, text="primero", bg="red", fg="black")
etiqueta.pack()

etiqueta = Label(ventana, text="SEGUNDO", bg="green", fg="white")
etiqueta.pack()

etiqueta = Label(ventana, text="tercero", bg="blue", fg="orange")
etiqueta.pack()

ventana.mainloop()
