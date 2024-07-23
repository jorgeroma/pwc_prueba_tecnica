import pandas as pd

data = {
    'Nombre':['Juan','María', 'Pedro','Ana', 'Luis'],
    'Edad':[25, 30, 35, 28, 32],
    'Ciudad':['Madrid','Barcelona','Sevilla','Valencia', 'Bilbao'],
    'Profesión': ['Ingeniero', 'Abogado', 'Médico', 'Arquitecto', 'Profesor'],
    'Salario': [50000, 60000, 70000, 55000, 65000]
}
data_df = pd.DataFrame(data)

# --------------------------------------------------------------------------

# calcula una operación
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

# Verifica si una cadena es un palíndromo
def check_palindrome(string_1, string_2):
	aux_string = ""
     
	for i in range(len(string_1) - 1, -1, -1):
		aux_string += string_1[i]
	
	return aux_string == string_2

# Adivina un número
def guess_number(operator_a, operator_b):
	return operator_a == operator_b

# Filtra por edad
def age_filter(age):
	return data_df[data_df['Edad'] > int(age)]