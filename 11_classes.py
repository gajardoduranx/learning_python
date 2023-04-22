### Classes ###
### Crea una instacia con sus caracteristicas y funcionalidades
# Definición
class EmptyPerson: # CamelCase
    pass # Evita la ejecución de las classes

print(EmptyPerson)
print(type(EmptyPerson()))

# Classe con constructor - el cual le a la posibiliad de recibir parametros
class Person:
    def __init__(self, name, surname, alias = "noneee"): # Constructor - self required
        # Definir propertys con self
        self.full_name = f"{name} {surname} {alias}" # New property utilizano los params
        self.__name = name # Property privada
        # self.surname = surname
    # Definir métodos o funciones
    
    def walk(self):
        print(f"{self.full_name} está caminando")

my_person = Person("Brasi", "Knekro") # Instancia de Person - 1era persona
print(my_person.full_name) # Utilización de propertys
my_person.walk() # llamada del method

my_other_person = Person("Jorge", "Gajardo", "Gobki") # 2da persona con alias
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Soy andrs de leon" # Las propiedades pueden ser mutadas
print(my_other_person.full_name)