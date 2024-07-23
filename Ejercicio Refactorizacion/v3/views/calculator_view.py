import tkinter as tk
from tkinter import messagebox
from tkinter import *

def calculator_view():

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
 
	# --------------------------------------------------------------------------
	
	# Crear la ventana principal
	window = tk.Tk()
	window.title("Calculadora")

	# --------------------------------------------------------------------------

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

	# --------------------------------------------------------------------------
