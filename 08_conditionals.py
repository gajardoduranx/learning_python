### Conditionals ###

my_condition = True

if my_condition:
    print("Condición del IF")


my_condition = 5 * 3

if my_condition == 8:
    print("Condición igual a 8")

if my_condition > 5 and my_condition < 10: #Si es True
    print("La condición es mayor a 5 y menor a 10")
elif my_condition == 1:
    print("Es igual a 1") # Comprobación adicional
else: # Si es False
    print("La condición es menor a 5 o mayor a 10")

print("Continuación")

my_string = ''

if my_string:
    print("Mi cadena de text no es vacia") # False

if my_string == "":
    print("String vacio")
