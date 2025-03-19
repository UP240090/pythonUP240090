print(" ")
# Ejercicio 1
print("Ejercicio 1")
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
length = len(it_companies)
print(length)

print(" ")
# Ejercicio 2
print("Ejercicio 2")
it_companies.add('Twitter')
print(it_companies)

print(" ")
# Ejercicio 3
print("Ejercicio 3")
it_companies.update(['Snapchat', 'Tiktok', 'Spotify'])
print(it_companies)

print(" ")
# Ejercicio 4
print("Ejercicio 4")
it_companies.remove('Microsoft')
print(it_companies)

print(" ")
# Ejercicio 5
print("Ejercicio 5")
# "remove" genra un error si el elemento no esta en la lista
# "discard" no genera ningun error si el elemnto no esta en la lista
