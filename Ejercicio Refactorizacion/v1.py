import random
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import *
# -----------------------------------------------------------------------

data = {
    'Nombre':['Juan','María', 'Pedro','Ana', 'Luis'],
    'Edad':[25, 30, 35, 28, 32],
    'Ciudad':['Madrid','Barcelona','Sevilla','Valencia', 'Bilbao'],
    'Profesión': ['Ingeniero', 'Abogado', 'Médico', 'Arquitecto', 'Profesor'],
    'Salario': [50000, 60000, 70000, 55000, 65000]
}

# -----------------------------------------------------------------------

# Calcula una operación
operation_sign = input("Ingrese operación (+, -, *, /): ")
operator_a = input("un número: ")
operator_b = input("otro número: ")

def compute_operation(operation_sign, a_operator, b_operator):
	a_operator = float(a_operator)
	b_operator = float(b_operator)

	if operation_sign == "+":
		result = a_operator + b_operator
	elif operation_sign == "-":
		result = a_operator - b_operator
	elif operation_sign == "*":
		result = a_operator * b_operator
	elif operation_sign == "/":
		result = a_operator / b_operator
	else:
		result = None
    
	if result%1 == 0:
		return str(int(result))
	return str(result)

result = compute_operation(operation_sign, operator_a, operator_b)
print("El resultado es: " + result)

# -----------------------------------------------------------------------

# Verifica si una cadena es un palíndromo
string_1 = input("Ingrese una cadena: ")
string_2 = input("Ingrese otra cadena: ")

def check_palindrome(string_1, string_2):
	aux_string = ""
     
	for i in range(len(string_1) - 1, -1, -1):
		aux_string += string_1[i]
	
	return aux_string == string_2

if check_palindrome(string_1, string_2):
	print("Las cadenas son palíndromos")

# -----------------------------------------------------------------------

# Adivina un número
operator_a = random.randint(1, 10)
operator_b = input("Intente averiguar el número que pensé del 1 al 10: ")

def guess_number(operator_a, operator_b):
	return operator_a == operator_b

if guess_number(operator_b):
	print("¡Adivinaste! el número era: " + operator_a)

# -----------------------------------------------------------------------

# Filtra los datos por edad
data_df = pd.DataFrame(data)

print("Tabla de datos de referencia:")
print(data_df)

age_query = input("Ingrese una edad para filtrar:")

def age_filter(age):
	return data_df[data_df['Edad'] > int(age)]

print("Mayores de ", age_query, " años:")
print(age_filter(age_query))

# -----------------------------------------------------------------------

# Función para calcular una operación
def gui_compute_operation():
    sign = operation_input.get()
    number1 = float(num1_input.get())
    number2 = float(num2_input.get())

    result = compute_operation(sign, number1, number2)
    if result is None:
        messagebox.showerror("Error", "Operación no válida")
        return

    result_label.config(text="El resultado es: " + str(result))


# Función para verificar si una cadena es un palíndromo
def gui_check_palindrome():
    string1 = string1_input.get()
    string2 = string2_input.get()

    if check_palindrome(string1, string2):
        messagebox.showinfo("Resultado", "Las cadenas son palíndromos")
    else:
        messagebox.showinfo("Resultado", "Las cadenas no son palíndromos")

# Función para adivinar un número
def gui_guess_number():
    operator_a = random.randint(1, 10)
    correct_guess = guess_number(operator_a, int(number_guess_input.get()))

    if correct_guess:
        messagebox.showinfo("Resultado", "¡Adivinaste! El número era: " + str(operator_a))
    else:
        messagebox.showinfo("Resultado", "No adivinaste. El número era: " + str(operator_a))

# Función para filtrar por edad
def gui_age_filter():
    age = int(age_filter_input.get())
    filter_data = age_filter(age)
    messagebox.showinfo("Resultado", "Mayores de " + str(age) + " años:\n" + str(filter_data))
    
	
window = tk.Tk()
window.title("Ejemplo")

# --------------------------------------------------------------------------

