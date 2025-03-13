#Ejercicios del dia 4

print(" ")
# Ejercicio 1
print("Ejercicio 1")
print('Thirty', 'days', 'of', 'Python')

print(" ")
# Ejercicio 2
print("Ejercicio 2")
print('Coding', 'for', 'all')

print(" ")
# Ejercicio 3
print("Ejercicio 3")
company = "Coding for all"
print("Esta cadena se usara para mas cosas ","!",company,"!")

print(" ")
# Ejercicio 4
print("Ejercicio 4")
print(company)

print(" ")
# Ejercicio 5
print("Ejercicio 5")
longitud = len(company)
print("La longitud de la cadena es de: ", longitud)

print(" ")
# Ejercicio 6
print("Ejercicio 6")
cad_may = company.upper()
print("En mayusaculas seria: ", cad_may)

print(" ")
# Ejercicio 7
print("Ejercicio 7")
cad_min = company.lower()
print("En minusculas seria: ", cad_min)

print(" ")
# Ejercicio 8
print("Ejercicio 8")
cad_cap = company.capitalize()
print("En capitales seria: ", cad_cap)
cad_tit = company.title()
print("En titulo seria: ", cad_tit)
cad_swa = company.swapcase()
print("En swapcase seria: ", cad_swa)
#Esa funcion invierte las mayusculas y minusculas

print(" ")
# Ejercicio 9
print("Ejercicio 9")
primera_palabra = company.split()[0]
print(primera_palabra)

print(" ")
# Ejercicio 10
print("Ejercicio 10")
#Usar la funcion "Index" para obtener la posicion  al preguntar
print("La posision de la palabra Conding en la oracion es: ", company.index("Coding"))

print(" ")
# Ejercicio 11
print("Ejercicio 11")
nueva_cadena = company.replace('Coding', 'Python')
print(nueva_cadena)

print(" ")
# Ejercicio 12
print("Ejercicio 12")
frase = "Python for everyone"
frase_modi = frase.replace("Everyone", "All")
print(frase_modi)

print(" ")
# Ejercicio 13
print("Ejercicio 13")
palabras = company.split()
print(palabras)

print(" ")
# Ejercicio 14
print("Ejercicio 14")
empresas_tec = "Facebook,  Google, Microsoft, Apple, IBM, Oracle, Amazon"
lista_de_empresas = empresas_tec.split(', ')
print(lista_de_empresas)

print(" ")
# Ejercicio 15
print("Ejercicio 15")
primer_caracter = company[0]
print(primer_caracter)

print(" ")
# Ejercicio 16
print("Ejercicio 16")
ultimo_caracter = company[-1]
print(ultimo_caracter)

print(" ")
# Ejercicio 17
print("Ejercicio 17")
caracter_en_11 = company[11]
print(caracter_en_11)

print(" ")
# Ejercicio 18
print("Ejercicio 18")
acronimo = ''.join([palabra[0] for palabra in frase.split()]).upper()
print(acronimo)

print(" ")
# Ejercicio 19
print("Ejercicio 19")
frase = "Coding for all"
acronimo = ''.join([palabra[0] for palabra in frase.split()]).upper()
print(acronimo)  

print(" ")
# Ejercicio 20
print("Ejercicio 20")
indice_c = company.index('C')  #Busca el índice de la primera aparición de 'C'
print(indice_c)  

print(" ")
# Ejercicio 21
print("Ejercicio 21")
indice_f = company.index('f')
print(indice_f)

print(" ")
# Ejercicio 22
print("Ejercicio 22")
frase2 = "Coding For All People"
ultimo_indice_l = frase2.rfind('l') 
print(ultimo_indice_l)  

print(" ")
# Ejercicio 23
print("Ejercicio 23")
frase3 = "You cannot end a sentence with because because because is a conjunction"
primer_indice_because = frase3.find('because')
print(primer_indice_because)  

print(" ")
# Ejercicio 24
print("Ejercicio 24")
ultimo_indice_because = frase.rfind('because')
print(ultimo_indice_because)

print(" ")
# Ejercicio 25
print("Ejercicio 25")
frase5 = "You cannot end a sentence with because because because is a conjunction"
first_occurrence = frase5.find("because")
print("La posición de la primera ocurrencia de 'because' es:", first_occurrence)

print(" ")
# Ejercicio 26
print("Ejercicio 26")
frase5 = "You cannot end a sentence with because because because is a conjunction"
extracted_phrase = frase5[31:50]
print("La frase extraída es:", extracted_phrase)

print(" ")
# Ejercicio 27
print("Ejercicio 27")
frase5 = "You cannot end a sentence with because because because is a conjunction"
modified_sentence = frase5.replace("because because because", "")
print("La oración modificada es:", modified_sentence.strip())

print(" ")
# Ejercicio 28
print("Ejercicio 28")
empieza_con_coding = company.startswith('Coding')
print(f'¿Empieza con "Coding"? {empieza_con_coding}')

print(" ")
# Ejercicio 29
print("Ejercicio 29")
termina_con_coding = company.endswith('coding')
print(f'¿Termina con "coding"? {termina_con_coding}')

print(" ")
# Ejercicio 30
print("Ejercicio 30")
cadena_con_espacios = "   Coding For All      "
cadena_sin_espacios = cadena_con_espacios.strip()
print(f'Antes: "{cadena_con_espacios}"')
print(f'Después: "{cadena_sin_espacios}"')

print(" ")
# Ejercicio 31
print("Ejercicio 31")
variable1 = "30DaysOfPython"
variable2 = "thirty_days_of_python"
es_identificador1 = variable1.isidentifier()
es_identificador2 = variable2.isidentifier()
print(f'¿"{variable1}" es un identificador válido? {es_identificador1}')
print(f'¿"{variable2}" es un identificador válido? {es_identificador2}')

print(" ")
# Ejercicio 32
print("Ejercicio 32")
librerias_python = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
resultado = ' # '.join(librerias_python)
print(resultado)

print(" ")
# Ejercicio 33
print("Ejercicio 33")
#se usa de \n para separar oraciones
print("Estoy disfrutando este desafío.\nMe pregunto qué sigue.")

print(" ")
# Ejercicio 34
print("Ejercicio 34")
print("Nombre\tEdad\tPaís\tCiudad")
print("Asabeneh\t250\tFinlandia\tHelsinki")

print(" ")
# Ejercicio 35
print("Ejercicio 35")
radio = 10
area = 3.14 * radio ** 2
print(f'El área de un círculo con radio {radio} es {area:.2f} metros cuadrados.')

print(" ")
# Ejercicio 36
print("Ejercicio 36")
a, b = 8, 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

#REVISADO
print("Revisado")