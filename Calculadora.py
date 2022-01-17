from cgitb import text
from distutils import command
from tkinter import *
from re import X
import tkinter as tk
import parser

inicio = tk.Tk()
inicio.title("Inicio Calculadora")
inicio.geometry("500x500+400+80")
inicio.resizable(width=False, height=False)
fondo_inicio = tk.PhotoImage(file="Bienvenido.png")
fondo_inicio1 = tk.Label(inicio, image = fondo_inicio ).place(x=0,y=0, relheight=1, relwidth=1)

#Funcion para cambiar el color
i = 0

def cambiar_color2():
    Boton_Fisica["bg"] = "#E10032"

def cambiar_color3():
    Boton_Quimica["bg"] = "#E10032"

def cambiar_color4():
    Boton_Trigonometria["bg"] = "#E10032"

#Funcion que abre una nueva ventana que conduce a la Calculadora aritmetica
def calculadora_aritmetica():
    Boton_aritmetica["bg"] = "#E10032"
    inicio.withdraw()
    Calc_Aritmetica = tk.Toplevel()
    Calc_Aritmetica.title("Calculadora Aritmetica")
    #Calc_Aritmetica.geometry("500x500+400+80")
    Calc_Aritmetica.resizable(width=False, height=False)
    #fondo_inicio = tk.PhotoImage(file="Bienvenido.png")
    #fondo_inicio1 = tk.Label(Calc_Aritmetica, image = fondo_inicio ).place(x=0,y=0, relheight=1, relwidth=1)
    
    display = Entry(Calc_Aritmetica)
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
    Button(Calc_Aritmetica, text="1", command=lambda:obtener_numeros(1)).grid(row=2, column=0, sticky=W+E)
    Button(Calc_Aritmetica, text="2", command=lambda:obtener_numeros(2)).grid(row=3, column=0, sticky=W+E)
    Button(Calc_Aritmetica, text="3", command=lambda:obtener_numeros(3)).grid(row=4, column=0, sticky=W+E)
    Button(Calc_Aritmetica, text="4", command=lambda:obtener_numeros(4)).grid(row=2, column=1, sticky=W+E)
    Button(Calc_Aritmetica, text="5", command=lambda:obtener_numeros(5)).grid(row=3, column=1, sticky=W+E)
    Button(Calc_Aritmetica, text="6", command=lambda:obtener_numeros(6)).grid(row=4, column=1, sticky=W+E)
    Button(Calc_Aritmetica, text="7", command=lambda:obtener_numeros(7)).grid(row=2, column=2, sticky=W+E)
    Button(Calc_Aritmetica, text="8", command=lambda:obtener_numeros(8)).grid(row=3, column=2, sticky=W+E)
    Button(Calc_Aritmetica, text="9", command=lambda:obtener_numeros(9)).grid(row=4, column=2, sticky=W+E)
    Button(Calc_Aritmetica, text="0", command=lambda:obtener_numeros(0)).grid(row=5, column=1, sticky=W+E)
    Button(Calc_Aritmetica, text="AC", command=lambda:limpiar()).grid(row=5, column=0, sticky=W+E)
    Button(Calc_Aritmetica, text=".").grid(row=5, column=2, sticky=W+E)

    #Teclado operaciones basicas
    Button(Calc_Aritmetica, text="←", command=lambda:eliminar_caracter()).grid(row=2, column=3,columnspan=2, sticky=W+E)
    Button(Calc_Aritmetica, text="+", command=lambda:operaciones("+")).grid(row=3, column=3, sticky=W+E)
    Button(Calc_Aritmetica, text="-", command=lambda:operaciones("-")).grid(row=4, column=3, sticky=W+E)
    Button(Calc_Aritmetica, text="*", command=lambda:operaciones("*")).grid(row=5, column=3, sticky=W+E)
    Button(Calc_Aritmetica, text="÷", command=lambda:operaciones("/")).grid(row=3, column=4, sticky=W+E)
    Button(Calc_Aritmetica, text="√", command=lambda:operaciones("√")).grid(row=4, column=4, sticky=W+E)
    Button(Calc_Aritmetica, text="x²", command=lambda:operaciones("**2")).grid(row=5, column=4, sticky=W+E)
    Button(Calc_Aritmetica, text="=", command=lambda:calcular()).grid(row=6, column=0,columnspan=6, sticky=W+E)
    Calc_Aritmetica.mainloop()




#Botones inicio
Boton_aritmetica =tk.Button(inicio,
 command = calculadora_aritmetica,
 width=22,text="ARITMETICA",
 font="BodoniFLF", 
 cursor="hand2", 
 bg = "#151B25",
 fg="#DBE8E1",
 relief="flat")
Boton_aritmetica.place(x=125, y=235)

Boton_Fisica =tk.Button(inicio, 
 width=22,
 text="FISICA",
 command=cambiar_color2,
 font="BodoniFLF", 
 cursor="hand2", 
 bg = "#151B25", 
 fg="#DBE8E1",
 relief="flat")
Boton_Fisica.place(x=125, y=280)

Boton_Quimica =tk.Button(inicio,
 width=22,
 text="QUIMICA",
 command=cambiar_color3,
 font="BodoniFLF",
 cursor="hand2",
 bg = "#151B25", 
 fg="#DBE8E1",
 relief="flat")
Boton_Quimica.place(x=125, y=325)

Boton_Trigonometria =tk.Button(inicio, 
 width=22,
 text="TRIGONOMETRIA",
 command=cambiar_color4,
 font="BodoniFLF",
 cursor="hand2", 
 bg = "#151B25", 
 fg="#DBE8E1",
 relief="flat")
Boton_Trigonometria.place(x=125, y=370)


inicio.mainloop()