# Calcular operación
operation_label = tk.Label(window, text="Ingrese operación (+, -, *, /):")
operation_label.pack()
operation_input = tk.Entry(window)
operation_input.pack()

num1_label = tk.Label(window, text="Ingrese un número:")
num1_label.pack()
num1_input = tk.Entry(window)
num1_input.pack()

num2_label = tk.Label(window, text="Ingrese otro número:")
num2_label.pack()
num2_input = tk.Entry(window)
num2_input.pack()

calculate_button = tk.Button(window, text="Calcular", command=gui_compute_operation)
calculate_button.pack()
result_label = tk.Label(window, text="")
result_label.pack()

# --------------------------------------------------------------------------

# Verificar palíndromo
string1_label = tk.Label(window, text="Ingrese una cadena:")
string1_label.pack()
string1_input = tk.Entry(window)
string1_input.pack()

string2_label = tk.Label(window, text="Ingrese otra cadena:")
string2_label.pack()
string2_input = tk.Entry(window)
string2_input.pack()

check_palindrome_button = tk.Button(window, text="Verificar Palíndromo", command=gui_check_palindrome)
check_palindrome_button.pack()

# --------------------------------------------------------------------------

# Adivinar número
number_guess_label = tk.Label(window, text="Intente averiguar el número que pensé del 1 al 10:")
number_guess_label.pack()
number_guess_input = tk.Entry(window)
number_guess_input.pack()
guess_number_button = tk.Button(window, text="Adivinar Número", command=gui_guess_number)
guess_number_button.pack()

# --------------------------------------------------------------------------

# Filtrar por edad
age_filter_label = tk.Label(window, text="Ingrese una edad para filtrar:")
age_filter_label.pack()
age_filter_input = tk.Entry(window)
age_filter_input.pack()

age_filter_button = tk.Button(window, text="Filtrar", command=gui_age_filter)
age_filter_button.pack()

window.mainloop()

# -----------------------------------------------------------------------

# Añade un carácter
def add_char(caracter):
    input_field.insert(tk.END, caracter)

# Limpiar la pantalla de la calculadora
def clear_screen():
    input_field.delete(0, tk.END)

# Calcular el resultado de la expresión
def calculate():
    expresion = input_field.get()
    try:
        resultado = eval(expresion)
        clear_screen()
        input_field.insert(tk.END, resultado)
    except:
        clear_screen()
        messagebox.showerror("Error", "Expresión inválida")

# Borrar un caracter
def delete_character():
    input_field.delete(len(input_field.get()) - 1)

# Borrar todos los caracteres
def clear_all():
    clear_screen()

# Escribe un punto decimal
def insert_decimal_point():
    input_field.insert(tk.END, '.')


# Crear la ventana principal
window = tk.Tk()
window.title("Calculadora")

# Crear la entrada de la calculadora
input_field = tk.Entry(window, width=30)
input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Crear los botones numéricos
numbers = [
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
for number, row, col in numbers:
    button = tk.Button(window, text=number, width=5, command=lambda numero=number: add_char(numero))
    button.grid(row=row, column=col, padx=5, pady=5)

# Crear los botones de operaciones
signs = ['+', '-', '*', '/']
for i, sign in enumerate(signs):
    button = tk.Button(window, text=sign, width=5, command=lambda operacion=sign: add_char(operacion))
    button.grid(row=i + 1, column=3, padx=5, pady=5)

# Crear el botón de igual
equal_button = tk.Button(window, text='=', width=5, command=calculate)
equal_button.grid(row=4, column=2, padx=5, pady=5)

# Crear el botón de limpiar
clear_button = tk.Button(window, text='C', width=5, command=clear_all)
clear_button.grid(row=4, column=1, padx=5, pady=5)

# Crear el botón de borrar
delete_button = tk.Button(window, text='⌫', width=5, command=delete_character)
delete_button.grid(row=0, column=3, padx=5, pady=5)

# Crear el botón de punto decimal
decimal_button = tk.Button(window, text='.', width=5, command=insert_decimal_point)
decimal_button.grid(row=4, column=0, padx=5, pady=5)

# Iniciar el bucle de eventos de la ventana
window.mainloop()