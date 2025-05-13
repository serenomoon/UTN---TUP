# Escribir una función que reciba una lista de enteros, 
# la misma calculará y devolverá el promedio de todos los números.

def lista_enteros(enteros: list) -> float:
    """Calcula promedio de los enteros ingresados

    Args:
        enteros (list): Array de enteros ingresado

    Returns:
        float: Devuelve el promedio
    """
    suma_enteros = 0
    for i in range(len(enteros)):
        suma_enteros += enteros[i]
    return suma_enteros / len(enteros)
