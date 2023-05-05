### Exceptions Handling ###
## Manejo de errores
# Try - Run this code
# Catch - Execute this code when there is an exception (May or may not have a condition)
# Else - No exceptions? Run this code
# Finally - Always run this code

number_one, number_two = 5, 1
number_two = "1"

# Try - Except
try:
    print(number_one + number_two)
except: # Cuando hay un error 
    print("Se ha producido un error")

# Try - Except - Else - Finally

try:
    print(number_one + number_two)
except: 
    print("Se ha producido un error")
# Opcional: else and finally
else: # Se ejecuta cuando no hay error 
    print("La ejecución continúa correctamente")
finally: # Se ejecuta si o si
    print("La ejecución continua con finally")

## Excepciones por tipo - ValueError, TypeError, etc
try:
    print(number_one + number_two)
except ValueError: 
    print("Se ha producido un ValueError")
except TypeError: 
    print("Se ha producido un TypeError")

## Captura de la información de la excepción - error
try:
    print(number_one + number_two)
except ValueError as error: 
    print(error)
except Exception as error: # General
    print(error)