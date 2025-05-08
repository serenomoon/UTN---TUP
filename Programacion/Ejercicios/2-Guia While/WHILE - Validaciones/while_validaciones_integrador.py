# Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga 
# y validación de datos.
 
# Los datos requeridos son:
# - Apellido
# - Edad, entre 18 y 90 años inclusive.
# - Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
# - Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

# Una vez ingresados y validados los datos, mostrarlos por pantalla.

apellido = input("Ingrese apellido: ")
edad = int(input("Ingrese edad: "))
print("ESTADO CIVIL: ")
print("1 - Soltero/a")
print("2 - Casado/a")
print("3 - Divorciado/a")
print("4 - Viudo/a")
estado_civil = int(input("Ingrese estado civil correspondiente: "))
numero_legajo = int(input("Ingrese numero de legajo: "))

while edad < 18 or edad > 90:
    edad = int(input("Error!! La edad debe ser entre 18 y 90 años, Reingrese edad: "))
while estado_civil != 1 and estado_civil != 2 and estado_civil != 3 and estado_civil != 4:
    print("Error!! Reingrese estado civil: ")
    print("1 - Soltero/a")
    print("2 - Casado/a")
    print("3 - Divorciado/a")
    print("4 - Viudo/a")
    estado_civil = int(input("Ingrese estado civil correspondiente: "))
while numero_legajo <= 999 or numero_legajo > 9999:
    numero_legajo = int(input("Error!! Reingrese numero de legajo de 4 cifras y sin ceros a la izquierda: "))

print(f"Apellido: {apellido}")
print(f"Edad: {edad}")
if estado_civil == 1:
    estado_civil_str = "Soltero/a"
elif estado_civil == 2:
    estado_civil_str = "Casado/a"
elif estado_civil == 3:
    estado_civil_str = "Divorciado/a"
else:
    estado_civil_str = "Viudo/a"
print(f"Estado civil: {estado_civil_str}")
print(f"Numero de legajo: {numero_legajo}")