import tkinter
ventana = tkinter.Tk()
labelPrueba = tkinter.Label(ventana, text = "Calculadora")
ventana.resizable(0,0)
ventana.title("Calculadora Multifuncional")
labelPrueba.pack(side = tkinter.LEFT)
ventana.geometry("500x500")
ventana.mainloop()
Mensaje = tkinter.Label(ventana, text="Prueba 2 y qué ricas las empanadas")