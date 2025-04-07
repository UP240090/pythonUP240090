print(" ")
# Ejercicio 1
print("Ejercicio 1")
nums = [-4, -3, -2, -1, 0, 2, 4, 6]
neg_cero = [n for n in nums if n <= 0]
print(neg_cero)  

print(" ")
# Ejercicio 2
print("Ejercicio 2")
listas = [[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]
flat = [num for sublist in listas for num in sublist[0]]
print(flat)  

print(" ")
# Ejercicio 3
print("Ejercicio 3")
tuplas = [(x, 1, x, x**2, x**3, x**4, x**5) for x in range(11)]
print(tuplas)

print(" ")
# Ejercicio 4
print("Ejercicio 4")
paises = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flat_paises = [[p[0].upper(), p[0][:3].upper(), p[1].upper()] for sublist in paises for p in sublist]     # Extraemos valores los convertimos en mayúsculas y añadimos sus códigos
print(flat_paises) 

print(" ")
# Ejercicio 5
print("Ejercicio 5")
dic_paises = [{'pais': p[0].upper(), 'ciudad': p[1].upper()} for sublist in paises for p in sublist]
print(dic_paises)

print(" ")
# Ejercicio 6
print("Ejercicio 6")
nombres = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]   # Unimos los nombres con un espacio entre ellos
nombres_fmt = [' '.join(p) for sublist in nombres for p in sublist]
print(nombres_fmt)

print(" ")
# Ejercicio 7
print("Ejercicio 7")
pendiente = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x1 != x2 else "Indefinida"
interseccion = lambda x1, y1, m: y1 - m*x1
print(pendiente(2, 3, 5, 7)) 
print(interseccion(2, 3, 1.33))  

#  En otro dia ya habia usado la funciond de "lambda"

print("revisado")