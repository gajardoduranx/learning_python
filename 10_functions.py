### Functions ###
### Encapsula una logica, resuelve un problema, evita errores, realiza una funcionalidad especificada
# Definición
def my_function ():
    print("Esto es una función")
# Llamada a la función
my_function ()

# Las funciones pueden recibir codigo y devolver codigo (input and output)
def sum_two_values (first_number, second_number):
    print(first_number + second_number)

# sum_two_values () TypeError ya que requiere 2 argumentos
sum_two_values (3, 5)
sum_two_values ("3", " cosas") # Concatena los string

## Function con Return
def sum_two_values_with_return (first_number, second_number):
    total = first_number + second_number
    return total 
# El return devuelve o retorna codigo, el cual se le asigna a una variable
my_result = sum_two_values_with_return(10, 5) # Con Return - Code
my_result = sum_two_values(10, 5) # Sin Return - None

print(my_result)

def print_name (name, surname):
    print(f"Nombre: {name} Apellido: {surname}")

print_name("Jorge", "Gajardo")
print_name(surname = "Moure", name = "Brais") # Se puede definir el orden

# Definición de valores por defecto - Default
def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Jorge", "Gajardo", "Gonku") # Con alias
print_name_with_default("Anahis", "Iglesias") # Sin alias - Default

# Parametros Infinitos - Parametros dinamicos
def print_texts(*texts): # Con el * se pueden pasar muchos parametros 
    print(type(texts)) # Lo interpreta como un tupla
    for elem in texts: # Se pueden iterar denntro
        print(elem.upper()) # Los transforma en mayuscula

print_texts("Hola", "Como", "Estas", "...")

