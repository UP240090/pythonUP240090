print(" ")
# Ejercicio 1
print("Ejercicio 1")
#1
sum_tot = 0
for numero in range(101):
    sum_tot += numero
print("La suma total de todos los numeros es: ", sum_tot)

#2
sum_par = 0
sum_imp = 0

for numero in range(101):
    if numero % 2 == 0:      # Usando el restante de la divicion entre dos, decide si es par o impar usando el "if", si lo es entonces que lo sume a "sum_par" si no a "sum_imp"
        sum_par += numero
    else:
        sum_imp += numero

print("La suma total de numeros pares es: ")
print("La suma total de numeros impares es: ")