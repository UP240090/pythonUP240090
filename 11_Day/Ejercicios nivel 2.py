print(" ") 
# Ejercicio 1
print("Ejercicio 1")
def pares_e_impares(rango):
    contador_pares = 0
    contador_impares = 0
    for i in range(rango+1):
        if i % 2 == 0:
            contador_pares += 1
        else:
            contador_impares += 1
    print(f"El número de impares es {contador_impares}.")
    print(f"El número de pares es {contador_pares}.")
pares_e_impares(100)

print(" ") 
# Ejercicio 2
print("Ejercicio 2")
def factorial(numero):
    resultado = 1
    for i in range(1, numero+1):
        resultado *= i
    return resultado
print(factorial(5))

print(" ") 
# Ejercicio 3
print("Ejercicio 3")
def esta_vacio(lista):
    if len(lista):
        print("No está vacío")
    else: 
        print("Está vacío")