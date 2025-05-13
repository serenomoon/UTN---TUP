# Escribir una función que permita ingresar la cantidad de números que reciba como parámetro. 
# Crear el array con la función del punto 1.
from arrays_unidimensionales1 import crear_array


def cantidad_numeros(cantidad_a_ingresar:int) -> list:
    """Crea un array con la cantidad de numeros que querramos ingersar
        y luego nos deja ingresar uno por uno

    Args:
        cantidad_a_ingresar (int): Largo del array a crear

    Returns:
        _type_: Devuelve el array con los numeros ingresados
    """
    array = crear_array(cantidad_a_ingresar)
    for i in range(cantidad_a_ingresar):
        numero = input(f"Ingresa el numero para la posicion {i}: ")
        array[i] = int(numero)
    return array
