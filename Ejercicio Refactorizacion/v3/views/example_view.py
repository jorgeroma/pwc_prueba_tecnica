import tkinter as tk
from tkinter import messagebox
import random

from utils import utils

def example_view():
	
	# Función para calcular una operación
	def gui_compute_operation():
		sign = operation_input.get()
		number1 = float(num1_input.get())
		number2 = float(num2_input.get())

		result = utils.compute_operation(sign, number1, number2)
		if result is None:
			messagebox.showerror("Error", "Operación no válida")
			return

		result_label.config(text="El resultado es: " + str(result))


	# Función para verificar si una cadena es un palíndromo
	def gui_check_palindrome():
		string1 = string1_input.get()
		string2 = string2_input.get()

		if utils.check_palindrome(string1, string2):
			messagebox.showinfo("Resultado", "Las cadenas son palíndromos")
		else:
			messagebox.showinfo("Resultado", "Las cadenas no son palíndromos")

	# Función para adivinar un número
	def gui_guess_number():
		operator_a = random.randint(1, 10)
		correct_guess = utils.guess_number(operator_a, int(number_guess_input.get()))

		if correct_guess:
			messagebox.showinfo("Resultado", "¡Adivinaste! El número era: " + str(operator_a))
		else:
			messagebox.showinfo("Resultado", "No adivinaste. El número era: " + str(operator_a))

	# Función para filtrar por edad
	def gui_age_filter():
		age = int(age_filter_input.get())
		filter_data = utils.age_filter(age)
		messagebox.showinfo("Resultado", "Mayores de " + str(age) + " años:\n" + str(filter_data))
		
	# --------------------------------------------------------------------------

	# Crear la ventana principal
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
