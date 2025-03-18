print(" ")
# Ejercicio 1
print("Ejercicio 1")
# Lista vacía
lista_vacia = []

print(" ")
# Ejercicio 2
print("Ejercicio 2")
#Lista con más de 5 elementos
mi_lista = [1, 2, 3, 4, 5, 6, 7]

print(" ")
# Ejercicio 3
print("Ejercicio 3")
longitud_lista = len(mi_lista)
print("La longitud de la lista es:", longitud_lista)

print(" ")
# Ejercicio 4
print("Ejercicio 4")
primer_elemento = mi_lista[0]
elemento_medio = mi_lista[len(mi_lista) // 2]
ultimo_elemento = mi_lista[-1]

print("Primer elemento:", primer_elemento)
print("Elemento del medio:", elemento_medio)
print("Último elemento:", ultimo_elemento)

print(" ")
# Ejercicio 5
print("Ejercicio 5")
# Lista con datos personales
datos_personales = ["Manuel", 18, 1.63, "Viudo", "Aguascalientes, México"]
print("Datos personales:", datos_personales)

print(" ")
# Ejercicio 6
print("Ejercicio 6")
empresas_tecnologia = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

print(" ")
# Ejercicio 7
print("Ejercicio 7")
print(empresas_tecnologia)

print(" ")
# Ejercicio 8
print("Ejercicio 8")
numero_empresas = len(empresas_tecnologia)
print(numero_empresas)

print(" ")
# Ejercicio 9
print("Ejercicio 9")
primera_empresa = empresas_tecnologia[0]
empresa_del_medio = empresas_tecnologia[len(empresas_tecnologia) // 2]
ultima_empresa = empresas_tecnologia[-1]
print(primera_empresa)
print(empresa_del_medio)
print(ultima_empresa)

print(" ")
# Ejercicio 10
print("Ejercicio 10")
empresas_tecnologia[3] = "Tesla"
print(empresas_tecnologia)

print(" ")
# Ejercicio 11
print("Ejercicio 11")
empresas_tecnologia.append("Spotify")
print(empresas_tecnologia)

print(" ")
# Ejercicio 12
print("Ejercicio 12")
empresas_tecnologia.insert(len(empresas_tecnologia) // 2, "Salesforce")
print(empresas_tecnologia)

print(" ")
# Ejercicio 13
print("Ejercicio 13")
empresas_tecnologia[1] = empresas_tecnologia[1].upper()  # Cambiando "Google" a mayúsculas
print(empresas_tecnologia)

print(" ")
# Ejercicio 14
print("Ejercicio 14")
empresas_unidas = "#;  ".join(empresas_tecnologia)
print(empresas_unidas)

print(" ")
# Ejercicio 15
print("Ejercicio 15")
existe_empresa = "Apple" in empresas_tecnologia
print(existe_empresa)

print(" ")
# Ejercicio 16
print("Ejercicio 16")
empresas_tecnologia.sort()
print("Lista ordenada:", empresas_tecnologia)

print(" ")
# Ejercicio 17
print("Ejercicio 17")
empresas_tecnologia.reverse()
print("Lista en orden descendente:", empresas_tecnologia)

print(" ")
# Ejercicio 18
print("Ejercicio 18")
primeras_tres = empresas_tecnologia[:3]
print("Primeras tres empresas: ", primeras_tres)

print(" ")
# Ejercicio 19
print("Ejercicio 19")
ultimas_tres = empresas_tecnologia[-3:]
print("Las ultimas tres empresas son: ",ultimas_tres)

print(" ")
# Ejercicio 20
print("Ejercicio 20")
indice_medio = len(empresas_tecnologia) // 2
empresas_medio = empresas_tecnologia[indice_medio - 1:indice_medio + 1] if len(empresas_tecnologia) % 2 == 0 else [empresas_tecnologia[indice_medio]]
print("Empresa del medio:", empresas_medio)

print(" ")
# Ejercicio 21
print("Ejercicio 21")
del empresas_tecnologia[0]
print("Lista despues de eliminar la primera empresa: ",empresas_tecnologia)

print(" ")
# Ejercicio 22
print("Ejercicio 22")
indice_medio = len(empresas_tecnologia) // 2
if len(empresas_tecnologia) % 2 != 0:  #Longitud impar
    del empresas_tecnologia[indice_medio]
else:  #Longitud par
    del empresas_tecnologia[indice_medio - 1:indice_medio + 1]
print("Lista después de eliminar las empresas del medio:", empresas_tecnologia)

print(" ")
# Ejercicio 23
print("Ejercicio 23")
empresas_tecnologia.pop()
print("La lista desues de eliminar la ultima empresa: ",empresas_tecnologia)

print(" ")
# Ejercicio 24
print("Ejercicio 24")
empresas_tecnologia.clear()
print("Lista despues de eliminar todas las empresas: ",empresas_tecnologia)

print(" ")
# Ejercicio 25
print("Ejercicio 25")
del empresas_tecnologia

print(" ")
# Ejercicio 26
print("Ejercicio 26")
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']  #Tecnologías frontend
back_end = ['Node', 'Express', 'MongoDB']  #Tecnologías backend

pila_completa = front_end + back_end  #Combinando las listas
print("Lista combinada:", pila_completa) #Usando el "+" combina las dos listas

print(" ")
# Ejercicio 27
print("Ejercicio 27")
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
pila_completa = front_end + back_end
indice_redux = pila_completa.index('Redux') + 1
pila_completa.insert(indice_redux, 'Python')
pila_completa.insert(indice_redux + 1,'SQL')
print(pila_completa)
#REVISADO
print("Revisado")