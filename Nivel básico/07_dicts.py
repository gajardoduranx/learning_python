## Dictionaries ##
# Definir
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

# Estructura Clave:Valor como un objeto o JSON
my_other_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 25, 1: "Python"}

my_dict = {
    "Nombre": "Jorge",
    "Apellido": "Moure",
    "Edad": 23,
    "Lenguajes": {"Python", "Swift", "Kotlin"}
}
print(my_dict)
print(len(my_dict))

#Acceder a los elementos con la Clave o Keys
print(my_dict["Lenguajes"])
my_dict["Nombre"] = "El jajas" # Actualizar valores
print(my_dict["Nombre"])

my_dict["Calle"] = "Calle MoureDev" # Agrega datos
print(my_dict)

del my_dict["Calle"] # Eliminación de claves y valores
print(my_dict)

# Al utilizar la palabra clave IN se debe buscar la clave o key
print("El jajas" in my_dict) # False 
print("Nombre" in my_dict) # True 

print(my_dict.items()) # Retorna una lista con todos los elementos (cada elemento como tupla)
print(my_dict.keys()) # Retorna una lista con las claves o keys
print(my_dict.values()) # Retoarno los datos o valores

my_new_dict = dict.fromkeys(("Nombre", 1)) # Crea un diccionario con las claves de los argumentos del mmetodo (se le puede pasar una lis, tuple. set, etc)
print(my_new_dict) # El segundo parametro de fromkeys sirve para insertar valores

#Al transformarlo a otro tipo de dato: este toma las claves o key solamente
print(list(my_dict))
print(tuple(my_dict))
print(set(my_dict))
