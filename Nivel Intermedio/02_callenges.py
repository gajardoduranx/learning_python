### Challenges ###
## 1.-Fizzbuzz
def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("FizzBuzz")
        elif index % 3 == 0:
            print("Fizz")
        elif index % 5 == 0:
            print("Buzz")
        else:
            print(index)

# fizzbuzz()

## 2.-Anacronico
## [::-1] inversión de dato
def anacronico(first_string, second_string):
    # return print(first_string == second_string[::-1])
    if first_string.lower() == second_string.lower():
        return False
    return sorted(first_string.lower()) == sorted(first_string.lower())

# print(anacronico("Roma", "Amor"))

# Fibonacci

def fibonacci():
    prev = 0
    next = 1
    for i in range(0, 50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib

# fibonacci()

# Números primos
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# print(is_prime(5))

def reverse(text):
    reversed_text = text[::-1]
    return reversed_text

print(reverse("Hola mundo"))