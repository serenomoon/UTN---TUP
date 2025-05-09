def crear_vector(contenido: any, dimension: int):
    vector = [contenido] * dimension
    return vector

# vector_a = crear_vector(None,5)
# print(vector_a)

def cargar_lista(vector: list, mensaje: str):
    exito = False #Comienza la bandera baja (ahorramos un else)
    if type(vector) == list and type(mensaje) == str:
        exito = True #Usamos una "bandera" para no usar prints
        for i in range(len(vector)):
            vector[i] = int(input(mensaje))
    #No se retorna vector porque es mutable, no hace falta
    return exito 
#No usar 2 returns para evitar que en funciones mas largas se nos pase uno y quede sin salida.


def mostrar_lista(vector: list):
    for i in range(len(vector)):
        print(vector[i])


def buscar_maximo(vector: list):
    maximo = 0
    for i in range(len(vector)):
        if vector[i] > maximo or i == 0:
            maximo = vector[i]
    return maximo


# def mostrar_posiciones_maximos(vector: list, maximo):
#     for i in range(len(vector)):
#         if vector[i] == maximo:
#             print(i)

#Cambiamos maximo, x valor, para buscar cualquier edad en la lista
def mostrar_posiciones_valor(vector: list, valor: int):
    bandera = False
    for i in range(len(vector)):
        if vector[i] == valor:
            bandera = True
            print(i)
    if bandera == False:
        print("No se encontro el valor") #Aca usamos print porque es una funcion para mostrar


def determinar_paridad(numero) -> bool:
    es_par = False
    if numero % 2 == 0:
        es_par = True
    return es_par

def buscar_numero_par(vector: list):
    bandera = False
    for i in range(len(vector)):
        es_par = determinar_paridad(vector[i])
        if es_par:
            bandera = True
            break
    return bandera

###################MAIN#######################

# edades = crear_vector(None, 5)

# if cargar_lista(edades, "Ingrese una edad: "): #Si devuelve True, muestra la lista
#     mostrar_lista(edades) #Si pongo un entero, se rompe, xq no es iterable
#     maxima_edad = buscar_maximo(edades)
#     print(f"La edad maxima es: {maxima_edad}")
#     print("El maximo esta en las posiciones: ")
#     mostrar_posiciones_valor(edades, maxima_edad)
#     print(f"Edad especifica buscada: ")
#     edad_ingresada = int(input("Ingresar edad: "))
#     mostrar_posiciones_valor(edades, edad_ingresada)
#     print(f"Cantidad de edades encontradas: {edad_ingresada}")

#     if buscar_numero_par(edades):
#         print("Por lo menos hay una edad par")
#     else:
#         print("No hay edad pares")
# else:
#     print("Hubo un error")




