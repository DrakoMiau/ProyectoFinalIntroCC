
import sys
from tkinter import * 
import tkinter as tk
from tkinter import font
import parser
import tkinter.font as fnt

i = 0

def pantalla_inicio():
    global p_inicio
    inicio.withdraw()
    p_inicio = tk.Toplevel()
    p_inicio.title("Inicio Calculadora")
    p_inicio.geometry("500x500+400+80")
    p_inicio.resizable(width=False, height=False)
    fondo_inicio = tk.PhotoImage(file="Bienvenido.png")
    fondo_inicio1 = tk.Label(p_inicio, image = fondo_inicio ).place(x=0,y=0, relheight=1, relwidth=1)


    Boton_Fisica =tk.Button(p_inicio, 
    width=25,
    text="CONVERSION DE UNIDADES",
    font="BodoniFLF", 
    command=conversion_unidades,
    cursor="hand2", 
    bg = "#151B25", 
    fg="#DBE8E1",
    relief="flat")
    Boton_Fisica.place(x=116, y=280)


    Boton_aritmetica =tk.Button(p_inicio,
    command = calculadora_aritmetica,
    width=22,
    text="ARITMETICA",
    font="BodoniFLF", 
    cursor="hand2", 
    bg = "#151B25",
    fg="#DBE8E1",
    relief="flat"        )
    Boton_aritmetica.place(x=125, y=235)
    
    p_inicio.mainloop()
#######################################    CALCULADORA ARITMETICA   ############################################
def calculadora_aritmetica():
    p_inicio.withdraw()
    Calc_Aritmetica = tk.Toplevel()
    fondo_aritmetica = tk.PhotoImage(file="Aritmetica.png")
    fondo_aritmetica1 = tk.Label(Calc_Aritmetica, image = fondo_aritmetica ).place(x=0,y=0, relheight=1, relwidth=1)
    Calc_Aritmetica.title("Calculadora Aritmetica")
    Calc_Aritmetica.geometry("539x565+361+80")
    Calc_Aritmetica.resizable(width=False, height=False)
    display = Entry(Calc_Aritmetica, font=("Bodoni", 40), bg="#DBE8E1", relief="flat")
    display.place(x=45, y= 35, width=450, height=100)

    def factorial(n):   
        return 1 if (n==1 or n==0) else n * factorial(n - 1); 

    def calculate():
        result=factorial(int(display.get()))
        limpiar()
        display.insert(0,result)

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

            
    def calcular():
        estado_display = display.get()
        try:
            exp_matematica = parser.expr(estado_display).compile()
            resultado = eval(exp_matematica)
            limpiar()
            display.insert(0,resultado)
        except: 
            limpiar()


    #Teclado Numerico
    Uno = tk.Button(Calc_Aritmetica,font=("Bodoni",18, font.BOLD),bg = "#DBE8E1",relief="flat", text="1", command=lambda:obtener_numeros(1))
    Uno.place(x=45.5, y=172)

    Dos = tk.Button(Calc_Aritmetica,font=("Bodoni",18, font.BOLD), bg = "#DBE8E1",relief="flat", text="2", command=lambda:obtener_numeros(2))
    Dos.place(x=145.5, y=172)

    Tres = tk.Button(Calc_Aritmetica,font=("Bodoni",18, font.BOLD), bg = "#DBE8E1",relief="flat", text="3", command=lambda:obtener_numeros(3))
    Tres.place(x=243, y=172)

    Cuatro = tk.Button(Calc_Aritmetica,font=("Bodoni",18, font.BOLD),bg = "#DBE8E1",relief="flat", text="4", command=lambda:obtener_numeros(4))
    Cuatro.place(x=45.5, y=270.5)

    Cinco = tk.Button(Calc_Aritmetica,font=("Bodoni",18, font.BOLD), bg = "#DBE8E1",relief="flat", text="5", command=lambda:obtener_numeros(5))
    Cinco.place(x=145., y=270.5)

    Seis = tk.Button(Calc_Aritmetica,font=("Bodoni",18, font.BOLD),bg = "#DBE8E1",relief="flat",  text="6", command=lambda:obtener_numeros(6))
    Seis.place(x=245, y=270.5)

    Siete = tk.Button(Calc_Aritmetica,font=("Bodoni",18, font.BOLD),bg = "#DBE8E1",relief="flat", text="7", command=lambda:obtener_numeros(7))
    Siete.place(x=45.5, y=370.5)

    Ocho = tk.Button(Calc_Aritmetica,font=("Bodoni",18, font.BOLD),bg = "#DBE8E1", relief="flat",text="8", command=lambda:obtener_numeros(8))
    Ocho.place(x= 145, y=370.5)

    Nueve = tk.Button(Calc_Aritmetica,font=("Bodoni",18, font.BOLD),bg = "#DBE8E1",relief="flat", text="9", command=lambda:obtener_numeros(9))
    Nueve.place(x= 243, y=370.5)

    Cero = tk.Button(Calc_Aritmetica,font=("Bodoni",18, font.BOLD),bg = "#DBE8E1",relief="flat", text="0", command=lambda:obtener_numeros(0))
    Cero.place(x=46, y= 469)

    AC = tk.Button(Calc_Aritmetica,font=("Bodoni",15, font.BOLD),bg = "#DBE8E1",relief="flat", text="AC", command=lambda:limpiar())
    AC.place(x=140, y=474)

    Punto = tk.Button(Calc_Aritmetica,font=("Bodoni",18, font.BOLD),bg = "#DBE8E1",relief="flat", text=".", command=lambda:obtener_numeros("."))
    Punto.place(x=248, y=468)

    #Teclado operaciones basicas
    Eliminar = tk.Button(Calc_Aritmetica,font=("Bodoni",19, font.BOLD),bg = "#DBE8E1", text="⟵",relief="flat", command=lambda:eliminar_caracter())
    Eliminar.place(x=375, y=171)
    
    Mas = tk.Button(Calc_Aritmetica,font=("Bodoni",18, font.BOLD),bg = "#DBE8E1", text="+",relief="flat", command=lambda:operaciones("+"))
    Mas.place(x=341, y=272)

    Menos = tk.Button(Calc_Aritmetica,font=("Bodoni",18, font.BOLD),bg = "#DBE8E1", text="-",relief="flat", command=lambda:operaciones("-"))
    Menos.place(x=345, y=368)

    Multi = tk.Button(Calc_Aritmetica,font=("Bodoni",18, font.BOLD),bg = "#DBE8E1", text="×",relief="flat", command=lambda:operaciones("*"))
    Multi.place(x=440, y= 272)

    Div = tk.Button(Calc_Aritmetica,font=("Bodoni",18, font.BOLD),bg = "#DBE8E1", text="÷",relief="flat", command=lambda:operaciones("/"))
    Div.place(x=440, y=370)

    Pot = tk.Button(Calc_Aritmetica,font=("Bodoni",16, font.BOLD),bg = "#DBE8E1", text="!",relief="flat", command=calculate)
    Pot.place(x= 341, y= 471) 

    Igual = tk.Button(Calc_Aritmetica,font=("Bodoni",18, font.BOLD),bg = "#DBE8E1", text="=",relief="flat", command=lambda:calcular())
    Igual.place(x=440, y=468)

    atras = tk.Button(Calc_Aritmetica,fg="#E10032" , bg = "#DBE8E1",font = fnt.Font(size = 6), text="VOLVER",relief="flat", command=lambda:[p_inicio.deiconify(),pantalla_inicio,Calc_Aritmetica.destroy() ])
    atras.place(x=18, y=537)
    Calc_Aritmetica.mainloop()
###################################################################################################################
###############################################################################################################
#######################################   SECCION DE CONVERSIONES    ##################################################################   
def conversion_unidades():
    global conversion_unidades1
    p_inicio.withdraw()
    conversion_unidades1 = tk.Toplevel()
    conversion_unidades1.title("Conversion de Unidades")
    fondo_conversion = tk.PhotoImage(file="Conversion.png")
    fondo_conversion1 = tk.Label(conversion_unidades1, image = fondo_conversion ).place(x=0,y=0, relheight=1, relwidth=1)
    conversion_unidades1.title("Conversion de Unidades")
    conversion_unidades1.geometry("500x500+400+80")
    conversion_unidades1.resizable(width=False, height=False)

    Temperatura =tk.Button(conversion_unidades1,
    command = unidades_temp,
    width=22,text="Unidades de Temperatura",
    font="BodoniFLF", 
    cursor="hand2", 
    bg = "#DBE8E1",
    fg="#E10032",
    relief="flat")
    Temperatura.place(x=125, y=90)

    Energia =tk.Button(conversion_unidades1,
    command = unidades_ene,
    width=22,text="Unidades de Energia",
    font="BodoniFLF", 
    cursor="hand2", 
    bg = "#DBE8E1",
    fg="#E10032",
    relief="flat")
    Energia.place(x=125, y=180)

    Longitud =tk.Button(conversion_unidades1,
    command = unidades_longitud,
    width=22,text="Unidades de Longitud",
    font="BodoniFLF", 
    cursor="hand2", 
    bg = "#DBE8E1",
    fg="#E10032",
    relief="flat")
    Longitud.place(x=125, y=270)

    Volumen =tk.Button(conversion_unidades1,
    command = unidades_volumen,
    width=22,text="Unidades de Volumen",
    font="BodoniFLF", 
    cursor="hand2", 
    bg = "#DBE8E1",
    fg="#E10032",
    relief="flat")
    Volumen.place(x=125, y=360)
    conversion_unidades1.mainloop()
