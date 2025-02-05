from tkinter import *

#mi primera ventana
vent1 = Tk()
vent1.title("ETL")
vent1.geometry("400x400")
vent1.configure(bg="beige")


etiqueta = Label(vent1,text="Hola Mundo",font=("Arial",13),bg="beige",fg="blue")
etiqueta.grid(column=0,row=0)

#aqui defino una operacion de cambio
def modificacion():
    etiqueta.configure(text="Texto nuevo",bg="red")

bot = Button(vent1,text='click',font=("Arial",13),bg="gray",fg="black",command=modificacion)
bot.grid(column=0,row=1)

vent1.mainloop()
