from tkinter import *

ventana = Tk()

etiqueta = Label(ventana, text="primero", bg="red", fg="black")
etiqueta.pack(padx = 5, pady = 20, side = LEFT, fill=BOTH , expand = True)

etiqueta = Label(ventana, text="SEGUNDO", bg="green", fg="white")
etiqueta.pack(padx = 5, pady = 20, side = LEFT, fill=BOTH , expand = True)

etiqueta = Label(ventana, text="tercero", bg="blue", fg="orange")
etiqueta.pack(padx = 5, pady = 20, side = LEFT, fill=BOTH , expand = True)

ventana.mainloop()
