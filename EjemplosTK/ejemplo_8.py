from tkinter import *

ventana = Tk()
ventana.title("Projecto 1")
ventana.geometry("250x200")
ventana.configure(bg="beige")

etiqueta_v = Label(ventana, text="Voltaje",font=("Arial",13), bg="beige", fg="black")
etiqueta_v.grid(column = 0, row = 0, sticky = "w")

volt = Entry(ventana,font=("Arial",13),fg="blue")
volt.grid(column=1,row=0)

etiqueta_c = Label(ventana, text="Corriente",font=("Arial",13), bg="beige", fg="black")
etiqueta_c.grid(column = 0, row = 1, sticky = "w")

corr = Entry(ventana,font=("Arial",13),fg="blue")
corr.grid(column=1,row=1)


etiqueta_p = Label(ventana, text="Potencia",font=("Arial",13), bg="beige", fg="black")
etiqueta_p.grid(column = 0, row = 2, sticky = "w")

potencia = Label(ventana,font=("Arial",13),fg="blue")
potencia.grid(column=1,row=2)


etiqueta_r = Label(ventana, text="Resistencia",font=("Arial",13), bg="beige", fg="black")
etiqueta_r.grid(column = 0, row = 3, sticky = "w")

resis = Label(ventana,font=("Arial",13),fg="blue")
resis.grid(column=1, row=3)

def procesar():
    potencia.configure(text=str(eval(volt.get())*eval(corr.get())))
    resis.configure(text=str(eval(volt.get())/eval(corr.get())))

def reset():
    volt.delete(0,END)
    corr.delete(0,END)
    potencia.configure(text="")
    resis.configure(text="")

boton_p = Button(ventana,text="Procesar",font=("Arial",13),command=procesar)
boton_p.grid(column=1,row=4)

boton_l = Button(ventana,text="Limpiar",font=("Arial",13),command=reset)
boton_l.grid(column=1,row=5)

ventana.mainloop()
