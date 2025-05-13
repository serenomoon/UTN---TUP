# Escribir una función que reciba como parámetros una lista de enteros 
# y retorne la posición del valor máximo encontrado.

def valor_maximo_array(enteros:list) -> int:
    """Encuentra la posicion del numero mas alto de un array

    Args:
        enteros (list): Array de numeros enteros ingresados

    Returns:
        int: Devuelve posicion del numero mas alto
    """
    posicion = 0
    maximo = enteros[0]
    for i in range(1, len(enteros)):
        if enteros[i] > maximo:
            maximo = enteros[i]
            posicion = i
    return posicion

maximo = valor_maximo_array([2,5,23,54,10])
print(maximo)
