# Como es de público conocimiento, la NASA reconoció que se han encontrado restos
# biológicos no humanos en otros planetas. Dada esta situación, y en su afán de
# blanquear tantos años de avistamientos desmentidos, nos piden que realicemos un
# programa que permita llevar un control de los mismos para mostrarlos a la sociedad.

# Por cada avistamiento se registra:
# ● Nombre del empleado que notificó el avistamiento
# ● Forma de la nave (Platillo, Esférica, Ovalada)
# ● Velocidad máxima de la nave (mayor a 100 km/h)
# ● Tipo de mensaje (Ninguno - Claro - Incomprensible)

# En esta opción el usuario podrá cargar avistamientos hasta que lo desee.

# Se desea saber:
# a. Velocidad promedio según la forma de la nave.
# b. Porcentaje de avistamientos con algún tipo de mensaje, Siempre y cuando la
# velocidad se encuentre entre los 200 km/h y los 500 km/h.
# c. Tipo de mensaje menos recibido.
# d. Nombre del empleado y forma de la nave del avistamiento con mensajes
# Incomprensibles, de las naves que resultaron ser más rápidas.
# e. Cantidad de avistamientos que superen los 250 Km/h, cuyo mensaje sea
# Claro o incomprensible y que sea de tipo Esférica.
# f. Si por lo menos algún empleado se llama “Mercedes”

seguir = "si"

contador_platillo = 0
contador_esferica = 0
contador_ovalada = 0
contador_ninguno = 0
contador_claro = 0
contador_incomprensible = 0
acumulador_km_platillo = 0
acumulador_km_esferica = 0
acumulador_km_ovalada = 0

contador_avistamiento_mensaje_km = 0

while seguir == "si":

    nombre_empletado = input("Ingrese nombre del empleado: ")
    forma_nave = input("Ingrese forma de la nave (Platillo - Esferica - Ovalada): ")

    while forma_nave != "Platillo" and forma_nave != "Esferica" and forma_nave != "Ovalada":
        forma_nave = input("Error!! Reingrese forma de la nave (Platillo - Esferica - Ovalada): ")
  
    velocidad_maxima = int(input("Ingrese velocidad de la nave: "))
    while velocidad_maxima <= 100:
        velocidad_maxima = int(input("Reingrese velocidad de la nave: "))

    tipo_mensaje = input("Ingrese tipo de mensaje (Ninguno - Claro - Incomprensible): ")
    while tipo_mensaje != "Ninguno" and tipo_mensaje != "Claro" and tipo_mensaje != "Incomprensible":
        tipo_mensaje = input("Error!! Reingrese tipo de mensaje (Ninguno - Claro - Incomprensible): ")

    seguir = input("Desea continuar? si/no: ")
    while seguir != "si" and seguir != "no":
        seguir = input("Reingrese: Desea continuar? si/no: ")

    #Procesos (se repiten)
    # a. Velocidad promedio según la forma de la nave.
    match forma_nave:
        case "Esferica":
            contador_esferica += 1
            acumulador_km_esferica += velocidad_maxima
        case "Ovalada":
            contador_ovalada += 1
            acumulador_km_ovalada += velocidad_maxima
        case "Platillo":
            contador_platillo += 1
            acumulador_km_platillo += velocidad_maxima
    
    # b. Porcentaje de avistamientos con algún tipo de mensaje, Siempre y cuando la
    # velocidad se encuentre entre los 200 km/h y los 500 km/h.
    if tipo_mensaje != "Ninguno" and (velocidad_maxima >= 200 and velocidad_maxima <= 500):
        contador_avistamiento_mensaje_km += 1

    # c. Tipo de mensaje menos recibido.
    match tipo_mensaje:
        case "Ninguno":
            contador_ninguno += 1
        case "Claro":
            contador_claro+= 1
        case "Incomprensible":
            contador_incomprensible += 1


#Procesos (no se repiten) y Salidas
# a. Velocidad promedio según la forma de la nave.
print("a. El promedio de velocidad para: \n")
if contador_esferica > 0:
    promedio_esferica = acumulador_km_esferica / contador_esferica
    print(f"\tEsferica: {promedio_esferica} km/h")
else:
    print(f"\tEsferica: no hubo registro")

if contador_ovalada > 0:
    promedio_ovalada = acumulador_km_ovalada / contador_ovalada
    print(f"\tOvalada: {promedio_ovalada} km/h")
else:
    print(f"\tOvalada: no hubo registro")

if contador_platillo > 0:
    promedio_platillo = acumulador_km_platillo / contador_platillo
    print(f"\tPlatillo: {promedio_platillo} km/h")
else:
    print(f"\tPlatillo: no hubo registro")

# b. Porcentaje de avistamientos con algún tipo de mensaje, Siempre y cuando la
# velocidad se encuentre entre los 200 km/h y los 500 km/h.
contador_general = contador_ovalada + contador_esferica + contador_platillo
porcentaje = (contador_avistamiento_mensaje_km * 100) / contador_general
print(f"b. El porcentaje de avistamientos que cumplen la condicion es: {porcentaje:.2f}%")

# c. Tipo de mensaje menos recibido.
if contador_ninguno < contador_claro and contador_ninguno < contador_incomprensible:
    print("El tipo de mensaje menos recibido es: Ninguno")
elif contador_claro < contador_incomprensible:
    print("El tipo de mensaje menos recibido es: Claro")
else:
    print("El tipo de mensaje menos recibido es: Incomprensible")