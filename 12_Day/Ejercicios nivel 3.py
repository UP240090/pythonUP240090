print(" ")
# Ejercicio 1
print("Ejercicio 1")
import random

def shuffle_list(lst):
    random.shuffle(lst)     # Esto modifica la lista original
    return lst

print(shuffle_list([1, 2, 3, 4, 5]))

print(" ")
# Ejercicio 2
print("Ejercicio 2")
def unique_random_numbers():
    return random.sample(range(10), 7)    # Selecciona 7 valores únicos de 0 a 9

print(unique_random_numbers())