### Error Types ###
## Tipos de errores que se pueden producir ##

## 1.- SyntaxError: Error de sintaxis
# print "Hola comunidad" # SyntaxError
print("Hola comunidad")

## 2.- NameError: Nombre de variable no definida
# print(name) # Error

## 3.- IndexError
my_list = ["Python", "JavaScript", "Dart"]
print(my_list[0]) # Primero
print(my_list[-1]) # Ultimo
# print(my_list[3]) # IndexError - No existe

## 4.- ModuleNotFoundError - Importar modulos que no existen
# import maths
import math

# 5.- AttributeError - Atributo no exisistente
# print(math.PI) # Error
print(math.pi)

# 6.- KeyError - No existe la clave en el diccionario
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35}
print(my_dict["Edad"])
# print(my_dict["Edads"]) # KeyError

# 7.- TypeError - Tipo de dato que no existe
# print(my_list["0"])
print(my_list[0])
print(my_list[False])

# 8.- ImportError - Importar algo que no existe
# from math import PI # Error
from math import pi
print(pi)

# 9.- ValueError
# my_int = int("10 años")
my_int = int("10")
print(type(my_int))

# 10.-ZeroDivisionError
# print(4/0) # Error
