print(" ")
# Ejercicio 1
print("Ejercicio 1")
# Diccionario
persona = {
    'nombre': 'Asabeneh',
    'apellido': 'Yetayeh',
    'edad': 250,
    'pais': 'Finlandia',
    'casado': True,
    'habilidades': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'direccion': {
        'calle': 'Calle Espacial',
        'codigo_postal': '02210'
    }
}


#1
if 'habilidades' in persona:
    habilidades = persona['habilidades']
    ind_central = len(habilidades) // 2
    print(f"La habilidad central es: {habilidades[ind_central]}")

#2
if 'habilidades' in persona:
    tiene_python = 'Python' in persona['habilidades']
    print(f"La persona {'tiene' if tiene_python else 'no tiene'} la habiulidad Python")
#Utilizamos ciclos dentro de los ciclos para definir siu la intruccion es en plural o singuar, es este caso si tiene o no tiene

#3
if 'habilidades' in persona:
    habilidades = persona['habilidades']
    if set(['JavaScrip', 'React']) == set(habilidades):
        print("Es un desarrollador de front-end")
    elif set(['Node', 'Python', 'MongoDB']).issubset(habilidades):
        print("Es un desarrollador back-end")
    elif set(['React', 'Node', 'MongoDB']).issubset(habilidades):
        print("Es un desarrollador fullstack")
    else:
        print("No es desaarrollador conocido")
# Usamos "issubset" para evaluar si el conjunto está contenido en las habilidades.

#4
if persona.get('casado') and persona.get('pais') == 'Finlandia':
    print(f"{persona['nombre']}{persona['apellido']} vive en Finlandia y esta casado")
# Utilizamos "get" para acceder a una llave ("keys") del diccionario 

print("Revisado")