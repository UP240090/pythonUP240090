print(" ")
# Ejercicio 1
print("Ejercicio 1")
def sum_dos_num(a, b):
    return a + b
print(sum_dos_num(3, 5))

print(" ")
# Ejercicio 2
print("Ejercicio 2")
def area_cir(r):
    pi = 3.141592
    return pi * r * r
print(area_cir(10))

print(" ")
# Ejercicio 3
print("Ejercicio 3")
def suma_todos(*nums):
    if all(isinstance(n, (int, float)) for n in nums):
        return sum(nums)
    return "Solo numneros"
print(suma_todos(3, 2, 5))

print(" ")
# Ejercicio 4
print("Ejercicio 4")
def c_a_f(c):
    return(c * 9/5) + 32
print(c_a_f(30))

print(" ")
# Ejercicio 5
print("Ejercicio 5")
def estacion(mes):
    i = {
        "Dic": "Invierno", "Ene": "Invierno", "Feb": "Invierno",
        "Mar": "Primavera", "Abr": "Primavera", "May": "Primavera",
        "Jun": "Verano", "Jul": "Verano", "Ago": "Verano",
        "Sep": "Otoño", "Oct": "Otoño", "Nov": "Otoño"
    }
    return i.get(mes, "Mes no válido")

print(estacion("Abr"))

print(" ")
# Ejercicio 6
print("Ejercicio 6")
def pendiente(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1) if x1 != x2 else "Indefinida"
print(pendiente(1, 2, 3, 5))

print(" ")
# Ejercicio 7
print("Ejercicio 7")
import math
def ec_cuadr(a, b, c):
    d = b**2 - 4*a*c
    if d < 0: return "No tienr soluciones reales"
    if d == 0: return -b / (2*a)
    return (-b + math.sqrt(d)) / (2*a), (-b - math.sqrt(d)) / (2*a)
print(ec_cuadr(1, -3, 2))

print(" ")
# Ejercicio 8
print("Ejercicio 8")
def imprimir(lst):
    for i in lst:
        print(i)
imprimir(["Hola", "Python", "Muindo"])
    
print(" ")
# Ejercicio 9
print("Ejercicio 9")
def invertir(lst):
    return lst[::-1]
print(invertir([1, 2, 3, 4, 5])) 

print(" ")
# Ejercicio 10
print("Ejercicio 10")
def capitalizar(lst):
    return[i.capitalize() for i in lst]
print(capitalizar(["hola", "mundo", "python"]))

print(" ")
# Ejercicio 11
print("Ejercicio 11")
def agregar(lst, elem):
    lst.append(elem)
    return lst

print(agregar(['Papa', 'Tomate'], 'Carne'))

print(" ")
# Ejercicio 12
print("Ejercicio 12")
def eliminar(lst, elem):
    if elem in lst:
        lst.remove(elem)
    return lst
print(eliminar(['Papa', 'Tomate'], 'Tomate'))

print(" ")
# Ejercicio 13
print("Ejercicio 13")
def suma_rango(n):
    return sum(range(n + 1))
print(suma_rango(5))

print(" ")
# Ejercicio 14
print("Ejercicio 14")
def sum_impar(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)
print(sum_impar(5))

print(" ")
# Ejercicio 15
print("Ejercicio 15")
def sum_par(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)
print(sum_par(5))