print(" ")
# Ejercicio 1
print("Ejercicio 1")
cali = float(input("Ingresa tu claificacion: "))

if 8 <= cali <= 10:
    mensage = "Bieeeeen"
elif 7 <= cali <= 8.9:
    mensage = "Bien"
elif 6 <= cali <= 6.9:
    mensage = "Reprobado pa"
elif 5 <= cali <= 5.9:
    mensage = "Que haces con tu miserable vida?"
elif 0 <= cali <= 4.9:
    mensage = "Haz considerado darte de baja?" 
else:
    mensage = "Introduce tu calificacion"
print(f"Considera esto amigo: {mensage}")

print(" ")
# Ejercicio 2
print("Ejercicio 2")
mes = input("Ingresa el mes: ").capitalize()

if mes in ['Septiembre', 'Ocubre', 'Noviembre']:
    estacion = 'Otoño'
elif mes in ['Diciembre', 'Enero', 'Febrero']:
    estacion = 'Invierno'
elif mes in ['Marzo', 'Abril', 'Mayo']:
    estacion = 'Primavera'
elif mes in ['Junio', 'Julio', 'Agosto']:
    estacion = 'Verano'
else:
    estacion = "Ingresa bien el mes"
print(f"La estacion actual es: {estacion}")

print(" ")
# Ejercicio 3
print("Ejercicio 3")
frutas = ['Platano', 'Naranja', 'Mango', 'Limon']
fruta = input("Ingresa una fruta: ").capitalize()

if fruta in frutas:
    print(f"Esta fruta ya esta en la lista {frutas}")
else:
    frutas.append(fruta)
    print("La lista actualizada es esta: ", frutas)

print("Revisado")