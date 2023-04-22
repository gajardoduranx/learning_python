### Strings ###

my_string = "Mi string"
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon saldo de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un string \n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Jorge", "Gajardo", 25

print('Mi nombre es %s %s y mi edad es %d' %(name, surname, age)) # definir y pasarle de esta forma las variables y datos (%s para str y %d para int)
print('Mi nombre es {} {} y mi edad es {}'.format(name, surname, age)) # define los datos en orden
print(f'Mi nombre es {name} {surname} y mi edad es {age}') #f_string - inferencia de datos

# Desempaquetado de caracteres
languaje = "python"
a, b, c, d, e, f = languaje
print(a)
print(b)

# División de caracteres de un string
languaje_slice = languaje[1:4]
print(languaje_slice)
languaje_slice = languaje[-2]
print(languaje_slice)
languaje_slice = languaje[0:6:2]
print(languaje_slice)

#reverse de un string
reversed_languaje = languaje[::-1]
print(reversed_languaje)

# Metodos del sistema para String
print(languaje.capitalize()) # Primera letra en mayuscula
print(languaje.upper()) # Todo en mayuscula
print(languaje.count("t")) # Contador de caracteres
print(languaje.isnumeric()) # verifica si el strig es un numero o no
print("1".isnumeric()) # es true
print(languaje.lower()) # Todo en minuscula
print(languaje.upper().isupper()) # transformacion a mayuscula y verificacion isupper()
print(languaje.startswith("py")) # verifica si el string comienza con ciertos caracteres