from tkinter import *

ventana = Tk()

etiqueta = Label(ventana, text="a", bg="red", fg="black")
etiqueta.place(x = 0, y = 0, width = 40)

etiqueta = Label(ventana, text="b", bg="green", fg="white")
etiqueta.place(x = 41, y = 22, width = 40)

etiqueta = Label(ventana, text="c", bg="blue", fg="orange")
etiqueta.place(x = 82, y = 44, width = 40)

ventana.mainloop()
