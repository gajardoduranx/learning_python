### File Handling ###

## Trabajar con ficheros como:
# .txt file
import os

txt_file = open("./Nivel Intermedio/my_file.txt", "w+") # Primer param: Ruta, segundo param: Mode (w, w+, r, etc)
# Creación de fichero o archivo
txt_file.write("Mi nombre es Jorge\nMi apellido es Gajardo\nTengo 25 años\nMe gusta Python")
## r+ - Leer y escribir
# print(txt_file.read()) Leer
# print(txt_file.read(10))
print(txt_file.readline()) # Lectura linea a linea
print(txt_file.readline())
# print(txt_file.readlines()) # Devuelve una lista con todas las lineas como elementos
for line in txt_file.readlines(): # Itera la lista anteriorr
    print(line)
    

txt_file.write("\nY mi lenguaje favorito es Python") # Escritura
print(txt_file.readline())

txt_file.close()

os.remove("./Nivel Intermedio/my_file.txt")

# .json file - Archivo tipo JSON
# Creación de un archivo .json
import json

json_file = open("./Nivel Intermedio/my_file.json", "w+")
json_test = {
    "name": "Brais",
    "surname": "Moure",
    "Age": 25,
    "languajes": ["Python", "JavaScript", "Java"],
    "website": "https://moure.dev"
    }

# param1: objeto(dict), File, indentación
json.dump(json_test, json_file, indent = 4)

json_file.close()

# Leer Archivo json
with open("./Nivel Intermedio/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# Recuperar y parsear archivo json a dict
json_dict = json.load(open("./Nivel Intermedio/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv file
import csv

csv_file = open("./Nivel Intermedio/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "languaje", "website"])
csv_writer.writerow(["Jorge", "Gajardo", "25", "Python", "https://mouredev.dev"])
csv_writer.writerow(["roswell", "", 2, True])

csv_file.close()

with open("./Nivel Intermedio/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)
# .xlsx file
# import xlrd # Debe instalarse
# .xml file
import xml