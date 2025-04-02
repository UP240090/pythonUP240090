print(" ")
# Ejercicio 1
print("Ejercicio 1")
edad = int(input("Introduce tu edad: "))
if edad >= 18:
    print("Puedes conducir pa")
else:
    años_faltantes = 18 - edad
    print(f"Te faltan {años_faltantes} años para poder conducir")

print(" ")
# Ejercicio 2
print("Ejercicio 2")
mi_edad = 18
tu_edad = int(input("Ingresa tu edad: "))

if tu_edad > mi_edad:
    diferencia = tu_edad - mi_edad
    print(f"Eres {diferencia} {'año' if diferencia == 1 else 'años'} mayor que yo")
elif tu_edad < mi_edad:
    diferencia = mi_edad - tu_edad
    print(f"Soy {diferencia} {'año' if diferencia == 1 else 'años'} mayor que tu")
else:
    print("Tenemos la misma edad")

print(" ")
# Ejercicio 3
print("Ejercicio 3")
num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introcuce el segundo numero: "))

if num1 > num2:
    print(f"El primer numero {num1} es mas grande que el segundo {num2}")
elif num1 < num2:
    print(f"El segundo numero {num2} es mas grande que el primer numero {num1}")
else:
    print(f"Los dos numeros {num1} y {num2} son iguales")

print("Revisado")