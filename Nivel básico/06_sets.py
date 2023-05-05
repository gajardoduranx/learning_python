### Tipo de dato complex: Sets ###
# Definición
my_set = set()
my_other_set = {} # Inicialmente es un diccionario

print(type(my_set))
print(type(my_other_set))

my_other_set = {"Brain", "Moure", 35} # Ahora un set
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add(400)
print(my_other_set) # Un set es una estructura desordenada

my_other_set.add(400)
print(my_other_set) # Un set no admite elementos repetidos

## No tiene index, por lo cual no se puede acceder con set[9]

# Checkear elementos con in
print("Moure" in my_other_set) # True or False

my_other_set.remove("Moure") # Remueve un elemento del set
print(my_other_set)

my_other_set.clear() # Limpia todo el set
print(my_other_set)

my_set = {"Brais", "Moure", 35}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"JavaScript", "Python", "Swift"}
my_new_set = my_set.union(my_other_set) # Union de set
print(my_new_set)

print(my_new_set.difference(my_set)) # Analiza las diferencia entre dos sets