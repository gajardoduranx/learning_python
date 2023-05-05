### Higher Order Functions ###
## Trabajar con funciones dentro de funciones ##

from functools import reduce

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_number_and_add_value(num_one, num_two, fun):
    return fun(num_two + num_one)

print(sum_two_number_and_add_value(3, 4, sum_one))
print(sum_two_number_and_add_value(3, 4, sum_five))

### Closures ###

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

sumaa = sum_ten(5)
print(sumaa(1))
print(sum_ten(5)(1))

### Built-in Higher Order Functions ###

numbers = [2, 5, 10, 12, 34, 60]

## Map

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce

def sum_reducer(num_one, two_one):
    return num_one + two_one


print(reduce(sum_reducer, numbers))
print(reduce(lambda one, two: one + two, numbers))