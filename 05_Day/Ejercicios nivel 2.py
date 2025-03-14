#Ejercicios nivel 2
print("Ejercicios nivel 2")

print(" ")
# Ejercicio 1
print("Ejercicio 1")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_ages = ages[0]
max_ages = ages[-1]
print(f"Edades ordenadas: {ages}")
print(f"Edad minima: {min_ages}, Edad maxima: {max_ages}")

ages.append(min_ages)
ages.append(max_ages)
print(f"Lista actualizada: {ages}")

ages.sort() #Ordenar despues de haber agregado 
media = len(ages) // 2
if len(ages) % 2 == 0:
    mediana = (ages[media - 1]+ ages[media]) / 2
else:
    mediana = ages[media]
print(f"Edad mediana: {mediana}")

promedio = sum(ages) / len(ages)
print(f"Edad promedio: {promedio}")

age_rango = max_ages - min_ages
print(f"Rango de edades: {age_rango}")

min_dife = abs(min_ages - promedio)
max_dife = abs(max_ages - promedio)
print(f"La diferencia minima con el promedio es: {min_dife}")
print(f"La diferencia maxima con el promedio es: {max_dife}")

print(" ")
# Ejercicio 2
print("Ejercicio 2")
variable = "En mi casita lo termino" #:)
print(variable)


