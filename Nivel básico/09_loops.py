### Loops: bucles ###
## Funcionalidad o mecanismo para iterar o repetir una operación

# While: Mientras es True, itera el codigo
my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 1 # Es necesario que en algun momento la condición sea False
    ## Cuidado con hacer un Loops Infinito
else: # Opcional
    print("La codición es False por ser mayor a 10")
    print("Se detiene el Loops")

while my_condition < 20:
    my_condition += 2
    if my_condition == 16:
        print("Se detiene el loops")
        break
    print(my_condition)
    
### Bucle For
## Iteración de un listado(list, tuple, sets) de elementos
print("bucle for")
my_list = [25, 23, 34, 67, 50]

for element in my_list: # Itera el listado
    print(element)

my_tuple = (25, 1.77, "Jorge", "Gajar")

for element in my_tuple: # Itera los elementos
    print(element)

my_set = {"clave", 12, "Jojos"}

for element in my_set: # Itera los elementos desordenados
    print(element)
    
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 25, 1: "Python"}

for element in my_dict: # Itera las claves del dict
    print(element)
    
for element in my_dict.values(): # Itera los valores del dict
    print(element)
## Opcional: Break, Else or Continue (El continue detiene la ejecución y sigue con la siguiente iteración)