### Regular Expressions ###
## Formulas y codigo para realizar matches o emparejamientos ##
## Cada leguaje tiene su propia interpretacióm ##
import re 

my_string = "Esta es la lección número 7: Expresiones regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I)
print(match)
start, end =  match.span()
print(my_string[start:end])
print(re.match("Esta es la lección", my_other_string))
print(re.match("Expresiones regulares", my_string))