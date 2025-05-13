# Escribir una función que reciba como parámetros una lista de enteros 
# y muestre la/las posiciones en donde se encuentra el valor máximo hallado.

def valores_maximos_array(enteros:list) -> int:
    """Encuentra la/las posicion/posiciones del/de los numero/s mas alto/s de un array

    Args:
        enteros (list): Array de numeros enteros ingresados

    Returns:
        int: Devuelve posicion del/de los numero/s mas alto/s
    """
    maximo = enteros[0]
    for i in range(1, len(enteros)):
        if enteros[i] > maximo:
            maximo = enteros[i]
    for j in range(len(enteros)):
        if enteros[j] == maximo:
            print(j)


