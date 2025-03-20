print(" ")
# Ejercicio 1
print("Ejercicio 1")
perro = {}
print(perro)

print(" ")
# Ejercicio 2
print("Ejercicio 2")
perro['nombre'] = 'Stuby'
perro['color'] = 'Blanco'
perro['raza'] = 'Husky'
perro['patas'] = 4
perro['edad'] = 3
print(perro)

print(" ")
# Ejercicio 3
print("Ejercicio 3")
estudiante = {
    'nombre': 'Manuel',
    'apellido': 'Rubalcava',
    'género': 'Masculino',
    'edad': 18,
    'estado_civil': 'Divorciado',
    'habilidades': ['Python', 'Macros'],
    'país': 'México',
    'ciudad': 'Aguascalientes',
    'dirección': {
        'calle': 'Paseo a San Gerardo',
        'código_postal': '20480'
    }
}
print(estudiante)

print(" ")
# Ejercicio 4
print("Ejercicio 4")
print(len(estudiante))

print(" ")
# Ejercicio 5
print("Ejercicio 5")
habilidades = estudiante['habilidades']
print(habilidades)
print(type(habilidades))

print(" ")
# Ejercicio 6
print("Ejercicio 6")
estudiante['habilidades'].append('HTML')
estudiante['habilidades'].append('CSS')
print(estudiante['habilidades'])

print(" ")
# Ejercicio 7
print("Ejercicio 7")
claves = estudiante.keys()
print(list(claves))

print(" ")
# Ejercicio 8
print("Ejercicio 8")
valores = estudiante.values()
print(list(valores))

print(" ")
# Ejercicio 9
print("Ejercicio 9")
elementos = estudiante.items()
print(list(elementos))
# El operador 'items' nos da pares clave-valor como si fuera una tupla

print(" ")
# Ejercicio 10
print("Ejercicio 10")
estudiante.pop('edad')
print(estudiante)
# Usamos 'pop' para eliminar la clave especifica

print(" ")
# Ejercicio 11
print("Ejercicio 11")
del perro