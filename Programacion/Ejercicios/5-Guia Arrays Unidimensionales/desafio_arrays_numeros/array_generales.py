from Input import get_init

def crear_vector(contenido: any, dimension: int) -> list:
    """Crea un vector repitiendo el "contenido" en cada uno de los espacios defiinidos por "dimension"
    Args:
        contenido (any): Contenido que llenara los indices del array (Ej: None)
        dimension (int): Cantidad de indices o posiciones que tendra el array

    Returns:
        list: Devuelve una lista "cruda"
    """
    vector = [contenido] * dimension
    return vector


def cargar_lista(vector: list) -> bool:
    """Cambia los valores de la lista objetivo por valores definidos por el usuario

    Args:
        vector (list): Lista a modificar

    Returns:
        bool: Devuelve True al terminar
    """
    exito = False 
    if type(vector) == list:
        exito = True 
        for i in range(len(vector)):
            numero = get_init("", "Error", -1000, 1000)
            vector[i] = numero
    return exito 


def es_par(numero) -> bool:
    """Chequea si un numero es par, si lo es, devuelve True

    Args:
        numero (_type_): numero a analizar

    Returns:
        bool: Devuelve True de ser par, de lo contrario False
    """
    es_par = False
    if numero % 2 == 0:
        es_par = True
    return es_par


def mostrar_lista(vector: list):
    """Muestra la lista objetivo en consola

    Args:
        vector (list): Lista a mostrar
    """
    for i in range(len(vector)):
        print(f"{i+1}- {vector[i]}")









