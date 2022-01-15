from tkinter import *
from math import *
import parser

root = Tk()
root.title("Calculadora")
display = Entry(root)
display.grid(row= 1, columnspan=6, sticky= W+E)
i = 0

def obtener_numeros(n):
    global i
    display.insert(i,n)
    i+=1

def operaciones(o):
    global i
    longitud_o = len(o)
    display.insert(i,o)
    i+= longitud_o

def limpiar():
    display.delete(0, END)

def eliminar_caracter():
    estado_display = display.get()
    if len(estado_display):
        nuevo_estado = estado_display[:-1]
        limpiar()
        display.insert(0,nuevo_estado)
    else:
        limpiar()
        display.insert(0, "Error")
        
def calcular():
    estado_display = display.get()
    try:
        exp_matematica = parser.expr(estado_display).compile()
        resultado = eval(exp_matematica)
        limpiar()
        display.insert(0,resultado)

    except expression as indentifier: 
        limpiar()
        display.insert(0, "Error")

#Teclado Numerico
Button (root, text="1", command=lambda:obtener_numeros(1)).grid(row=2, column=0, sticky=W+E)
Button(root, text="2", command=lambda:obtener_numeros(2)).grid(row=3, column=0, sticky=W+E)
Button(root, text="3", command=lambda:obtener_numeros(3)).grid(row=4, column=0, sticky=W+E)
Button(root, text="4", command=lambda:obtener_numeros(4)).grid(row=2, column=1, sticky=W+E)
Button(root, text="5", command=lambda:obtener_numeros(5)).grid(row=3, column=1, sticky=W+E)
Button(root, text="6", command=lambda:obtener_numeros(6)).grid(row=4, column=1, sticky=W+E)
Button(root, text="7", command=lambda:obtener_numeros(7)).grid(row=2, column=2, sticky=W+E)
Button(root, text="8", command=lambda:obtener_numeros(8)).grid(row=3, column=2, sticky=W+E)
Button(root, text="9", command=lambda:obtener_numeros(9)).grid(row=4, column=2, sticky=W+E)
Button(root, text="0", command=lambda:obtener_numeros(0)).grid(row=5, column=1, sticky=W+E)
Button(root, text="AC", command=lambda:limpiar()).grid(row=5, column=0, sticky=W+E)
Button(root, text=".").grid(row=5, column=2, sticky=W+E)

#Teclado operaciones basicas
Button(root, text="←", command=lambda:eliminar_caracter()).grid(row=2, column=3,columnspan=2, sticky=W+E)
Button(root, text="+", command=lambda:operaciones("+")).grid(row=3, column=3, sticky=W+E)
Button(root, text="-", command=lambda:operaciones("-")).grid(row=4, column=3, sticky=W+E)
Button(root, text="", command=lambda:operaciones("")).grid(row=5, column=3, sticky=W+E)
Button(root, text="÷", command=lambda:operaciones("÷")).grid(row=3, column=4, sticky=W+E)
Button(root, text="√", command=lambda:operaciones("√")).grid(row=4, column=4, sticky=W+E)
Button(root, text="x²", command=lambda:operaciones("²")).grid(row=5, column=4, sticky=W+E)
Button(root, text=".", command=lambda:operaciones(".")).grid(row=5, column=4, sticky=W+E)
Button(root, text="=", command=lambda:calcular()).grid(row=6, column=0,columnspan=6, sticky=W+E)



root.mainloop()