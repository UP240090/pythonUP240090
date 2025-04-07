print(" ")
# Ejercicio 1
print("Ejercicio 1")
import random
import string
def random_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))
print(random_user_id())

print(" ")
# Ejercicio 2
print("Ejercicio 2")
def user_id_gen_by_user():
    num_chars = int(input("Ingrese la cantidad de caracteres por ID: "))
    num_ids = int(input("Ingrese el número de IDs a generar: "))
    ids = [''.join(random.choices(string.ascii_letters + string.digits, k=num_chars)) for _ in range(num_ids)]
    return "\n".join(ids)
print(user_id_gen_by_user())

print(" ")
# Ejercicio 3
print("Ejercicio 3")
def rgb_color_gen():
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    return f"rgb({r},{g},{b})"
print(rgb_color_gen())

print("revisado")