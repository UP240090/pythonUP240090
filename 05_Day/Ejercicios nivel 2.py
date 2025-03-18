#Ejercicios nivel 2
print("Ejercicios nivel 2")

print(" ")
# Ejercicio 1
print("Ejercicio 1")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_ages = ages[0]
max_ages = ages[-1]
print(f"Edades ordenadas: {ages}")
print(f"Edad minima: {min_ages}, Edad maxima: {max_ages}")

ages.append(min_ages)
ages.append(max_ages)
print(f"Lista actualizada: {ages}")

ages.sort() #Ordenar despues de haber agregado 
media = len(ages) // 2
if len(ages) % 2 == 0:
    mediana = (ages[media - 1]+ ages[media]) / 2
else:
    mediana = ages[media]
print(f"Edad mediana: {mediana}")

promedio = sum(ages) / len(ages)
print(f"Edad promedio: {promedio}")

age_rango = max_ages - min_ages
print(f"Rango de edades: {age_rango}")

min_dife = abs(min_ages - promedio)
max_dife = abs(max_ages - promedio)
print(f"La diferencia minima con el promedio es: {min_dife}")
print(f"La diferencia maxima con el promedio es: {max_dife}")

print(" ")
# Ejercicio 2
print("Ejercicio 2")
paises = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
    'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain',
    'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan',
    'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria',
    'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde',
    'Central African Republic', 'Chad', 'Chile', 'China', 'Colombi', 'Comoros',
    'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba',
    'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic',
    'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea',
    'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The',
    'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea',
    'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India',
    'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan',
    'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait',
    'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya',
    'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi',
    'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania',
    'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco',
    'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand',
    'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama',
    'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar',
    'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia',
    'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia',
    'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore',
    'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain',
    'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria',
    'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago',
    'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine',
    'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan',
    'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']

pais_medio = len(paises)
if pais_medio % 2 == 1:
    mitad = [paises[pais_medio // 2]]
else:
    pais_medio = [paises[(pais_medio // 2) - 1]]
print("El pais del medio es: ",mitad)

print(" ")
# Ejercicio 3
print("Ejercicio 3")
analis_paises = len(paises)
medio = (analis_paises + 1) // 2 #Este conjunto "(analis_paises + 1) // 2" se usa para determinar donde se va a partir el codigo, tomando en cuenta que si la lista es impar el primer grupo tenga un oais mas.
primer_grupo = paises[:medio]
segundo_grupo = paises[medio:]
print("El 1er grupo es: ", primer_grupo)
print("El 2do grupo es: ",segundo_grupo)

print(" ")
# Ejercicio 4
print("Ejercicio 4")
paises_2 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
#Desempaquetar
primero, segundo, tercero, *paises_escandinavos = paises_2
print("Primer pais: ",primero)
print("Segundo pais: ",segundo)
print("Tercer pais: ",tercero)
print("Paises escandiavos: ",paises_escandinavos)
#"Escandinavos" se refiere al resto
