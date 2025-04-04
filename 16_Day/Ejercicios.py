print(" ")
# Ejercicio 1
print("Ejercicio 1")
from datetime import datetime
now = datetime.now()
dia = now.day
mes = now.month
anio = now.year
hora = now.hour
minuto = now.minute
segundo = now.second
timestamp = now.timestamp()
print(f'Día: {dia}, Mes: {mes}, Año: {anio}, Hora: {hora}, Minuto: {minuto}, Segundo: {segundo}')
print(f'Timestamp: {timestamp}')

print(" ")
# Ejercicio 2
print("Ejercicio 2")
formato = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Fecha formateada:", formato)

print(" ")
# Ejercicio 3
print("Ejercicio 3")
fecha_str = "5 December, 2019"
fecha_obj = datetime.strptime(fecha_str, "%d %B, %Y")
print("Fecha convertida:", fecha_obj)

print(" ")
# Ejercicio 4
print("Ejercicio 4")
from datetime import date
hoy = date.today()
ano_nuevo = date(hoy.year + 1, 1, 1)  # Año Nuevo del siguiente año
dif = ano_nuevo - hoy
print(f'Tiempo restante para Año Nuevo: {dif.days} días')

print(" ")
# Ejercicio 5
print("Ejercicio 5")
inicio_epoch = datetime(1970, 1, 1)
dif_epoch = now - inicio_epoch
print(f'Tiempo desde el 1 de enero de 1970: {dif_epoch.days} días, {dif_epoch.seconds} segundos')

print(" ")
# Ejercicio 6
print("Ejercicio 6")
# 1
from datetime import datetime
fechas = [datetime(2024, 1, 1), datetime(2024, 2, 1), datetime(2024, 3, 1)]
for fecha in fechas:
    print(f"Registro de datos en: {fecha.strftime('%d/%m/%Y')}")

# 2
from datetime import datetime
def registrar_evento(accion):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] Acción registrada: {accion}")
registrar_evento("Usuario inició sesión")

# 3
from datetime import datetime
titulo = "Cómo mejorar en Python"
fecha_publicacion = datetime.now().strftime("%d de %B de %Y")
print(f"{titulo} - Publicado el {fecha_publicacion}")