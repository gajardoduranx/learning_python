### List Comprehension ###

my_original_list =  [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_range = range(8)
print(list(my_range))

my_list = [i for i in my_original_list] # Iteración de lista original que crea otra lista basada en la original
print(my_list)
my_list = [i * 2 for i in range(8)] # Creación de lista modificada y basada en otra
print(my_list)
## Se le puede pasar una función también