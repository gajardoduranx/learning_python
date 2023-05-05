### Tipo de dato complejo: Lists ###
#Nos brinda operaciones propias de ua lista como estructura de dato, a diferencia de un array
# Definir una lista
my_list = list() 
my_other_list = [] 

print(len(my_list))
my_list = [35, 20, 30, 45, 30, 18]
print(my_list)
print(len(my_list))

my_other_list = [25, "coco", True]
print(my_other_list)
print(type(my_other_list)) # Tipo de dato - list

# Acceder a los datos de la lista
print(my_other_list[0]) # Primer elemento
print(my_other_list[1]) # Segundo elemento
print(my_other_list[2]) # Tercer elemento
print(my_other_list[-1]) # Ultimo elemento - tercero
print(my_other_list[-2]) # Penultimo elemento - segundo
print(my_other_list[-3]) # Antepenultimo elemento - primer
# print(my_other_list[-4])  IndexError

print(my_list.count(30)) # El count() - Retorna el numero de repeticiones de un valor

num, str, bool = my_other_list # Toma la totalidad de los valores de la lista en orden y se asignan a las variables
print(num, str, bool)

print(my_list + my_other_list) # Concatenación de listas

# Metodos de listas 

my_other_list.append("Mouredev") # Inserta un elemento al final de la lista
print(my_other_list)

my_other_list.insert(1, "uno") # Inserta un elemento en el indice indicado en el primer parametro
print(my_other_list)

my_other_list.remove("uno") # Remueve el primer elemento que coincida con lo indicado
print(my_other_list)

print(my_other_list.pop()) # Elimina el ultimo elemeto y nos lo devuelve, se puede guardar en una variable
print(my_other_list)
print(my_other_list.pop(2)) # Si se le pasa un numero, elimina el elemento conn el indice indicado
print(my_other_list)

my_list.sort() # Ordena la lista de menor a mayor
print(my_list)

print(my_list[1:3]) #Obtiene los elementos de la lista que se indican

my_list.clear() # Elimina todos los elementos de la lista
print(my_list)

my_new_list = my_other_list.copy() # Copia la lista y se le asigna a ua variable
print(my_new_list)

my_new_list.reverse() # Invierte el setido de la lista
print(my_new_list) 


