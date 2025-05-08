# Ingresamos la edad (18 y 50) y el genero de 10 personas (Masculino, Femenino, No Binario).
# Necesitamos saber:
# a. Cuál es el porcentaje de personas de genero Masculino.
# b. Cuál es el porcentaje de personas de genero Femenino.
# c. Cuál es el porcentaje de personas de genero No Binario.
# d. Cuál es la edad de la persona de genero Femenino mas joven.

i = 0
contador_masculino = 0
contador_femenino = 0
contador_no_binario = 0
minima_edad_femenina = 0
bandera_femenina = False
CANTIDAD = 5

while i < CANTIDAD:
    nombre = input("Ingrese el nombre: ")
    genero = input("Ingrese el genero: ")
    while genero != "Masculino" or genero != "Femenino" or genero != "No Binario":
        genero = input("Error!! Reingrese el genero: ")
    edad = int(input("Ingrese la edad: "))

    while edad < 18 or edad > 50:
        edad = input("Error!! Reingrese la edad: ")


    match genero:
        case "Masculino":
            contador_masculino += 1
            acumulador_edad_masculina += edad
        case "Femenino":
            contador_femenino += 1
            bandera_femenina = True
            if edad < minima_edad_femenina or contador_femenino == 1:
                minima_edad_femenina = edad
                nombre_femenina_mas_joven = nombre
        case _: #case "No Binario"
            contador_no_binario += 1

    i += 1

porcentaje_masculino = contador_masculino * 100 / CANTIDAD
porcentaje_femenino = contador_femenino * 100 / CANTIDAD
# porcentaje_no_binario = contador_no_binario * 100 / CANTIDAD
porcentaje_no_binario = 100 - (porcentaje_masculino + porcentaje_femenino) # Otra forma de hacerlo

if contador_masculino > 0:
    promedio_edad_masculina = acumulador_edad_masculina / contador_masculino
    print(f"Promedio edad Masculina: {promedio_edad_masculina}")

print(f"El porcentaje Masculino es: {porcentaje_masculino}")
print(f"El porcentaje Femenino es: {porcentaje_femenino}")
print(f"El porcentaje No Binario es: {porcentaje_no_binario}")

if bandera_femenina == True:
    print(f"Nombre femenina mas joven: {nombre_femenina_mas_joven}")
    print(f"Edad femenina mas joven: {minima_edad_femenina}")
