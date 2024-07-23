o = input("Ingrese operación (+, -, *, /): ")
a = input("un número: ")
b = input("otro número: ")
if o == "+":
     x=a+b
elif o == "-":
   x=a-b
elif o == "*":
   x=a*b
elif o == "/":
      x=a/b
print("El resultado es:"+x)
c1 = input("Ingrese una cadena: ")
c2 = input("Ingrese otra cadena: ")
c1i = ""
for i in range(len(c1) - 1, -1, -1):
      c1i += c1[i]
if c1i == c2:
  print("Las cadenas son palíndromos")
import random
a=random.randint(1, 10)
b=input("Intente averiguar el número que pensé del 1 al 10: ")
if a == b:
  print("¡Adivinaste! el número era: "+a)
import pandas as p
d={'Nombre':['Juan','María', 'Pedro','Ana', 'Luis'],'Edad':[25, 30, 35, 28, 32],'Ciudad':['Madrid','Barcelona','Sevilla','Valencia', 'Bilbao'],'Profesión': ['Ingeniero', 'Abogado', 'Médico', 'Arquitecto', 'Profesor'],'Salario': [50000, 60000, 70000, 55000, 65000]}
print("Tabla de datos de referencia:");df=p.DataFrame(d);print(df);
e=input("Ingrese una edad para filtrar:");x=df[df['Edad']>int(e)];print("Mayores de ",e," años:");print(x)

import tkinter as tk
from tkinter import messagebox
import random
import pandas as pd


def c():
    o = o_e.get()
    n1 = float(n1_e.get())
    n2 = float(n2_e.get())

    if o == "+":
        x = n1 + n2
    elif o == "-":
        x = n1 - n2
    elif o == "*":
        x = n1 * n2
    elif o == "/":
        x = n1 / n2
    else:
        messagebox.showerror("Error", "Operación no válida")
        return

    r_l.config(text="El resultado es: " + str(x))


# Función para verificar si una cadena es un palíndromo
def v():
    c1 = c1_e.get()
    c2 = c2_e.get()
    c1i = c1[::-1]

    if c1i == c2:
        messagebox.showinfo("Resultado", "Las cadenas son palíndromos")
    else:
        messagebox.showinfo("Resultado", "Las cadenas no son palíndromos")
def ad():
    np = random.randint(1, 10)
    nu = int(nu_e.get())

    if nu == np:
        messagebox.showinfo("Resultado", "¡Adivinaste! El número era: " + str(np))
    else:
        messagebox.showinfo("Resultado", "No adivinaste. El número era: " + str(np))
def f():
    ef = int(e_e.get())
    rf = df[df['Edad'] > ef]
    messagebox.showinfo("Resultado", "Mayores de " + str(ef) + " años:\n" + str(rf))
window = tk.Tk()
window.title("Ejemplo")
o_l = tk.Label(window, text="Ingrese operación (+, -, *, /):")
o_l.pack()
o_e = tk.Entry(window)
o_e.pack()
n1_l = tk.Label(window, text="Ingrese un número:")
n1_l.pack()
n1_e = tk.Entry(window)
n1_e.pack()
n2_l = tk.Label(window, text="Ingrese otro número:")
n2_l.pack()
n2_e = tk.Entry(window)
n2_e.pack()

c_bt = tk.Button(window, text="Calcular", command=c)
c_bt.pack()

r_l = tk.Label(window, text="")
r_l.pack()

c1_l = tk.Label(window, text="Ingrese una cadena:")
c1_l.pack()
c1_e = tk.Entry(window)
c1_e.pack()

c2_l = tk.Label(window, text="Ingrese otra cadena:")
c2_l.pack()
c2_e = tk.Entry(window)
c2_e.pack()

vpb = tk.Button(window, text="Verificar Palíndromo", command=v)
vpb.pack()

# ---
nola = tk.Label(window, text="Intente averiguar el número que pensé del 1 al 10:")
nola.pack()
nu_e = tk.Entry(window)
nu_e.pack()
adb = tk.Button(window, text="Adivinar Número", command=ad)
adb.pack()
df = pd.DataFrame({'Nombre': ['Juan', 'María', 'Pedro', 'Ana', 'Luis'],
                   'Edad': [25, 30, 35, 28, 32],
                   'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia', 'Bilbao'],
                   'Profesión': ['Ingeniero', 'Abogado', 'Médico', 'Arquitecto', 'Profesor'],
                   'Salario': [50000, 60000, 70000, 55000, 65000]})
label_de_edad_tinker = tk.Label(window, text="Ingrese una edad para filtrar:")
label_de_edad_tinker.pack()
e_e = tk.Entry(window)
e_e.pack()
btdf = tk.Button(window, text="Filtrar", command=f)
btdf.pack()
window.mainloop()

import tkinter as tk
from tkinter import *

def agregar_caracter(caracter):
    entrada.insert(tk.END, caracter)


def limpiar_pantalla():
    entrada.delete(0, tk.END)


def calcular():
    expresion = entrada.get()
    try:
        resultado = eval(expresion)
        limpiar_pantalla()
        entrada.insert(tk.END, resultado)
    except:
        limpiar_pantalla()
        messagebox.showerror("Error", "Expresión inválida")


def borrar_caracter():
    entrada.delete(len(entrada.get()) - 1)


def limpiar_todo():
    limpiar_pantalla()


def punto_decimal():
    entrada.insert(tk.END, '.')


# Crear la ventana principal
window = tk.Tk()
window.title("Calculadora")

# Crear la entrada de la calculadora
entrada = tk.Entry(window, width=30)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Crear los botones numéricos
numeros = [
    ('7', 1, 0),
    ('8', 1, 1),
    ('9', 1, 2),
    ('4', 2, 0),
    ('5', 2, 1),
    ('6', 2, 2),
    ('1', 3, 0),
    ('2', 3, 1),
    ('3', 3, 2),
    ('0', 4, 0)
]
for numero, fila, columna in numeros:
    boton = tk.Button(window, text=numero, width=5, command=lambda numero=numero: agregar_caracter(numero))
    boton.grid(row=fila, column=columna, padx=5, pady=5)

# Crear los botones de operaciones
operaciones = ['+', '-', '*', '/']
for i, operacion in enumerate(operaciones):
    boton = tk.Button(window, text=operacion, width=5, command=lambda operacion=operacion: agregar_caracter(operacion))
    boton.grid(row=i + 1, column=3, padx=5, pady=5)

# Crear el botón de igual
igual_boton = tk.Button(window, text='=', width=5, command=calcular)
igual_boton.grid(row=4, column=2, padx=5, pady=5)

# Crear el botón de limpiar
limpiar_boton = tk.Button(window, text='C', width=5, command=limpiar_todo)
limpiar_boton.grid(row=4, column=1, padx=5, pady=5)

# Crear el botón de borrar
borrar_boton = tk.Button(window, text='⌫', width=5, command=borrar_caracter)
borrar_boton.grid(row=0, column=3, padx=5, pady=5)

# Crear el botón de punto decimal
decimal_boton = tk.Button(window, text='.', width=5, command=punto_decimal)
decimal_boton.grid(row=4, column=0, padx=5, pady=5)

# Iniciar el bucle de eventos de la ventana
window.mainloop()