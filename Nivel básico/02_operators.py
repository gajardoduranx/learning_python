### Operadores Aritmeticos ###

print(3 + 4) # Suma
print(3 - 4) # Resta
print(3 * 4) # Multiplicación
print(3 / 4) # División - nos devuelve un dato float
print(3 % 4) # Modulo
print(3 // 4) # División aproximada hacia abajo - nos devuelve un entero (int)
print(3 ** 4) # Potencia

print("Hola" + "Jorge") # Concatenación con +
print("Hola" + str(5))
print("repetido" * (3 * 4)) # Repetición de str * int
print("repetido" * int(5.0)) 

### Operadores Comparativos ###

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

print("Hola" > "Bola") # Comparación segun ordenación alabetica por ASCII
print(len("Hola") > len("Bola")) # Comparación por numero de caracteres

### Operadores Lógicos ###

print(3 > 4 and "Hola" > "Pyrhon") # AND - false y false = false
print(3 > 4 or "Hola" > "Pyrhon") # OR - false o false = false
print(3 < 4 and "Hola" < "Pyrhon") # OR - true o true = true
print(3 < 4 or "Hola" > "Pyrhon") # OR - true o false = true

print(not(3 > 4)) # NOT - Negar la condición - not(false) = true