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

print(" ")
# Ejercicio 9
print("Ejercicio 9")
#Usamos la funcion len() para contar el numero de caracteres en la cadena de las palabras
len_python = len("python")
len_dragon = len("dragon")
#Declarar la comparaciopn falsa
print("La longitud de 'Python' es igual que la longitud de 'dragon': ", len_python == len_dragon)

print(" ")
# Ejercicio 10
print("Ejercicio 10")
in_python = "on" in "python"
in_dragon = "on" in "dragon"
#Operar viendo si la palabra "on" se encuebtra en ambas palabras
print("'on' esta en 'python' y 'dragon': ",in_python and in_dragon)

print(" ")
# Ejercicio 11
print("Ejercicio 11")
oracion = "I hope this course is not full of jargon"
contiene_jargon = "jargon" in oracion
#El operador en la instriuccion que es "in" dice si esta o no esta lo que busca
print("Esta oracion contiene 'jargon':",contiene_jargon)

print(" ")
# Ejercicio 12
print("Ejercicio 12")
in_python = "on" not in "python"
in_dragon = "on" not in "dragon"
#Operar viendo si la palabra "on" se encuebtra en ambas palabras
print("No hay 'on' en 'python' y 'dragon': ",in_python and in_dragon)

print(" ")
# Ejercicio 13
print("Ejercicio 13")
longitud_python = len("python")
longitud_float = float(longitud_python)
longitud_str = str(longitud_float)
print("Longitud de 'python':", longitud_python)
print("Longitud en 'float':", longitud_float)
print("Longitud en 'str':", longitud_str)

print(" ")
# Ejercicio 14
print("Ejercicio 14")
numero = int(input("Ingresa un numero entero, si no no funciona :(  "))
es_par = numero % 2 == 0
#El modulo del "%" te da el residuo de la division
print(f"El numero {numero} es par: ", es_par)

print(" ")
# Ejercicio 15
print("Ejercicio 15")
division_entera = 7 // 3
valor_convertido = int(2.7)
#El operador "//" nos da como resultado el numero entero de la division
print("La division entera de 7 entre 3 es igual al valor convertido de 2.7: ", division_entera == valor_convertido)

print(" ")
# Ejercicio 16
print("Ejercicio 16")
tipo_cadena = type("10")
tipo_entero = type(10)
print("El tipo de '10' es igual que el tipo de 10: ", tipo_cadena == tipo_entero)

print(" ")
# Ejercicio 17
print("Ejercicio 17")
try:
    valor = int('9.8')
except ValueError:
    valor = None
print("int('9.8') es igual a 10:", valor == 10)
#Estos dos operadores se usan para determinar excepciones, es como el "if" y "else"

print(" ")
# Ejercicio 18
print("Ejercicio 18")
horas = float(input("Ingresa las horas que chambeaste: "))
tph = float(input("Cuanto ganas por hora: "))
pago_semanal = horas * tph
print("Tu pago semanal es: ","$",pago_semanal, "pechereques")
