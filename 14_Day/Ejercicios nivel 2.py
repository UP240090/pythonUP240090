print(" ")
# Ejercicio 1
print("Ejercicio 1")
ciudades = ["Aguascalientes", "Guadalajara", "Sao Paulo", "San Gerardo"]
mayusculas = list(map(str.upper, ciudades))
print(mayusculas)

print(" ")
# Ejercicio 2
print("Ejercicio 2")
nums = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, nums))
print(cuadrados)

print(" ")
# Ejercicio 3
print("Ejercicio 3")
nombres = ["Manuel", "Renata", "Luis", "Rocio"]
nombres_mayus = list(map(str.upper, nombres))
print(nombres_mayus)

print(" ")
# Ejercicio 4
print("Ejercicio 4")
paises = ["Finland", "Sweden", "Iceland", "Mexico"]
tierra = list(filter(lambda x: 'land' in x.lower(), paises))
print(tierra)

print(" ")
# Ejercicio 5
print("Ejercicio 5")
seis_letras = list(filter(lambda x: len(x) == 6, paises))
print(seis_letras)

print(" ")
# Ejercicio 6
print("Ejercicio 6")
mas_seis = list(filter(lambda x: len(x) >= 6, paises))
print(mas_seis)

print(" ")
# Ejercicio 7
print("Ejercicio 7")
e_paises = list(filter(lambda x: x.startswith("E"), paises))
print(e_paises)

print(" ")
# Ejercicio 8
print("Ejercicio 8")
from functools import reduce
nums = [1, 2, 3, 4, 5]
resultado = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, map(lambda x: x**2, nums)))
print(resultado)

print(" ")
# Ejercicio 9
print("Ejercicio 9")
def get_string_lists(lst):
    return [x for x in lst if isinstance(x, str)]
print(get_string_lists([1, "Hola", 2.5, "Python"]))

print(" ")
# Ejercicio 10
print("Ejercicio 10")
suma_total = reduce(lambda x, y: x + y, nums)
print(suma_total)

print(" ")
# Ejercicio 11
print("Ejercicio 11")
paises = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
frase = reduce(lambda x, y: x + ", " + y, paises[:-1]) + f" y {paises[-1]} son países nórdicos."
print(frase)

print(" ")
# Ejercicio 12
print("Ejercicio 12")
def categorize_countries(lst, patron):
    return [p for p in lst if patron in p.lower()]
print(categorize_countries(paises, "land"))

print(" ")
# Ejercicio 13
print("Ejercicio 13")
def contar_por_letra(lst):
    conteo = {}
    for pais in lst:
        inicial = pais[0].upper()
        conteo[inicial] = conteo.get(inicial, 0) + 1
    return conteo
print(contar_por_letra(paises))

print(" ")
# Ejercicio 14
print("Ejercicio 14")
def get_first_ten_countries(lst):
    return lst[:10]
print(get_first_ten_countries(paises))

print(" ")
# Ejercicio 15
print("Ejercicio 15")
def get_last_ten_countries(lst):
    return lst[-10:]
print(get_last_ten_countries(paises))