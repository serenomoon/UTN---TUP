# 📌 Desafío: Encuesta Tecnológica en UTN Technologies
# UTN Technologies, una reconocida software factory, está en la búsqueda de ideas para su próximo desarrollo en Python, 
# con el objetivo de revolucionar el mercado.

# Las tecnologías en evaluación son:
#  🔹 Inteligencia Artificial (IA)
#  🔹 Realidad Virtual/Aumentada (RV/RA)
#  🔹 Internet de las Cosas (IOT)

# Para tomar una decisión informada, la empresa ha lanzado una encuesta entre sus empleados con el propósito de analizar ciertas métricas.
# 🔹 Recolección de Datos

# Cada empleado encuestado deberá proporcionar la siguiente información:
#  ✔️ Nombre
#  ✔️ Edad (debe ser 18 años o más)
#  ✔️ Género (Masculino, Femenino, Otro)
#  ✔️ Tecnología elegida (IA, RV/RA, IOT)

# El sistema deberá permitir ingresar los datos de 10 empleados mediante la terminal.
# 🔹 Análisis de Datos

# A partir de las respuestas, se deben calcular las siguientes métricas:
# 1️⃣ Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años (inclusive).

# 2️⃣ Porcentaje de empleados que NO votaron por IA, siempre y cuando:
# Su género no sea Femenino 
# Su edad está entre los 33 y 40 años.

# 3️⃣ Empleado masculino de mayor edad: Mostrar su nombre y la tecnología que votó.
contador = 0

masculinos_ia = 0
masculinos_iot = 0
no_ia = 0

edad_mayor_masculino = 0

while contador < 10:

    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    while edad < 18:
        edad = int(input("Reingrese su edad: "))
    print("Ingrese su genero: \n1 - Masculino\n2 - Femenino\n3 - Otro")
    genero = int(input("Genero: "))
    while genero != 1 and genero != 2 and genero != 3:
        genero = int(input("Reingrese el genero: "))
    print("Ingrese una tecnologia: \n1 - IA \nRV/RA \n3 - IOT")
    tecnologia = int(input("Tecnologia: "))
    while tecnologia != 1 and tecnologia != 2 and tecnologia != 3:
        tecnologia = int(input("Reingrese una tecnologia: "))

    if genero == 1:
        if edad >= 25 and edad <= 50:
            if tecnologia == 1:
                masculinos_ia += 1
            elif tecnologia == 3:
                masculinos_iot += 1
        if edad > edad_mayor_masculino:
                edad_mayor_masculino = edad
                nombre_mayor_masculino = nombre
                tecnologia_mayor_masculino = tecnologia
    if genero != 2:
        if edad >= 33 and edad <= 40:
            if tecnologia != 1:
                no_ia += 1 

    contador += 1

print(f"Empleados masculinos entre 25 y 50 años que votaron por IA: {masculinos_ia}")
print(f"Empleados masculinos entre 25 y 50 años que votaron por IOT: {masculinos_iot}")
print(f"Empleados masculinos/otros que no votaron por IA entre 33 y 40: {no_ia}")
if tecnologia_mayor_masculino == 1:
    tecnologia_texto = "IA"
elif tecnologia_mayor_masculino == 2:
    tecnologia_texto = "RV/RA"
else:
    tecnologia_texto = "IOT"
print(f"Empleado masculino de mayor edad:\nNombre: {nombre_mayor_masculino}\nEdad: {edad_mayor_masculino}\nTecnologia: {tecnologia_texto}")


