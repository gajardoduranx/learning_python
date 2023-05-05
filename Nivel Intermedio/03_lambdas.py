### Lambdas ###
## Se entiende como una función que recibe parametros y realiza una función. 
# Esta función lambda no tiene nombre, es mas simplificada y se le pasa a una variable

# suma = lambda num_one, num_two: num_one + num_two

# print(suma(3, 5))

def burbuja(lista):
    for i in range(0, len(lista) - 1):
        print("foruno", i)
        for j in range(0, len(lista)-i-1):
            print("fordos", j)
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
print(burbuja([3, 6, 1, 8]))