###################################################################################################################
###############################################################################################################
###############################################################################################################   
def unidades_temp():
    global VentanaTemp
    conversion_unidades1.withdraw()
    VentanaTemp = tk.Toplevel()
    fondo_VentanaTemp = tk.PhotoImage(file="Temp.png")
    fondo_ub = tk.Label(VentanaTemp, image=fondo_VentanaTemp).place(x=0, y=0, relheight=1, relwidth=1)
    VentanaTemp.title("Conversion unidades de Temperatura")
    VentanaTemp.geometry("500x500+400+80")
    VentanaTemp.resizable(width=False, height=False)
    Titulo = tk.Label(VentanaTemp,text=("UNIDADES DE TEMPERATURA"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=115, y=75)

    btn_celsius = tk.Button(VentanaTemp,
     width=12,
     text="CELSIUS",
     font="Bodoni",
     command= celsius,
     cursor="hand2",
     bg="#DBE8E1",
     fg="#E10032",
     relief="flat")
    btn_celsius.place(x=180, y=245)

    btn_farenheit = tk.Button(VentanaTemp,
     width=12,
     text="FARENHEIT",
     font="Bodoni",
     command= farenheit,
     cursor="hand2",
     bg="#DBE8E1",
     fg="#E10032",
     relief="flat")
    btn_farenheit.place(x=180, y=312)

    btn_farenheit = tk.Button(VentanaTemp,
     width=12,
     text="KELVIN",
     font="Bodoni",
     command= Kelvin,
     cursor="hand2",
     bg="#DBE8E1",
     fg="#E10032",
     relief="flat")
    btn_farenheit.place(x=180, y=378)

    btn_volver = tk.Button(VentanaTemp,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[conversion_unidades1.deiconify(), conversion_unidades, VentanaTemp.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)  

    VentanaTemp.mainloop()
def celsius():
    VentanaTemp.withdraw()
    Ventana_Celsius = tk.Toplevel()
    Ventana_Celsius.geometry("500x500+400+80")
    Ventana_Celsius.title("Conversion de Grados Celsius")
    Ventana_Celsius.resizable(width=False, height=False)
    Fondo_Ventana_Celsius = tk.PhotoImage(file="Conversion2.png")
    Fondo_ub_Celsius = tk.Label(Ventana_Celsius,image=Fondo_Ventana_Celsius).place(x=0, y=0, relheight=1, relwidth=1)
    Titulo = tk.Label(Ventana_Celsius,text=("CELSIUS"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=210, y=75)
    numero1 = tk.StringVar()
    numero2 = tk.StringVar()

    Texto1 = tk.Label(Ventana_Celsius,text=("Digite el valor en Celsius"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto1.place(x=65, y=145)

    Texto2 = tk.Label(Ventana_Celsius,text=("Resultado en Farenheit"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto2.place(x=280, y=145)

    Texto3 = tk.Label(Ventana_Celsius,text=("Digite el valor en Celsius"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto3.place(x=65, y=294)

    Texto4 = tk.Label(Ventana_Celsius,text=("Resultado en Kelvin"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto4.place(x=280, y=294)

    entrada1 = Entry(Ventana_Celsius,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero1)
    entrada1.place(x=69, y=174)

    entrada2 = Entry(Ventana_Celsius,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero2)
    entrada2.place(x=69, y=330)

    salida1 =  tk.Entry(Ventana_Celsius,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida1.place(x=280, y=175)

    salida2 =  tk.Entry(Ventana_Celsius,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida2.place(x=280, y=330)


    def conversion1():
        salida1.delete(0, END)
        num = int(numero1.get())
        resultado = (num*9/5)+32
        salida1.insert(0,resultado)

    def conversion2():
        salida2.delete(0, END)
        num = int(numero2.get())
        resultado =  num+273.15
        salida2.insert(0,resultado)

    btn_volver = tk.Button(Ventana_Celsius,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[VentanaTemp.deiconify(),unidades_temp,Ventana_Celsius.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)   
   
    
    btn_conversion1 = tk.Button(Ventana_Celsius,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion1.place(x= 215, y= 227)

    btn_conversion2 = tk.Button(Ventana_Celsius,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion2,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion2.place(x= 215, y= 380)

    Ventana_Celsius.mainloop()
def farenheit():
    VentanaTemp.withdraw()
    Ventana_farenheit = tk.Toplevel()
    Ventana_farenheit.geometry("500x500+400+80")
    Ventana_farenheit.title("Conversion de Grados Farenheit")
    Ventana_farenheit.resizable(width="false", height="false" )
    Fondo_Ventana_farenheit = tk.PhotoImage(file="Conversion2.png")
    Fondo_ub_Celsius = tk.Label(Ventana_farenheit,image=Fondo_Ventana_farenheit).place(x=0, y=0, relheight=1, relwidth=1)
    Titulo = tk.Label(Ventana_farenheit,text=("FARENHEIT"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=205, y=75)
    numero1 = tk.StringVar()
    numero2 = tk.StringVar()
    

    Texto1 = tk.Label(Ventana_farenheit,text=("Digite el valor en Farenheit"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto1.place(x=65, y=145)

    Texto2 = tk.Label(Ventana_farenheit,text=("Resultado en Celsius"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto2.place(x=280, y=145)

    Texto3 = tk.Label(Ventana_farenheit,text=("Digite el valor en Farenheit"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto3.place(x=65, y=294)

    Texto4 = tk.Label(Ventana_farenheit,text=("Resultado en Kelvin"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto4.place(x=280, y=294)

    entrada1 = Entry(Ventana_farenheit,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero1)
    entrada1.place(x=69, y=174)

    entrada2 = Entry(Ventana_farenheit,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero2)
    entrada2.place(x=69, y=330)

    salida1 =  tk.Entry(Ventana_farenheit,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida1.place(x=280, y=175)

    salida2 =  tk.Entry(Ventana_farenheit,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida2.place(x=280, y=330)

    def conversion1():
        salida1.delete(0, END)
        num = int(numero1.get())
        resultado = (num-32)*5/9
        salida1.insert(0,resultado)

    def conversion2():
        salida2.delete(0, END)
        num = int(numero2.get())
        resultado = (num-32)*5/9+273.15
        salida2.insert(0,resultado)

    btn_volver = tk.Button(Ventana_farenheit,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[VentanaTemp.deiconify(),unidades_temp, Ventana_farenheit.destoy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)   
    
    
    btn_conversion1 = tk.Button(Ventana_farenheit,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion1.place(x= 215, y= 227)

    btn_conversion2 = tk.Button(Ventana_farenheit,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion2,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion2.place(x= 215, y= 380)

    Ventana_farenheit.mainloop()
def Kelvin():
    VentanaTemp.withdraw()
    Ventana_Kelvin = tk.Toplevel()
    Ventana_Kelvin.geometry("500x500+400+80")
    Ventana_Kelvin.resizable(height="false", width="false")
    Ventana_Kelvin.title("Conversion de Grados Kelvin")
    Fondo_Ventana_Kelvin = tk.PhotoImage(file="Conversion2.png")
    Fondo_ub_Celsius = tk.Label(Ventana_Kelvin,image=Fondo_Ventana_Kelvin).place(x=0, y=0, relheight=1, relwidth=1)
    Titulo = tk.Label(Ventana_Kelvin,text=("KELVIN"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=215, y=75)
    numero1 = tk.StringVar()
    numero2 = tk.StringVar()

    Texto1 = tk.Label(Ventana_Kelvin,text=("Digite el valor en Kelvin"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto1.place(x=65, y=145)

    Texto2 = tk.Label(Ventana_Kelvin,text=("Resultado en Farenheit"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto2.place(x=280, y=145)

    Texto3 = tk.Label(Ventana_Kelvin,text=("Digite el valor en Kelvin"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto3.place(x=65, y=294)

    Texto4 = tk.Label(Ventana_Kelvin,text=("Resultado en Celsius"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto4.place(x=280, y=294)

    entrada1 = Entry(Ventana_Kelvin,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero1)
    entrada1.place(x=69, y=174)

    entrada2 = Entry(Ventana_Kelvin,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero2)
    entrada2.place(x=69, y=330)

    salida1 =  tk.Entry(Ventana_Kelvin,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida1.place(x=280, y=175)

    salida2 =  tk.Entry(Ventana_Kelvin,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida2.place(x=280, y=330)


    def conversion1():
        salida1.delete(0, END)
        num = int(numero1.get())
        resultado = (num-273.15)*9/5+32
        salida1.insert(0,resultado)

    def conversion2():
        salida2.delete(0, END)
        num = int(numero2.get())
        resultado = num-273.15
        salida2.insert(0,resultado)

    btn_volver = tk.Button(Ventana_Kelvin,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[VentanaTemp.decoinify(),unidades_temp, Ventana_Kelvin.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)  
    
    btn_conversion1 = tk.Button(Ventana_Kelvin,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion1.place(x= 215, y= 227)

    btn_conversion2 = tk.Button(Ventana_Kelvin,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion2,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion2.place(x= 215, y= 380)
    Ventana_Kelvin.mainloop()

###################################################################################################################
###############################################################################################################
###############################################################################################################
def unidades_ene():
    global Ventana_Energia1
    conversion_unidades1.withdraw()
    Ventana_Energia1 = tk.Toplevel()
    Ventana_Energia1.title("Conversion Unidades de Energia")
    Ventana_Energia1.geometry("500x500+400+80")
    Energia_img  = tk.PhotoImage(file="Conversiones.png")
    Img_ub_Energia = tk.Label(Ventana_Energia1,image=Energia_img).place(x=0, y=0, relheight=1, relwidth=1)
    Titulo = tk.Label(Ventana_Energia1,text=("UNIDADES DE ENERGIA"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=130, y=75)
    btn_BTU = tk.Button(Ventana_Energia1,
     width=12,
     text="BTU",
     font="Bodoni",
     command = BTU,
     cursor="hand2",
     bg="#DBE8E1",
     fg="#E10032",
     relief="flat")
    btn_BTU.place(x=180, y=175)

    btn_Julio = tk.Button(Ventana_Energia1,
     width=12,
     text="Julio",
     font="Bodoni",
     command= Julio,
     cursor="hand2",
     bg="#DBE8E1",
     fg="#E10032",
     relief="flat")
    btn_Julio.place(x=180, y=376)

    btn_Vatio = tk.Button(Ventana_Energia1,
     width=12,
     text="Vatio",
     font="Bodoni",
     command= Vatio,
     cursor="hand2",
     bg="#DBE8E1",
     fg="#E10032",
     relief="flat")
    btn_Vatio.place(x=180, y=307)

    btn_Kilovatio = tk.Button(Ventana_Energia1,
     width=12,
     text="Kilovatio",
     font="Bodoni",
     command= Kilovatio,
     cursor="hand2",
     bg="#DBE8E1",
     fg="#E10032",
     relief="flat")
    btn_Kilovatio.place(x=180, y=240)

    btn_mas = tk.Button(Ventana_Energia1,
    width=13,
    text="Mas conversiones",
    font = fnt.Font(size = 8),
    command=unidades_ene2,
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_mas.place(x=208, y=440)

    btn_volver = tk.Button(Ventana_Energia1,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[conversion_unidades1.deiconify(),conversion_unidades, Ventana_Energia1.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)

    Ventana_Energia1.mainloop()
    unidades_ene()
def unidades_ene2():
    global Ventana_Energia2
    Ventana_Energia1.withdraw()
    Ventana_Energia2 = tk.Toplevel()
    Ventana_Energia2.title("Conversion Unidades de Energia")
    Ventana_Energia2.geometry("500x500+400+80")
    Energia_img  = tk.PhotoImage(file="Conversiones.png")
    Img_ub_Energia = tk.Label(Ventana_Energia2,image=Energia_img).place(x=0, y=0, relheight=1, relwidth=1)
    Titulo = tk.Label(Ventana_Energia2,text=("UNIDADES DE ENERGIA"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=130, y=75)
    btn_Kilocaloria = tk.Button(Ventana_Energia2,
     width=12,
     text="Kilocaloria",
     font="Bodoni",
     command= Kilocaloria,
     cursor="hand2",
     bg="#DBE8E1",
     fg="#E10032",
     relief="flat")
    btn_Kilocaloria.place(x=180, y=240)

    btn_Caloria = tk.Button(Ventana_Energia2,
     width=12,
     text="Caloria",
     font="Bodoni",
     command= Caloria,
     cursor="hand2",
     bg="#DBE8E1",
     fg="#E10032",
     relief="flat")
    btn_Caloria.place(x=180, y=307)

    btn_Kilojulio = tk.Button(Ventana_Energia2,
     width=12,
     text="Kilojulio",
     font="Bodoni",
     command= Kilojulio,
     cursor="hand2",
     bg="#DBE8E1",
     fg="#E10032",
     relief="flat")
    btn_Kilojulio.place(x=180, y=175)

    btn_Electronvoltio = tk.Button(Ventana_Energia2,
     width=12,
     text="Electronvoltio",
     font="Bodoni",
     command= Electronvoltio,
     cursor="hand2",
     bg="#DBE8E1",
     fg="#E10032",
     relief="flat")
    btn_Electronvoltio.place(x=180, y=376)

    btn_mas = tk.Button(Ventana_Energia2,
    width=13,
    text="Volver",
    font = fnt.Font(size = 8),
    command=lambda:[Ventana_Energia1.deiconify(), unidades_ene, Ventana_Energia2.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_mas.place(x=208, y=440)

    btn_volver = tk.Button(Ventana_Energia2,
    width=15,
    height=15,
    text="",
    command=conversion_unidades,
    cursor="hand2",
    bg="#151B25",
    fg="#151B25",
    relief="flat")
    btn_volver.place(x=5, y=465)

    Ventana_Energia2.mainloop()
def Julio():
    Ventana_Energia1.withdraw()
    Ventana_Julio = tk.Toplevel()
    Ventana_Julio.geometry("500x500+400+80")
    Ventana_Julio.title("Conversion de Julio")
    Ventana_Julio.resizable(width=False, height=False)
    fondo_Ventana_Julio = tk.PhotoImage(file="Conversion1.png")
    fondo_ub_Ventana_Julio = tk.Label(Ventana_Julio, image=fondo_Ventana_Julio).place(x=0, y=0,relheight=1, relwidth=1)
    numero1 = tk.StringVar()
    numero2 = tk.StringVar()
    Titulo = tk.Label(Ventana_Julio,text=("JULIOS"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=215, y=75)

    Texto1 = tk.Label(Ventana_Julio,text=("Digite el valor en Julios"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto1.place(x=65, y=145)

    Texto2 = tk.Label(Ventana_Julio,text=("Resultado en BTU"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto2.place(x=280, y=145)

    Texto3 = tk.Label(Ventana_Julio,text=("Digite el valor en Julios"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto3.place(x=65, y=294)

    Texto4 = tk.Label(Ventana_Julio,text=("Resultado en Vatios"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto4.place(x=280, y=294)

    entrada1 = Entry(Ventana_Julio,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero1)
    entrada1.place(x=69, y=174)

    entrada2 = Entry(Ventana_Julio,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero2)
    entrada2.place(x=69, y=330)

    salida1 =  tk.Entry(Ventana_Julio,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida1.place(x=280, y=175)

    salida2 =  tk.Entry(Ventana_Julio,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida2.place(x=280, y=330)

    def conversion1():
        salida1.delete(0, END)
        num = int(numero1.get())
        resultado = num/1055
        salida1.insert(0, resultado)
   
    def conversion2():
        salida2.delete(0, END)
        num = int(numero2.get())
        resultado = num/3600
        salida2.insert(0, resultado)
   

    def siguiente1():
        Texto2.configure(text="Resultado en Kilovatio")
        Texto4.configure(text="Resultado en Kilojulio")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0,END)
        salida2.delete(0,END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/3600000
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente2)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/1000
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente2():
        Texto2.configure(text="Resultado en Caloria")
        Texto4.configure(text="Resultado en Kilocaloria")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/4.184
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente3)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/4184
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente3():
        Texto2.configure(text="Resultado en Electronvoltio")
        Texto3.configure(fg="#151b25")
        Texto4.configure(fg="#151B25")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0,END)
        salida2.delete(0, END)
        fondo_Ventana_Julio.configure(file="Conversion_Final.png")
        btn_conversion2.configure(width=500,height=5, bg="#151b25")
        btn_conversion2.place(x=0,y=330)
        btn_siguiente.place(x=235, y=286)

        def nueva_conversion1():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*(6.242*(10**18))
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion1)
        btn_siguiente.configure(command=siguiente4)
    
    def siguiente4():
        fondo_Ventana_Julio.configure(file="Conversion1.png")
        Texto2.configure(text="Resultado en BTU")
        Texto4.configure(text="Resultado en Vatios", fg="white")
        Texto3.configure(fg="white")
        btn_conversion2.configure(width=10,height=0, bg="#DBE8E1")
        btn_conversion2.place(x=215,y=380)
        btn_siguiente.place(x=236, y=434)
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0,END)
        salida2.delete(0,END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/1055
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente1)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/3600
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
    
    btn_volver = tk.Button(Ventana_Julio,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[Ventana_Energia1.deiconify(),unidades_ene, Ventana_Julio.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)


    btn_conversion1 = tk.Button(Ventana_Julio,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion1.place(x= 215, y= 227)

    btn_conversion2 = tk.Button(Ventana_Julio,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion2,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion2.place(x= 215, y= 380)
    

    btn_siguiente = tk.Button(Ventana_Julio,font = fnt.Font(size = 12), text="➤",command=siguiente1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_siguiente.place(x= 236, y= 434)
    Ventana_Julio.mainloop()
def BTU():
    Ventana_Energia1.withdraw()
    Ventana_BTU = tk.Toplevel()
    Ventana_BTU.geometry("500x500+400+80")
    Ventana_BTU.title("Conversion de BTU")
    Ventana_BTU.resizable(width="false", height="false" )
    Fondo_Ventana_BTU = tk.PhotoImage(file="Conversion1.png")
    Fondo_ub_Ventana_BTU = tk.Label(Ventana_BTU,image=Fondo_Ventana_BTU).place(x=0, y=0, relheight=1, relwidth=1)
    numero1 = tk.StringVar()
    numero2 = tk.StringVar()
    Titulo = tk.Label(Ventana_BTU,text=("BTU"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=225, y=75)

    Texto1 = tk.Label(Ventana_BTU,text=("Digite el valor en BTU"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto1.place(x=65, y=145)

    Texto2 = tk.Label(Ventana_BTU,text=("Resultado en Julios"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto2.place(x=280, y=145)

    Texto3 = tk.Label(Ventana_BTU,text=("Digite el valor en BTU"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto3.place(x=65, y=294)

    Texto4 = tk.Label(Ventana_BTU,text=("Resultado en Vatios"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto4.place(x=280, y=294)

    entrada1 = Entry(Ventana_BTU,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero1)
    entrada1.place(x=69, y=174)

    entrada2 = Entry(Ventana_BTU,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero2)
    entrada2.place(x=69, y=330)

    salida1 =  tk.Entry(Ventana_BTU,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida1.place(x=280, y=175)

    salida2 =  tk.Entry(Ventana_BTU,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida2.place(x=280, y=330)

    def conversion1():
        salida1.delete(0, END)
        num = int(numero1.get())
        resultado = num*1055
        salida1.insert(0, resultado)
   
    def conversion2():
        salida2.delete(0, END)
        num = int(numero2.get())
        resultado = num/3.412
        salida2.insert(0, resultado)
   

    def siguiente1():
        Texto2.configure(text="Resultado en Kilovatio")
        Texto4.configure(text="Resultado en Kilojulio")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0,END)
        salida2.delete(0,END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/3412
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente2)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/1055
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente2():
        Texto2.configure(text="Resultado en Caloria")
        Texto4.configure(text="Resultado en Kilocaloria")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*252
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente3)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/3.966
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente3():
        Texto2.configure(text="Resultado en Electronvoltio")
        Texto3.configure(fg="#151b25")
        Texto4.configure(fg="#151B25")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        Fondo_Ventana_BTU.configure(file="Conversion_Final.png")
        btn_conversion2.configure(width=500,height=5, bg="#151b25")
        btn_conversion2.place(x=0,y=330)
        btn_siguiente.place(x=235, y=286)

        def nueva_conversion1():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*(9.223*(10**18))
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion1)
        btn_siguiente.configure(command=siguiente4)
    
    def siguiente4():
        Texto2.configure(text="Resultado en Julios")
        Texto4.configure(text="Resultado en Vatios", fg="white")
        Fondo_Ventana_BTU.configure(file="Conversion1.png")
        Texto3.configure(fg="white")
        btn_conversion2.configure(width=10,height=0, bg="#DBE8E1")
        btn_siguiente.place(x= 236, y= 434)
        btn_conversion2.place(x=215,y=380)
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*1055
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente1)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/3.412
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    btn_volver = tk.Button(Ventana_BTU,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[Ventana_Energia1.deiconify(),unidades_ene, Ventana_BTU.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)

    btn_conversion1 = tk.Button(Ventana_BTU,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion1.place(x= 215, y= 227)

    btn_conversion2 = tk.Button(Ventana_BTU,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion2,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion2.place(x= 215, y= 380)
    

    btn_siguiente = tk.Button(Ventana_BTU,font = fnt.Font(size = 12), text="➤",command=siguiente1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_siguiente.place(x= 236, y= 434)

    Ventana_BTU.mainloop()
def Vatio():
    Ventana_Energia1.withdraw()
    Ventana_Vatio = tk.Toplevel()
    Ventana_Vatio.geometry("500x500+400+80")
    Ventana_Vatio.resizable(height="false", width="false")
    Ventana_Vatio.title("Conversion de Vatio")
    Fondo_Ventana_Vatio = tk.PhotoImage(file="Conversion1.png")
    Fondo_ub_Vatio = tk.Label(Ventana_Vatio,image=Fondo_Ventana_Vatio).place(x=0, y=0, relheight=1, relwidth=1)

    numero1 = tk.StringVar()
    numero2 = tk.StringVar()
    Titulo = tk.Label(Ventana_Vatio,text=("VATIOS"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=215, y=75)

    Texto1 = tk.Label(Ventana_Vatio,text=("Digite el valor en Vatios"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto1.place(x=65, y=145)

    Texto2 = tk.Label(Ventana_Vatio,text=("Resultado en BTU"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto2.place(x=280, y=145)

    Texto3 = tk.Label(Ventana_Vatio,text=("Digite el valor en Vatios"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto3.place(x=65, y=294)

    Texto4 = tk.Label(Ventana_Vatio,text=("Resultado en Julios"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto4.place(x=280, y=294)

    entrada1 = Entry(Ventana_Vatio,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero1)
    entrada1.place(x=69, y=174)

    entrada2 = Entry(Ventana_Vatio,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero2)
    entrada2.place(x=69, y=330)

    salida1 =  tk.Entry(Ventana_Vatio,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida1.place(x=280, y=175)

    salida2 =  tk.Entry(Ventana_Vatio,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida2.place(x=280, y=330)

    def conversion1():
        salida1.delete(0, END)
        num = int(numero1.get())
        resultado = num*3.412
        salida1.insert(0, resultado)
   
    def conversion2():
        salida2.delete(0, END)
        num = int(numero2.get())
        resultado = num*3600
        salida2.insert(0, resultado)
   

    def siguiente1():
        Texto2.configure(text="Resultado en Kilovatio")
        Texto4.configure(text="Resultado en Kilojulio")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/1000
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente2)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*3.6
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente2():
        Texto2.configure(text="Resultado en Caloria")
        Texto4.configure(text="Resultado en Kilocaloria")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*860
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente3)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/1.162
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente3():
        Texto2.configure(text="Resultado en Electronvoltio")
        Texto3.configure(fg="#151b25")
        Texto4.configure(fg="#151B25")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        Fondo_Ventana_Vatio.configure(file="Conversion_Final.png")
        btn_conversion2.configure(width=500,height=5, bg="#151b25")
        btn_conversion2.place(x=0,y=330)
        btn_siguiente.place(x=235, y=286)

        def nueva_conversion1():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*(9.223*(10**18))
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion1)
        btn_siguiente.configure(command=siguiente4)
    
    def siguiente4():
        Fondo_Ventana_Vatio.configure(file="Conversion1.png")
        Texto2.configure(text="Resultado en BTU")
        Texto4.configure(text="Resultado en Julios", fg="white")
        Texto3.configure(fg="white")
        btn_conversion2.configure(width=10,height=0, bg="#DBE8E1")
        btn_conversion2.place(x=215,y=380)
        btn_siguiente.place(x= 236, y= 434)
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*3.412
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente1)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*3600
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    btn_volver = tk.Button(Ventana_Vatio,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[Ventana_Energia1.deiconify(),unidades_ene, Ventana_Vatio.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)

    btn_conversion1 = tk.Button(Ventana_Vatio,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion1.place(x= 215, y= 227)

    btn_conversion2 = tk.Button(Ventana_Vatio,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion2,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion2.place(x= 215, y= 380)
    

    btn_siguiente = tk.Button(Ventana_Vatio,font = fnt.Font(size = 12), text="➤",command=siguiente1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_siguiente.place(x= 236, y= 434)
    Ventana_Vatio.mainloop()
def Kilovatio():
    Ventana_Energia1.withdraw()
    Ventana_Kilovatio = tk.Toplevel()
    Ventana_Kilovatio.geometry("500x500+400+80")
    Ventana_Kilovatio.title("Conversion de Kilovatio")
    Ventana_Kilovatio.resizable(width=False, height=False)
    fondo_Ventana_Kilovatio = tk.PhotoImage(file="Conversion1.png")
    fondo_ub_Ventana_Kilovatio = tk.Label(Ventana_Kilovatio, image=fondo_Ventana_Kilovatio).place(x=0, y=0,relheight=1, relwidth=1)
    numero1 = tk.StringVar()
    numero2 = tk.StringVar()
    Titulo = tk.Label(Ventana_Kilovatio,text=("KILOVATIOS"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=200, y=75)

    Texto1 = tk.Label(Ventana_Kilovatio,text=("Digite el valor en Kilovatios"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto1.place(x=65, y=145)

    Texto2 = tk.Label(Ventana_Kilovatio,text=("Resultado en BTU"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto2.place(x=280, y=145)

    Texto3 = tk.Label(Ventana_Kilovatio,text=("Digite el valor en Kilovatios"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto3.place(x=65, y=294)

    Texto4 = tk.Label(Ventana_Kilovatio,text=("Resultado en Vatios"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto4.place(x=280, y=294)

    entrada1 = Entry(Ventana_Kilovatio,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero1)
    entrada1.place(x=69, y=174)

    entrada2 = Entry(Ventana_Kilovatio,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero2)
    entrada2.place(x=69, y=330)

    salida1 =  tk.Entry(Ventana_Kilovatio,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida1.place(x=280, y=175)

    salida2 =  tk.Entry(Ventana_Kilovatio,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida2.place(x=280, y=330)

    def conversion1():
        salida1.delete(0, END)
        num = int(numero1.get())
        resultado = num*3412
        salida1.insert(0, resultado)
   
    def conversion2():
        salida2.delete(0, END)
        num = int(numero2.get())
        resultado = num*1000
        salida2.insert(0,resultado)
   

    def siguiente1():
        Texto2.configure(text="Resultado en Julios")
        Texto4.configure(text="Resultado en Kilojulio")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*(3.6(10**6))
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente2)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*3600
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente2():
        Texto2.configure(text="Resultado en Caloria")
        Texto4.configure(text="Resultado en Kilocaloria")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*860421
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente3)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*860
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente3():
        Texto2.configure(text="Resultado en Electronvoltio")
        Texto3.configure(fg="#151b25")
        Texto4.configure(fg="#151B25")
        Texto3.place(x= 290)
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        fondo_Ventana_Kilovatio.configure(file="Conversion_Final.png")
        btn_conversion2.configure(width=500,height=5, bg="#151b25")
        btn_conversion2.place(x=0,y=330)
        btn_siguiente.place(x=235, y=286)
        
        def nueva_conversion1():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*(9.223*(10**18))
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion1)
        btn_siguiente.configure(command=siguiente4)
    
    def siguiente4():
        Texto3.place(x= 65)
        fondo_Ventana_Kilovatio.configure(file="Conversion1.png")
        Texto2.configure(text="Resultado en BTU")
        Texto4.configure(text="Resultado en Vatios", fg="white")
        Texto3.configure(fg="white")
        btn_conversion2.configure(width=10,height=0, bg="#DBE8E1")
        btn_conversion2.place(x=215,y=380)
        btn_siguiente.place(x=236, y=434)
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*3412
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente1)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*1000
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)

    btn_volver = tk.Button(Ventana_Kilovatio,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[Ventana_Energia1.deiconify(),unidades_ene, Ventana_Kilovatio.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)  


    btn_conversion1 = tk.Button(Ventana_Kilovatio,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion1.place(x= 215, y= 227)

    btn_conversion2 = tk.Button(Ventana_Kilovatio,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion2,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion2.place(x= 215, y= 380)
    

    btn_siguiente = tk.Button(Ventana_Kilovatio,font = fnt.Font(size = 12), text="➤",command=siguiente1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_siguiente.place(x= 236, y= 434)

    Ventana_Kilovatio.mainloop()
def Kilojulio():
    Ventana_Energia2.withdraw()
    Ventana_Kilojulio = tk.Toplevel()
    Ventana_Kilojulio.geometry("500x500+400+80")
    Ventana_Kilojulio.title("Conversion de Kilojulio")
    Ventana_Kilojulio.resizable(width="false", height="false" )
    Fondo_Ventana_Kilojulio = tk.PhotoImage(file="Conversion1.png")
    Fondo_ub_Ventana_Kilojulio = tk.Label(Ventana_Kilojulio,image=Fondo_Ventana_Kilojulio).place(x=0, y=0, relheight=1, relwidth=1)
    numero1 = tk.StringVar()
    numero2 = tk.StringVar()
    Titulo = tk.Label(Ventana_Kilojulio,text=("KILOJULIOS"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=200, y=75)

    Texto1 = tk.Label(Ventana_Kilojulio,text=("Digite el valor en Kilojulios"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto1.place(x=65, y=145)

    Texto2 = tk.Label(Ventana_Kilojulio,text=("Resultado en BTU"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto2.place(x=280, y=145)

    Texto3 = tk.Label(Ventana_Kilojulio,text=("Digite el valor en Kilojulios"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto3.place(x=65, y=294)

    Texto4 = tk.Label(Ventana_Kilojulio,text=("Resultado en Vatios"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto4.place(x=280, y=294)

    entrada1 = Entry(Ventana_Kilojulio,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero1)
    entrada1.place(x=69, y=174)

    entrada2 = Entry(Ventana_Kilojulio,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero2)
    entrada2.place(x=69, y=330)

    salida1 =  tk.Entry(Ventana_Kilojulio,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida1.place(x=280, y=175)

    salida2 =  tk.Entry(Ventana_Kilojulio,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida2.place(x=280, y=330)

    def conversion1():
        salida1.delete(0, END)
        num = int(numero1.get())
        resultado = num/1.055
        salida1.insert(0, resultado)
   
    def conversion2():
        salida2.delete(0, END)
        num = int(numero2.get())
        resultado = num/3.6
        salida2.insert(0, resultado)
   

    def siguiente1():
        Texto2.configure(text="Resultado en Kilovatio")
        Texto4.configure(text="Resultado en Julios")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/3600
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente2)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*1000
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente2():
        Texto2.configure(text="Resultado en Caloria")
        Texto4.configure(text="Resultado en Kilocaloria")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*239
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente3)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/4.184
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente3():
        Texto2.configure(text="Resultado en Electronvoltio")
        Texto3.configure(fg="#151b25")
        Texto4.configure(fg="#151B25")
        Texto3.place(x=290)
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        Fondo_Ventana_Kilojulio.configure(file="Conversion_Final.png")
        btn_conversion2.configure(width=500,height=5, bg="#151b25")
        btn_conversion2.place(x=0,y=330)
        btn_siguiente.place(x=235, y=286)

        def nueva_conversion1():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*(9.223*(10**18))
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion1)
        btn_siguiente.configure(command=siguiente4)
    
    def siguiente4():
        Texto3.place(x=65)
        Fondo_Ventana_Kilojulio.configure(file="Conversion1.png")
        Texto2.configure(text="Resultado en BTU")
        Texto4.configure(text="Resultado en Vatios", fg="white")
        Texto3.configure(fg="white")
        btn_conversion2.configure(width=10,height=0, bg="#DBE8E1")
        btn_conversion2.place(x=215,y=380)
        btn_siguiente.place(x=236, y=434)
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/1.055
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente1)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/3.6
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    btn_volver = tk.Button(Ventana_Kilojulio,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[Ventana_Energia2.deiconify(),unidades_ene, Ventana_Kilojulio.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)

    btn_conversion1 = tk.Button(Ventana_Kilojulio,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion1.place(x= 215, y= 227)

    btn_conversion2 = tk.Button(Ventana_Kilojulio,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion2,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion2.place(x= 215, y= 380)
    

    btn_siguiente = tk.Button(Ventana_Kilojulio,font = fnt.Font(size = 12), text="➤",command=siguiente1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_siguiente.place(x= 236, y= 434)

    Ventana_Kilojulio.mainloop()
def Caloria():
    Ventana_Energia2.withdraw()
    Ventana_Caloria = tk.Toplevel()
    Ventana_Caloria.geometry("500x500+400+80")
    Ventana_Caloria.resizable(height="false", width="false")
    Ventana_Caloria.title("Conversion de Caloria")
    Fondo_Ventana_Caloria = tk.PhotoImage(file="Conversion1.png")
    Fondo_ub_Caloria = tk.Label(Ventana_Caloria,image=Fondo_Ventana_Caloria).place(x=0, y=0, relheight=1, relwidth=1)

    numero1 = tk.StringVar()
    numero2 = tk.StringVar()
    Titulo = tk.Label(Ventana_Caloria,text=("CALORIAS"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=210, y=75)

    Texto1 = tk.Label(Ventana_Caloria,text=("Digite el valor en Calorias"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto1.place(x=65, y=145)

    Texto2 = tk.Label(Ventana_Caloria,text=("Resultado en BTU"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto2.place(x=280, y=145)

    Texto3 = tk.Label(Ventana_Caloria,text=("Digite el valor en Calorias"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto3.place(x=65, y=294)

    Texto4 = tk.Label(Ventana_Caloria,text=("Resultado en Vatios"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto4.place(x=280, y=294)

    entrada1 = Entry(Ventana_Caloria,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero1)
    entrada1.place(x=69, y=174)

    entrada2 = Entry(Ventana_Caloria,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero2)
    entrada2.place(x=69, y=330)

    salida1 =  tk.Entry(Ventana_Caloria,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida1.place(x=280, y=175)

    salida2 =  tk.Entry(Ventana_Caloria,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida2.place(x=280, y=330)

    def conversion1():
        salida1.delete(0, END)
        num = int(numero1.get())
        resultado = num/252
        salida1.insert(0, resultado)
   
    def conversion2():
        salida2.delete(0, END)
        num = int(numero2.get())
        resultado = num/860
        salida2.insert(0, resultado)
   

    def siguiente1():
        Texto2.configure(text="Resultado en Kilovatio")
        Texto4.configure(text="Resultado en Kilojulio")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/860421
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente2)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/239
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente2():
        Texto2.configure(text="Resultado en Julios")
        Texto4.configure(text="Resultado en Kilocaloria")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*4.184
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente3)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/1000
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente3():
        Texto2.configure(text="Resultado en Electronvoltio")
        Texto3.configure(fg="#151b25")
        Texto4.configure(fg="#151B25")
        Texto3.place(x=290)
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        Fondo_Ventana_Caloria.configure(file="Conversion_Final.png")
        btn_conversion2.configure(width=500,height=5, bg="#151b25")
        btn_conversion2.place(x=0,y=330)
        btn_siguiente.place(x=235, y=286)

        def nueva_conversion1():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*(9.223*(10**18))
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion1)
        btn_siguiente.configure(command=siguiente4)
    
    def siguiente4():
        Texto3.place(x=65)
        Fondo_Ventana_Caloria.configure(file="Conversion1.png")
        Texto2.configure(text="Resultado en BTU")
        Texto4.configure(text="Resultado en Vatios", fg="white")
        Texto3.configure(fg="white")
        btn_conversion2.configure(width=10,height=0, bg="#DBE8E1")
        btn_conversion2.place(x=215,y=380)
        btn_siguiente.place(x=236, y=434)
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/252
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente1)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/860
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)

    btn_volver = tk.Button(Ventana_Caloria,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[Ventana_Energia2.deiconify(),unidades_ene, Ventana_Caloria.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)   


    btn_conversion1 = tk.Button(Ventana_Caloria,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion1.place(x= 215, y= 227)

    btn_conversion2 = tk.Button(Ventana_Caloria,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion2,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion2.place(x= 215, y= 380)
    

    btn_siguiente = tk.Button(Ventana_Caloria,font = fnt.Font(size = 12), text="➤",command=siguiente1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_siguiente.place(x= 236, y= 434)
    Ventana_Caloria.mainloop()
def Kilocaloria():
    Ventana_Energia2.withdraw()
    Ventana_Kilocaloria = tk.Toplevel()
    Ventana_Kilocaloria.geometry("500x500+400+80")
    Ventana_Kilocaloria.title("Conversion de Kilocaloria")
    Ventana_Kilocaloria.resizable(width=False, height=False)
    fondo_Ventana_Kilocaloria = tk.PhotoImage(file="Conversion1.png")
    fondo_ub_Ventana_Kilocaloria = tk.Label(Ventana_Kilocaloria, image=fondo_Ventana_Kilocaloria).place(x=0, y=0,relheight=1, relwidth=1)
    numero1 = tk.StringVar()
    numero2 = tk.StringVar()
    Titulo = tk.Label(Ventana_Kilocaloria,text=("KILOCALORIAS"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=190, y=75)

    Texto1 = tk.Label(Ventana_Kilocaloria,text=("Digite el valor en Kilocalorias"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto1.place(x=65, y=145)

    Texto2 = tk.Label(Ventana_Kilocaloria,text=("Resultado en BTU"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto2.place(x=280, y=145)

    Texto3 = tk.Label(Ventana_Kilocaloria,text=("Digite el valor en Julios"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto3.place(x=65, y=294)

    Texto4 = tk.Label(Ventana_Kilocaloria,text=("Resultado en Vatios"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto4.place(x=280, y=294)

    entrada1 = Entry(Ventana_Kilocaloria,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero1)
    entrada1.place(x=69, y=174)

    entrada2 = Entry(Ventana_Kilocaloria,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero2)
    entrada2.place(x=69, y=330)

    salida1 =  tk.Entry(Ventana_Kilocaloria,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida1.place(x=280, y=175)

    salida2 =  tk.Entry(Ventana_Kilocaloria,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida2.place(x=280, y=330)

    def conversion1():
        salida1.delete(0, END)
        num = int(numero1.get())
        resultado = num*3.966
        salida1.insert(0, resultado)
   
    def conversion2():
        salida2.delete(0, END)
        num = int(numero2.get())
        resultado = num*1.162
        salida2.insert(0, resultado)
   

    def siguiente1():
        Texto2.configure(text="Resultado en Kilovatio")
        Texto4.configure(text="Resultado en Kilojulio")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/860
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente2)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*4.184
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente2():
        Texto2.configure(text="Resultado en Caloria")
        Texto4.configure(text="Resultado en Julios")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*1000
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente3)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*4184
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente3():
        Texto2.configure(text="Resultado en Electronvoltio")
        Texto3.configure(fg="#151b25")
        Texto4.configure(fg="#151B25")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        fondo_Ventana_Kilocaloria.configure(file="Conversion_Final.png")
        btn_conversion2.configure(width=500,height=5, bg="#151b25")
        btn_conversion2.place(x=0,y=330)
        btn_siguiente.place(x=235, y=286)

        def nueva_conversion1():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*(9.223*(10**18))
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion1)
        btn_siguiente.configure(command=siguiente4)
    
    def siguiente4():
        fondo_Ventana_Kilocaloria.configure(file="Conversion1.png")
        Texto2.configure(text="Resultado en BTU")
        Texto4.configure(text="Resultado en Vatios", fg="white")
        Texto3.configure(fg="white")
        btn_conversion2.configure(width=10,height=0, bg="#DBE8E1")
        btn_conversion2.place(x=215,y=380)
        btn_siguiente.place(x=236, y=434)
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*3.966
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente1)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*1.162
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    btn_volver = tk.Button(Ventana_Kilocaloria,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[Ventana_Energia2.deiconify(),unidades_ene, Ventana_Kilocaloria.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)

    btn_conversion1 = tk.Button(Ventana_Kilocaloria,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion1.place(x= 215, y= 227)

    btn_conversion2 = tk.Button(Ventana_Kilocaloria,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion2,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion2.place(x= 215, y= 380)
    

    btn_siguiente = tk.Button(Ventana_Kilocaloria,font = fnt.Font(size = 12), text="➤",command=siguiente1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_siguiente.place(x= 236, y= 434)

    Ventana_Kilocaloria.mainloop()
def Electronvoltio():
    Ventana_Energia2.withdraw()
    Ventana_Electronvoltio = tk.Toplevel()
    Ventana_Electronvoltio.geometry("500x500+400+80")
    Ventana_Electronvoltio.resizable(height="false", width="false")
    Ventana_Electronvoltio.title("Conversion de Electronvoltio")
    Fondo_Ventana_Electronvoltio = tk.PhotoImage(file="Conversion1.png")
    Fondo_ub_Electronvoltio = tk.Label(Ventana_Electronvoltio,image=Fondo_Ventana_Electronvoltio).place(x=0, y=0, relheight=1, relwidth=1)

    numero1 = tk.StringVar()
    numero2 = tk.StringVar()
    Titulo = tk.Label(Ventana_Electronvoltio,text=("ELECTRONVOLTIOS"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=165, y=75)

    Texto1 = tk.Label(Ventana_Electronvoltio,text=("Digite el valor en E.Voltios"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto1.place(x=65, y=145)

    Texto2 = tk.Label(Ventana_Electronvoltio,text=("Resultado en BTU"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto2.place(x=280, y=145)

    Texto3 = tk.Label(Ventana_Electronvoltio,text=("Digite el valor en E.Voltios"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto3.place(x=65, y=294)

    Texto4 = tk.Label(Ventana_Electronvoltio,text=("Resultado en Vatios"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto4.place(x=280, y=294)

    entrada1 = Entry(Ventana_Electronvoltio,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero1)
    entrada1.place(x=69, y=174)

    entrada2 = Entry(Ventana_Electronvoltio,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero2)
    entrada2.place(x=69, y=330)

    salida1 =  tk.Entry(Ventana_Electronvoltio,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida1.place(x=280, y=175)

    salida2 =  tk.Entry(Ventana_Electronvoltio,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida2.place(x=280, y=330)

    def conversion1():
        salida1.delete(0, END)
        num = int(numero1.get())
        resultado = num/(9.223*(10**18))
        salida1.insert(0,resultado)
   
    def conversion2():
        salida2.delete(0, END)
        num = int(numero2.get())
        resultado = num/(9.223*(10**18))
        salida2.insert(0,resultado)
   

    def siguiente1():
        Texto2.configure(text="Resultado en Kilovatio")
        Texto4.configure(text="Resultado en Kilojulio")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/(9.223*(10**18))
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente2)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/(9.223*(10**18))
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente2():
        Texto2.configure(text="Resultado en Caloria")
        Texto4.configure(text="Resultado en Kilocaloria")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/(9.223*(10**18))
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente3)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/(9.223*(10**18))
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente3():
        Texto2.configure(text="Resultado en Julios")
        Texto3.configure(fg="#151b25")
        Texto3.place(x=290)
        Texto4.configure(fg="#151B25")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        Fondo_Ventana_Electronvoltio.configure(file="Conversion_Final.png")
        btn_conversion2.configure(width=500,height=5, bg="#151b25")
        btn_conversion2.place(x=0,y=330)
        btn_siguiente.place(x=235, y=286)

        def nueva_conversion1():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/(6.242*(10**18))
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion1)
        btn_siguiente.configure(command=siguiente4)
    
    def siguiente4():
        Fondo_Ventana_Electronvoltio.configure(file="Conversion1.png")
        Texto2.configure(text="Resultado en BTU")
        Texto4.configure(text="Resultado en Vatios", fg="white")
        Texto3.configure(fg="white")
        Texto3.place(x=65)
        btn_conversion2.configure(width=10,height=0, bg="#DBE8E1")
        btn_conversion2.place(x=215,y=380)
        btn_siguiente.place(x=236, y=434)
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/(9.223*(10**18))
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente1)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/(9.223*(10**18))
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    btn_volver = tk.Button(Ventana_Electronvoltio,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[Ventana_Energia2.deiconify(),unidades_ene, Ventana_Electronvoltio.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)

    btn_conversion1 = tk.Button(Ventana_Electronvoltio,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion1.place(x= 215, y= 227)

    btn_conversion2 = tk.Button(Ventana_Electronvoltio,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion2,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion2.place(x= 215, y= 380)
    

    btn_siguiente = tk.Button(Ventana_Electronvoltio,font = fnt.Font(size = 12), text="➤",command=siguiente1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_siguiente.place(x= 236, y= 434)
    Ventana_Electronvoltio.mainloop()

###################################################################################################################
###############################################################################################################
###############################################################################################################
def unidades_longitud():
    global Ventana_Longitud1
    conversion_unidades1.withdraw()
    Ventana_Longitud1 = tk.Toplevel()
    Ventana_Longitud1.title("Conversion Unidades de Longitud")
    Ventana_Longitud1.geometry("500x500+400+80")
    Longitud_img  = tk.PhotoImage(file="Conversiones.png")
    Img_ub_Longitud = tk.Label(Ventana_Longitud1,image=Longitud_img).place(x=0, y=0, relheight=1, relwidth=1)
    Titulo = tk.Label(Ventana_Longitud1,text=("UNIDADES DE LONGITUD"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=130, y=75)
    btn_Milimetro = tk.Button(Ventana_Longitud1,
     width=12,
     text="Milimetro",
     font="Bodoni",
     command= Milimetro,
     cursor="hand2",
     bg="#DBE8E1",
     fg="#E10032",
     relief="flat")
    btn_Milimetro.place(x=180, y=175)

    btn_Centimetro = tk.Button(Ventana_Longitud1,
     width=12,
     text="Centimetro",
     font="Bodoni",
     command= Centimetro,
     cursor="hand2",
     bg="#DBE8E1",
     fg="#E10032",
     relief="flat")
    btn_Centimetro.place(x=180, y=376)

    btn_Pulgada = tk.Button(Ventana_Longitud1,
     width=12,
     text="Pulgada",
     font="Bodoni",
     command= Pulgada,
     cursor="hand2",
     bg="#DBE8E1",
     fg="#E10032",
     relief="flat")
    btn_Pulgada.place(x=180, y=307)

    btn_Pie = tk.Button(Ventana_Longitud1,
     width=12,
     text="Pie",
     font="Bodoni",
     command= Pie,
     cursor="hand2",
     bg="#DBE8E1",
     fg="#E10032",
     relief="flat")
    btn_Pie.place(x=180, y=240)

    btn_mas = tk.Button(Ventana_Longitud1,
    width=13,
    text="Mas conversiones",
    font = fnt.Font(size = 8),
    command=unidades_longitud2,
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_mas.place(x=208, y=440)

    btn_volver = tk.Button(Ventana_Longitud1,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[conversion_unidades1.deiconify(),conversion_unidades,Ventana_Longitud1.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)
   
    Ventana_Longitud1.mainloop()
    unidades_longitud()
def unidades_longitud2():
    global Ventana_Longitud2
    Ventana_Longitud1.withdraw()
    Ventana_Longitud2 = tk.Toplevel()
    Ventana_Longitud2.title("Conversion Unidades de Longitud")
    Ventana_Longitud2.geometry("500x500+400+80")
    Longitud_img  = tk.PhotoImage(file="Conversiones.png")
    Img_ub_Longitud = tk.Label(Ventana_Longitud2,image=Longitud_img).place(x=0, y=0, relheight=1, relwidth=1)
    Titulo = tk.Label(Ventana_Longitud2,text=("UNIDADES DE LONGITUD"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=130, y=75)
    btn_Metro = tk.Button(Ventana_Longitud2,
     width=12,
     text="Metro",
     font="Bodoni",
     command= Metro,
     cursor="hand2",
     bg="#DBE8E1",
     fg="#E10032",
     relief="flat")
    btn_Metro.place(x=180, y=175)

    btn_Yarda = tk.Button(Ventana_Longitud2,
     width=12,
     text="Yarda",
     font="Bodoni",
     command= Yarda,
     cursor="hand2",
     bg="#DBE8E1",
     fg="#E10032",
     relief="flat")
    btn_Yarda.place(x=180, y=240)
    
    btn_Kilometro = tk.Button(Ventana_Longitud2,
     width=12,
     text="Kilometro",
     font="Bodoni",
     command= Kilometro,
     cursor="hand2",
     bg="#DBE8E1",
     fg="#E10032",
     relief="flat")
    btn_Kilometro.place(x=180, y=307)

    btn_Milla = tk.Button(Ventana_Longitud2,
     width=12,
     text="Milla",
     font="Bodoni",
     command= Milla,
     cursor="hand2",
     bg="#DBE8E1",
     fg="#E10032",
     relief="flat")
    btn_Milla.place(x=180, y=376)

    btn_mas = tk.Button(Ventana_Longitud2,
    width=13,
    text="Volver",
    font = fnt.Font(size = 8),
    command=lambda:[Ventana_Longitud1.deiconify(),unidades_longitud, Ventana_Longitud2.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_mas.place(x=208, y=440)

    btn_volver = tk.Button(Ventana_Longitud2,
    width=15,
    height=15,
    text="",
    command=conversion_unidades,
    cursor="hand2",
    bg="#151B25",
    fg="#151B25",
    relief="flat")
    btn_volver.place(x=5, y=465)


    Ventana_Longitud2.mainloop()
def Metro():
    Ventana_Longitud2.withdraw()
    Ventana_Metro = tk.Toplevel()
    Ventana_Metro.geometry("500x500+400+80")
    Ventana_Metro.title("Conversion de Metro")
    Ventana_Metro.resizable(width=False, height=False)
    fondo_Ventana_Metro = tk.PhotoImage(file="Conversion1.png")
    fondo_ub_Ventana_Metro = tk.Label(Ventana_Metro, image=fondo_Ventana_Metro).place(x=0, y=0,relheight=1, relwidth=1)
    numero1 = tk.StringVar()
    numero2 = tk.StringVar()
    Titulo = tk.Label(Ventana_Metro,text=("METROS"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=215, y=75)

    Texto1 = tk.Label(Ventana_Metro,text=("Digite el valor en Metros"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto1.place(x=65, y=145)

    Texto2 = tk.Label(Ventana_Metro,text=("Resultado en Milimetros"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto2.place(x=280, y=145)

    Texto3 = tk.Label(Ventana_Metro,text=("Digite el valor en Metros"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto3.place(x=65, y=294)

    Texto4 = tk.Label(Ventana_Metro,text=("Resultado en Centimetros"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto4.place(x=280, y=294)

    entrada1 = Entry(Ventana_Metro,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero1)
    entrada1.place(x=69, y=174)

    entrada2 = Entry(Ventana_Metro,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero2)
    entrada2.place(x=69, y=330)

    salida1 =  tk.Entry(Ventana_Metro,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida1.place(x=280, y=175)

    salida2 =  tk.Entry(Ventana_Metro,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida2.place(x=280, y=330)

    def conversion1():
        salida1.delete(0, END)
        num = int(numero1.get())
        resultado = num*1000
        salida1.insert(0, resultado)
   
    def conversion2():
        salida2.delete(0, END)
        num = int(numero2.get())
        resultado = num*100
        salida2.insert(0, resultado)
   

    def siguiente1():
        Texto2.configure(text="Resultado en Pulgadas")
        Texto4.configure(text="Resultado en Pies")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*39.37
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente2)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*3.281
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente2():
        Texto2.configure(text="Resultado en Yardas")
        Texto4.configure(text="Resultado en Kilometros")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*1.094
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente3)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*0.001
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente3():
        Texto2.configure(text="Resultado en Millas")
        Texto3.configure(fg="#151b25")
        Texto3.place(x=290)
        Texto4.configure(fg="#151B25")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        fondo_Ventana_Metro.configure(file="Conversion_Final.png")
        btn_conversion2.configure(width=500,height=5, bg="#151b25")
        btn_conversion2.place(x=0,y=330)
        btn_siguiente.place(x=235, y=286)

        def nueva_conversion1():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/1609
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion1)
        btn_siguiente.configure(command=siguiente4)
    
    def siguiente4():
        fondo_Ventana_Metro.configure(file="Conversion1.png")
        Texto2.configure(text="Resultado en Milimetros")
        Texto4.configure(text="Resultado en Centimetros", fg="white")
        Texto3.configure(fg="white")
        Texto3.place(x=65)
        btn_conversion2.configure(width=10,height=0, bg="#DBE8E1")
        btn_conversion2.place(x=215,y=380)
        btn_siguiente.place(x=236, y=434)
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*1000
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente1)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*100
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    btn_volver = tk.Button(Ventana_Metro,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[Ventana_Longitud2.deiconify(),unidades_longitud2, Ventana_Metro.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)

    btn_conversion1 = tk.Button(Ventana_Metro,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion1.place(x= 215, y= 227)

    btn_conversion2 = tk.Button(Ventana_Metro,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion2,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion2.place(x= 215, y= 380)
    

    btn_siguiente = tk.Button(Ventana_Metro,font = fnt.Font(size = 12), text="➤",command=siguiente1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_siguiente.place(x= 236, y= 434)

    Ventana_Metro.mainloop()
def Pie():
    Ventana_Longitud1.withdraw()
    Ventana_Pie = tk.Toplevel()
    Ventana_Pie.geometry("500x500+400+80")
    Ventana_Pie.title("Conversion de Pie")
    Ventana_Pie.resizable(width="false", height="false" )
    Fondo_Ventana_Pie = tk.PhotoImage(file="Conversion1.png")
    Fondo_ub_Ventana_Pie = tk.Label(Ventana_Pie,image=Fondo_Ventana_Pie).place(x=0, y=0, relheight=1, relwidth=1)
    numero1 = tk.StringVar()
    numero2 = tk.StringVar()
    Titulo = tk.Label(Ventana_Pie,text=("PIES"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=220, y=75)

    Texto1 = tk.Label(Ventana_Pie,text=("Digite el valor en Pies"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto1.place(x=65, y=145)

    Texto2 = tk.Label(Ventana_Pie,text=("Resultado en Milimetros"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto2.place(x=280, y=145)

    Texto3 = tk.Label(Ventana_Pie,text=("Digite el valor en Pies"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto3.place(x=65, y=294)

    Texto4 = tk.Label(Ventana_Pie,text=("Resultado en Centimetros"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto4.place(x=280, y=294)

    entrada1 = Entry(Ventana_Pie,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero1)
    entrada1.place(x=69, y=174)

    entrada2 = Entry(Ventana_Pie,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero2)
    entrada2.place(x=69, y=330)

    salida1 =  tk.Entry(Ventana_Pie,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida1.place(x=280, y=175)

    salida2 =  tk.Entry(Ventana_Pie,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida2.place(x=280, y=330)

    def conversion1():
        salida1.delete(0, END)
        num = int(numero1.get())
        resultado = num*305
        salida1.insert(0, resultado)
   
    def conversion2():
        salida2.delete(0, END)
        num = int(numero2.get())
        resultado = num*30.48
        salida2.insert(0, resultado)
   

    def siguiente1():
        Texto2.configure(text="Resultado en Pulgadas")
        Texto4.configure(text="Resultado en Metros")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*12
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente2)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/3.281
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente2():
        Texto2.configure(text="Resultado en Yardas")
        Texto4.configure(text="Resultado en Kilometros")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/3
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente3)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/3281
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente3():
        Texto2.configure(text="Resultado en Millas")
        Texto3.configure(fg="#151b25")
        Texto4.configure(fg="#151B25")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        Fondo_Ventana_Pie.configure(file="Conversion_Final.png")
        btn_conversion2.configure(width=500,height=5, bg="#151b25")
        btn_conversion2.place(x=0,y=330)
        btn_siguiente.place(x=235, y=286)

        def nueva_conversion1():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/5280
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion1)
        btn_siguiente.configure(command=siguiente4)
    
    def siguiente4():
        Fondo_Ventana_Pie.configure(file="Conversion1.png")
        Texto2.configure(text="Resultado en Milimetros")
        Texto4.configure(text="Resultado en Centimetros", fg="white")
        Texto3.configure(fg="white")
        btn_conversion2.configure(width=10,height=0, bg="#DBE8E1")
        btn_conversion2.place(x=215,y=380)
        btn_siguiente.place(x=236, y=434)
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*305
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente1)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*30.48
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    btn_volver = tk.Button(Ventana_Pie,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[Ventana_Longitud1.deiconify(),unidades_longitud, Ventana_Pie.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)

    btn_conversion1 = tk.Button(Ventana_Pie,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion1.place(x= 215, y= 227)

    btn_conversion2 = tk.Button(Ventana_Pie,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion2,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion2.place(x= 215, y= 380)
    

    btn_siguiente = tk.Button(Ventana_Pie,font = fnt.Font(size = 12), text="➤",command=siguiente1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_siguiente.place(x= 236, y= 434)

    Ventana_Pie.mainloop()
def Pulgada():
    Ventana_Longitud1.withdraw()
    Ventana_Pulgada = tk.Toplevel()
    Ventana_Pulgada.geometry("500x500+400+80")
    Ventana_Pulgada.resizable(height="false", width="false")
    Ventana_Pulgada.title("Conversion de Pulgada")
    Fondo_Ventana_Pulgada = tk.PhotoImage(file="Conversion1.png")
    Fondo_ub_Pulgada = tk.Label(Ventana_Pulgada,image=Fondo_Ventana_Pulgada).place(x=0, y=0, relheight=1, relwidth=1)

    numero1 = tk.StringVar()
    numero2 = tk.StringVar()
    Titulo = tk.Label(Ventana_Pulgada,text=("PULGADAS"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=205, y=75)

    Texto1 = tk.Label(Ventana_Pulgada,text=("Digite el valor en Pulgadas"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto1.place(x=65, y=145)

    Texto2 = tk.Label(Ventana_Pulgada,text=("Resultado en Milimetros"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto2.place(x=280, y=145)

    Texto3 = tk.Label(Ventana_Pulgada,text=("Digite el valor en Pulgadas"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto3.place(x=65, y=294)

    Texto4 = tk.Label(Ventana_Pulgada,text=("Resultado en Centimetros"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto4.place(x=280, y=294)

    entrada1 = Entry(Ventana_Pulgada,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero1)
    entrada1.place(x=69, y=174)

    entrada2 = Entry(Ventana_Pulgada,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero2)
    entrada2.place(x=69, y=330)

    salida1 =  tk.Entry(Ventana_Pulgada,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida1.place(x=280, y=175)

    salida2 =  tk.Entry(Ventana_Pulgada,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida2.place(x=280, y=330)

    def conversion1():
        salida1.delete(0, END)
        num = int(numero1.get())
        resultado = num*25.4
        salida1.insert(0, resultado)
   
    def conversion2():
        salida2.delete(0, END)
        num = int(numero2.get())
        resultado = num*2.54
        salida2.insert(0, resultado)
   

    def siguiente1():
        Texto2.configure(text="Resultado en Metros")
        Texto4.configure(text="Resultado en Pies")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/39.37
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente2)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/12
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente2():
        Texto2.configure(text="Resultado en Yardas")
        Texto4.configure(text="Resultado en Kilometros")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/36
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente3)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/39370
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente3():
        Texto2.configure(text="Resultado en Millas")
        Texto3.configure(fg="#151b25")
        Texto3.place(x=290)
        Texto4.configure(fg="#151B25")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        Fondo_Ventana_Pulgada.configure(file="Conversion_Final.png")
        btn_conversion2.configure(width=500,height=5, bg="#151b25")
        btn_conversion2.place(x=0,y=330)
        btn_siguiente.place(x=235, y=286)

        def nueva_conversion1():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/63360
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion1)
        btn_siguiente.configure(command=siguiente4)
    
    def siguiente4():
        Fondo_Ventana_Pulgada.configure(file="Conversion1.png")
        Texto2.configure(text="Resultado en Milimetros")
        Texto4.configure(text="Resultado en Centimetros", fg="white")
        Texto3.configure(fg="white")
        Texto3.place(x=65)
        btn_conversion2.configure(width=10,height=0, bg="#DBE8E1")
        btn_conversion2.place(x=215,y=380)
        btn_siguiente.place(x=236, y=434)
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*25.4
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente1)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*2.54
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    btn_volver = tk.Button(Ventana_Pulgada,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[Ventana_Longitud1.deiconify(),unidades_longitud, Ventana_Pulgada.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)

    btn_conversion1 = tk.Button(Ventana_Pulgada,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion1.place(x= 215, y= 227)

    btn_conversion2 = tk.Button(Ventana_Pulgada,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion2,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion2.place(x= 215, y= 380)
    

    btn_siguiente = tk.Button(Ventana_Pulgada,font = fnt.Font(size = 12), text="➤",command=siguiente1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_siguiente.place(x= 236, y= 434)
    Ventana_Pulgada.mainloop()
def Milla():
    Ventana_Longitud2.withdraw()
    Ventana_Milla = tk.Toplevel()
    Ventana_Milla.geometry("500x500+400+80")
    Ventana_Milla.title("Conversion de Milla")
    Ventana_Milla.resizable(width=False, height=False)
    fondo_Ventana_Milla = tk.PhotoImage(file="Conversion1.png")
    fondo_ub_Ventana_Milla = tk.Label(Ventana_Milla, image=fondo_Ventana_Milla).place(x=0, y=0,relheight=1, relwidth=1)
    numero1 = tk.StringVar()
    numero2 = tk.StringVar()
    Titulo = tk.Label(Ventana_Milla,text=("MILLAS"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=215, y=75)

    Texto1 = tk.Label(Ventana_Milla,text=("Digite el valor en Millas"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto1.place(x=65, y=145)

    Texto2 = tk.Label(Ventana_Milla,text=("Resultado en Milimetros"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto2.place(x=280, y=145)

    Texto3 = tk.Label(Ventana_Milla,text=("Digite el valor en Millas"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto3.place(x=65, y=294)

    Texto4 = tk.Label(Ventana_Milla,text=("Resultado en Centimetros"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto4.place(x=280, y=294)

    entrada1 = Entry(Ventana_Milla,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero1)
    entrada1.place(x=69, y=174)

    entrada2 = Entry(Ventana_Milla,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero2)
    entrada2.place(x=69, y=330)

    salida1 =  tk.Entry(Ventana_Milla,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida1.place(x=280, y=175)

    salida2 =  tk.Entry(Ventana_Milla,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida2.place(x=280, y=330)

    def conversion1():
        salida1.delete(0, END)
        num = int(numero1.get())
        resultado = num*(1.609*(10**6))
        salida1.insert(0, resultado)
   
    def conversion2():
        salida2.delete(0, END)
        num = int(numero2.get())
        resultado = num*160934
        salida2.insert(0, resultado)
   

    def siguiente1():
        Texto2.configure(text="Resultado en Pulgadas")
        Texto4.configure(text="Resultado en Pies")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*63360
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente2)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*5280
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente2():
        Texto2.configure(text="Resultado en Yardas")
        Texto4.configure(text="Resultado en Kilometros")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*1760
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente3)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*1.609
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente3():
        Texto2.configure(text="Resultado en Metros")
        Texto3.configure(fg="#151b25")
        Texto3.place(x=290)
        Texto4.configure(fg="#151B25")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        fondo_Ventana_Milla.configure(file="Conversion_Final.png")
        btn_conversion2.configure(width=500,height=5, bg="#151b25")
        btn_conversion2.place(x=0,y=330)
        btn_siguiente.place(x=235, y=286)

        def nueva_conversion1():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*1609
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion1)
        btn_siguiente.configure(command=siguiente4)
    
    def siguiente4():
        fondo_Ventana_Milla.configure(file="Conversion1.png")
        Texto2.configure(text="Resultado en Milimetros")
        Texto4.configure(text="Resultado en Centimetros", fg="white")
        Texto3.configure(fg="white")
        Texto3.place(x=65)
        btn_conversion2.configure(width=10,height=0, bg="#DBE8E1")
        btn_conversion2.place(x=215,y=380)
        btn_siguiente.place(x=234, y=434)
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*(1.609*(10**6))
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente1)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*160934
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    btn_volver = tk.Button(Ventana_Milla,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[Ventana_Longitud2.deiconify(),unidades_longitud2, Ventana_Milla.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)

    btn_conversion1 = tk.Button(Ventana_Milla,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion1.place(x= 215, y= 227)

    btn_conversion2 = tk.Button(Ventana_Milla,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion2,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion2.place(x= 215, y= 380)
    

    btn_siguiente = tk.Button(Ventana_Milla,font = fnt.Font(size = 12), text="➤",command=siguiente1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_siguiente.place(x= 236, y= 434)

    Ventana_Milla.mainloop()
def Yarda():
    Ventana_Longitud2.withdraw()
    Ventana_Yarda = tk.Toplevel()
    Ventana_Yarda.geometry("500x500+400+80")
    Ventana_Yarda.title("Conversion de Yarda")
    Ventana_Yarda.resizable(width="false", height="false" )
    Fondo_Ventana_Yarda = tk.PhotoImage(file="Conversion1.png")
    Fondo_ub_Ventana_Yarda = tk.Label(Ventana_Yarda,image=Fondo_Ventana_Yarda).place(x=0, y=0, relheight=1, relwidth=1)
    numero1 = tk.StringVar()
    numero2 = tk.StringVar()
    Titulo = tk.Label(Ventana_Yarda,text=("YARDAS"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=215, y=75)

    Texto1 = tk.Label(Ventana_Yarda,text=("Digite el valor en Yardas"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto1.place(x=65, y=145)

    Texto2 = tk.Label(Ventana_Yarda,text=("Resultado en Milimetros"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto2.place(x=280, y=145)

    Texto3 = tk.Label(Ventana_Yarda,text=("Digite el valor en Yardas"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto3.place(x=65, y=294)

    Texto4 = tk.Label(Ventana_Yarda,text=("Resultado en Centimetros"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto4.place(x=280, y=294)

    entrada1 = Entry(Ventana_Yarda,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero1)
    entrada1.place(x=69, y=174)

    entrada2 = Entry(Ventana_Yarda,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero2)
    entrada2.place(x=69, y=330)

    salida1 =  tk.Entry(Ventana_Yarda,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida1.place(x=280, y=175)

    salida2 =  tk.Entry(Ventana_Yarda,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida2.place(x=280, y=330)

    def conversion1():
        salida1.delete(0, END)
        num = int(numero1.get())
        resultado = num*914
        salida1.insert(0, resultado)
   
    def conversion2():
        salida2.delete(0, END)
        num = int(numero2.get())
        resultado = num*91.44
        salida2.insert(0, resultado)
   

    def siguiente1():
        Texto2.configure(text="Resultado en Pulgadas")
        Texto4.configure(text="Resultado en Pies")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*36
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente2)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*3
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente2():
        Texto2.configure(text="Resultado en Metros")
        Texto4.configure(text="Resultado en Kilometros")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/1.094
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente3)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/1094
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente3():
        Texto2.configure(text="Resultado en Millas")
        Texto3.configure(fg="#151b25")
        Texto3.place(x=290)
        Texto4.configure(fg="#151B25")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        Fondo_Ventana_Yarda.configure(file="Conversion_Final.png")
        btn_conversion2.configure(width=500,height=5, bg="#151b25")
        btn_conversion2.place(x=0,y=330)
        btn_siguiente.place(x=235, y=286)

        def nueva_conversion1():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/1760
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion1)
        btn_siguiente.configure(command=siguiente4)
    
    def siguiente4():
        Fondo_Ventana_Yarda.configure(file="Conversion1.png")
        Texto2.configure(text="Resultado en Milimetros")
        Texto4.configure(text="Resultado en Centimetros", fg="white")
        Texto3.configure(fg="white")
        Texto3.place(x=65)
        btn_conversion2.configure(width=10,height=0, bg="#DBE8E1")
        btn_conversion2.place(x=215,y=380)
        btn_siguiente.place(x=236, y=434)
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*914
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente1)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*91.44
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    btn_volver = tk.Button(Ventana_Yarda,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[Ventana_Longitud2.deiconify(),unidades_longitud, Ventana_Yarda.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)

    btn_conversion1 = tk.Button(Ventana_Yarda,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion1.place(x= 215, y= 227)

    btn_conversion2 = tk.Button(Ventana_Yarda,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion2,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion2.place(x= 215, y= 380)
    

    btn_siguiente = tk.Button(Ventana_Yarda,font = fnt.Font(size = 12), text="➤",command=siguiente1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_siguiente.place(x= 236, y= 434)

    Ventana_Yarda.mainloop()
def Kilometro():
    Ventana_Longitud2.withdraw()
    Ventana_Kilometro = tk.Toplevel()
    Ventana_Kilometro.geometry("500x500+400+80")
    Ventana_Kilometro.resizable(height="false", width="false")
    Ventana_Kilometro.title("Conversion de Kilometro")
    Fondo_Ventana_Kilometro = tk.PhotoImage(file="Conversion1.png")
    Fondo_ub_Kilometro = tk.Label(Ventana_Kilometro,image=Fondo_Ventana_Kilometro).place(x=0, y=0, relheight=1, relwidth=1)

    numero1 = tk.StringVar()
    numero2 = tk.StringVar()
    Titulo = tk.Label(Ventana_Kilometro,text=("KILOMETROS"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=190, y=75)

    Texto1 = tk.Label(Ventana_Kilometro,text=("Digite el valor en Kilometros"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto1.place(x=65, y=145)

    Texto2 = tk.Label(Ventana_Kilometro,text=("Resultado en Milimetros"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto2.place(x=280, y=145)

    Texto3 = tk.Label(Ventana_Kilometro,text=("Digite el valor en Kilometros"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto3.place(x=65, y=294)

    Texto4 = tk.Label(Ventana_Kilometro,text=("Resultado en Centimetros"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto4.place(x=280, y=294)

    entrada1 = Entry(Ventana_Kilometro,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero1)
    entrada1.place(x=69, y=174)

    entrada2 = Entry(Ventana_Kilometro,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero2)
    entrada2.place(x=69, y=330)

    salida1 =  tk.Entry(Ventana_Kilometro,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida1.place(x=280, y=175)

    salida2 =  tk.Entry(Ventana_Kilometro,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida2.place(x=280, y=330)

    def conversion1():
        salida1.delete(0, END)
        num = int(numero1.get())
        resultado = num*(10**6)
        salida1.insert(0, resultado)
   
    def conversion2():
        salida2.delete(0, END)
        num = int(numero2.get())
        resultado = num*100000
        salida2.insert(0, resultado)
   

    def siguiente1():
        Texto2.configure(text="Resultado en Pulgadas")
        Texto4.configure(text="Resultado en Pies")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*39370
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente2)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*3281
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente2():
        Texto2.configure(text="Resultado en Yardas")
        Texto4.configure(text="Resultado en Metros")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*1094
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente3)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*1000
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente3():
        Texto2.configure(text="Resultado en Millas")
        Texto3.configure(fg="#151b25")
        Texto3.place(x=290)
        Texto4.configure(fg="#151B25")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        Fondo_Ventana_Kilometro.configure(file="Conversion_Final.png")
        btn_conversion2.configure(width=500,height=5, bg="#151b25")
        btn_conversion2.place(x=0,y=330)
        btn_siguiente.place(x=235, y=286)

        def nueva_conversion1():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/1.609
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion1)
        btn_siguiente.configure(command=siguiente4)
    
    def siguiente4():
        Fondo_Ventana_Kilometro.configure(file="Conversion1.png")
        Texto2.configure(text="Resultado en Milimetros")
        Texto4.configure(text="Resultado en Centimetros", fg="white")
        Texto3.configure(fg="white")
        Texto3.place(x=65)
        btn_conversion2.configure(width=10,height=0, bg="#DBE8E1")
        btn_conversion2.place(x=215,y=380)
        btn_siguiente.place(x=236, y=434)
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*(10**6)
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente1)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*100000
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        


    btn_conversion1 = tk.Button(Ventana_Kilometro,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion1.place(x= 215, y= 227)

    btn_conversion2 = tk.Button(Ventana_Kilometro,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion2,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion2.place(x= 215, y= 380)
    
    btn_volver = tk.Button(Ventana_Kilometro,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[Ventana_Longitud2.deiconify(),unidades_longitud2, Ventana_Kilometro.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)

    btn_siguiente = tk.Button(Ventana_Kilometro,font = fnt.Font(size = 12), text="➤",command=siguiente1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_siguiente.place(x= 236, y= 434)
    Ventana_Kilometro.mainloop()
def Centimetro():
    Ventana_Longitud1.withdraw()
    Ventana_Centimetro = tk.Toplevel()
    Ventana_Centimetro.geometry("500x500+400+80")
    Ventana_Centimetro.resizable(height="false", width="false")
    Ventana_Centimetro.title("Conversion de Centimetro")
    Fondo_Ventana_Centimetro = tk.PhotoImage(file="Conversion1.png")
    Fondo_ub_Centimetro = tk.Label(Ventana_Centimetro,image=Fondo_Ventana_Centimetro).place(x=0, y=0, relheight=1, relwidth=1)

    numero1 = tk.StringVar()
    numero2 = tk.StringVar()
    Titulo = tk.Label(Ventana_Centimetro,text=("CENTIMETROS"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=180, y=75)

    Texto1 = tk.Label(Ventana_Centimetro,text=("Digite el valor en Centimetros"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto1.place(x=65, y=145)

    Texto2 = tk.Label(Ventana_Centimetro,text=("Resultado en Milimetros"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto2.place(x=280, y=145)

    Texto3 = tk.Label(Ventana_Centimetro,text=("Digite el valor en Centimetros"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto3.place(x=65, y=294)

    Texto4 = tk.Label(Ventana_Centimetro,text=("Resultado en Metros"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto4.place(x=280, y=294)

    entrada1 = Entry(Ventana_Centimetro,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero1)
    entrada1.place(x=69, y=174)

    entrada2 = Entry(Ventana_Centimetro,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero2)
    entrada2.place(x=69, y=330)

    salida1 =  tk.Entry(Ventana_Centimetro,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida1.place(x=280, y=175)

    salida2 =  tk.Entry(Ventana_Centimetro,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida2.place(x=280, y=330)

    def conversion1():
        salida1.delete(0, END)
        num = int(numero1.get())
        resultado = num*10
        salida1.insert(0, resultado)
   
    def conversion2():
        salida2.delete(0, END)
        num = int(numero2.get())
        resultado = num/100
        salida2.insert(0, resultado)
   

    def siguiente1():

        Texto2.configure(text="Resultado en Pulgadas")
        Texto4.configure(text="Resultado en Pies")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/2.54
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente2)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/30.48
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente2():
        Texto2.configure(text="Resultado en Yardas")
        Texto4.configure(text="Resultado en Kilometros")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/91.44
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente3)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/100000
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente3():
        Texto2.configure(text="Resultado en Millas")
        Texto3.configure(fg="#151b25")
        Texto3.place(x=290)
        Texto4.configure(fg="#151B25")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        Fondo_Ventana_Centimetro.configure(file="Conversion_Final.png")
        btn_conversion2.configure(width=500,height=5, bg="#151b25")
        btn_conversion2.place(x=0,y=330)
        btn_siguiente.place(x=235, y=286)

        def nueva_conversion1():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/160934
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion1)
        btn_siguiente.configure(command=siguiente4)
    
    def siguiente4():
        Fondo_Ventana_Centimetro.configure(file="Conversion1.png")
        Texto2.configure(text="Resultado en Milimetros")
        Texto4.configure(text="Resultado en Metros", fg="white")
        Texto3.configure(fg="white")
        Texto3.place(x=65)
        btn_conversion2.configure(width=10,height=0, bg="#DBE8E1")
        btn_conversion2.place(x=215,y=380)
        btn_siguiente.place(x=236, y=434)
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*10
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente1)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/100
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    btn_volver = tk.Button(Ventana_Centimetro,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[Ventana_Longitud1.deiconify(),unidades_longitud, Ventana_Centimetro.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)

    btn_conversion1 = tk.Button(Ventana_Centimetro,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion1.place(x= 215, y= 227)

    btn_conversion2 = tk.Button(Ventana_Centimetro,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion2,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion2.place(x= 215, y= 380)
    

    btn_siguiente = tk.Button(Ventana_Centimetro,font = fnt.Font(size = 12), text="➤",command=siguiente1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_siguiente.place(x= 236, y= 434)
    Ventana_Centimetro.mainloop()
def Milimetro():
    Ventana_Longitud1.withdraw()
    Ventana_Milimetro = tk.Toplevel()
    Ventana_Milimetro.geometry("500x500+400+80")
    Ventana_Milimetro.resizable(height="false", width="false")
    Ventana_Milimetro.title("Grados Milimetro")
    Fondo_Ventana_Milimetro = tk.PhotoImage(file="Conversion1.png")
    Fondo_ub_Milimetro = tk.Label(Ventana_Milimetro,image=Fondo_Ventana_Milimetro).place(x=0, y=0, relheight=1, relwidth=1)

    numero1 = tk.StringVar()
    numero2 = tk.StringVar()
    Titulo = tk.Label(Ventana_Milimetro,text=("MILIMETROS"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=200, y=75)

    Texto1 = tk.Label(Ventana_Milimetro,text=("Digite el valor en Milimetros"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto1.place(x=65, y=145)

    Texto2 = tk.Label(Ventana_Milimetro,text=("Resultado en Centimetros"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto2.place(x=280, y=145)

    Texto3 = tk.Label(Ventana_Milimetro,text=("Digite el valor en Milimetros"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto3.place(x=65, y=294)

    Texto4 = tk.Label(Ventana_Milimetro,text=("Resultado en Metros"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto4.place(x=280, y=294)

    entrada1 = Entry(Ventana_Milimetro,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero1)
    entrada1.place(x=69, y=174)

    entrada2 = Entry(Ventana_Milimetro,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero2)
    entrada2.place(x=69, y=330)

    salida1 =  tk.Entry(Ventana_Milimetro,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida1.place(x=280, y=175)

    salida2 =  tk.Entry(Ventana_Milimetro,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida2.place(x=280, y=330)

    def conversion1():
        salida1.delete(0, END)
        num = int(numero1.get())
        resultado = num/10
        salida1.insert(0, resultado)
   
    def conversion2():
        salida2.delete(0, END)
        num = int(numero2.get())
        resultado = num/1000
        salida2.insert(0, resultado)
   

    def siguiente1():
        Texto2.configure(text="Resultado en Pulgadas")
        Texto4.configure(text="Resultado en Pies")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/25.4
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente2)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/305
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente2():
        Texto2.configure(text="Resultado en Yardas")
        Texto4.configure(text="Resultado en Kilometros")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/914
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente3)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/(10**6)
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente3():
        Texto2.configure(text="Resultado en Millas")
        Texto3.configure(fg="#151b25")
        Texto3.place(x=290)
        Texto4.configure(fg="#151B25")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        Fondo_Ventana_Milimetro.configure(file="Conversion_Final.png")
        btn_conversion2.configure(width=500,height=5, bg="#151b25")
        btn_conversion2.place(x=0,y=330)
        btn_siguiente.place(x=235, y=286)

        def nueva_conversion1():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/(1.609*(10**6))
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion1)
        btn_siguiente.configure(command=siguiente4)
    
    def siguiente4():
        Fondo_Ventana_Milimetro.configure(file="Conversion1.png")
        Texto2.configure(text="Resultado en Centimetros")
        Texto4.configure(text="Resultado en Metros", fg="white")
        Texto3.configure(fg="white")
        Texto3.place(x=65)
        btn_conversion2.configure(width=10,height=0, bg="#DBE8E1")
        btn_conversion2.place(x=215,y=380)
        btn_siguiente.place(x=236, y=434)
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/10
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente1)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/1000
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    btn_volver = tk.Button(Ventana_Milimetro,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[Ventana_Longitud1.deiconify(),unidades_longitud, Ventana_Milimetro.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)

    btn_conversion1 = tk.Button(Ventana_Milimetro,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion1.place(x= 215, y= 227)

    btn_conversion2 = tk.Button(Ventana_Milimetro,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion2,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion2.place(x= 215, y= 380)
    

    btn_siguiente = tk.Button(Ventana_Milimetro,font = fnt.Font(size = 12), text="➤",command=siguiente1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_siguiente.place(x= 236, y= 434)
    Ventana_Milimetro.mainloop()
    
###################################################################################################################
###############################################################################################################
###############################################################################################################
def unidades_volumen():
    global Ventana_Volumen1
    conversion_unidades1.withdraw()
    Ventana_Volumen1 = tk.Toplevel()
    Ventana_Volumen1.title("Conversion Unidades de Volumen")
    Ventana_Volumen1.geometry("500x500+400+80")
    Volumen_img  = tk.PhotoImage(file="Conversiones.png")
    Img_ub_Volumen = tk.Label(Ventana_Volumen1,image=Volumen_img).place(x=0, y=0, relheight=1, relwidth=1)
    Titulo = tk.Label(Ventana_Volumen1,text=("UNIDADES DE VOLUMEN"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=130, y=75)
    btn_Mililitro = tk.Button(Ventana_Volumen1,
     width=12,
     text="Mililitro",
     font="Bodoni",
     command= Mililitro,
     cursor="hand2",
     bg="#DBE8E1",
     fg="#E10032",
     relief="flat")
    btn_Mililitro.place(x=180, y=175)

    btn_Cuarto = tk.Button(Ventana_Volumen1,
     width=12,
     text="Cuarto",
     font="Bodoni",
     command= Cuarto,
     cursor="hand2",
     bg="#DBE8E1",
     fg="#E10032",
     relief="flat")
    btn_Cuarto.place(x=180, y=376)

    btn_Litro = tk.Button(Ventana_Volumen1,
     width=12,
     text="Litro",
     font="Bodoni",
     command= Litro,
     cursor="hand2",
     bg="#DBE8E1",
     fg="#E10032",
     relief="flat")
    btn_Litro.place(x=180, y=307)

    btn_Galon = tk.Button(Ventana_Volumen1,
     width=12,
     text="Galon",
     font="Bodoni",
     command=Galon,
     cursor="hand2",
     bg="#DBE8E1",
     fg="#E10032",
     relief="flat")
    btn_Galon.place(x=180, y=240)

    btn_mas = tk.Button(Ventana_Volumen1,
    width=13,
    text="Mas conversiones",
    font = fnt.Font(size = 8),
    command=unidades_volumen2,
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_mas.place(x=208, y=440)

    btn_volver = tk.Button(Ventana_Volumen1,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[conversion_unidades1.deiconify(),conversion_unidades, Ventana_Volumen1.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)

    Ventana_Volumen1.mainloop()
    unidades_volumen()
def unidades_volumen2():
    global Ventana_Volumen2
    Ventana_Volumen1.withdraw()
    Ventana_Volumen2 = tk.Toplevel()
    Ventana_Volumen2.title("Conversion Unidades de Longitud")
    Ventana_Volumen2.geometry("500x500+400+80")
    Longitud_img  = tk.PhotoImage(file="Volumen2.png")
    Img_ub_Longitud = tk.Label(Ventana_Volumen2,image=Longitud_img).place(x=0, y=0, relheight=1, relwidth=1)
    Titulo = tk.Label(Ventana_Volumen2,text=("UNIDADES DE VOLUMEN"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=130, y=75)
    btn_Pie_Cubico = tk.Button(Ventana_Volumen2,
     width=12,
     text="Pie Cubico",
     font="Bodoni",
     command= Pie_Cubico,
     cursor="hand2",
     bg="#DBE8E1",
     fg="#E10032",
     relief="flat")
    btn_Pie_Cubico.place(x=180, y=175)

    btn_Metro_Cubico = tk.Button(Ventana_Volumen2,
     width=12,
     text="Metro Cubico",
     font="Bodoni",
     command=Metro_Cubico,
     cursor="hand2",
     bg="#DBE8E1",
     fg="#E10032",
     relief="flat")
    btn_Metro_Cubico.place(x=180, y=240)
    
    btn_mas = tk.Button(Ventana_Volumen2,
    width=13,
    text="Volver",
    font = fnt.Font(size = 8),
    command=lambda:[Ventana_Volumen1.deiconify(),unidades_volumen, Ventana_Volumen2.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_mas.place(x=205, y=308)

    btn_volver = tk.Button(Ventana_Volumen2,
    width=15,
    height=15,
    text="",
    command=conversion_unidades,
    cursor="hand2",
    bg="#151B25",
    fg="#151B25",
    relief="flat")
    btn_volver.place(x=5, y=465)
    Ventana_Volumen2.mainloop()
    unidades_longitud2()
def Pie_Cubico():
    Ventana_Volumen2.withdraw()
    Ventana_Pie_Cubico = tk.Toplevel()
    Ventana_Pie_Cubico.geometry("500x500+400+80")
    Ventana_Pie_Cubico.title("Conversion de Pie Cubico")
    Ventana_Pie_Cubico.resizable(width=False, height=False)
    fondo_Ventana_Pie_Cubico = tk.PhotoImage(file="Conversion1.png")
    fondo_ub_Ventana_Pie_Cubico = tk.Label(Ventana_Pie_Cubico, image=fondo_Ventana_Pie_Cubico).place(x=0, y=0,relheight=1, relwidth=1)
    numero1 = tk.StringVar()
    numero2 = tk.StringVar()
    Titulo = tk.Label(Ventana_Pie_Cubico,text=("PIES CUBICOS"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=190, y=75)

    Texto1 = tk.Label(Ventana_Pie_Cubico,text=("Digite el valor en P.Cubicos"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto1.place(x=65, y=145)

    Texto2 = tk.Label(Ventana_Pie_Cubico,text=("Resultado en Mililitros"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto2.place(x=280, y=145)

    Texto3 = tk.Label(Ventana_Pie_Cubico,text=("Digite el valor en P.Cubicos"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto3.place(x=65, y=294)

    Texto4 = tk.Label(Ventana_Pie_Cubico,text=("Resultado en Cuartos"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto4.place(x=280, y=294)

    entrada1 = Entry(Ventana_Pie_Cubico,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero1)
    entrada1.place(x=69, y=174)

    entrada2 = Entry(Ventana_Pie_Cubico,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero2)
    entrada2.place(x=69, y=330)

    salida1 =  tk.Entry(Ventana_Pie_Cubico,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida1.place(x=280, y=175)

    salida2 =  tk.Entry(Ventana_Pie_Cubico,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida2.place(x=280, y=330)

    def conversion1():
        salida1.delete(0, END)
        num = int(numero1.get())
        resultado = num*28317
        salida1.insert(0, resultado)
   
    def conversion2():
        salida2.delete(0, END)
        num = int(numero2.get())
        resultado = num*29.922
        salida2.insert(0, resultado)
   

    def siguiente1():
        Texto2.configure(text="Resultado en Litros")
        Texto4.configure(text="Resultado en Galones")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*28.317
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente3)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*7.481
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
    
    
    def siguiente3():
        Texto2.configure(text="Resultado en M.Cubicos")
        fondo_Ventana_Pie_Cubico.configure(file="Conversion_Final.png")
        Texto3.configure(fg="#151b25")
        Texto3.place(x=290)
        Texto4.configure(fg="#151B25")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        fondo_Ventana_Pie_Cubico.configure(file="Conversion_Final.png")
        btn_conversion2.configure(width=500,height=5, bg="#151b25")
        btn_conversion2.place(x=0,y=330)
        btn_siguiente.place(x=235, y=286)

        def nueva_conversion1():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num+15
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion1)
        btn_siguiente.configure(command=siguiente4)
    
    def siguiente4():
        fondo_Ventana_Pie_Cubico.configure(file="Conversion1.png")
        Texto2.configure(text="Resultado en Mililitros")
        Texto4.configure(text="Resultado en Cuartos", fg="white")
        Texto3.configure(fg="#151B25")
        Texto3.place(x=290)
        Texto4.configure(fg="#151B25")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        fondo_Ventana_Pie_Cubico.configure(file="Conversion_Final.png")
        btn_conversion2.configure(width=500,height=5, bg="#151b25")
        btn_conversion2.place(x=0,y=330)
        btn_siguiente.place(x=235, y=286)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*28317
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente1)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*29.922
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    btn_volver = tk.Button(Ventana_Pie_Cubico,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[Ventana_Volumen2.deiconify(),unidades_volumen2, Ventana_Pie_Cubico.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)

    btn_conversion1 = tk.Button(Ventana_Pie_Cubico,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion1.place(x= 215, y= 227)

    btn_conversion2 = tk.Button(Ventana_Pie_Cubico,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion2,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion2.place(x= 215, y= 380)
    

    btn_siguiente = tk.Button(Ventana_Pie_Cubico,font = fnt.Font(size = 12), text="➤",command=siguiente1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_siguiente.place(x= 236, y= 434)

    Ventana_Pie_Cubico.mainloop()
def Litro():
    Ventana_Volumen1.withdraw()
    Ventana_Litro = tk.Toplevel()
    Ventana_Litro.geometry("500x500+400+80")
    Ventana_Litro.title("Conversion de Litro")
    Ventana_Litro.resizable(width="false", height="false" )
    Fondo_Ventana_Litro = tk.PhotoImage(file="Conversion1.png")
    Fondo_ub_Ventana_Litro = tk.Label(Ventana_Litro,image=Fondo_Ventana_Litro).place(x=0, y=0, relheight=1, relwidth=1)
    numero1 = tk.StringVar()
    numero2 = tk.StringVar()
    Titulo = tk.Label(Ventana_Litro,text=("LITROS"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=215, y=75)

    Texto1 = tk.Label(Ventana_Litro,text=("Digite el valor en Litros"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto1.place(x=65, y=145)

    Texto2 = tk.Label(Ventana_Litro,text=("Resultado en Mililitros"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto2.place(x=280, y=145)

    Texto3 = tk.Label(Ventana_Litro,text=("Digite el valor en Litros"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto3.place(x=65, y=294)

    Texto4 = tk.Label(Ventana_Litro,text=("Resultado en Cuartos"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto4.place(x=280, y=294)

    entrada1 = Entry(Ventana_Litro,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero1)
    entrada1.place(x=69, y=174)

    entrada2 = Entry(Ventana_Litro,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero2)
    entrada2.place(x=69, y=330)

    salida1 =  tk.Entry(Ventana_Litro,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida1.place(x=280, y=175)

    salida2 =  tk.Entry(Ventana_Litro,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida2.place(x=280, y=330)

    def conversion1():
        salida1.delete(0, END)
        num = int(numero1.get())
        resultado = num*1000
        salida1.insert(0, resultado)
   
    def conversion2():
        salida2.delete(0, END)
        num = int(numero2.get())
        resultado = num*1.057
        salida2.insert(0, resultado)
   

    def siguiente1():
        Texto2.configure(text="Resultado en Galones ")
        Texto4.configure(text="Resultado en P.Cubicos")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/3.785
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente3)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/28.317
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente3():
        Texto2.configure(text="Resultado en M.Cubico")
        Texto3.configure(fg="#151b25")
        Texto3.place(x=290)
        Texto4.configure(fg="#151B25")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        Fondo_Ventana_Litro.configure(file="Conversion_Final.png")
        btn_conversion2.configure(width=500,height=5, bg="#151b25")
        btn_conversion2.place(x=0,y=330)
        btn_siguiente.place(x=235, y=286)

        def nueva_conversion1():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/1000
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion1)
        btn_siguiente.configure(command=siguiente4)
    
    def siguiente4():
        Fondo_Ventana_Litro.configure(file="Conversion1.png")
        Texto2.configure(text="Resultado en Mililitro")
        Texto4.configure(text="Resultado en Cuarto", fg="white")
        Texto3.configure(fg="white")
        Texto3.place(x=65)
        btn_conversion2.configure(width=10,height=0, bg="#DBE8E1")
        btn_conversion2.place(x=215,y=380)
        btn_siguiente.place(x=236, y=434)
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*1000
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente1)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*1.057
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    btn_volver = tk.Button(Ventana_Litro,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[Ventana_Volumen1.deiconify(),unidades_volumen, Ventana_Litro.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)

    btn_conversion1 = tk.Button(Ventana_Litro,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion1.place(x= 215, y= 227)

    btn_conversion2 = tk.Button(Ventana_Litro,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion2,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion2.place(x= 215, y= 380)
    

    btn_siguiente = tk.Button(Ventana_Litro,font = fnt.Font(size = 12), text="➤",command=siguiente1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_siguiente.place(x= 236, y= 434)

    Ventana_Litro.mainloop()
def Galon():
    Ventana_Volumen1.withdraw()
    Ventana_Galon = tk.Toplevel()
    Ventana_Galon.geometry("500x500+400+80")
    Ventana_Galon.resizable(height="false", width="false")
    Ventana_Galon.title("Conversion de Galon")
    Fondo_Ventana_Galon = tk.PhotoImage(file="Conversion1.png")
    Fondo_ub_Galon = tk.Label(Ventana_Galon,image=Fondo_Ventana_Galon).place(x=0, y=0, relheight=1, relwidth=1)

    numero1 = tk.StringVar()
    numero2 = tk.StringVar()
    Titulo = tk.Label(Ventana_Galon,text=("GALONES"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=205, y=75)

    Texto1 = tk.Label(Ventana_Galon,text=("Digite el valor en Galones"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto1.place(x=65, y=145)

    Texto2 = tk.Label(Ventana_Galon,text=("Resultado en Mililitros"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto2.place(x=280, y=145)

    Texto3 = tk.Label(Ventana_Galon,text=("Digite el valor en Galones"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto3.place(x=65, y=294)

    Texto4 = tk.Label(Ventana_Galon,text=("Resultado en Cuartos"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto4.place(x=280, y=294)

    entrada1 = Entry(Ventana_Galon,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero1)
    entrada1.place(x=69, y=174)

    entrada2 = Entry(Ventana_Galon,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero2)
    entrada2.place(x=69, y=330)

    salida1 =  tk.Entry(Ventana_Galon,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida1.place(x=280, y=175)

    salida2 =  tk.Entry(Ventana_Galon,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida2.place(x=280, y=330)

    def conversion1():
        salida1.delete(0, END)
        num = int(numero1.get())
        resultado = num*3785
        salida1.insert(0, resultado)
   
    def conversion2():
        salida2.delete(0, END)
        num = int(numero2.get())
        resultado = num*4
        salida2.insert(0, resultado)
   

    def siguiente1():
        Texto2.configure(text="Resultado en Litros ")
        Texto4.configure(text="Resultado en Pies Cubicos")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*3.785
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente3)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/7.481
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente3():
        Fondo_Ventana_Galon.configure(file="Conversion_Final.png")
        Texto2.configure(text="Resultado en Metro Cubico")
        Texto3.configure(fg="#151B25")
        Texto3.place(x=290)
        Texto4.configure(fg="#151B25")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        Fondo_Ventana_Galon.configure(file="Conversion_Final.png")
        btn_conversion2.configure(width=500,height=5, bg="#151b25")
        btn_conversion2.place(x=0,y=330)
        btn_siguiente.place(x=235, y=286)

        def nueva_conversion1():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/264
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion1)
        btn_siguiente.configure(command=siguiente4)
    
    def siguiente4():
        Fondo_Ventana_Galon.configure(file="Conversion1.png")
        Texto2.configure(text="Resultado en Mililitro")
        Texto4.configure(text="Resultado en Cuarto", fg="white")
        Texto3.configure(fg="white")
        Texto3.place(x=65)
        btn_conversion2.configure(width=10,height=0, bg="#DBE8E1")
        btn_conversion2.place(x=215,y=380)
        btn_siguiente.place(x=236, y=434)
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*3785
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente1)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*4
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    btn_volver = tk.Button(Ventana_Galon,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[Ventana_Volumen1.deiconify(),unidades_volumen, Ventana_Galon.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)

    btn_conversion1 = tk.Button(Ventana_Galon,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion1.place(x= 215, y= 227)

    btn_conversion2 = tk.Button(Ventana_Galon,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion2,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion2.place(x= 215, y= 380)
    

    btn_siguiente = tk.Button(Ventana_Galon,font = fnt.Font(size = 12), text="➤",command=siguiente1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_siguiente.place(x= 236, y= 434)
    Ventana_Galon.mainloop()
def Cuarto():
    Ventana_Volumen1.withdraw()
    Ventana_Cuarto = tk.Toplevel()
    Ventana_Cuarto.geometry("500x500+400+80")
    Ventana_Cuarto.title("Conversion de Cuarto")
    Ventana_Cuarto.resizable(width=False, height=False)
    fondo_Ventana_Cuarto = tk.PhotoImage(file="Conversion1.png")
    fondo_ub_Ventana_Cuarto = tk.Label(Ventana_Cuarto, image=fondo_Ventana_Cuarto).place(x=0, y=0,relheight=1, relwidth=1)
    numero1 = tk.StringVar()
    numero2 = tk.StringVar()
    Titulo = tk.Label(Ventana_Cuarto,text=("CUARTOS"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=210, y=75)

    Texto1 = tk.Label(Ventana_Cuarto,text=("Digite el valor en Cuartos"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto1.place(x=65, y=145)

    Texto2 = tk.Label(Ventana_Cuarto,text=("Resultado en Mililitros"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto2.place(x=280, y=145)

    Texto3 = tk.Label(Ventana_Cuarto,text=("Digite el valor en Cuartos"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto3.place(x=65, y=294)

    Texto4 = tk.Label(Ventana_Cuarto,text=("Resultado en Litros"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto4.place(x=280, y=294)

    entrada1 = Entry(Ventana_Cuarto,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero1)
    entrada1.place(x=69, y=174)

    entrada2 = Entry(Ventana_Cuarto,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero2)
    entrada2.place(x=69, y=330)

    salida1 =  tk.Entry(Ventana_Cuarto,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida1.place(x=280, y=175)

    salida2 =  tk.Entry(Ventana_Cuarto,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida2.place(x=280, y=330)

    def conversion1():
        salida1.delete(0, END)
        num = int(numero1.get())
        resultado = num*946
        salida1.insert(0, resultado)
   
    def conversion2():
        salida2.delete(0, END)
        num = int(numero2.get())
        resultado = num*1.057
        salida2.insert(0, resultado)
   

    def siguiente1():
        Texto2.configure(text="Resultado en Galones ")
        Texto4.configure(text="Resultado en Pies Cubicos")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/4
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente3)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/29.922
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente3():
        fondo_Ventana_Cuarto.configure(file="Conversion_Final.png")
        Texto2.configure(text="Resultado en Metro Cubico")
        Texto3.configure(fg="#151B25")
        Texto3.place(x=290)
        Texto4.configure(fg="#151B25")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        fondo_Ventana_Cuarto.configure(file="Conversion_Final.png")
        btn_conversion2.configure(width=500,height=5, bg="#151b25")
        btn_conversion2.place(x=0,y=330)
        btn_siguiente.place(x=235, y=286)

        def nueva_conversion1():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/1057
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion1)
        btn_siguiente.configure(command=siguiente4)
    
    def siguiente4():
        fondo_Ventana_Cuarto.configure(file="Conversion1.png")
        Texto2.configure(text="Resultado en Mililitros")
        Texto4.configure(text="Resultado en Litros", fg="white")
        Texto3.configure(fg="white")
        Texto3.place(x=65)
        btn_conversion2.configure(width=10,height=0, bg="#DBE8E1")
        btn_conversion2.place(x=215,y=380)
        btn_siguiente.place(x=236, y=434)
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*946
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente1)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/1.057
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    btn_volver = tk.Button(Ventana_Cuarto,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[Ventana_Volumen1.deiconify(),unidades_volumen, Ventana_Cuarto.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)

    btn_conversion1 = tk.Button(Ventana_Cuarto,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion1.place(x= 215, y= 227)

    btn_conversion2 = tk.Button(Ventana_Cuarto,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion2,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion2.place(x= 215, y= 380)
    

    btn_siguiente = tk.Button(Ventana_Cuarto,font = fnt.Font(size = 12), text="➤",command=siguiente1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_siguiente.place(x= 236, y= 434)

    Ventana_Cuarto.mainloop()
def Mililitro():
    Ventana_Volumen1.withdraw()
    Ventana_Mililitro = tk.Toplevel()
    Ventana_Mililitro.geometry("500x500+400+80")
    Ventana_Mililitro.title("Conversion de Mililitro")
    Ventana_Mililitro.resizable(width="false", height="false" )
    Fondo_Ventana_Mililitro = tk.PhotoImage(file="Conversion1.png")
    Fondo_ub_Ventana_Mililitro = tk.Label(Ventana_Mililitro,image=Fondo_Ventana_Mililitro).place(x=0, y=0, relheight=1, relwidth=1)
    numero1 = tk.StringVar()
    numero2 = tk.StringVar()
    Titulo = tk.Label(Ventana_Mililitro,text=("MILILITROS"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=205, y=75)

    Texto1 = tk.Label(Ventana_Mililitro,text=("Digite el valor en Mililitros"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto1.place(x=65, y=145)

    Texto2 = tk.Label(Ventana_Mililitro,text=("Resultado en Cuartos"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto2.place(x=280, y=145)

    Texto3 = tk.Label(Ventana_Mililitro,text=("Digite el valor en Mililitros"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto3.place(x=65, y=294)

    Texto4 = tk.Label(Ventana_Mililitro,text=("Resultado en Litros"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto4.place(x=280, y=294)

    entrada1 = Entry(Ventana_Mililitro,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero1)
    entrada1.place(x=69, y=174)

    entrada2 = Entry(Ventana_Mililitro,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero2)
    entrada2.place(x=69, y=330)

    salida1 =  tk.Entry(Ventana_Mililitro,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida1.place(x=280, y=175)

    salida2 =  tk.Entry(Ventana_Mililitro,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida2.place(x=280, y=330)

    def conversion1():
        salida1.delete(0, END)
        num = int(numero1.get())
        resultado = num/946
        salida1.insert(0, resultado)
   
    def conversion2():
        salida2.delete(0, END)
        num = int(numero2.get())
        resultado = num/1000
        salida2.insert(0, resultado)
   

    def siguiente1():
        Texto2.configure(text="Resultado en Galones ")
        Texto4.configure(text="Resultado en Pies Cubicos")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/3785
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente3)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/28317
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente3():
        Fondo_Ventana_Mililitro.configure(file="Conversion_Final.png")
        Texto2.configure(text="Resultado en Metros Cubicos")
        Texto3.configure(fg="#151B25")
        Texto3.place(x=290)
        Texto4.configure(fg="#151B25")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        Fondo_Ventana_Mililitro.configure(file="Conversion_Final.png")
        btn_conversion2.configure(width=500,height=5, bg="#151b25")
        btn_conversion2.place(x=0,y=330)
        btn_siguiente.place(x=235, y=286)

        def nueva_conversion1():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*(10**6)
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion1)
        btn_siguiente.configure(command=siguiente4)
    
    def siguiente4():
        Fondo_Ventana_Mililitro.configure(file="Conversion1.png")
        Texto2.configure(text="Resultado en Cuartos")
        Texto4.configure(text="Resultado en Litros", fg="white")
        Texto3.configure(fg="white")
        Texto3.place(x=65)
        btn_conversion2.configure(width=10,height=0, bg="#DBE8E1")
        btn_conversion2.place(x=215,y=380)
        btn_siguiente.place(x=236, y=434)
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num/946
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente1)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num/1000
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    btn_volver = tk.Button(Ventana_Mililitro,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[Ventana_Volumen1.deiconify(),unidades_volumen, Ventana_Mililitro.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)

    btn_conversion1 = tk.Button(Ventana_Mililitro,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion1.place(x= 215, y= 227)

    btn_conversion2 = tk.Button(Ventana_Mililitro,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion2,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion2.place(x= 215, y= 380)
    

    btn_siguiente = tk.Button(Ventana_Mililitro,font = fnt.Font(size = 12), text="➤",command=siguiente1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_siguiente.place(x= 236, y= 434)

    Ventana_Mililitro.mainloop()
def Metro_Cubico():
    Ventana_Volumen2.withdraw()
    Ventana_Metro_Cubico = tk.Toplevel()
    Ventana_Metro_Cubico.geometry("500x500+400+80")
    Ventana_Metro_Cubico.resizable(height="false", width="false")
    Ventana_Metro_Cubico.title("Conversion de Metro Cubico")
    Fondo_Ventana_Metro_Cubico = tk.PhotoImage(file="Conversion1.png")
    Fondo_ub_Metro_Cubico = tk.Label(Ventana_Metro_Cubico,image=Fondo_Ventana_Metro_Cubico).place(x=0, y=0, relheight=1, relwidth=1)

    numero1 = tk.StringVar()
    numero2 = tk.StringVar()
    Titulo = tk.Label(Ventana_Metro_Cubico,text=("METROS CUBICOS"),fg=("#E10032") ,font=("Bodoni"), bg="#DBE8E1", relief="flat")
    Titulo.place(x=170, y=75)

    Texto1 = tk.Label(Ventana_Metro_Cubico,text=("Digite el valor en M.Cubicos"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto1.place(x=65, y=145)

    Texto2 = tk.Label(Ventana_Metro_Cubico,text=("Resultado en Cuartos"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto2.place(x=280, y=145)

    Texto3 = tk.Label(Ventana_Metro_Cubico,text=("Digite el valor en M.Cubicos"),fg=("White") ,font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto3.place(x=65, y=294)

    Texto4 = tk.Label(Ventana_Metro_Cubico,text=("Resultado en Litros"),fg=("White"),  font=("Bodoni", 11), bg="#151B25", relief="flat")
    Texto4.place(x=280, y=294)

    entrada1 = Entry(Ventana_Metro_Cubico,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero1)
    entrada1.place(x=69, y=174)

    entrada2 = Entry(Ventana_Metro_Cubico,width=18, font=("Bodoni", 11), bg="#DBE8E1", relief="flat", textvariable=numero2)
    entrada2.place(x=69, y=330)

    salida1 =  tk.Entry(Ventana_Metro_Cubico,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida1.place(x=280, y=175)

    salida2 =  tk.Entry(Ventana_Metro_Cubico,font=("Bodoni", 11), bg="#DBE8E1", relief="flat")
    salida2.place(x=280, y=330)

    def conversion1():
        salida1.delete(0, END)
        num = int(numero1.get())
        resultado = num*1057
        salida1.insert(0, resultado)
   
    def conversion2():
        salida2.delete(0, END)
        num = int(numero2.get())
        resultado = num*1000
        salida2.insert(0, resultado)
   

    def siguiente1():
        Texto2.configure(text="Resultado en Galones ")
        Texto4.configure(text="Resultado en P.Cubicos")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*264
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente3)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*35.315
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    
    def siguiente3():
        Fondo_Ventana_Metro_Cubico.configure(file="Conversion_Final.png")
        Texto2.configure(text="Resultado en Mililitros")
        Texto3.configure(fg="#151b25")
        Texto3.place(x=290)
        Texto4.configure(fg="#151B25")
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        Fondo_Ventana_Metro_Cubico.configure(file="Conversion_Final.png")
        btn_conversion2.configure(width=500,height=5, bg="#151b25")
        btn_conversion2.place(x=0,y=330)
        btn_siguiente.place(x=235, y=286)

        def nueva_conversion1():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*(10**6)
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion1)
        btn_siguiente.configure(command=siguiente4)
    
    def siguiente4():
        Fondo_Ventana_Metro_Cubico.configure(file="Conversion1.png")
        Texto2.configure(text="Resultado en Cuartos")
        Texto4.configure(text="Resultado en Litros", fg="white")
        Texto3.configure(fg="white")
        Texto3.place(x=65)
        btn_conversion2.configure(width=10,height=0, bg="#DBE8E1")
        btn_conversion2.place(x=215,y=380)
        btn_siguiente.place(x=236, y=434)
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        salida1.delete(0, END)
        salida2.delete(0, END)
        def nueva_conversion():
            salida1.delete(0, END)
            num = int(numero1.get())
            resultado = num*1057
            salida1.insert(0, resultado)
        btn_conversion1.configure(command=nueva_conversion)
        btn_siguiente.configure(command=siguiente1)
        def nueva_conversion2():
            salida2.delete(0, END)
            num = int(numero2.get())
            resultado = num*1000
            salida2.insert(0, resultado)
        btn_conversion2.configure(command=nueva_conversion2)
        
    btn_volver = tk.Button(Ventana_Metro_Cubico,
    text="VOLVER",
    font = fnt.Font(size = 6),
    command=lambda:[Ventana_Volumen2.deiconify(),unidades_volumen2, Ventana_Metro_Cubico.destroy()],
    cursor="hand2",
    bg="#DBE8E1",
    fg="#E10032",
    relief="flat")
    btn_volver.place(x=23, y=470)

    btn_conversion1 = tk.Button(Ventana_Metro_Cubico,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion1.place(x= 215, y= 227)

    btn_conversion2 = tk.Button(Ventana_Metro_Cubico,width=10,font=("Bodoni", 7), text="CONVERTIR",command=conversion2,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_conversion2.place(x= 215, y= 380)
    

    btn_siguiente = tk.Button(Ventana_Metro_Cubico,font = fnt.Font(size = 12), text="➤",command=siguiente1,cursor="hand2",bg="#DBE8E1", fg="#E10032", relief="flat" )
    btn_siguiente.place(x= 236, y= 434)
    Ventana_Metro_Cubico.mainloop()

######################################     Ventana Inicio  ##############################################################
inicio = tk.Tk()
inicio.title("Inicio")
inicio.geometry("500x500+400+80")
inicio.resizable(width="false", height="false")
inicio_img = tk.PhotoImage(file="Bienvenida.png")
inicio_ub_img = tk.Label(inicio, image=inicio_img).place(x=0, y=0, relheight=1, relwidth=1)
btn_inicio = tk.Button(inicio,text="DE CLICK EN LA PANTALLA PARA COMENZAR", width=500, height=500, relief="flat", command=pantalla_inicio, bg="#151b25", fg="#e10032")
btn_inicio.configure(font=("Bodoni MT", 16))
btn_inicio.place(x=0, y=0, relheight=1, relwidth=1)
inicio.mainloop()