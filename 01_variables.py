### variables ###

# Defininiendo una variable con snake_case (convención)
first_variable = "Un string"
#Cocatnación con un f_string
string_concatenado = f"Esto es {first_variable}"
# Concatenación de variables en un print
print(string_concatenado, first_variable)
print('Primer Variable:', first_variable)
# Operadores de pertenencia (in / not in)
print('es' in string_concatenado) # True
print("jorge" not in first_variable) # False

# Variables en 1 sola linea
name, surname, alias, age = "Jorge", "Gajar", "gon", 25
print("Me llamo:", name, surname, "Mi alias:", alias, "Edad:", age)

# Transformación a string con str()
entero = 5
print(entero, type(entero)) # Variable tipo Int
string = str(entero) # Transformación
print(string, type(string)) # Variable tipo Str

# Función del sistema - len()
print(len(string_concatenado)) # - Nos devuelve el numero de caracteres - length

# Función del sistema - input() - detienela ejecución de la consola para responder
first_name = input("what's your name?")
edad = input("old year?")

print(first_name)
print(edad)



