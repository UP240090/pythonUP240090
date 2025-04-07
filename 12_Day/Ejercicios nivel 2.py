print(" ")
# Ejercicio 1
print("Ejercicio 1")
import random
def list_of_hexa_colors(n):
    hex_colors = ['#' + ''.join(random.choices('0123456789abcdef', k=6)) for _ in range(n)]    #"random.choices('0123456789abcdef', k=6" selecciona 6 caracteres hexadecimales
    return hex_colors
print(list_of_hexa_colors(3)) 

print(" ")
# Ejercicio 2
print("Ejercicio 2")
def list_of_rgb_colors(n):
    rgb_colors = [f"rgb({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)})" for _ in range(n)]
    return rgb_colors

print(list_of_rgb_colors(3))
print(" ")
# Ejercicio 3
print("Ejercicio 3")
def generate_colors(tipo, cantidad):
    if tipo == 'hexa':
        return list_of_hexa_colors(cantidad)
    elif tipo == 'rgb':
        return list_of_rgb_colors(cantidad)
    else:
        return "Tipo no válido. Usa 'hexa' o 'rgb'."

print(generate_colors('hexa', 3)) 
print(generate_colors('rgb', 3))  

print("revisado")