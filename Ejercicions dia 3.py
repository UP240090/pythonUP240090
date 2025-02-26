# Ejercicios del dia 3

print(" ")
# Ejercicio 1
print("Ejercicio 1")
edad = 20
estatura = 1.74
numcom = 4j
print (type(edad), edad)
print(type(estatura), estatura)
print(type(numcom), numcom)

print(" ")
# Ejercicio 2
print("Ejercicio 2")
base = float(input("Introduce la base del triangulo: "))
altura = float(input("Introduce la altura del triangulo: "))
area = ((base * altura)/2)
print ("El area del triangulo es: ", area)

print(" ")
# Ejercicio 3
print("Ejercicio 3")
lado_a = float(input("Introduce el lado a del triangulo: "))
lado_b = float(input("Introduce el lado b del triangulo: "))
lado_c = float(input("Introduce el lado c del triangulo: "))
perimetro = (lado_a + lado_b + lado_c)
print ("El perimetro del triangulo es de :", perimetro)

print(" ")
# Ejercicio 4
print("Ejercicio 4")
baser = float(input("Introduce la medida de la base del rectangulo: "))
alturar = float(input("Introduce la medida de la altura del rectangulo: "))
arearec = (baser*alturar)
perimetrorec = ((baser + alturar)*2)
print ("El area del rectangulo es:", arearec)
print ("El perimetro del rectangulo es:", perimetrorec)

print(" ")
# Ejercicio 5
print("Ejercicio 5")
radio = float(input("Introduce el radio del circulo: "))
pi = 3.14159
areacir = (pi * (radio ** 2))
perimetrocir = (2 * pi * radio)
print ("El area del circulo es de: ", areacir)
print ("El perimetro del circulo es de: ", perimetrocir)

print(" ")
# Ejercicio 6
print("Ejercicio 6")
x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente = (y2 - y1) / (x2 - x1)
print("Pendiente:", pendiente)
distancia_euclidiana = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Distancia euclidiana:", distancia_euclidiana)

print(" ")
# Ejercicio 7
print("Ejercicio 7")
x1, y1 = 2, 2
x2, y2 = 6, 10
m2 = (y2 - y1) / (x2 - x1)
print("Pendiente entre los puntos (2, 2) y (6, 10):", m2)

print(" ")
# Ejercicio 8
print("Ejercicio 8")
#Declarar los valores de x a probar
x_valores = [-3, -2, -1, 0, 1, 2, 3]
for x in x_valores:
    y = x**2 + 6*x + 9
    print(f"Para x = {x}, y = {y}")
#(for x in x_valores:) significa que para resolver y con los valores de x_valores
#Resuelva sustituyendo los valores que le diste obteniendo los valores de y 
