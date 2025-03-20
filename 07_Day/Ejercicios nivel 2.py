print(" ")
# Ejercicio 1
print("Ejercicio 1")
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
ab = A.union(B) # "union" Une los elemntos sin duplicarlos
print(ab)

print(" ")
# Ejercicio 2
print("Ejercicio 2")
interseccion_ab = A.intersection(B)
print(interseccion_ab)

print(" ")
# Ejercicio 3
print("Ejercicio 3")
subconjunto = A.issubset(B)
print(subconjunto)

print(" ")
# Ejercicio 4
print("Ejercicio 4")
disjuntos = A.isdisjoint(B)
print(disjuntos)

print(" ")
# Ejercicio 5
print("Ejercicio 5")
A.update(B)
print(A)

B.update(A)
print(B)

print(" ")
# Ejercicio 6
print("Ejercicio 6")
dif_simetrica = A.symmetric_difference(B)
print(dif_simetrica)

print(" ")
# Ejercicio 7
print("Ejercicio 7")
del A
del B