print(" ")
# Ejercicio 1
print("Ejercicio 1")
for numero in range(11):
    print(numero)

numero = 0
while numero <= 10:
    print(numero)
    numero += 1

print(" ")
# Ejercicio 2
print("Ejercicio 2")
for numero in range(10, -1, -1):
    print(numero)
    # Usamos "(10, -1, -1)" para declarar el paso del decremento

numero = 0
while numero >= 0:
    print(numero)
    numero -= 1

print(" ")
# Ejercicio 3
print("Ejercicio 3")
for linea in range(1, 8):
    print('#' * linea)

print(" ")
# Ejercicio 4
print("Ejercicio 4")
for fila in range(8):     # Con este recorremos las 8 filas
    for columna in range(8):     # Con este recorremos las 8 columnas 
        print('#', end = ' ')
    print()

print(" ")
# Ejercicio 5
print("Ejercicio 5")
for numero in range(11):
    print(f'{numero} X {numero} = {numero * numero}')

print(" ")
# Ejercicio 6
print("Ejercicio 6")
tecnologias = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for tecnologia in tecnologias:
    print(tecnologia)

print(" ")
# Ejercicio 7
print("Ejercicio 7")
for numero in range(0, 101, 2):      # Usamos ese rango para iterar de dos en dos comenzando de cero
    print(numero)

print(" ")
# Ejercicio 8
print("Ejercicio 8")
for numero in range(1, 101, 2):      # Usamos ese rango para iterar de dos en dos comenzando de uno para obtener los impares
    print(numero) 

print("Revisado")