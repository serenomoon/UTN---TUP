from array_generales import *

def sumar_numeros_pares(vector: list) -> int:
    """Suma todos los nuemeros pares de una lista y devuelve el valor total

    Args:
        vector (list): Lista a analizar

    Returns:
        int: Total de la suma de los numeros pares
    """
    suma_pares = 0
    for i in range(len(vector)):
        par = es_par(vector[i])
        if par:
            suma_pares += vector[i]
    return suma_pares


def positivos_negativos(vector: list):
    """Cuenta la cantidad de numeros negativos y positivos de una lista y los muestra en consola

    Args:
        vector (list): Lista a analizar
    """
    negativos = 0
    positivos = 0
    for i in range(len(vector)):
        if vector[i] > 0:
            positivos += 1
        else:
            negativos += 1
    print(f"Cantidad de negativos: {negativos}\nCantidad de positivos: {positivos}")


def buscar_maximo_impar(vector: list):
    """Busca el mayor numero impar de una lista y lo retorna

    Args:
        vector (list): Lista a analizar

    Returns:
        _type_: Numero mayor impar
    """
    maximo_impar = None
    for i in range(len(vector)):
        if vector[i] % 2 != 0:
            if maximo_impar is None or vector[i] > maximo_impar:
                maximo_impar = vector[i]
    return maximo_impar


def lista_numeros_pares(vector: list) -> list:
    """Itera una lista en busca de numeros pares y los devuelve en una lista nueva

    Args:
        vector (list): Lista a analizar

    Returns:
        list: Lista de numeros pares
    """
    cantidad_pares = 0
    continuar = 0
    for i in range(len(vector)):
        if es_par(vector[i]):
            cantidad_pares += 1
    vector_pares = crear_vector(None,cantidad_pares)
    for j in range(len(vector_pares)):
        for c in range(continuar,len(vector)):
            if es_par(vector[c]):
                vector_pares[j] = vector[c]
                continuar = c + 1
                break
    return  vector_pares


def lista_numeros_posiciones_impares(vector: list) -> list:
    """Busca en una lista todas las posiciones/indices impares y crea una nueva lista con los valores allados
    en dichos indices

    Args:
        vector (list): Lista a analizar

    Returns:
        list: Lista de valores en posiciones imapres
    """
    posiciones_impares = 0
    continuar = 0
    for i in range(len(vector)):
        if not es_par(i):
            posiciones_impares += 1
    vector_posiciones_impares = crear_vector(None,posiciones_impares)
    for j in range(len(vector_posiciones_impares)):
        for c in range(continuar,len(vector)):
            if not es_par(c):
                vector_posiciones_impares[j] = vector[c]
                continuar = c + 1
                break
    return  vector_posiciones_impares
