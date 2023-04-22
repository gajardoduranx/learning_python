### Tipo de dato complejo: Tuples ###
## Definir tuple
my_tuple = tuple()
my_other_tuple = (34, 56, True)

my_tuple = (25, 1.77, "Jorge", "Gajar")
print(my_tuple)
print(type(my_tuple))

# Elementos
print(my_tuple[0]) # Primero
print(my_tuple[-1]) # Ultimo
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Jorge")) # Vuenta elementos repetidos
print(my_tuple.index("Gajar")) # Devuelve el indice del elemento

## Las tuplas son inmutables
# my_tuple[1] = 1.80 'tuple' object does not support item assigment

# Pero se pueden sumar
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6]) # Obtengo un pedazo de la tupla del index 3 al 6

# Para mutar los elementos de una tuple (imposible) sera necesario transformarlo en una lista
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[0] = 0
my_tuple.insert(1, "Rojo")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# borrar tupla
# del my_tuple
# print(my_tuple)