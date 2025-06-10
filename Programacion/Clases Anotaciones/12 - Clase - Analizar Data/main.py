from datos_personas_con_puntos import datos

# Iteramos entre nombres con un for each    
# En este caso persona seria como datos[i]
# for persona in datos:
#     print(persona['nombre']) 


# Mosramos todos los datos de las paersonas
def mostrar_datos(lista_datos: list) -> None:
    for persona in lista_datos: 
        print(f"{persona["nombre"]:<15} {persona["edad"]:<5}", end = "")
        if len(persona["hobbies"]) == 0:
            print("Sin hobbies", end = "")
        else:
            for hobbie in persona["hobbies"]:
                print(hobbie, end = " - ")
        print("")

# mostrar_datos(datos)

# Mppstramos solo una persona
def mostrar_una_persona(persona: dict) -> None:
    print(f"{persona["nombre"]:<15} {persona["edad"]:<5}", end = "")
    if len(persona["hobbies"]) == 0:
        print("Sin hobbies", end = "")
    else:
        for hobbie in persona["hobbies"]:
            print(hobbie, end = " - ")
    print("")

una_persona = datos[2]

# mostrar_una_persona(una_persona)



#Entonces podemos anidar, granularizar y mejoerar las funciones:
def mostrar_hobbies(lista_hobbies: list) -> None:
    if len(lista_hobbies) == 0:
        print("Sin hobbies", end = "")
    else:
        for hobbie in lista_hobbies:
            print(hobbie, end = " | ")
    print("")


def mostrar_una_persona_2(persona: dict) -> None:
    print(f"{persona["nombre"]:<15} {persona["edad"]:<5}", end = "")
    mostrar_hobbies(persona["hobbies"])


def mostrar_datos_2(lista_personas: list) -> None:
    for persona in lista_personas:
        mostrar_una_persona_2(persona)


def mostrar_datos_sofia(lista_personas: list) -> None:
    for persona in lista_personas:
        if persona["nombre"] == "Sofía":
            mostrar_una_persona_2(persona)


# Mejoramos la funcion para que sea mas generica
def mostrar_datos_por_nombre(lista_personas: list, nombre: str) -> None:
    for persona in lista_personas:
        if persona["nombre"] == nombre:
            mostrar_una_persona_2(persona)


def mostrar_datos_por_edad(lista_personas: list, edad: int) -> None:
    for persona in lista_personas:
        if persona["edad"] == edad:
            mostrar_una_persona_2(persona)


# Unimos ambas funciones en algo mas generico:
def mostrar_datos_clave(lista_personas: list, clave: str, valor: int | str) -> None:
    for persona in lista_personas:
        if persona[clave] == valor:
            mostrar_una_persona_2(persona)


# Mostramos todos los datos:
# mostrar_datos_2(datos)

# Mostramos los datos de las personas que se llaman Sofia:
# mostrar_datos_sofia(datos)

# Mostramos los datos de las personas por us nombre:
# mostrar_datos_por_nombre(datos,"Luis")

# Mostramos a las personas con 23 años:
# mostrar_datos_por_edad(datos,23)

# Mostramos la persona usando datos clave:
# mostrar_datos_clave(datos, "edad", 23)


# Buscamos personas con el mayor puntaje o edad, x ej
def retornar_maximo(lista_personas: list, clave: str):
    maximo = 0
    for persona in lista_personas:
        if persona[clave] > maximo:
            maximo = persona[clave]
    return maximo


def personas_mayor_puntaje(lista_personas: list, clave: str) -> None:
    maximo = retornar_maximo(lista_personas,clave)
    mostrar_datos_clave(lista_personas,clave,maximo)

# print("El puntaje mas alto es: ", retornar_maximo(datos, 'puntos'))
# print("La edad mas grande es: ", retornar_maximo(datos, 'edad'))
# personas_mayor_puntaje(datos, 'puntos')
# personas_mayor_puntaje(datos, 'edad')



# Una de las formas para almacenar los hobbies y quitar los repetidos
def retornar_total_hobbies(lista_personas: list) -> None:
    lista_hobbies = []
    for persona in lista_personas:
        for hobbies in persona["hobbies"]:
                lista_hobbies.append(hobbies)
    lista_hobbies = set(lista_hobbies)
    return lista_hobbies




