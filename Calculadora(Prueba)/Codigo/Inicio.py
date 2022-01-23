from cgitb import text
from distutils import command
from tkinter import *
from re import X
import tkinter as tk
from tkinter import font
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

##########################################    CALCULADORA ARITMETICA   ####################################################
def calculadora_aritmetica():
    Boton_aritmetica["bg"] = "#E10032"
    inicio.withdraw()
    Calc_Aritmetica = tk.Toplevel()
    fondo_aritmetica = tk.PhotoImage(file="Aritmetica.png")
    fondo_aritmetica1 = tk.Label(Calc_Aritmetica, image = fondo_aritmetica ).place(x=0,y=0, relheight=1, relwidth=1)
    Calc_Aritmetica.title("Calculadora Aritmetica")
    Calc_Aritmetica.geometry("539x539+400+80")
    Calc_Aritmetica.resizable(width=False, height=False)
    display = Entry(Calc_Aritmetica, font=("Times New Roman", 40), bg="#DBE8E1", relief="flat")
    

    display.place(x=45, y= 35, width=450, height=100)
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
    Uno = tk.Button(Calc_Aritmetica,font=("Times New Roman",19, font.BOLD),bg = "#DBE8E1",relief="flat", text="1", command=lambda:obtener_numeros(1))
    Uno.place(x=45.5, y=170.5)

    Dos = tk.Button(Calc_Aritmetica,font=("Times New Roman",19, font.BOLD), bg = "#DBE8E1",relief="flat", text="2", command=lambda:obtener_numeros(2))
    Dos.place(x=145.5, y=170.5)

    Tres = tk.Button(Calc_Aritmetica,font=("Times New Roman",19, font.BOLD), bg = "#DBE8E1",relief="flat", text="3", command=lambda:obtener_numeros(3))
    Tres.place(x=245, y=170.5)

    Cuatro = tk.Button(Calc_Aritmetica,font=("Times New Roman",19, font.BOLD),bg = "#DBE8E1",relief="flat", text="4", command=lambda:obtener_numeros(4))
    Cuatro.place(x=45.5, y=270.5)

    Cinco = tk.Button(Calc_Aritmetica,font=("Times New Roman",19, font.BOLD), bg = "#DBE8E1",relief="flat", text="5", command=lambda:obtener_numeros(5))
    Cinco.place(x=145., y=270.5)

    Seis = tk.Button(Calc_Aritmetica,font=("Times New Roman",19, font.BOLD),bg = "#DBE8E1",relief="flat",  text="6", command=lambda:obtener_numeros(6))
    Seis.place(x=245, y=270.5)

    Siete = tk.Button(Calc_Aritmetica,font=("Times New Roman",19, font.BOLD),bg = "#DBE8E1",relief="flat", text="7", command=lambda:obtener_numeros(7))
    Siete.place(x=45.5, y=370.5)

    Ocho = tk.Button(Calc_Aritmetica,font=("Times New Roman",19, font.BOLD),bg = "#DBE8E1", relief="flat",text="8", command=lambda:obtener_numeros(8))
    Ocho.place(x= 145, y=370.5)

    Nueve = tk.Button(Calc_Aritmetica,font=("Times New Roman",19, font.BOLD),bg = "#DBE8E1",relief="flat", text="9", command=lambda:obtener_numeros(9))
    Nueve.place(x= 243, y=370.5)

    Cero = tk.Button(Calc_Aritmetica,font=("Times New Roman",19, font.BOLD),bg = "#DBE8E1",relief="flat", text="0", command=lambda:obtener_numeros(0))
    Cero.place(x=46, y= 469)

    AC = tk.Button(Calc_Aritmetica,font=("Times New Roman",15, font.BOLD),bg = "#DBE8E1",relief="flat", text="AC", command=lambda:limpiar())
    AC.place(x=138.5, y=475)

    Punto = tk.Button(Calc_Aritmetica,font=("Times New Roman",19, font.BOLD),bg = "#DBE8E1",relief="flat", text=".")
    Punto.place(x=248, y=468)

    #Teclado operaciones basicas
    Eliminar = tk.Button(Calc_Aritmetica,font=("Times New Roman",20, font.BOLD),bg = "#DBE8E1", text="⟵",relief="flat", command=lambda:eliminar_caracter())
    Eliminar.place(x=375, y=170)
    
    Mas = tk.Button(Calc_Aritmetica,font=("Times New Roman",19, font.BOLD),bg = "#DBE8E1", text="+",relief="flat", command=lambda:operaciones("+"))
    Mas.place(x=343, y=270.5)

    Menos = tk.Button(Calc_Aritmetica,font=("Times New Roman",19, font.BOLD),bg = "#DBE8E1", text="-",relief="flat", command=lambda:operaciones("-"))
    Menos.place(x=345, y=368)

    Multi = tk.Button(Calc_Aritmetica,font=("Times New Roman",19, font.BOLD),bg = "#DBE8E1", text="×",relief="flat", command=lambda:operaciones("*"))
    Multi.place(x=440, y= 270.5)

    Div = tk.Button(Calc_Aritmetica,font=("Times New Roman",19, font.BOLD),bg = "#DBE8E1", text="÷",relief="flat", command=lambda:operaciones("/"))
    Div.place(x=440, y=370)

    Pot = tk.Button(Calc_Aritmetica,font=("Times New Roman",17, font.BOLD),bg = "#DBE8E1", text="X²",relief="flat", command=lambda:operaciones("**2"))
    Pot.place(x= 341, y= 471) 

    Igual = tk.Button(Calc_Aritmetica,font=("Times New Roman",19, font.BOLD),bg = "#DBE8E1", text="=",relief="flat", command=lambda:calcular())
    Igual.place(x=440, y=468)
    
    Calc_Aritmetica.mainloop()
    








######################################   SECCION BOTONES PESTAÑA INICIO   #####################################################
#Botones inicio
Boton_aritmetica =tk.Button(inicio,
 command = calculadora_aritmetica,
 width=22,text="ARITMETICA",
 font="BodoniFLF", 
 cursor="hand2", 
 bg = "#151B25",
 fg="#DBE8E1",
 relief="flat"
 )
Boton_aritmetica.place(x=125, y=235)


Boton_Fisica =tk.Button(inicio, 
 width=25,
 text="CONVERSION DE UNIDADES",
 command=cambiar_color2,
 font="BodoniFLF", 
 cursor="hand2", 
 bg = "#151B25", 
 fg="#DBE8E1",
 relief="flat")
Boton_Fisica.place(x=116, y=280)

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
