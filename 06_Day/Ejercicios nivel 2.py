print(" ")
# Ejercicio 1
print("Ejercicio 1")
miembros_de_mi_famila = ("Renata", "Emiliano", "Luis", "Rocio")
hermana, hermano, papá, mamá, = miembros_de_mi_famila
print("Mi papá se llama: ", papá)
print("Mi mamá se llama: ", mamá)
print("Mi hermano se llama: ", hermano)
print("Mi hermana se llama: ", hermana)

print(" ")
# Ejercicio 2
print("Ejercicio 2")
frutas = ("Manzana", "Platano", "Fresa")
verduras = ("Zanahoria", "Espinaca", "Pepino")
produ_animal = ("Leche", "Huevo", "Queso")
alimentos_tp = frutas + verduras + produ_animal
print(alimentos_tp)

print(" ")
# Ejercicio 3
print("Ejercicio 3")
alimentos_tp
alimentos_lt = list(alimentos_tp)
print(alimentos_lt)

print(" ")
# Ejercicio 4
print("Ejercicio 4")
longitud = len(alimentos_tp)
if longitud % 2 == 0:
    producto_central = alimentos_tp[longitud // 2 - 1: longitud // 2 + 1]
else:
    producto_central = alimentos_tp[longitud // 2: longitud // 2 + 1]

print("El producto central es: ", producto_central)

print(" ")
# Ejercicio 5
print("Ejercicio 5")
alimentos_lt
primeros_tres = alimentos_lt[:3]
ultimos_tres = alimentos_lt[-3:]
print("Los tres primeros alimentos son: ", primeros_tres)
print("Los tres ultimos alimentos son: ", ultimos_tres)

print(" ")
# Ejercicio 6
print("Ejercicio 6")
alimentos_tp
del alimentos_tp
try:
    print(alimentos_tp)
except NameError:
    print("La tupla 'alimentos_tp' fue eliminada")

print(" ")
# Ejercicio 7
print("Ejercicio 7")
paises_nordicos = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
if "Estonia" in paises_nordicos:
    print("Estonia es un pais nordico.")
else:
    print("Estonia no es un pais nordico.")

if "Iceland" in paises_nordicos:
    print("Iceland es un pais nordico.")
else:
    print("Iceland no es un pais nordico.")


print("Revisado")